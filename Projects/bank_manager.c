#include <stdlib.h>
#include <stdio.h>
// #include <windows.h>

int i, j;
int main_exit;

void menu();
struct date
{
    int day, month, year;
};

struct
{
    char name[60];
    int acc_no, age;
    char adresse[60];
    char citizenship[15];
    double phone;
    char acc_type[10];
    float amt;  
    struct date dob;
    struct date deposite;
    struct date withdraw;
} add, upd, check, rem, transaction;


float interest(float rate, float t, int amount)
{
    float SI;
    SI = (rate*t*amount)/100.0;
    return (SI);
}

void fordelay(int j)
{
    int i, k;
    for(i=0; i<j; i++)
        i=k;
}

void new_acc()
{
    int choice;
    FILE *ptr;

    ptr=fopen("record.dat", "a+");
    account_no:
    system("cls");
    printf("\t\t\t\xB2\xB2\xB2 ADD RECORD \xB2\xB2\xB2\xB2");
    printf()
    scanf
    printf
    scanf

    while (/* condition */)
    {

    }
    
}

