# network/network_segmentation.sh

# Create Docker network segments for different roles
docker network create admin_network
docker network create employee_network

# Run containers with different network access
docker run -d --name admin_container --network admin_network alpine sleep 1000
docker run -d --name employee_container --network employee_network alpine sleep 1000
