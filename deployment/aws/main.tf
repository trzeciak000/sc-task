module "simple-eks" {
  source  = "vistaprint/simple-eks/aws"
  version = "0.4.0"
  cluster_name = "sc-task-cluster"
  profile = "sc-task"
  region = "eu-central-1"
  cluster_version = 1.24
  vpc_name = "sc-task-vpc"
}

