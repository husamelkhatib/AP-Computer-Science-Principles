# dotnet tool install -g dotnet-script
export PATH="$PATH:/home/runner/.dotnet/tools"
export DOTNET_ROOT=$(dirname $(readlink -f $(which dotnet)))

# Run with "bash setup.sh"