#include <stdio.h>
#include <string.h>

//number of customers the program can handle
#define NUM_C 3 

//customer data structure
struct customer{
	char 	f_name[10];
	char    l_name[15];
	int	balance;
};

//customer database as array of structs
struct customer customers[NUM_C];

//function to print binary representation of the database
int print_customers_b(){
	for (int i = 0; i < NUM_C; i++) {
        printf("Customer %d:\n", i);
        printf("First Name (binary): ");
        for (size_t j = 0; j < sizeof(customers[i].f_name); j++) {
            printf("%02x ", customers[i].f_name[j]);
        }
        printf("\n");

        printf("Last Name (binary): ");
        for (size_t j = 0; j < sizeof(customers[i].l_name); j++) {
            printf("%02x ", customers[i].l_name[j]);
        }
        printf("\n");

        printf("Balance (binary): ");
        unsigned char *ptr = (unsigned char *)&customers[i].balance;
        for (size_t j = 0; j < sizeof(customers[i].balance); j++) {
            printf("%02x ", ptr[j]);
        }
        printf("\n");

        printf("\n");
    }
	return(0);
}

//print out the content of our costomer database
int print_customers(){
	int i;
	for(i = 0; i < NUM_C; i++){
		printf("Customer %d   :\n", i);
		printf("   First Name: %s\n", customers[i].f_name);
		printf("   Last Name : %s\n", customers[i].l_name);
		printf("   Balance   : %d\n", customers[i].balance);
	}
	return(0);
}

// function to update forename
int update_f_name(int id, char* f_name){
	strcpy(customers[id].f_name, f_name);
	return(0);
}

// function to update lastname
int update_l_name(int id, char* l_name){
	strcpy(customers[id].l_name, l_name);
	return(0);
}

// function to update an entire customer record
int update_customer(int id, char* f_name, char* l_name){
	strcpy(customers[id].f_name, f_name);
	strcpy(customers[id].l_name, l_name);
	return(0);
}

// function to update balance
int update_balance(int id, int balance){
	customers[id].balance = balance;
	return(0);
}

// a function to populate the database 
// (might be from file or network in a practical setting)
int add_customers(){
	update_customer(0, "Utz", "Roedig");
	update_balance(0,500);
	update_customer(1, "Hans", "Wurst");
	update_balance(1,50000);
	update_customer(2, "Keith", "Richards");
	update_balance(2,100);
	return(0);
}

// our interface for a worker that allows name changes
int edit_customer(){
	int option;
	char f_name[256];
	char l_name[256];

	while (1){
		printf( "\n");
		printf( "p = print customers; ");
		printf( "e = edit customer;");
		printf( "x = exit: ");
   		option = getchar( );
		getchar( );
		switch(option){
			case 112: 
				print_customers();
				break;
			case 101: 
				printf( "Customer ID: ");
   				option = getchar( );
				getchar( );
				option = option - 48;
				if (option<0 || option > NUM_C) {
					printf("no customer record!\n");
					return(0);
				}
				printf("New first name: ");
				fgets(f_name, sizeof(f_name), stdin);
				f_name[strcspn(f_name, "\n")] = 0;
				update_f_name(option, f_name);
				printf("New last name: ");
				fgets(l_name, sizeof(f_name), stdin);
				l_name[strcspn(l_name, "\n")] = 0;
				update_l_name(option, l_name);
				break;
			case 120: 
				return(0);
				break;
			default: 
				break;
		}
		
		print_customers_b();
	}
	
	return(0);
}

int main(void){
	add_customers();

	print_customers();
	
	edit_customer();

	print_customers();
}

