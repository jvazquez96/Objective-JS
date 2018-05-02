# This only works on macOS since HomeBrew is only for macOS
echo "Installing Homebrew"
if test ! $(which brew); then
    echo "Installing homebrew..."
    ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi
echo "Installing Python 3"
brew install python3
echo "Install Antlr4 Runtime"
pip3 install antlr4-python3-runtime
echo "Installing or updating git"
brew install git