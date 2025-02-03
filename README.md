# Project Overview

This project trains a YOLO model to detect cricket balls using a dataset from Roboflow and converts the trained model to TFLite format.

## Requirements

- **Python Version**: 3.11.0
  - Download here: [Python 3.11.0](https://www.python.org/downloads/release/python-3110/)
  - Note: Do not install the latest version as it does not support TensorFlow yet.
- **CUDA**: Make use of GPU to run the Python code.

## Steps

1. **Install the required Python version**:
   - Download and install Python 3.11.0 from the link above.

2. **Download Project and Extract the Data**:
   - Download the dataset from [Roboflow](https://universe.roboflow.com/cricket-rfyd8/cricket-balls-l1us5).
   - Extract the data to match the following folder structure:
     ```
     test/
         images/
         labels/
             1_mp4-1_jpg.rf.40a35a37956e4668942ff130b6b4e2d7.txt
             1_mp4-11_jpg.rf.fb68b45941eef5d4cf84ddc4f6bc7412.txt
             1_mp4-15_jpg.rf.d00c324641f98f9b81da5dc993c4f595.txt
             1_mp4-18_jpg.rf.ce1bab5241d53918ef593af9b47884e0.txt
             1_mp4-29_jpg.rf.61becb16dec00f6e7fff75c02dcf0f98.txt
             ...
     train/
         images/
         labels/
             ...
         labels.cache
     valid/
         images/
         labels/
             ...
         labels.cache
     [best.pt](http://_vscodecontentref_/0)
     [data.yaml](http://_vscodecontentref_/1)
     [execute.py](http://_vscodecontentref_/2)
     [README.dataset.txt](http://_vscodecontentref_/3)
     [README.md](http://_vscodecontentref_/4)
     [README.roboflow.txt](http://_vscodecontentref_/5)
     [tfliteconvert.py](http://_vscodecontentref_/6)
     ```

3. **Check and Change the Value of Epochs**:
   - Open [`execute.py`](execute.py) and modify the `epochs` parameter in the `model.train` function. The recommended number is 300 and above.

4. **Train the Model**:
   - Run the following command to train the model:
     ```sh
     python execute.py
     ```

5. **Locate the Best Model File**:
   - After training, locate the [best.pt](http://_vscodecontentref_/7) file and copy it to the root project directory.

6. **Install Dependencies**:
   - Run the following commands to install the required dependencies:
     ```sh
     pip install ultralytics
     pip install tensorflow
     ```

7. **Convert the Model to TFLite Format**:
   - Run the following command to convert the [best.pt](http://_vscodecontentref_/8) model to TFLite format:
     ```sh
     python tfliteconvert.py
     ```

## Files

- [execute.py](http://_vscodecontentref_/9): Script to train the YOLO model.
- [tfliteconvert.py](http://_vscodecontentref_/10): Script to convert the trained model to TFLite format.
- [data.yaml](http://_vscodecontentref_/11): Configuration file for the dataset.
- [test](http://_vscodecontentref_/12), [train](http://_vscodecontentref_/13), [valid](http://_vscodecontentref_/14): Directories containing the dataset images and labels.

## Notes

- Ensure that you have a compatible GPU and CUDA installed to speed up the training process.
- The training process may take a significant amount of time depending on the number of epochs and the size of the dataset.