import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_correct_variable_declaration(self):
        input = "var x int = 10;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_correct_string_declaration(self):
        input = """var y = "Hello";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_correct_string_with_newline(self):
        input = """var y = "Hello \\n";"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_correct_const_declaration(self):
        input = """const pi = 3.14;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_correct_const_expression(self):
        input = """const MaxSize = 100 + 50;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_function_declaration(self):
        input = """func add(x int, y int) int { return x + y; }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_method_declaration(self):
        input = """func (p Person) Speak() string { return "Hello" ;}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_array_access(self):
        input = """var a [2][3]array;
            a[2][3] := b[2] + 1;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_struct_field_access(self):
        input = """type Person struct {
                name string ;
                age int ;
                }
                person.name := "John";
                person.age := 30;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_array_literal(self):
        input = """arr := [3]int{10, 20, 30}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_struct_literal(self):
        input = """q := Person{name: "Alice", age: 30}"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_function_call(self):
        input = """q := add(10, 20)"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_if_statement(self):
        input = """func main() {
            if (x > 10) {
            println("x is greater than 10");
            break;
            } else if x == 10 {
            continue;
            println("x is equal to 10")
            } else {
            println("x is less than 10");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_for_statement_1(self):
        input = """func main() {
                for i < 10 {
                // loop body
                }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_for_statement_2(self):
        input = """func main() {
            for i := 0; i < 10; i+=1 {
            println(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_for_statement_3(self):
        input = """func main() {
            arr := [3]int{10, 20, 30}
            for index, value := range arr {
            // index: 0, 1, 2
            // value: 10, 20, 30
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))


    def test_nested_loops(self):
        input = """func main() {
            for i := 0; i < 10; i+=1 {
            if i % 2 == 0 {
            continue
            break;
            }
            println(i)
            }
            if (i % 2 == 0) {
            continue
            }
            println(i);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))
    def test_nested_if_else(self):
        input = """func main() {
            if x > 10 {
                if y < 5 {
                    println("x > 10 and y < 5");
                } else {
                    println("x > 10 and y >= 5");
                }
            } else {
                println("x <= 10");
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_function_with_no_return_type(self):
        input = """func foo(x int, y int) {
            println(x + y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_function_with_return_type(self):
        input = """func foo(x int, y int) int {
            return x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_function_with_multiple_parameters(self):
        input = """func foo(x int, y int, z int) int {
            return x + y + z;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_function_with_array_parameter(self):
        input = """func foo(arr [3]int) int {
            return arr[0] + arr[1] + arr[2];
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_function_with_struct_parameter(self):
        input = """type Person struct {
            name string;
            age int;
        }
        func foo(p Person) string {
            return p.name;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_function_with_interface_parameter(self):
        input = """type Speaker interface {
            Speak() string;
        }
        func foo(s Speaker) string {
            return s.Speak();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_interface_with_method(self):
        input = """type Speaker interface {
            Speak() string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_struct_with_multiple_fields(self):
        input = """type Person struct {
            name string;
            age int;
            address string;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_struct_with_nested_struct(self):
        input = """type Address struct {
            street string;
            city string;
        }
        type Person struct {
            name string;
            age int;
            address Address;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_struct_with_array_field(self):
        input = """type Person struct {
            name string;
            age int;
            scores [3]int;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_struct_with_interface_field(self):
        input = """type Speaker interface {
            Speak() string;
        }
        type Person struct {
            name string;
            age int;
            speaker Speaker;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_array_declaration(self):
        input = """var arr [3]int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_array_initialization(self):
        input = """var arr [3]int = [3]int{1, 2, 3};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_array_access_in_expression(self):
        input = """var arr [3]int = [3]int{1, 2, 3};
        var x int = arr[0] + arr[1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_multi_dimensional_array(self):
        input = """var arr [2][3]int;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_multi_dimensional_array_initialization(self):
        input = """var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_multi_dimensional_array_access(self):
        input = """var arr [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}};
        var x int = arr[0][1];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_nested_function_calls(self):
        input = """func add(x int, y int) int {
            return x + y;
        }
        func main() {
            var result int = add(add(1, 2), add(3, 4));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_function_call_with_array_argument(self):
        input = """func sum(arr [3]int) int {
            return arr[0] + arr[1] + arr[2];
        }
        func main() {
            var arr [3]int = [3]int{1, 2, 3};
            var result int = sum(arr);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_function_call_with_struct_argument(self):
        input = """type Person struct {
            name string;
            age int;
        }
        func printName(p Person) {
            println(p.name);
        }
        func main() {
            var p Person = Person{name: "John", age: 30};
            printName(p);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_function_call_with_interface_argument(self):
        input = """type Speaker interface {
            Speak() string;
        }
        func printSpeech(s Speaker) {
            println(s.Speak());
        }
        type Person struct {
            name string;
        }
        func (p Person) Speak() string {
            return "Hello, " + p.name;
        }
        func main() {
            var p Person = Person{name: "John"};
            printSpeech(p);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_return_statement_in_function(self):
        input = """func add(x int, y int) int {
            return x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_return_statement_in_void_function(self):
        input = """func foo() {
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_break_statement_in_loop(self):
        input = """func main() {
            for i := 0; i < 10; i+=1 {
                if i == 5 {
                    break;
                }
                println(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_continue_statement_in_loop(self):
        input = """func main() {
            for i := 0; i < 10; i+=1 {
                if i % 2 == 0 {
                    continue;
                }
                println(i);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_nested_loops_with_break_continue(self):
        input = """func main() {
            for i := 0; i < 10; i+=1 {
                for j := 0; j < 10; j+=1 {
                    if j == 5 {
                        break;
                    }
                    if j % 2 == 0 {
                        continue;
                    }
                    println(i, j);
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_variable_declaration_in_loop(self):
        print("test_variable_declaration_in_loop")
        input = """func main() {
            for i := 0; i < 10; i+=1 {
                var x int = i * 2;
                println(x);
            }
        }"""
        
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))
        
    print("test_variable_declaration_in_loop")
    def test_variable_declaration_in_if(self):
        print("test_another")
        input = """func main() {
            if true {
                var x int = 10;
                println(x);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_variable_declaration_in_function(self):
        input = """func foo() {
            var x int = 10;
            println(x);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_variable_declaration_in_struct(self):
        input = """type Person struct {
            name string;
            age int;
        }
        func main() {
            var p Person = Person{name: "John", age: 30};
            println(p.name);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_variable_declaration_in_interface(self):
        input = """type Speaker interface {
            Speak() string;
        }
        type Person struct {
            name string;
        }
        func (p Person) Speak() string {
            return "Hello, " + p.name;
        }
        func main() {
            var p Person = Person{name: "John"};
            println(p.Speak());
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_function_call_with_multiple_arguments(self):
        input = """func add(x int, y int, z int) int {
            return x + y + z;
        }
        func main() {
            var result int = add(1, 2, 3);
            println(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_function_call_with_no_arguments(self):
        input = """func foo() {
            println("Hello");
        }
        func main() {
            foo();
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_function_call_with_expression_arguments(self):
        input = """func add(x int, y int) int {
            return x + y;
        }
        func main() {
            var result int = add(1 + 2, 3 * 4);
            println(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_function_call_with_array_access_arguments(self):
        input = """func sum(arr [3]int) int {
            return arr[0] + arr[1] + arr[2];
        }
        func main() {
            var arr [3]int = [3]int{1, 2, 3};
            var result int = sum(arr);
            println(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_function_call_with_struct_access_arguments(self):
        input = """type Person struct {
            name string;
            age int;
        }
        func printName(name string) {
            println(name);
        }
        func main() {
            var p Person = Person{name: "John", age: 30};
            printName(p.name);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_function_call_with_method_call_arguments(self):
        input = """type Person struct {
            name string;
        }
        func (p Person) Speak() string {
            return "Hello, " + p.name;
        }
        func printSpeech(speech string) {
            println(speech);
        }
        func main() {
            var p Person = Person{name: "John"};
            printSpeech(p.Speak());
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_function_call_with_nested_function_call_arguments(self):
        input = """func add(x int, y int) int {
            return x + y;
        }
        func multiply(x int, y int) int {
            return x * y;
        }
        func main() {
            var result int = add(multiply(2, 3), add(4, 5));
            println(result);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))
    def test_array_Struct(self):
        input = """type Person struct {
            name string;
        }
        func (p Person) Speak() string {
            return "Hello, " + p.name;
        }
        func printSpeech(speech string) {
            println(speech);
            }
        func main() {
            var p [2]Person=[2]Person{Person{name: "John"},Person{name: "pether"}};
            printSpeech(p[0].Speak())
            printSpeech(p[1].Speak())
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))
    def test_array_Struct2(self):
        input = """type Person struct {
            name string;
        }
        func (p Person) Speak() string {
            return "Hello, " + p.name;
        }
        func printSpeech(speech string) {
            println(speech);
            }
        func main() {
            var p [2]Person
            p[0].name:="John";
            p[1].name:="pether";
            printSpeech(p[0].Speak())
            printSpeech(p[1].Speak())
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))
    def test_2array_in_struct_access(self):
        input = """type Person struct {
            name [2]string;
        }
        func (p Person) Speak() string {
            return "Hello, " + p.name;
        }
        func printSpeech(speech string) {
            println(speech);
            }
        func main() {
            var p [2]Person;
            p[0].name[1]="John";
            p[1].name[1]="pether"
    
            printSpeech(p[0].Speak());
            printSpeech(p[1].Speak())
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))
    def test_nested_comments(self):
        input = """/* This is a /* nested */ comment */"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_nested_comments_with_code(self):
        input = """func main() {
            /* This is a /* nested */ comment */
            println("Hello, World!");
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_while_loop(self):
        input = """func main() {
            for x < 10 {
                x += 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))


    def test_function_with_default_parameter(self):
        input = """func foo(x int, y int) int {
            return x + y;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_function_with_variadic_parameter(self):
        input = """func sum(nums int) int {
            total := 0;
            for dsa, num := range nums {
                total += num;
            }
            return total;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_function_with_named_return_values(self):
        input = """func divide(a int, b int) (quotient int, remainder int) {
            quotient = a / b;
            remainder = a % b;
            return;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_type_conversion(self):
        input = """func main() {
            var x int = 42;
            var y float64 = float64(x);
            println(y);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_pointer_declaration(self):
        input = """func main() {
            var x int = 42;
            var p int = x;
            println(p);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_pointer_arithmetic(self):
        input = """func main() {
            var arr [3]int = [3]int{1, 2, 3};
            var p int = arr[0];
            println((p + 1));
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_pointer_to_struct(self):
        input = """type Person struct {
            name string;
            age int;
        }
        func main() {
            var p Person = Person{name: "John", age: 30};
            var ptr Person = p;
            println(ptr.name);
        }"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))
    def test_illegal_var_declaration(self):
        input = """
        const test = a[1].b.d(1,);
        """
        expect = "Error on line 2 col 33: )"
        self.assertTrue(TestParser.checkParser(input,expect,286))
        
    def test_illegal_var_declaration_1(self):
        input = """
        const test = a[1].b.d.;
        """
        expect = "Error on line 2 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,287))
        
    def test_illegal_var_declaration_2(self):
        input = """const test = Student {student hcmut};"""
        expect = "Error on line 1 col 22: {"
        self.assertTrue(TestParser.checkParser(input,expect,288))
        
    def test_illegal_var_declaration_3(self):
        input = """
        const test = a[1,2,4][2];
        """
        expect = "Error on line 2 col 25: ,"
        self.assertTrue(TestParser.checkParser(input,expect,289))