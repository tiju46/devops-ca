provider "aws" {
  region = "eu-west-1"   # Ireland
}

resource "aws_instance" "myserver" {
  ami = "ami-0c1c30571d2dae5c9"   # Ubuntu
  instance_type = "t3.micro"
  key_name = "tiju-key"


  tags = {
    Name = "simple-docker-server"
  }
}
