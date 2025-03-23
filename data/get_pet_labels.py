#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')

    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)

    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for the following item:
         index 0 = pet image label (string)
    """
    
    # Step 1: Get all filenames in the given directory
    filename_list = listdir(image_dir)
    
    # Step 2: Initialize an empty dictionary to store results
    results_dic = dict()

    # Step 3: Iterate through all the filenames in the directory
    for filename in filename_list:
        # Step 3.1: Initialize an empty string for the pet name
        pet_label = ""
        
        # Step 3.2: Convert the filename to lowercase
        filename_lower = filename.lower()
        
        # Step 3.3: Split the filename by underscores ('_') to get the words
        word_list = filename_lower.split('_')
        
        # Step 3.4: Extract words that are alphabetic (pet name)
        for word in word_list:
            if word.isalpha():
                pet_label += word + " "
        
        # Step 3.5: Strip any leading or trailing spaces from the label
        pet_label = pet_label.strip()
        
        # Step 4: Add the filename and the label to the dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Key=", filename, "already exists in results_dic with value =", results_dic[filename])

    # Step 5: Return the dictionary
    return results_dic
