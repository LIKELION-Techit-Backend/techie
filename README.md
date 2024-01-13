# techie

### How to deploy to AWS Beanstalk

1. Zip the current repo using the following command. Below command ensures the hidden `.ebextensions` folder gets included.
    ```bash
    zip -r ../techit.zip \.* *
    ```
2. Go to `config/settings.py` and set `DEBUG` to `False`.
3. Go visit AWS beanstalk and just upload the zip file and deploy.