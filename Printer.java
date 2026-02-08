interface Printer {
void print();
}
interface Scanner {
void scan();
}
interface FaxMachine {
void fax();
}
class SimplePrinter implements Printer {
@Override
public void print() {
// Print the document
}
}
class Photocopier implements Printer,
Scanner, FaxMachine {
@Override
public void print() {
// Print the document
}
@Override
public void scan() {
// Scan the document
}
@Override
public void fax() {
// Fax the document
}
}