git add -A
echo "Enter to commit"
read varname
git commit --all -m "$1"
echo "Enter to push"
read varname
git push
