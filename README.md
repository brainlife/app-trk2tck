[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.100-blue.svg)](https://doi.org/10.25663/bl.app.100)

# app-trk2tck
This App converts a .trk file (TrackVis format) to a .tck file (MRtrix format) using NiBabel.

### Author
- [Soichi Hayashi](hayashis@iu.edu)

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your publications and code reusing this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations
We kindly ask that you cite the following articles when publishing papers and code using this code. 

1. Tournier, J.‐D., Calamante, F. and Connelly, A. (2012), MRtrix: Diffusion tractography in crossing fiber regions. Int. J. Imaging Syst. Technol., 22: 53-66. [https://doi.org/10.1002/ima.22005](https://doi.org/10.1002/ima.22005)

2. Avesani, P., McPherson, B., Hayashi, S. et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. Sci Data 6, 69 (2019). [https://doi.org/10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## Running the app
### On [Brainlife.io](http://brainlife.io/) 
You can submit this App online at [https://doi.org/10.25663/bl.app.100](https://doi.org/10.25663/bl.app.100) via the "Execute" tab.

Input: \
A .trk file (TrackVis format).

Output: \
A .tck file (MRtrix format).

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
  "trk": "./track.trk",
}
```

3. Launch the App by executing `main`

```bash
./main
```

### Output
The output file, called `track.tck`, will be generated under the current working directory (pwd). 

#### Product.json
The secondary output of this app is `product.json`. This file allows web interfaces, DB and API calls on the results of the processing. 

### Dependencies
This App only requires [singularity](https://www.sylabs.io/singularity/) to run. If you don't have singularity, you will need to install following dependencies:
* NiBabel >=2.2.0: https://nipy.org/nibabel/

#### MIT Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University
