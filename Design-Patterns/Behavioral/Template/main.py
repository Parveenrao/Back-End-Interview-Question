from base_order import OrderProcessor
from upi_order import UPIOrderProcessor
from credit_card import CreditCardOrderProcessor
from cod_order import CashOnDeliveryOrderProcessor


def run(order_process : OrderProcessor) -> None:
    order_process.process_order()



def main()-> None:

    processors : list[OrderProcessor] = [

        UPIOrderProcessor(),
        CreditCardOrderProcessor(),
        CashOnDeliveryOrderProcessor()
    ]    


    for processor in processors:
        print("-" * 40)

        run(processor)


if __name__ == "__main__":
    main()
