#include <iostream>
using namespace std;

#define SIZE 50

class Person {
    int id;
    char name[SIZE];

public:
    virtual void aboutMe() {
	cout << "I am a person.";
    }
    ~Person() {
	cout << "Delete a person." << endl;
    }
};

class Student : public Person {
public:
    void aboutMe() {
	cout << "I am a student." << endl;
    }
}; 

void test1() {
    Student stu;
    stu.aboutMe();
}


class Base {
public:
    virtual void show() {cout<<"Base class\n"; }
    void p() {cout<<"parent p\n";}
};

class Deri: public Base {
public:
    void show() {cout<<"Derived\n";}
    void p() {cout<<"child p\n";}

};

void test2() {
    Base *bp = new Deri;
    //Base *bp = new Base;
    bp->Base::p();
}

int main(int argc, char *argv[])
{
    test2();
    return 0;
}

