# Translation API Demo

## Dependencies
the following dependencies should be installed on your client before deploying this demo
* Google Cloud SDK ([Install gcloud](https://cloud.google.com/sdk/docs/install))
* have a cloud.console account

## Getting started 
Follow these steps to config and deploy the Google translation demo:


1. Clone the repo

    ```
    git clone https://github.com/John-Anthony-L/Translation-API-demo.git
    ```


2. Run the setup.sh file
    ```
    source setup.sh
    ```
    This creates the virtual environment and installs all required packages


3. Edit the constants.py file 

    This file should be updated to reflect your GCP project ID, your naming convensions, and desired parameters. By editing the constants file, you are able to customize how many langauges you want to translate into and thier naming convention.


## to run
In order to run the script, within the command line you will need to create the virtual environment and install the required packages. setup.sh does this for you

after that is successful, please run **demo.py**  **excel file we wish to translate**, note that it is important to have an "English" column to translate. After translation is complete into all reqeusted languages (see constants.py) it will create a file that is identical to the input file with the translated languages added.

### files:
* jam_city_demo.py: the main file which runs the demo
* setup.sh: the setup bash script
* translation_API.py: the translation object
* constants.py: constants which the rest of the project uses
* helper.py: additional functions



<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See `LICENSE` for more information.
