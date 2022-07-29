#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import required libraries
import numpy as np
import pandas as pd
import pickle

# Define a function for the model deployment
def My_Cars_Model(input_df):

    # Create copies for the input data frame
    df_raw = input_df.copy()
    df = input_df.copy()

    ######################
    # Data preprocessing #
    ######################

    # Drop the 'Mileage' and 'Model' columns
    df.drop(['Mileage','Model'], axis = 1, inplace=True)

    # Creating dummy variables
    df['Brand_BMW'] = df['Brand'].apply(lambda x: 1 if x == 'BMW' else 0)
    df['Brand_Mercedes-Benz'] = df['Brand'].apply(lambda x: 1 if x == 'Mercedes-Benz' else 0)
    df['Brand_Mitsubishi'] = df['Brand'].apply(lambda x: 1 if x == 'Mitsubishi' else 0)
    df['Brand_Renault'] = df['Brand'].apply(lambda x: 1 if x == 'Renault' else 0)
    df['Brand_Toyota'] = df['Brand'].apply(lambda x: 1 if x == 'Toyota' else 0)
    df['Brand_Volkswagen'] = df['Brand'].apply(lambda x: 1 if x == 'Volkswagen' else 0) 
    
    df['Body_hatch'] = df['Body'].apply(lambda x: 1 if x == 'hatch' else 0)
    df['Body_other'] = df['Body'].apply(lambda x: 1 if x == 'other' else 0)    
    df['Body_sedan'] = df['Body'].apply(lambda x: 1 if x == 'sedan' else 0)    
    df['Body_vagon'] = df['Body'].apply(lambda x: 1 if x == 'vagon' else 0)   
    df['Body_van'] = df['Body'].apply(lambda x: 1 if x == 'van' else 0)   
    
    df['Engine Type_Gas'] = df['Engine Type'].apply(lambda x: 1 if x == 'Gas' else 0)    
    df['Engine Type_Other'] = df['Engine Type'].apply(lambda x: 1 if x == 'Other' else 0)    
    df['Engine Type_Petrol'] = df['Engine Type'].apply(lambda x: 1 if x == 'Petrol' else 0)    
    
    df['Registration_yes'] = df['Registration'].apply(lambda x: 1 if x == 'yes' else 0)    
    
    # Drop columns 'Brand', 'Body', 'Engine Type', 'Registration'
    df.drop(['Brand', 'Body', 'Engine Type', 'Registration'], axis = 1, inplace=True)
    
    # Feature scaling
    # Load the scaler file
    with open('Cars_Standard_Scaler','rb') as scaler_file:
        scaler = pickle.load(scaler_file)

    # Define which colums to scale / not to scale
    to_scale_cols = ['Year','EngineV']
    
    df_to_scale = df[to_scale_cols]
    df_not_to_scale = df.drop(to_scale_cols,axis = 1)
    
    # Transform df_to_scale using the scaler
    df_scaled_arr = scaler.transform(df_to_scale)
    
    # Store the scaled data as dataframe
    df_scaled = pd.DataFrame(data = df_scaled_arr, columns=df_to_scale.columns)
    
    # Combine the dataframe with df_not_to_scale
    df_scaled = pd.concat([df_scaled, df_not_to_scale],axis = 1)
    
    # Rearrange columns to ensure order
    df_scaled = df_scaled[['Year', 'EngineV', 'Brand_BMW', 'Brand_Mercedes-Benz',
                          'Brand_Mitsubishi', 'Brand_Renault', 'Brand_Toyota', 'Brand_Volkswagen',
                          'Body_hatch', 'Body_other', 'Body_sedan', 'Body_vagon', 'Body_van',
                          'Engine Type_Gas', 'Engine Type_Other', 'Engine Type_Petrol',
                          'Registration_yes']]

    #################################
    # Loading model for predictions #
    #################################
    
    # Load the linear model
    with open('Cars_Linear_Model','rb') as model_file:
        linear_model = pickle.load(model_file)

    # Predict log_price using the model
    predicted_log_price = linear_model.predict(df_scaled)
    
    # Convert the log_price to price
    predicted_price = np.round(np.exp(predicted_log_price),1)
    
    # Create a dataframe containing the predicted prices
    df_predictions = pd.DataFrame(data = predicted_price,columns=['Predicted Price'])
    
    # Combine the original input_df with the predicted price column into a single dataframe and output it
    df_raw_with_pred = pd.concat([df_raw,df_predictions],axis = 1)
    return df_raw_with_pred

