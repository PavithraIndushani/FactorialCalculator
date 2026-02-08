interface Document {
void print();
void scan();
void fax();
}

class SimplePrinter implements Document {
@Override
public void print() {
// Print the document
}
@Override
public void scan() {
// Not applicable for
SimplePrinter
}
@Override
public void fax() {
// Not applicable for
SimplePrinter
}
}
class Photocopier implements Document {
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