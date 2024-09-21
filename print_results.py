#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/display_summary.py
#                                                                             
# PROGRAMMER: Shreya Kumari
# DATE CREATED: 
# REVISED DATE: 
# PURPOSE: This script defines the `display_results` function, which prints the 
#          classification results statistics from the provided statistics dictionary 
#          (`stats_summary`). Additionally, it provides options for the user to print 
#          cases of misclassified dogs and breeds using the classification 
#          results dictionary (`classification_results`).  
#         This function inputs:
#            - The classification results dictionary as `classification_results` within 
#              the `display_results` function and as `results` for the function call 
#              within the main script.
#            - The statistics dictionary as `stats_summary` within the `display_results`
#              function and `results_stats` for the function call within the main script.
#            - The CNN model architecture as `cnn_model` within the `display_results` 
#              function and `in_arg.arch` for the function call within main. 
#            - Prints Incorrectly Classified Dogs as `show_misclassified_dogs` within
#              the `display_results` function and is set as either a boolean value 
#              True or False in the function call within main (defaults to False).
#            - Prints Incorrectly Classified Breeds as `show_misclassified_breeds` within
#              the `display_results` function and is set as either a boolean value 
#              True or False in the function call within main (defaults to False).
#         This function does not return anything other than printing a summary
#         of the final results.
##
# TODO: Define the `display_results` function below by replacing the `None`
#       below with the function definition of the `display_results` function. 
#       Notice that this function doesn't need to return anything because it  
#       prints a summary of the results using `classification_results` and 
#       `stats_summary`.
#
def display_results(classification_results, stats_summary, cnn_model, 
                    show_misclassified_dogs=False, show_misclassified_breeds=False):
    """
    Prints a summary of classification results, followed by misclassified 
    dog and breed cases if the user requests additional details.
    
    Parameters:
      classification_results - Dictionary with key as image filename and value as a List:
                   index 0 = pet image label (string)
                   index 1 = classifier label (string)
                   index 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifier labels and 0 = no match between labels
                   index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet image 'is-NOT-a' dog. 
                   index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      stats_summary - Dictionary containing the classification statistics 
                      (either a percentage or a count), where the key is the 
                      statistic's name (starting with 'pct' for percentage 
                      or 'n' for count) and the value is the statistic's value.
      cnn_model - Indicates which CNN model architecture was used to classify 
                  the pet images. Values must be either: 'resnet', 'alexnet', 'vgg' (string)
      show_misclassified_dogs - True to print misclassified dog images; 
                                False to suppress printing (default).
      show_misclassified_breeds - True to print misclassified dog breeds; 
                                  False to suppress printing (default).
    Returns:
           None - simply printing results.
    """    
    # Print a summary of the model and basic statistics
    print('\nSummary for CNN Model Architecture: {}'.format(cnn_model.upper()))
    print('\nTotal Images: {} \nDog Images: {} \nNot-a-Dog Images: {}'.format(
        stats_summary['n_images'], stats_summary['n_dogs_img'], stats_summary['n_notdogs_img']))
    
    # Print percentages in stats_summary dictionary
    for stat_name in stats_summary:
        if stat_name.startswith('pct'):
            print('{}: {:.2f}%'.format(stat_name, stats_summary[stat_name]))
    
    # Check and print incorrectly classified dogs if requested
    if show_misclassified_dogs and (
            stats_summary['n_correct_dogs'] + stats_summary['n_correct_notdogs'] 
            != stats_summary['n_images']):
        print('\nIncorrect Dog/Not-a-Dog Classifications:')
        for filename in classification_results:
            if sum(classification_results[filename][3:]) == 1:
                print('Pet Label: {}   Classified as: {}'.format(
                    classification_results[filename][0], classification_results[filename][1]))
    
    # Check and print incorrectly classified breeds if requested
    if show_misclassified_breeds and (
            stats_summary['n_correct_dogs'] != stats_summary['n_correct_breed']):
        print('\nIncorrect Breed Classifications:')
        for filename in classification_results:
            if (sum(classification_results[filename][3:]) == 2 and 
                classification_results[filename][2] == 0):
                print('Pet Label: {}   Classified as: {}'.format(
                    classification_results[filename][0], classification_results[filename][1]))