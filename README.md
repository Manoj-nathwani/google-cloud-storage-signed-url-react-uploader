## What we want
- Upload files directly to Google Cloud Storage without having it go via our App Engine instance as it eats up all the memory and crashes the instance.
- We want to upload these files within a complex react application, not just a single `<Form>` dedicated to a single file upload.
- We want everything secured using the [Signed URLs API](https://cloud.google.com/storage/docs/access-control/signed-urls)


## What's the problem?
- Unfortunately the Signed URLs API only supports `storage.googleapis.com` via [PUT requests](https://cloud.google.com/storage/docs/access-control/signing-urls-with-helpers#code-samples) which do not support CORS
- The catch is that the only domain which supports CORS is `<my-bucket>.storage.googleapis.com` as it uses [Cross-origin resource sharing](https://cloud.google.com/storage/docs/cross-origin) settings, so if you want to upload files via a browser it isn't possible.

## The solution
- [Generate a signed POST](https://cloud.google.com/storage/docs/xml-api/post-object#python) which allows you to use it in a HTML form which also has this awesome `success_action_redirect` settubg which we can use to redirect back to our app once completed.
- The above along with some fairly simple iframe and react work allows you to fully create a react element which allows you to upload multiple files one-by-one and have them display on the page once completed.
- Obviously you'll have to add authentication EVERYWHERE as this is a super minimal example

## How it works
- The homepage displays a `Add file` button
- Every time you click it a new iframe is appended to the page
- Each iframe is a window to `/file_upload` which renders a single file uploader.
- Once a file is successfully uploaded to google cloud storage it displays the file in the browser directly from Google Cloud Storage

That's all!

Now you'll just have to add authentication to everything to stop bad guys spamming files to your GCP account and you're done 🚀

![](https://i.imgur.com/Yzws9o7.png)
