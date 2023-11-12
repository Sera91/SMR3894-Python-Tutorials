# The project: Audio denoising and classification
-----------------------------------------------------------------------------
## Intro
The customer request is to create a tool to denoise audio tracks and classify them into three classes: human voices, musical instruments, and others.

To denoise the audio you should not use any ML algorithm but you are suggested to adopt a specific Wiener filter. In the section "What is a Wiener filter", below, you can find a brief introduction to the theory of Wiener filters

To classify the audio tracks you can perform the audio analysis in the Fourier Domain (applying FFT to the original signal).
It's suggested to show the differences among the three classes of audio tracks by applying visualization tools to the audio signals.

Once finished with this task, you can compare this classification with the one obtainable with a Convolution Neural Network (CNN) applied to the images obtained from padding the audio tracks. (For this step you can take advantage of PyTorch or Keras)

## What is a Wiener Filter?
From Wikipedia:
"The filter, used to produce an estimate of a desired or target random process by linear time-invariant (LTI) filtering of an observed noisy process, assuming known stationary signal, noise spectra, and additive noise, was proposed by Norbert Wiener during the 1940s and published in 1949. The discrete-time equivalent of Wiener's work was derived independently by Andrey Kolmogorov and published in 1941. Hence the theory is often called the Wiener–Kolmogorov filtering theory (cf. Kriging). "

The goal of the Wiener filter is to compute a statistical estimate of an unknown signal using a related signal in input and filtering that known signal to produce the estimate as an output. For example, the known signal might consist of an unknown signal of interest that has been corrupted by additive noise. The Wiener filter can be used to filter out the noise from the corrupted signal to provide an estimate of the underlying signal of interest. The Wiener filter is based on a statistical approach, and a more detailed account of the theory is given in the article by Welch Loyd: ["Wiener-Hopf Theory"](https://web.archive.org/web/20060920081221/http://csi.usc.edu/PDF/wienerhopf.pdf)

This filter is commonly used to denoise audio signals, especially voice recordings, as a preprocessor before speech recognition. 

Let's consider a filter system with Wiener Filter $h_W(n)$:

$$\large
x(n)=y(n)*h_W(n)
$$

meaning we filter our distorted signal y(n) with our still unknown filter $h_W(n)$.

The convolution $h_W(n)$ of (with filter length L) with y(n) can be written as  a matrix multiplication:

$$\large
x(n)=\sum_{m=0}^{L-1}y(n-m)\cdot h_W(m)
$$

Now let's define 2 vectors. The first is a vector of the **past L samples of our noisy signal y**, up to the present sample at time n, (bold face font to indicate that it is a vector)

$$\large
\boldsymbol y(n)=[y(n-L+1),...,y(n-1),y(n)]$$

The next vector contains the **time-reversed impulse response**,

$$\large
\boldsymbol h_W=[h_W(L-1),...,h_W(1),h_W(0)]
$$

Using those 2 vectors, we can rewrite our convolution equation above as a vector multiplication,

$$\large
x(n)= \boldsymbol y(n) \cdot \boldsymbol {h_W}^T
$$

**Observe** that $\boldsymbol h_W$ has no time index because it already contains all the samples of the time-reversed impulse response, and is constant.

We can now also put the output signal x(n) into the **row vector**,

$$\large
\boldsymbol x =[x(0),x(1),...]
$$

To obtain this column vector, we simply assemble all the row vectors of our noisy signal $\boldsymbol y(n)$ into a matrix $\boldsymbol A$,


$$\large
\boldsymbol A =\left[\matrix{\boldsymbol y(0) \\ \boldsymbol y(1) \\ \vdots  } \right] $$

With this matrix, we obtain the result of our convolution at all time steps n:

$$\large
\boldsymbol  A \cdot \boldsymbol  {h_W}^T = \boldsymbol  x^T$$


For the example of a filter length of $h_W$ of L=2 we have,

$$
  \begin{bmatrix}y(0)  y(1) \\ y(1)  y(2) \\ y(2)  y(3)\\ \vdots  \vdots \end{bmatrix}  \cdot \begin{bmatrix}h_W(1) \\ h_W(0) \end{bmatrix}  = \begin{bmatrix}{ x(0) \\  x(1) \\ x(2) \\ \vdots  }\end{bmatrix}  $$

**Observe** again that the vector $\boldsymbol h_w$ in this equation is the time-reversed impulse response of our filter. This is the **matrix multiplication** formulation of our **convolution**.

We can now obtain the minimum mean squared error **solution** of this matrix multiplication using the so-called Moore-Penrose **Pseudo Inverse**:

$$\large
\boldsymbol A^T \cdot \boldsymbol A \cdot \boldsymbol {h_W}^T = \boldsymbol A ^T \cdot \boldsymbol x^T
$$

Here, $\boldsymbol A ^T \cdot \boldsymbol A$ is now a square matrix, and usually invertible, such that we obtain our solution

$$\large
\boldsymbol {h_W}^T = (\boldsymbol A ^T \cdot \boldsymbol A) ^{-1} \boldsymbol A ^T \cdot \boldsymbol x^T$$

This pseudo-inverse finds the column vector $\boldsymbol h^T$ which minimizes the distance to a given $\boldsymbol x$ with the matrix $\boldsymbol A$ (which contains our signal to be filtered). This $\boldsymbol h_w$ is now the **solution** we where looking for. This solution has the minimum mean squared distance to the un-noisy version of all solutions.

## The data

To structure and test the first class of your audio data analysis pipeline, the denoiser, a possibility is to use the clean subset of audio tracks in the Freesound mono audio track dataset, [DBR-dataset](https://zenodo.org/records/1069747), first adding white random noise to each track, and then, trying to remove the white noise from the signal.

Using the same dataset you can also train/test your classifier.

Once tested the audio analysis pipeline on this dataset you are requested to create a small data set yourself, registering similar audio tracks and paying attention to the standardization of the input data.


## Useful tools
To convert the audio tracks into signals treatable with Scipy you can use the PyAudio library. 

To construct the Wiener filter you can use the Scipy and Numpy libraries.

To convert the audio tracks into images you can apply padding yourself, using the library previously cited, or you can use a dedicated function from the Librosa library.



