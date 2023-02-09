# Simple Translation App

This is a simple translation app that uses Amazon Web Services (AWS) to provide a user-friendly interface for translating text. The app makes use of the following AWS services:

- Lambda function: To process the text, source language, and target language inputs and perform the translation.
- API Gateway: To invoke the Lambda function for the frontend.
- S3 bucket: To host the frontend webpage.
- Cloudfront: To serve the webpage hosted on the S3 bucket.
- Route53: To route custom domains to the API Gateway and CloudFront
- Cert manager: To create ssl certs to be able to use HTTPS
# Frontend

The frontend of the app is built using Bootstrap, jQuery, HTML, and CSS. It provides a simple page for users to input the text to be translated, choose the source and    target languages, and get the translated text. The page is hosted on a private S3 bucket and served through Cloudfront, making it accessible at https://translate.letstrack.nl .

# Supported Languages

The app supports most of the languages with an auto detect feature. The user can choose the source and target languages from the dropdown menus on the frontend page.

# Error Handling

The app includes error handling to ensure a smooth user experience. If an error occurs during the translation process, the app will display an error message to the user.

# Future Improvements

Future improvements could include adding more language options, improving the translation accuracy, and enhancing the frontend design.

# Conclusion

This simple translation app demonstrates the capabilities of AWS services for building a user-friendly and efficient translation tool. With its simple interface and comprehensive error handling, it provides a smooth user experience for anyone looking to translate text quickly and easily.



