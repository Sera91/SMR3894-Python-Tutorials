# The project

You are requested to create a tool to denoise audio tracks and classify them into three classes: human voices, musical instruments, and others.

To denoise the audio you should not use any ML algorithm but you are suggested to adopt a specific Wiener filter:

To classify the 

Once finished this task, you can compare this classification with the one obtainable with a Convolution Neural Network (CNN) applied to the images obtained from padding the audio tracks.


# The data

To structure and test the first class of you audio pipeline, the denoiser, a psossibility is to use the Freesound mono audio track dataset,  , first adding white random noise to each track, and then, trying to remove the white noise from the signal.

Using the same dataset you can also train/test your classifier 


# Useful tools
