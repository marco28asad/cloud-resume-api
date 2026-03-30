import json

def lambda_handler(event, context):
    resume = {
        "name": "Marco Asad",
        "title": "Aspiring Cloud Engineer",
        "location": "Baltimore, MD",
        "email": "marcoasad28@gmail.com",
        "linkedin": "linkedin.com/in/marco-asad-6a56a03ab",
        "github": "github.com/marco28asad",
        "certifications": [
            "CompTIA Network+",
            "CompTIA Security+"
        ],
        "projects": [
            {
                "name": "Cloud Resume API",
                "description": "Built a serverless REST API on AWS using Lambda and API Gateway",
                "tech": ["AWS Lambda", "API Gateway", "Python"]
            }
        ]
    }
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(resume, indent=2)
    }
