{% if cookiecutter.kind == "image" %}
# USAGE: this script is used to create an image dataset that is NOT hosted on HuggingFace but points to the original files
# to download and generate the dataset.
# Full image loading script template at https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py
# Full documentation at https://huggingface.co/docs/datasets/main/en/image_dataset#loading-script
# TODO: Address all TODOs and remove all explanatory comments

import csv
import os
import datasets
import io
import tarfile

# TODO: Provide citation or if it is not needed remove it
# Example citation:
_CITATION = """\
@article{article_id,
author    = {Author List},
title     = {Dataset Paper Title},
journal   = {Publication Venue},
year      = {2525}
}
"""
_DESCRIPTION = """\
{{cookiecutter.description}}"""
_HOMEPAGE = "{{cookiecutter.homepage}}"
_LICENSE = "{{cookiecutter.license}}"  #Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses

#Needed for datasets.Features EXAMPLE
_NAMES = [
    "False",
    "True"
]

# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
_URLS = "{{cookiecutter.url}}"

#define dataset
class {{cookiecutter.__repo_name}}(datasets.GeneratorBasedBuilder):

    VERSION = datasets.Version("2.14.4") #Source https://github.com/huggingface/datasets/releases

    def _info(self):
    # TODO: Define the different columns of the dataset and their types.
    # If you require sub-sets in your dataset see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

        # This defines the different columns of the dataset and their types
        # list of types: https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Value
        features = datasets.Features( #EXAMPLE:
            {
                "image": datasets.Image(),
                "label": datasets.ClassLabel(names=_NAMES)
            }
        )

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features= features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION
        )

{% if "tar" in cookiecutter.url%}
    {% if cookiecutter.splits == "none"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download(_URLS) # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        return [
            datasets.SplitGenerator(
                name="full",
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir) #iterate over files in tar file
                },
            )
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the tar file contained
    # a csv file with the labels and the name of the images. The images were sitting in a different folder as jpg files.

        #find csv file and read in contents
        for file_path, file_obj in files:
            if ".csv" in file_path:
                csv_bytes = file_obj.read() 
                csv_contents = str(csv_bytes,'UTF-8')
                break

        #iterate over files and match with labels to generate examples
        for file_path, file_obj in files:
            filename = os.path.basename(file_path)
            if ".jpg" in filename:
                for row in csv.DictReader(csv_contents.strip().splitlines(),delimiter=','):
                    if os.path.basename(row['image']) == filename:
                        yield file_path,{
                            "image": {"path": file_path, "bytes": file_obj.read()},
                            "label": row['label']
                        }
    {% elif cookiecutter.splits == "2-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download(_URLS) # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir), #iterate over files in tar file
                    "split": "train"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir),
                    "split": "test"
                },      
            )
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files, split):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the tar file contained the images in the following format:
    #     my_dataset/
    # ├── split_1/
    # │   ├── label_1/
    # │   │   ├── file_1.jpg
    # │   │   ├── file_2.jpg
    # │   │   ├── file_3.jpg
    # │   │   ├──...
    # │   ├── label_n/...
    # ├── split_n/...

        for file_path, file_obj in files:
            label = file_path.split("/")[1] #get second element of path
            splitfolder = file_path.split("/")[0] #get first element of path
            if splitfolder == split: #only iterate over files in the split folder to split images to their assigned splits
                yield file_path,{
                            "image": {"path": file_path, "bytes": file_obj.read()},
                            "label": label
                        }
    {% elif cookiecutter.splits == "3-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download(_URLS) # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir), #iterate over files in tar file
                    "split": "train"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir),
                    "split": "val"
                },      
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir),
                    "split": "test"
                },      
            )
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files, split):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the tar file contained the images in the following format:
    #     my_dataset/
    # ├── split_1/
    # │   ├── label_1/
    # │   │   ├── file_1.jpg
    # │   │   ├── file_2.jpg
    # │   │   ├── file_3.jpg
    # │   │   ├──...
    # │   ├── label_n/...
    # ├── split_n/...

        for file_path, file_obj in files:
            label = file_path.split("/")[1] #get second element of path
            splitfolder = file_path.split("/")[0] #get first element of path
            if splitfolder == split: #only iterate over files in the split folder to split images to their assigned splits
                yield file_path,{
                            "image": {"path": file_path, "bytes": file_obj.read()},
                            "label": label
                        }
    {%- endif %}
{% elif "zip" in cookiecutter.url%}
    {% if cookiecutter.splits == "none"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:
        data_dir = dl_manager.download_and_extract(_URLS) #files in zip can be extracted
        image_dir = os.path.join(data_dir, "my-dataset/all")
        metadata = os.path.join(data_dir, "snow_dataset/metadata.csv")

        return [
            datasets.SplitGenerator(
                name="full",
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_files(image_dir),
                    "metadata_path": metadata,
                },
            )
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files, metadata_path):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py
        
    #EXAMPLE: For this dataset the zip file contained
    # a csv file with the metadata and the images were sitting in a different folder as jpg files.
        
        #iterate over files and match with metadata to generate examples
        for file_path in files:
            with open(metadata_path, encoding="utf-8") as f:
                filename = os.path.basename(file_path)
                for row in csv.DictReader(f,delimiter=','):
                    if row['name'] == filename:
                        yield file_path,{
                            "image":file_path,
                            "label": row['label']
                        }
    {% elif cookiecutter.splits == "2-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:
        data_dir = dl_manager.download_and_extract(_URLS) #zip files can be extracted
        image_dir = os.path.join(data_dir, "my-dataset/all")
        metadata = os.path.join(data_dir, "snow_dataset/metadata.csv")

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_files(image_dir),
                    "metadata_path": metadata,
                    "split": "train"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_files(image_dir),
                    "metadata_path": metadata,
                    "split": "test"
                },
            )
            
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files, metadata_path,split):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` view (https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py)
        
    #EXAMPLE: For this dataset the zip file contained
    # a csv file with the metadata and the images were sitting in a different folder as jpg files.
        
        #iterate over files and match with metadata to generate examples
        for file_path in files:
            with open(metadata_path, encoding="utf-8") as f:
                filename = os.path.basename(file_path)
                for row in csv.DictReader(f,delimiter=','):
                    if row['name'] == filename and row['split'] == split: #only generate examples based on split to assign images to their assigned splits
                        yield file_path,{
                            "image":file_path,
                            "label": row['label']
                        }
    {% elif cookiecutter.splits == "3-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading/extracting the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:
        data_dir = dl_manager.download_and_extract(_URLS) #zip files can be extracted
        image_dir = os.path.join(data_dir, "my-dataset/all")
        metadata = os.path.join(data_dir, "snow_dataset/metadata.csv")

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_files(image_dir),
                    "metadata_path": metadata,
                    "split": "train"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_files(image_dir),
                    "metadata_path": metadata,
                    "split": "valid"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_files(image_dir),
                    "metadata_path": metadata,
                    "split": "test"
                },
            )
            
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files, metadata_path,split):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py
        
    #EXAMPLE: For this dataset the zip file contained
    # a csv file with the metadata and the images were sitting in a different folder as jpg files.
        
        #iterate over files and match with metadata to generate examples
        for file_path in files:
            with open(metadata_path, encoding="utf-8") as f:
                filename = os.path.basename(file_path)
                for row in csv.DictReader(f,delimiter=','):
                    if row['name'] == filename and row['split'] == split: #only generate examples based on split to assign images to their assigned splits
                        yield file_path,{
                            "image":file_path,
                            "label": row['label']
                        }
    {%- endif %}
{%- endif %}
{% elif cookiecutter.kind == "text" %}
# USAGE: this script is used to create a text dataset that is NOT hosted on HuggingFace but points to the original files
# to download and generate the dataset.
# Full text loading script template at https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py
# Full documentation at https://huggingface.co/docs/datasets/main/en/audio_dataset#loading-script
# TODO: Address all TODOs and remove all explanatory comments

import csv
import json
import os

import datasets

# TODO: Provide citation or if it is not needed remove it
# Example citation:
_CITATION = """\
@InProceedings{huggingface:dataset,
title = {A great new dataset},
author={huggingface, Inc.
},
year={2020}
}
"""

# TODO: Add description of the dataset here
# You can copy an official description
_DESCRIPTION = """\
{{cookiecutter.description}}"""
_HOMEPAGE = "{{cookiecutter.homepage}}"
_LICENSE = "{{cookiecutter.license}}"  #Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses

# The HuggingFace Datasets library doesn't host the datasets but only points to the original files.
# This can be an arbitrary nested dict/list of URLs (see below in `_split_generators` method)
_URLS = "{{cookiecutter.url}}"


#define dataset
class {{cookiecutter.__repo_name}}(datasets.GeneratorBasedBuilder):

    VERSION = datasets.Version("2.14.4") #Source https://github.com/huggingface/datasets/releases

    def _info(self):
    # TODO: Define the different columns of the dataset and their types.
    # If you require sub-sets in your dataset see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

        # This defines the different columns of the dataset and their types
        # list of types: https://huggingface.co/docs/datasets/main/en/package_reference/main_classes#datasets.Value
        features = datasets.Features( #EXAMPLE:
            {
                "sentence": datasets.Value("string"),
                "option1": datasets.Value("string"),
                "answer": datasets.Value("string")
                # These are the features of your dataset like images, labels ...
            }
            

        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

{% if "tar" in cookiecutter.url%}
    {% if cookiecutter.splits == "none"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download(_URLS) # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        return [
            datasets.SplitGenerator(
                name="full",
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir) #iterate over files in tar file
                },
            )
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the tar file contained
    # a JSON file with the sentence, option, and answer.

        #find JSON file and get file path
        for file_path, file_obj in files:
            if ".json" in file_path:
                json_filepath = file_path
                break

        with open(json_filepath, encoding="utf-8") as f:
            for key, row in enumerate(f):
                data = json.loads(row)
                yield key, {
                    "sentence": data["sentence"],
                    "option": data["option"],
                    "answer": data["answer"],
                }
    {% elif cookiecutter.splits == "2-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download(_URLS) # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir), #iterate over files in tar file
                    "split": "train"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir), #iterate over files in tar file
                    "split": "test"
                },
            )            
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files, split):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the tar file contained
    # a JSON file with the sentence, option, and answer.

        #find JSON file and get file path
        for file_path, file_obj in files:
            if ".json" in file_path:
                json_filepath = file_path
                break

        with open(json_filepath, encoding="utf-8") as f:
            for key, row in enumerate(f):
                data = json.loads(row)
                if data["split"] == split: #only iterate over rows to their assigned splits
                    yield key, {
                        "sentence": data["sentence"],
                        "option": data["option"],
                        "answer": data["answer"],
                    }
    {% elif cookiecutter.splits == "3-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download(_URLS) # By default the archives will be extracted and a path to a cached folder where they are extracted is returned instead of the archive

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir), #iterate over files in tar file
                    "split": "train"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir), #iterate over files in tar file
                    "split": "val"
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "files": dl_manager.iter_archive(data_dir), #iterate over files in tar file
                    "split": "test"
                },
            )          
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, files, split):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the tar file contained
    # a JSON file with the sentence, option, and answer.

        #find JSON file and get file path
        for file_path, file_obj in files:
            if ".json" in file_path:
                json_filepath = file_path
                break

        with open(json_filepath, encoding="utf-8") as f:
            for key, row in enumerate(f):
                data = json.loads(row)
                if data["split"] == split: #only iterate over rows to their assigned splits
                    yield key, {
                        "sentence": data["sentence"],
                        "option": data["option"],
                        "answer": data["answer"],
                    }
    {%- endif %}
{% elif "zip" in cookiecutter.url%}
    {% if cookiecutter.splits == "none"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download_and_extract(_URLS) #files in zip can be extracted

        return [
            datasets.SplitGenerator(
                name="full",
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "data.json")
                },
            )
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, filepath):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the zip file contained
    # a JSON file with the sentence, option, and answer.
        with open(filepath, encoding="utf-8") as f:
            for key, row in enumerate(f):
                data = json.loads(row)
                yield key, {
                    "sentence": data["sentence"],
                    "option": data["option"],
                    "answer": data["answer"],
                }
    {% elif cookiecutter.splits == "2-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download_and_extract(_URLS) #files in zip can be extracted

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "train.json")
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "test.json")
                },
            ) 
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, filepath):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the zip file contained
    # a JSON file with the sentence, option, and answer.
        with open(filepath, encoding="utf-8") as f:
            for key, row in enumerate(f):
                data = json.loads(row)
                yield key, {
                    "sentence": data["sentence"],
                    "option": data["option"],
                    "answer": data["answer"],
                }
    {% elif cookiecutter.splits == "3-splits"%}
    def _split_generators(self, dl_manager):
    # TODO: This method is tasked with downloading the data and defining the splits depending on the configuration

        # dl_manager is a datasets.download.DownloadManager that can be used to download and extract URLS
        # It can accept any type or nested list/dict and will give back the same structure with the url replaced with path to local files.
        #EXAMPLE:

        data_dir = dl_manager.download_and_extract(_URLS) #files in zip can be extracted

        return [
            datasets.SplitGenerator(
                name=datasets.Split.TRAIN,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "train.json")
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.VALIDATION,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "val.json")
                },
            ),
            datasets.SplitGenerator(
                name=datasets.Split.TEST,
                # These kwargs will be passed to _generate_examples
                gen_kwargs={
                    "filepath": os.path.join(data_dir, "test.json")
                },
            ) 
        ]

    # method parameters are unpacked from `gen_kwargs` as given in `_split_generators`
    def _generate_examples(self, filepath):
    #TODO: This method is tasked with generating your dataset from URL(S).
    # If you used sub-sets in `_split_generators` see https://github.com/huggingface/datasets/blob/main/templates/new_dataset_script.py

    #EXAMPLE: For this dataset the zip file contained
    # a JSON file with the sentence, option, and answer.
        with open(filepath, encoding="utf-8") as f:
            for key, row in enumerate(f):
                data = json.loads(row)
                yield key, {
                    "sentence": data["sentence"],
                    "option": data["option"],
                    "answer": data["answer"],
                }
    {%- endif %}
{%- endif %}
{% elif cookiecutter.kind == "audio" %}
# No script is configured
# Full documentation at https://huggingface.co/docs/datasets/main/en/dataset_script


{%- endif %}

