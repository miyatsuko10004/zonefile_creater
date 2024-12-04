import os
from dotenv import load_dotenv

def generate_dns_cnames():
    # Load environment variables from .env file
    load_dotenv()

    # Fetch the ELB domain from environment variable
    elb_domain = os.getenv("ELB_DOMAIN")
    if not elb_domain:
        raise ValueError("ELB_DOMAIN is not set in the .env file.")

    # Define the base domain
    base_domain = "testview{}.viewtest.net"

    # Define the output file path
    output_file = "dns_cnames.txt"

    # Open the file for writing
    with open(output_file, 'w') as f:
        # Generate CNAME records for testview1000 to testview1500
        for i in range(1000, 1501):
            # Format each line: domain TTL CNAME target
            record = f"{base_domain.format(i)} 300s CNAME {elb_domain}\n"
            f.write(record)

    print(f"DNS CNAME records have been generated in {output_file}")

# Run the function
generate_dns_cnames()
