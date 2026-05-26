check_even_odd(){
      if [ $(($1 %2)) -eq 0 ]; then
        echo "Even"
       else
           echo "Odd"
        fi
}
check_even_odd 2

