#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Wala' Essam
# DATE CREATED: 2025-03-21                                    
# REVISED DATE: 2025-03-23  
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    # TODO 0: Measures total program runtime by collecting start time
    start_time = time()
    
    # TODO 1: Define get_input_args function within the file get_input_args.py
    in_arg = get_input_args()

    # Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)

    # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
    results = get_pet_labels(in_arg.dir)  # Pass in_arg.dir instead of None

    # Function that checks Pet Images in the results Dictionary using results    
    check_creating_pet_image_labels(results)

    # TODO 3: Define classify_images function within the file classiy_images.py
    classify_images(in_arg.dir, results, in_arg.arch)  # Pass in_arg.dir and in_arg.arch

    # Function that checks Results Dictionary using results    
    check_classifying_images(results)    

    # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
    adjust_results4_isadog(results, in_arg.dogfile)  # Pass in_arg.dogfile

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    check_classifying_labels_as_dogs(results)

    # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
    results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    check_calculating_results(results, results_stats)

    # TODO 6: Define print_results function within the file print_results.py
    print_results(results, results_stats, in_arg.arch, True, True)  # Pass in_arg.arch

    # TODO 0: Measure total program runtime by collecting end time
    end_time = time()

    # TODO 0: Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time

    # Test the timing function with sleep
    sleep(5)  # Simulate a delay to test timing (Change this to test different values)

    print("\n** Total Elapsed Runtime:",
          str(int(tot_time / 3600)) + ":" +
          str(int((tot_time % 3600) / 60)) + ":" +
          str(int((tot_time % 3600) % 60)) )
    
    # Inside your main function, after collecting the necessary results

    def print_results_table(results_stats, in_arg):
        """
        This function prints out the results in the table format as requested.
        It uses the results from the classification and calculates key statistics to display.
        """
        # Extracting values from the results_stats dictionary (assuming the necessary fields are included)
        model_architectures = ['ResNet', 'AlexNet', 'VGG']
        correct_not_a_dog = [results_stats['ResNet']['not_a_dog_accuracy'], 
                            results_stats['AlexNet']['not_a_dog_accuracy'], 
                            results_stats['VGG']['not_a_dog_accuracy']]
        correct_dog = [results_stats['ResNet']['dog_accuracy'], 
                    results_stats['AlexNet']['dog_accuracy'], 
                    results_stats['VGG']['dog_accuracy']]
        breed_accuracy = [results_stats['ResNet']['breed_accuracy'], 
                        results_stats['AlexNet']['breed_accuracy'], 
                        results_stats['VGG']['breed_accuracy']]
        match_labels = [results_stats['ResNet']['label_match_accuracy'], 
                        results_stats['AlexNet']['label_match_accuracy'], 
                        results_stats['VGG']['label_match_accuracy']]

        # Print the table header
        print("\nCNN Model Architecture | % Not-a-Dog Correct | % Dogs Correct | % Breeds Correct | % Match Labels")
        print("-" * 80)

        # Print results for each model
        for i, model in enumerate(model_architectures):
            print(f"{model:<25} | {correct_not_a_dog[i]:<18} | {correct_dog[i]:<15} | {breed_accuracy[i]:<17} | {match_labels[i]:<16}")

    # In the main function, call print_results_table with the results_stats data and in_arg:
    # Assuming 'results_stats' contains the necessary accuracy data for each model

    print_results_table(results_stats, in_arg)



  

# Call to main function to run the program
if __name__ == "__main__":
    main()



# this is an example for a result which appear on a table


# # Total Images    40 
# # Dog Images      30 
# #Not-a-Dog Images 10


# CNN Model Architecture:  % Not-a-Dog correct  % Dogs correct  % Breeds correct % Match labels
# ResNet                   90.0%                100.0%          90.0%            82.5% 
# AlexNet                  100.0%               100.0%          80.0%            75.0% 
# VGG                      100.0%               100.0%          93.3%            87.5%