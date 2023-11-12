# The project: Audio denoising and classification
-----------------------------------------------------------------------------

The customer request is to create a tool to denoise audio tracks and classify them into three classes: human voices, musical instruments, and others.

To denoise the audio you should not use any ML algorithm but you are suggested to adopt a specific Wiener filter:

To classify the audio tracks you can perform the audio analysis in the Fourier Domain (applying FFT to the original signal).
It's suggested to show the differences among the three classes of audio tracks by applying visualization tools to the audio signals.

Once finished with this task, you can compare this classification with the one obtainable with a Convolution Neural Network (CNN) applied to the images obtained from padding the audio tracks. (For this step


# The data

To structure and test the first class of your audio data analysis pipeline, the denoiser, a possibility is to use the clean subset of audio tracks in the Freesound mono audio track dataset, [DBR-dataset](https://zenodo.org/records/1069747) , first adding white random noise to each track, and then, trying to remove the white noise from the signal.

Using the same dataset you can also train/test your classifier 


# Useful tools
To 

To construct the Wiener filter you can use the Scipy and Numpy libraries.

To visualize the 

