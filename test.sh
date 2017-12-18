DAY=$1

for FILE in $(ls sample_inputs/day${1}*); do
    echo -e "$(cat $FILE)\n"
    echo -e "$(./day${1}.py ${FILE})"
    echo -e "-----"
done
