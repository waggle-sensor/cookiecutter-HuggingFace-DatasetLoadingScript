--- 
# Full metadata template at https://github.com/huggingface/hub-docs/blob/main/datasetcard.md?plain=1

license: {{cookiecutter.license}}  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
#license_details: {license_details}  # Example: content or link to a license not present in https://hf.co/docs/hub/repositories-licenses
{% if cookiecutter.tags == "other" %}
# **** TODO: configure your tags here, more than one tag can be added ****
#tags:
#- {tag_0} # Example: audio,bio, natural-language-understanding, birds-classification
#- {tag_1}
{% elif cookiecutter.tags != "none" %}
# more than one category can be added
tags:
- {{cookiecutter.tags}}  # Example: audio,bio, natural-language-understanding, birds-classification
{%- endif %}
{% if cookiecutter.task_category != "other" %}
# more than one category can be added
task_categories:  # Full list at https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts
- {{cookiecutter.task_category}}
{% else %}
# **** TODO: configure your task_category here, more than one category can be added ****
#task_categories:  # Full list at https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts
#- {task_0} # Example: question-answering, image-classification
#- {task_1}
{%- endif %}
{% if cookiecutter.__realtask != "other" %}
# MORE THAN ONE TASK CAN BE ADDED
task_ids: # Full list at https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts
- {{cookiecutter.__realtask}}
{% else %}
# **** TODO: CONFIGURE YOUR TASK HERE, MORE THAN ONE TASK CAN BE ADDED ****
task_ids: # Full list at https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts
#- {subtask_0}  # Example: extractive-qa, multi-class-image-classification
#- {subtask_1}  
{%- endif %}
{% if cookiecutter.gated_dataset == true %}
extra_gated_fields: # More info at https://huggingface.co/docs/hub/datasets-gated
- Name: text
- Affiliation: text  
- Email: text 
- I agree to use this dataset in a responsible matter: checkbox
extra_gated_prompt: By clicking on "Access Dataset" below, you agree to use this dataset in a responsible matter.
extra_gated_heading: "Acknowledge license to access the repository"
extra_gated_button_content: "Access Dataset"
{%- endif %}
{% if cookiecutter.disable_viewer == true %}
viewer: false #disables dataset viewer on the dataset page
{%- endif %}
{% if cookiecutter.autotrain == true %}
{% if cookiecutter.task_category != "other" %}
# Optional. Add this if you want to encode a train and evaluation info in a structured way for AutoTrain or Evaluation on model Hub (https://huggingface.co/autotrain)
train-eval-index:
  - config: default # The dataset config name to use.
    task: {{cookiecutter.task_category}} # The task category name (same as task_category).
{% else %}
# **** TODO: configure your task_category here ****
# Optional. Add this if you want to encode a train and evaluation info in a structured way for AutoTrain or Evaluation on model Hub (https://huggingface.co/autotrain)
#train-eval-index:
#  - config: default # The dataset config name to use. Example for datasets without configs: default. Example for glue: sst2
#    task: {task_name} # The task category name (same as task_category). # Full list at https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts
{%- endif %}
{% if cookiecutter.__realtask != "other" %}
    task_id: {{cookiecutter.__realtask}} # The AutoTrain task id. # Full list at https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts
{% else %}
# **** TODO: configure your task here ****
#    task_id: {task_type} # The AutoTrain task id. Example: extractive_question_answering. # Full list at https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Types.ts
{%- endif %}
{% if cookiecutter.splits == "2-splits" %}
    splits:
      train_split: train      # The split to use for training.
      eval_split: test        # The split to use for evaluation.
{% elif cookiecutter.splits == "3-splits" %}
    splits:
      train_split: train            # The split to use for training. Example: train
      eval_split: validation        # The split to use for evaluation. Example: test
{%- endif %}
    col_mapping:                    # The columns mapping needed to configure the task_id.
    # Example for image_classification:
      # image: image 
      # label: label
{% if cookiecutter.metric == "other" %}
# **** TODO: configure your metric here, more than one metric can be added ****
#    metrics:
#      - type: {metric_type}   # The metric id. Example: wer. Use metric id from https://hf.co/metrics
#        name: {metric_name}   # Tne metric name to be displayed. Example: Test WER
{% elif cookiecutter.metric != "none" %}
# more than one category can be added
    metrics:
      - type: {{cookiecutter.metric}}  # The metric id. metric id from https://hf.co/metrics
        name: {{cookiecutter.metric}}  # Tne metric name to be displayed.
{%- endif %}
{%- endif %}
# OPTIONAL: Other configurations you can enable
#paperswithcode_id: {paperswithcode_id}  # Dataset id on PapersWithCode (from the URL). Example for SQuAD: squad
#configs:  # Optional for datasets with multiple configurations like glue.
#- {config_0}  # Example for glue: sst2
#- {config_1}  # Example for glue: cola
#annotations_creators:
#- {creator}  # Example: crowdsourced, found, expert-generated, machine-generated
#language_creators:
#- {creator}  # Example: crowdsourced, ...
#language_details:
#- {bcp47_lang_0}  # Example: fr-FR
#- {bcp47_lang_1}  # Example: en-US
#pretty_name: {pretty_name}  # Example: SQuAD
#source_datasets:
#- {source_dataset_0}  # Example: wikipedia
#- {source_dataset_1}  # Example: laion/laion-2b
---

# Table of Contents
- [Table of Contents](#table-of-contents)
- [Dataset Description](#dataset-description)
  - [Dataset Summary](#dataset-summary)
  - [Supported Tasks and Leaderboards](#supported-tasks-and-leaderboards)
  - [Languages](#languages)
- [Dataset Structure](#dataset-structure)
  - [Data Instances](#data-instances)
  - [Data Fields](#data-fields)
  - [Data Splits](#data-splits)
- [Dataset Creation](#dataset-creation)
  - [Curation Rationale](#curation-rationale)
  - [Source Data](#source-data)
    - [Initial Data Collection and Normalization](#initial-data-collection-and-normalization)
    - [Who are the source language producers?](#who-are-the-source-language-producers)
  - [Annotations](#annotations)
    - [Annotation process](#annotation-process)
    - [Who are the annotators?](#who-are-the-annotators)
  - [Personal and Sensitive Information](#personal-and-sensitive-information)
- [Considerations for Using the Data](#considerations-for-using-the-data)
  - [Social Impact of Dataset](#social-impact-of-dataset)
  - [Discussion of Biases](#discussion-of-biases)
  - [Other Known Limitations](#other-known-limitations)
- [Additional Information](#additional-information)
  - [Dataset Curators](#dataset-curators)
  - [Licensing Information](#licensing-information)
  - [Citation Information](#citation-information)
  - [Contributions](#contributions)

# Dataset Description
- **Homepage:** [{{cookiecutter.homepage}}]({{cookiecutter.homepage}})
- **Repository:** [If the dataset is hosted on github or has a github homepage, add URL here]()
- **Paper:** [If the dataset was introduced by a paper or there was a paper written describing the dataset, add URL here (landing page for Arxiv paper preferred)]()
- **Leaderboard:** [If the dataset supports an active leaderboard, add link here]()
- **Point of Contact:** {{cookiecutter.author}},[{{cookiecutter.email}}]({{cookiecutter.email}})
> TODO: Finish Dataset Description
## Dataset Summary

Briefly summarize the dataset, its intended use and the supported tasks. Give an overview of how and why the dataset was created. The summary should explicitly mention the languages present in the dataset (possibly in broad terms, e.g. *translations between several pairs of European languages*), and describe the domain, topic, or genre covered.
> TODO: Finish Dataset Summary
## Supported Tasks and Leaderboards

For each of the tasks tagged for this dataset, give a brief description of the tag, metrics, and suggested models (with a link to their HuggingFace implementation if available). Give a similar description of tasks that were not covered by the structured tag set.

EXAMPLE:
- `{{cookiecutter.task_category}}`: The dataset can be used to train a model for {{cookiecutter.__realtask }}, which consists in {{cookiecutter.description}}. Success on this task is typically measured by achieving a *high/low* [{{cookiecutter.metric}}](https://huggingface.co/metrics/{{cookiecutter.metric}}). The ([model name](https://huggingface.co/model_name) or [model class](https://huggingface.co/transformers/model_doc/model_class.html)) model currently achieves the following score. *[IF A LEADERBOARD IS AVAILABLE]:* This task has an active leaderboard which can be found at [leaderboard url]() and ranks models based on [{{cookiecutter.metric}}](https://huggingface.co/metrics/{{cookiecutter.metric}}) while also reporting [other metric name](https://huggingface.co/metrics/other_metric_name).
> TODO: Finish Supported Tasks and Leaderboards
## Languages

Provide a brief overview of the languages represented in the dataset. Describe relevant details about specifics of the language such as whether it is social media text, African American English,...

When relevant, please provide [BCP-47 codes](https://tools.ietf.org/html/bcp47), which consist of a [primary language subtag](https://tools.ietf.org/html/bcp47#section-2.2.1), with a [script subtag](https://tools.ietf.org/html/bcp47#section-2.2.3) and/or [region subtag](https://tools.ietf.org/html/bcp47#section-2.2.4) if available.
> TODO: Finish Languages
# Dataset Structure

## Data Instances

Provide an JSON-formatted example and brief description of a typical instance in the dataset. If available, provide a link to further examples.

```
{
  'example_field': ...,
  ...
}
```

Provide any additional information that is not covered in the other sections about the data here. In particular describe any relationships between data points and if these relationships are made explicit.
> TODO: Finish Data Instances
## Data Fields

List and describe the fields present in the dataset. Mention their data type, and whether they are used as input or output in any of the tasks the dataset currently supports. If the data has span indices, describe their attributes, such as whether they are at the character level or word level, whether they are contiguous or not, etc. If the datasets contains example IDs, state whether they have an inherent meaning, such as a mapping to other datasets or pointing to relationships between data points.

- `example_field`: description of `example_field`

Note that the descriptions can be initialized with the **Show Markdown Data Fields** output of the [Datasets Tagging app](https://huggingface.co/spaces/huggingface/datasets-tagging), you will then only need to refine the generated descriptions.
> TODO: Finish Data Fields
## Data Splits

Describe and name the splits in the dataset if there are more than one.

Describe any criteria for splitting the data, if used. If there are differences between the splits (e.g. if the training annotations are machine-generated and the dev and test ones are created by humans, or if different numbers of annotators contributed to each example), describe them here.

Provide the sizes of each split. As appropriate, provide any descriptive statistics for the features, such as average length.  For example:

{% if cookiecutter.splits == "2-splits" %}
|                         | train |    test    |
|-------------------------|------:|-----------:|
| Input Sentences         |       |            |
| Average Sentence Length |       |            |
{% elif cookiecutter.splits == "3-splits" %}
|                         | train | validation | test |
|-------------------------|------:|-----------:|-----:|
| Input Sentences         |       |            |      |
| Average Sentence Length |       |            |      |
{%- endif %}
> TODO: Finish Data Splits
# Dataset Creation

## Curation Rationale

What need motivated the creation of this dataset? What are some of the reasons underlying the major choices involved in putting it together?
> TODO: Finish Curation Rationale
## Source Data

This section describes the source data (e.g. news text and headlines, social media posts, translated sentences,...)
> TODO: Finish Source Data
### Initial Data Collection and Normalization

Describe the data collection process. Describe any criteria for data selection or filtering. List any key words or search terms used. If possible, include runtime information for the collection process.

If data was collected from other pre-existing datasets, link to source here and to their [Hugging Face version](https://huggingface.co/datasets/dataset_name).

If the data was modified or normalized after being collected (e.g. if the data is word-tokenized), describe the process and the tools used.
> TODO: Finish Initial Data Collection and Normalization
### Who are the source language producers?

State whether the data was produced by humans or machine generated. Describe the people or systems who originally created the data.

If available, include self-reported demographic or identity information for the source data creators, but avoid inferring this information. Instead state that this information is unknown. See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender.

Describe the conditions under which the data was created (for example, if the producers were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.

Describe other people represented or mentioned in the data. Where possible, link to references for the information.
> TODO: Finish Who are the source language producers?
## Annotations

If the dataset contains annotations which are not part of the initial data collection, describe them in the following paragraphs.
> TODO: Finish Annotations
### Annotation process

If applicable, describe the annotation process and any tools used, or state otherwise. Describe the amount of data annotated, if not all. Describe or reference annotation guidelines provided to the annotators. If available, provide interannotator statistics. Describe any annotation validation processes.
> TODO: Finish Annotation process
### Who are the annotators?

If annotations were collected for the source data (such as class labels or syntactic parses), state whether the annotations were produced by humans or machine generated.

Describe the people or systems who originally created the annotations and their selection criteria if applicable.

If available, include self-reported demographic or identity information for the annotators, but avoid inferring this information. Instead state that this information is unknown. See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender.

Describe the conditions under which the data was annotated (for example, if the annotators were crowdworkers, state what platform was used, or if the data was found, what website the data was found on). If compensation was provided, include that information here.
> TODO: Finish Who are the annotators?
## Personal and Sensitive Information

State whether the dataset uses identity categories and, if so, how the information is used. Describe where this information comes from (i.e. self-reporting, collecting from profiles, inferring, etc.). See [Larson 2017](https://www.aclweb.org/anthology/W17-1601.pdf) for using identity categories as a variables, particularly gender. State whether the data is linked to individuals and whether those individuals can be identified in the dataset, either directly or indirectly (i.e., in combination with other data).

State whether the dataset contains other data that might be considered sensitive (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history).  

If efforts were made to anonymize the data, describe the anonymization process.
> TODO: Finish Personal and Sensitive Information
# Considerations for Using the Data

## Social Impact of Dataset

Please discuss some of the ways you believe the use of this dataset will impact society.

The statement should include both positive outlooks, such as outlining how technologies developed through its use may improve people's lives, and discuss the accompanying risks. These risks may range from making important decisions more opaque to people who are affected by the technology, to reinforcing existing harmful biases (whose specifics should be discussed in the next section), among other considerations.

Also describe in this section if the proposed dataset contains a low-resource or under-represented language. If this is the case or if this task has any impact on underserved communities, please elaborate here.
> TODO: Finish Social Impact of Dataset
## Discussion of Biases

Provide descriptions of specific biases that are likely to be reflected in the data, and state whether any steps were taken to reduce their impact.

For Wikipedia text, see for example [Dinan et al 2020 on biases in Wikipedia (esp. Table 1)](https://arxiv.org/abs/2005.00614), or [Blodgett et al 2020](https://www.aclweb.org/anthology/2020.acl-main.485/) for a more general discussion of the topic.

If analyses have been run quantifying these biases, please add brief summaries and links to the studies here.
> TODO: Finish Discussion of Biases
## Other Known Limitations

If studies of the datasets have outlined other limitations of the dataset, such as annotation artifacts, please outline and cite them here.
> TODO: Finish Other Known Limitations
# Additional Information

## Dataset Curators

List the people involved in collecting the dataset and their affiliation(s). If funding information is known, include it here.
> TODO: Finish Dataset Curators
## Licensing Information

Provide the license and link to the license webpage if available.
> TODO: Finish Licensing Information
## Citation Information

Provide the [BibTex](http://www.bibtex.org/)-formatted reference for the dataset. For example: 
```
@article{article_id,
author    = {Author List},
title     = {Dataset Paper Title},
journal   = {Publication Venue},
year      = {2525}
}
```

If the dataset has a [DOI](https://www.doi.org/), please provide it here.
> TODO: Finish Citation
## Contributions

Thanks to [@github-username](https://github.com/<github-username>) for adding this dataset.

> TODO: Finish Contributions