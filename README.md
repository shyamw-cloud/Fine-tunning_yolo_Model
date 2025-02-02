### Model_training ### 
1. **Prepare Data**:
   - Place raw images in the `raw_data/` directory.
   - Run `scripts/preprocess.py` to split the data into training and validation sets.

   Cmd---
   python scripts/preprocess.py
  

2. **Train Model**:
   Cmd---
   python scripts/train.py
   

3. **Validate Model**:
   Cmd---
   python scripts/validate.py
   

4. **Save Model Locally**:
   Cmd---
   python scripts/deploy.py
   



### Next Steps
- **Test Model**: Deploy the model for real-time inference in a separate inference script.
- **Enhance Features**: Add hyperparameter tuning and advanced logging.
- **Deployment**: Integrate the model into a production pipeline using Flask or FastAPI.


### Running the FastAPI Application ### 
1. Navigate to the `scripts/` directory:
   Cmd---
   cd scripts
   

2. Start the FastAPI server:
   Cmd---
   python app.py
   

3. Open your browser or use a tool like Postman to access:
   - **Home**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - **Prediction Endpoint**: Send a POST request to [http://127.0.0.1:8000/predict](http://127.0.0.1:8000/predict) with an image file.

### Next Steps
- **Testing**: Test the API with sample defective images.
- **Logging**: Add detailed request and response logs for debugging.
- **Enhancements**: Integrate authentication for secure access.