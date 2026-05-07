read -p "Enter your grade" grade 

case $grade in
     A|a )
     echo "Excellent"
       ;;
     B|b)
    echo "Good"
       ;;
    C|c)
    echo "Average"
      ;;
    *)
    echo "Invalid"
     ;;
esac
