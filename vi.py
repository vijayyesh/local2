vijay
{
    "Version": "2012-10-17",
    "Id": "unique-id-to-describe-below-statement",
    "Statement": [
        {
            "Sid": "unique-sid",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::bucket_name/*"
        }
    ]
}