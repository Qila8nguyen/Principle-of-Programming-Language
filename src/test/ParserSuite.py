import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_parser01(self):
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 501))

    # #variable declare
    def test_parser02(self):
        input = """abc,bde,this_is,_hello : integer;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 502))

    def test_parser03(self):
        input = """ a03,b_de,this_is,_9_ello : integer = 10,20,9,0; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 503))
    
    def test_parser04(self):
        input = """ eqw,ww : float,"""
        expect = "Error on line 1 col 15: ,"
        self.assertTrue(TestParser.test(input, expect, 504))

    def test_parser05(self):
        input = """ ww,q : float = 1.2,2,2,22; """
        expect = "Error on line 1 col 21: ,"
        self.assertTrue(TestParser.test(input, expect, 505))

    def test_parser06(self):
        input = """ ww,q : float = 1.2; """
        expect = "Error on line 1 col 19: ;"
        self.assertTrue(TestParser.test(input, expect, 506))
    
    def test_parser07(self):
        input = """ a03,b_de,this_is,_9_ello : integer = 10,20,9,0; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 507))

    def test_parser08(self):
        input = """ ww,q : array [10_2,33] of boolean = 2,true; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 508))

    def test_parser09(self):
        input = """ ___s,q : array [1,] of string = 3.2, "inst"; """
        expect = "Error on line 1 col 19: ]"
        self.assertTrue(TestParser.test(input, expect, 509))

    def test_parser10(self):
        input = """ _ : string; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 510))

    def test_parser11(self):
        input = """_,_ : array [1,2] of float;"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 511))

    def test_parser12(self):
        input = """_,_ae : string = "hey", "i just met you";"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 512))

    def test_parser13(self):
        input = """ __2_a3,q_3_,oo : array [4,3] of integer = 3_3_32.2, 11, "inst"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 513))
    
    def test_parser14(self):
        input = """ oh_s : boolean = false; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 514))

    def test_parser15(self):
        input = """ _rr : boolean = true; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 515))

    def test_parser16(self):
        input = """ abcd = true """
        expect = "Error on line 1 col 6: ="
        self.assertTrue(TestParser.test(input, expect, 516))
    
    def test_parser17(self):
        input = """ _ : auto = "sie"; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 517))

    #parameter

    def test_parser18(self):
        input = """ main: function array [2,3] of string ( inherit para : integer) {
                if (min && berry) dosomething();
                else return none[4] % 9;
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 518))

    def test_parser19(self):
        input = """ main: function float (out para : boolean) {
            a[3] = !hey + eui[488,3_2];
            if (you < 3 ) 
                if (min && berry) dosomething();
                else return none[4];

            else {
                makeup();
                break;
                while (1) {
                    dobip(12,32,"sun", functioncall());
                }
            }
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 519))

    def test_parser20(self):
        input = """ main: function integer (para :integer) {} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 520))

    def test_parser21(self):
        input = """main: function auto ( para: array[5_6,0] of string) {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 521))

    def test_parser22(self):
        input = """main: function array [9] of string (inherit trck :integer) parent {
            while (m[0] && t <= x)
                if (x > 89 && min % 2) dododofunc();
                else funct_cal_e();
        }"""
        expect = "Error on line 1 col 59: parent"
        self.assertTrue(TestParser.test(input, expect, 522))

    # thiếu function declare type
    def test_parser23(self):
        input = """ x: integer = 3;
                    ham: function () inherit mother {
                         a90_ = !a[2e-10, -3/2%2] ;
                    } """
        expect = "Error on line 2 col 34: ("
        self.assertTrue(TestParser.test(input, expect, 523))
    
    # sai cách đặt parameter
    def test_parser24(self):
        input = """ tech: function integer (inherit bcd,ee :float) inherit parent {
            do 
                another_job(qji, camera, design);
                if (mintinh + km) {
                    hello();
                } 
            while (tech[3] != hi);
        }  """
        expect = "Error on line 1 col 36: ,"
        self.assertTrue(TestParser.test(input, expect, 524))

    #function declare

    def test_parser25(self):
        input = """this_is_name : function integer (inherit para : boolean, out para2 : integer, delta : float, ss_w : array [3] of integer) {} """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 525))

    def test_parser26(self):
        input = """ this_is_name : function integer (inherit para : boolean, out para2 : integer, delta : float) inherit parent_function {
             var_9 = 3*3+10::29>= 9;
             {
                break;
                continue;
                return nii;
             }
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 526))
    
    def test_parser27(self):
        input = """ this_is_name : function integer () inherit parent_function {
             w019_ee[10_2.e-10, -a[29,100]-2] = im[1,3] / 2 + "sub" && un % "shu"   ;
              _[9*30::"string","ahu"] = -3*3+91;
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 527))

    def test_parser28(self):
        input = """ this_is_9name : function integer (meme: string, arr: array[2] of boolean, out _ej: array[2,9_2] of string) inherit parent01 {
            do {
                return hhh = wlki:"ehu";
            } while (mm[5,0] && gi[3] >= 0);
        } """
        expect = "Error on line 3 col 27: ="
        self.assertTrue(TestParser.test(input, expect, 528))
    
    #Array declare

    def test_parser29(self):
        input = """ arr_decl: array [2_3,3_4_5] of integer; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 529))

    def test_parser30(self):
        input = """ arr_decl, dik: array [2_3,3_0_5] of string; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 530))

    def test_parser31(self):
        input = """ arr_decl, cool, fresh: array [0,3_4_5] of boolean = true, false, true; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 531))

    def test_parser32(self):
        input = """ arr_decl, arr: array [2_3,3_45] of float = 2.393, 39398E-10; """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 532))

    #ASSIGN

    def test_parser33(self):
        input = """ dem: function float () {
                A[9,0] = 3*3;
        }  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 533))
    
    def test_parser34(self):
        input = """ varia: function array [7,2_3] of integer (immi: boolean , out trrr: integer ) {
            goo();
            return mom + "sun" && trrr;
            for (i = 1, i> i, i && 93) return immed;
            do {
                dobydooo();
                legend: integer = "never die";
                substances();
            } while (hello >= hel)
        } """
        expect = "Error on line 10 col 8: }"
        self.assertTrue(TestParser.test(input, expect, 534))

    def test_parser35(self):
        input = """ varia: function array [7,2_3] of integer (immi: boolean , out trrr: integer ) {
            goo();
            return mom + "sun" && trrr;
            for (i = 1, i> i, i && 93) return immed;
            do {
                dobydooo();
                legend: integer = "never die";
                substances();
                if (u < 3 ) printInteger(oo);
                else readInteger();
            } while (hello >= hel);
        } """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 535))

    def test_parser36(self):
        input = """ """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 536))
    
    def test_parser37(self):
        input = """"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 537))

    # IF stmt
    def test_parser38(self):
        input = """ whollu: function boolean () {
            if (i > 0) hehe_23 = "sut";
            else uenei = arp[38,3];
        }  """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 538))

    def test_parser39(self):
        input = """ rigid: function string (){
            if (hu == 3) {
                if (kim >= 9) {
                    oki ();
                }
            } else if (a[93] != 3) call_func();
            else {
                aom = "dhun";
                return pinkky;
            }
        } 
         """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 539))


    def test_parser40(self):
        input = """ varia: function array [7,2_3] of integer (immi: boolean , out trrr: integer ) {
            goo();
            return mom + "sun" && trrr;
            for (i = 1, i> i, i && 93) return immed;
            do {
                dobydooo();
                legend: integer = "never die";
                substances()
            }
        } """
        expect = "Error on line 9 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 540))

    def test_parser41(self):
        input = """{
            r, s: integer; 
            r = 2.0; 
            a, b: array [5] of integer; 
            s = r * r * myPI; 
            a[0] = s;
            }"""
        expect = "Error on line 1 col 0: {"
        self.assertTrue(TestParser.test(input, expect, 541))

    def test_parser42(self):
        input = """x: integer = 65;
        fact: function integer (n: integer) {
            if (n == 0) return 1;
            else return n  * fact(n - 1);
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 542))

    def test_parser0(self):
        """Simple program: integermain() {} """
        input = """main: function void() {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 200))

    def test_parser1(self):
        input = """
            x: integer = 65;
            mess: function void (n: integer){
                return n/50 * 2;
            }
            main: function void () {
                delta: integer = makdhlawkdlqw();
                pri(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_parser2(self):
        input = """
            add: function integer(n: integer){
                sum: integer = 0;
                for (i = 0, i<=n, i+1){
                    sum = sum + i;
                }
                return sum;
            }
            main: function void () {
                delta: integer = add(10);
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_parser3(self):
        input = """
            x: integer = 65;
            fact: function integer(n: integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta: integer = fact(3);
                inc(x,delta);
                printInteger(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_parser4(self):
        input = """
            main: function void () {
                i: integer = 10;
                while (i!=0){
                    i = i - 1;
                }
                return  i;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_parser5(self):
        input = """
            main: function void () {
                i: integer = 10;
                while (i>20){
                    i = i + 2;
                }
                return  i;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))
    
    def test_parser6(self):
        input = """
            voidA: function integer(n: integer){
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_parser7(self):
        input = """
            main: function void () {
                delta: string = "dat";
                printString(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_parser8(self):
        input = """
            main: function void () {
                delta: float = 3.45;
                printFloat(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_parser9(self):
        input = """
            main: function void () {
                delta: boolean = true;
                printBoolean(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_parser10(self):
        input = """
            main: function void () {
                b: array [5] of integer;
                k[4] = 3;
                printInteger(h[4]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_parser11(self):
        input = """
            main: function void () {
                delta: integer = 3+34*30/5*16/4*2/2+19%4+2%2;
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_parser12(self):
        input = """
            main: function void () {
                i: integer = 10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_parser13(self):
        input = """
            main: function void () {
                i: integer = -10;
                do{
                    i = i - 1;
                }
                while (i!=0);
                return  i;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_parser14(self):
        input = """
            main: function void () {
                delta: float = 130.34e2;
                printFloat(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_parser15(self):
        input = """
            main: function void () {
                delta: string = "true";
                printString(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_parser16(self):
        input = """
            voidA: function integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_parser17(self):
        input = """
            voidA: function integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer){
                n = n + 24;
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_parser18(self):
        input = """
            main: function void () {
                delta: boolean = !true&&!false||true||false||!false;
                printBoolean(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))
    
    def test_parser19(self):
        input = """
            main: function void () {
                delta: string;
                delta = "abcd"::"298";
                printBoolean(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))
    
    def test_parser20(self):
        input = """
            main: function void () {
                delta: boolean = true;
                temp: boolean = !delta||false||!false;
                printBoolean(temp);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))
    
    def test_parser21(self):
        input = """
            main: function void () {
                a,c: boolean = true,!false;
                printBoolean(a);
                printBoolean(c);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 221))
        
        
    def test_parser22(self):
        input = """
            main: function void () {
                a,c: string = "true","!false";
                printString(a);
                printString(c);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_parser23(self):
        input = """
            main: function void () {
                a,c: string = "true","!false";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))
        
    def test_parser24(self):
        input = """
            main: function void () {
                a,c: string = "true","det/tsef";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))
        
    def test_parser25(self):
        input = """
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))
        
    def test_parser26(self):
        input = """
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)+24);
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 226))
        
    def test_parser27(self):
        input = """
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)%2);
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))
        
    def test_parser28(self):
        input = """
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34+voidA(3)));
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))
        
    def test_parser29(self):
        input = """
            voidA: function string (s: string){
                i: integer = 4;
                while (i>0){
                    s = s::"qua";
                }
                return s;
            }
            main: function void () {
                delta: string = "av";
                delta = voidA(delta);
                printString(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))
        
    def test_parser30(self):
        input = """
            voidAB: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(23);
                delta = delta/2 + delta/2/3;
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 230))
        
    def test_parser31(self):
        input = """
            voidA: function integer(n: array[5] of integer){
                return n[4];
            }
            main: function void () {
                delta: integer = 34+-4--5;
                delta = delta*2;
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_parser32(self):
        input = """
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        continue;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_parser33(self):
        input = """
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        break;
                    }
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_parser34(self):
        input = """
            main: function void () {
                for (i = 10, i >= 0, i - 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        break;
                    }
                }
                return;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_parser35(self):
        input = """
            s: string = "daylastring";
            main: function void () {
                printString(s);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 235))
        
    def test_parser36(self):
        input = """
            voidAB: function integer(n: integer){
                for (i = n, i >= 0, i - 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        return;
                    }
                }
            }
            main: function void () {
                voidAB(10);
                printInteger("/ndone");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))
        
    def test_parser37(self):
        input = """
            voidAB: function integer(){
                return 4+2;
            }
            main: function void () {
                delta: integer = voidAB();
                printInteger(delta);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 237))
        
    def test_parser38(self):
        input = """
            s: string = "daylastring";
            main: function void () {
                printString(s+"uk");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))
        
    def test_parser39(self):
        input = """
            s: boolean = true;
            main: function void () {
                s = false;
                printBoolean(s);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 239))
        
    def test_parser40(self):
        input = """
            s: float = 5.5;
            main: function void () {
                s = s/7;
                printFloat(s);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 240))
        
    def test_parser41(self):
        input = """
            main: function void () {
                s: integer;
                readInteger(s);
                printInteger(s);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 241))
        
    def test_parser42(self):
        input = """
            main: function void () {
                s: string;
                readString(s);
                printString(s::"acd");
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 242))
        
    def test_parser43(self):
        input = """
            main: function void () {
                s: boolean;
                readBoolean(s);
                printBoolean(s && true || false);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 243))
        
    def test_parser44(self):
        input = """
            main: function void () {
                s: float;
                readFloat(s);
                printFloat(s + 40.9);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 244))
        
    def test_parser45(self):
        input = """
            r, s: integer;
            main: function void () {
                a, b: array [5] of integer;
                r = 2.0;
                s = r * r * myPI;
                a[0] = s;
                printInteger(a[0]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 245))
        
    def test_parser46(self):
        input = """
            r, s: integer = 5,10;
            main: function void () {
                a, b: array [5] of integer;
                s = s * r * myPI;
                a[0] = s;
                printInteger(a[0]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 246))
        
    def test_parser47(self):
        input = """
            main: function void () {
                a, b: array [5] of integer;
                a[0] = 12;
                b[1] = a[0];
                printInteger(b[1]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 247))

    def test_parser48(self):
        input = """
            main: function void () {
                a, b: array [5] of integer;
                a[0] = 2;
                a[3] = 4;
                b[1] = a[1 + a[0]];
                printInteger(b[1]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 248))

    def test_parser49(self):
        input = """
            main: function void () {
                a: array [5,2] of integer;
                a[0,1] = 2;
                printInteger(a[0,1] + 2);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 249))

    def test_parser50(self):
        input = """
            main: function void () {
                a: array [5,2] of integer;
                a[0,1] = 2;
                a[0,2] = 5;
                printInteger(a[0,1] + a[0,2]);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 250))
        
    def test_parser51(self):
        input = """
            x integer = 65;
            mess: function integer(n: integer){
                return n/50 * 2;
            }
            main: function void () {
                delta: integer = mess(7);
                printInteger(delta);
            }
        """
        expect = "Error on line 2 col 14: integer"
        self.assertTrue(TestParser.test(input, expect, 251))

    def test_parser52(self):
        input = """
            add: function integer(n: integer){
                integer = 0;
                for (i = 0, i<=n, i+1){
                    sum = sum + i;
                }
                return sum;
            }
            main: function void () {
                delta: integer = add(10);
                printInteger(delta);
            }
        """
        expect = "Error on line 3 col 16: integer"
        self.assertTrue(TestParser.test(input, expect, 252))

    def test_parser53(self):
        input = """
            x: integer65;
            fact: function integer(n: integer){
                if (n == 0) return 1;
                else return n * fact(n-1);
            }
            inc: function void (out n: integer, delta: integer){
                n = n + delta;
            }
            main: function void () {
                delta := fact(3);
                inc(x,delta);
                printInteger(x);
            }
        """
        expect = "Error on line 2 col 15: integer65"
        self.assertTrue(TestParser.test(input, expect, 253))

    def test_parser54(self):
        input = """
            main: function void () {
                i: integer = 10;
                while (i=0){
                    i--;
                }
                return  i;
            }
        """
        expect = "Error on line 4 col 24: ="
        self.assertTrue(TestParser.test(input, expect, 254))

    def test_parser55(self):
        input = """
            function void () {
                i: integer = 10;
                while (i>20){
                    i+=2;
                }
                return  i;
            }
        """
        expect = "Error on line 2 col 12: function"
        self.assertTrue(TestParser.test(input, expect, 255))

    def test_parser56(self):
        input = """
            voidA: function integer(n: integer){
                return n%/10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = "Error on line 3 col 25: /"
        self.assertTrue(TestParser.test(input, expect, 256))

    def test_parser57(self):
        input = """
            main: function () {
                delta: string = "dat";
                printString(delta);
            }
        """
        expect = "Error on line 2 col 27: ("
        self.assertTrue(TestParser.test(input, expect, 257))

    def test_parser58(self):
        input = """
            main: function void () {
                delta: float == 3.45;
                printFloat(delta);
            }
        """
        expect = "Error on line 3 col 29: =="
        self.assertTrue(TestParser.test(input, expect, 258))

    def test_parser59(self):
        input = """
            main: function void () {
                delta: boolean = true;
                printBoolean(delta++);
            }
        """
        expect = "Error on line 4 col 35: +"
        self.assertTrue(TestParser.test(input, expect, 259))

    def test_parser60(self):
        input = """
            main: function void () {
                b: array [5] integer = [1,2,3,4,6];
                printInteger(b[4]);
            }
        """
        expect = "Error on line 3 col 29: integer"
        self.assertTrue(TestParser.test(input, expect, 260))

    def test_parser61(self):
        input = """
            main: function void () {
                delta: integer = 3+/2;
                printInteger(delta);
            }
        """
        expect = "Error on line 3 col 35: /"
        self.assertTrue(TestParser.test(input, expect, 261))

    def test_parser62(self):
        input = """
            main: function void () {
                i: integer = 10;
                {
                    i = i - 1;
                }
                while (i!=0)
                return  i;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 262))
    
    def test_parser63(self):
        input = """
            main: function void () {
                i: integer = 10;
                do{
                    i = i - 1;
                }
                while (i!=0)
                return  i;
            }
        """
        expect = "Error on line 8 col 16: return"
        self.assertTrue(TestParser.test(input, expect, 263))

    def test_parser64(self):
        input = """
            main: function void () {
                i: integer = -10;
                do{
                    i = i++;
                }
                while (i!=0);
                return  i;
            }
        """
        expect = "Error on line 5 col 26: +"
        self.assertTrue(TestParser.test(input, expect, 264))

    def test_parser65(self):
        input = """
            main: function void () {
                delta:= 34e2
                printFloat(delta);
            }
        """
        expect = "Error on line 3 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 265))

    def test_parser66(self):
        input = """
            main: function void () {
                delta: string = "true";
                4 = 5;
                printString(delta);
            }
        """
        expect = "Error on line 4 col 16: 4"
        self.assertTrue(TestParser.test(input, expect, 266))

    def test_parser67(self):
        input = """
            voidA: integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = "Error on line 2 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 267))

    def test_parser68(self):
        input = """
            voidA: function integer(n: integer) inherit voidB{
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(de,);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = "Error on line 6 col 33: )"
        self.assertTrue(TestParser.test(input, expect, 268))

    def test_parser69(self):
        input = """
            voidA: function integer(n: integer) inheri voidB{
                return n%10;
            }
            voidB: function void (out n: integer, delta: integer){
                n = n + voidA(delta);
            }
            main: function void () {
                delta: integer = 5;
                voidB(x,delta);
                printInteger(x);
            }
        """
        expect = "Error on line 2 col 48: inheri"
        self.assertTrue(TestParser.test(input, expect, 269))

    def test_parser70(self):
        input = """
            main: function void () {
                delta: bool = !true&&!false||true||false||!false;
                printBoolean(delta);
            }
        """
        expect = "Error on line 3 col 23: bool"
        self.assertTrue(TestParser.test(input, expect, 270))

    def test_parser71(self):
        input = """
            main: function void () {
                delta: string;
                delta = "abcd":"298";
                printBoolean(delta);
            }
        """
        expect = "Error on line 4 col 30: :"
        self.assertTrue(TestParser.test(input, expect, 271))

    def test_parser72(self):
        input = """
            main: function void () {
                delta: boolean = true;
                temp: boolean = !delta false||!false;
                printBoolean(temp);
            }
        """
        expect = "Error on line 4 col 39: false"
        self.assertTrue(TestParser.test(input, expect, 272))

    def test_parser73(self):
        input = """
            main: function void () {
                a,c: boolean = true,!false;
                printBoolean;
                printBoolean(c);
            }
        """
        expect = "Error on line 4 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 273))

    def test_parser74(self):
        input = """
            main: function void () {
                a,b: string = "!false";
                printString(a);
                printString(c);
            }
        """
        expect = "Error on line 3 col 38: ;"
        self.assertTrue(TestParser.test(input, expect, 274))

    def test_parser75(self):
        input = """
            main: function void () {
                a,c: string : "true","!false";
                v: string = a::c;
                printString(a);
                printString(v);
            }
        """
        expect = "Error on line 3 col 28: :"
        self.assertTrue(TestParser.test(input, expect, 275))

    def test_parser76(self):
        input = """
            main: function void () {
                a,c: string = "true","det\tsef";
                v: string = a::c;
                printString(a)
            }
        """
        expect = "Error on line 6 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 276))

    def test_parser77(self):
        input = """
            voidA: function integer(n: integer){
                return n+4+;
            }
            main: function void () {
                delta: integer = voidA(voidA(34));
                printInteger(delta);
            }
        """
        expect = "Error on line 3 col 27: ;"
        self.assertTrue(TestParser.test(input, expect, 277))

    def test_parser78(self):
        input = """
            voidA: function int{
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)+24);
                printInteger(delta);
            }
        """
        expect = "Error on line 2 col 28: int"
        self.assertTrue(TestParser.test(input, expect, 278))

    def test_parser79(self):
        input = """
            voidA: function integer(n: integer){
                n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA(34)%2);
                printInteger(delta);
            }
        """
        expect = "Error on line 3 col 17: +"
        self.assertTrue(TestParser.test(input, expect, 279))

    def test_parser80(self):
        input = """
            voidA: function integer(n: integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(voidA34+voidA(3)));
                printInteger(delta);
            }
        """
        expect = "Error on line 6 col 56: )"
        self.assertTrue(TestParser.test(input, expect, 280))

    def test_parser81(self):
        input = """
            main: function void () {
                delta string = "av";
                delta = voidA(delta);
                printString(delta);
            }
        """
        expect = "Error on line 3 col 22: string"
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_parser82(self):
        input = """
            voidAB: function integer(n integer){
                return n+4+2;
            }
            main: function void () {
                delta: integer = voidA(23);
                delta = delta/2 + delta/2/3;
                printInteger(delta);
            }
        """
        expect = "Error on line 2 col 39: integer"
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_parser83(self):
        input = """
            main: void () {
                delta: integer = 34+-4--5;
                delta = delta*2;
                printInteger(delta);
            }
        """
        expect = "Error on line 2 col 18: void"
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_parser84(self):
        input = """
            main: function void () {
                for (i = 1, i < 10, i + 1) {
                    if (4*2 >> i){
                        writeInt(i);
                        continue;
                    }
                }
            }
            //m cmt
        """
        expect = "Error on line 4 col 29: >"
        self.assertTrue(TestParser.test(input, expect, 284))
    
    def test_parser85(self):
        input = """
            main: function void () {
                for (i = 1, i < 10; i + 1) {
                    if (4*2 > i){
                        writeInt(i);
                        break;
                    }
                }
            }
        """
        expect = "Error on line 3 col 34: ;"
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_parser86(self):
        input = """
            main: function void () {
                for (i = 10, i >= 0, i = i- 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        break;
                    }
                }
                return;
            }
        """
        expect = "Error on line 3 col 39: ="
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_parser87(self):
        input = """
            s: string = "daylastring";
            main: function void () {
                (s);
            }
        """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_parser88(self):
        input = """
            voidAB: function integer(n: integer,){
                for (i = n, i >= 0, i - 1) {
                    if (4*2 > i){
                        writeInt(i*2);
                        return;
                    }
                }
            }
            main: function void () {
                voidAB(10);
                printInteger("/ndone");
            }
        """
        expect = "Error on line 2 col 48: )"
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_parser89(self):
        input = """
            voidAB: function integer(){
                return 4+2;
            }
            main: function void () {
                delta: integer = ();
                printInteger(delta);
            }
        """
        expect = "Error on line 6 col 33: ("
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_parser90(self):
        input = """
            s: string = "daylastring";
            main: function void () {
                printString(s::);
            }
        """
        expect = "Error on line 4 col 31: )"
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_parser91(self):
        input = """
            s: boolean = true;
            main: function void () {
                s = false;
                printBoolean(s);
                return
            }
        """
        expect = "Error on line 7 col 12: }"
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_parser92(self):
        input = """
            s: floa = 5.5;
            main: function void () {
                s = s/7;
                printFloat(s);
            }
        """
        expect = "Error on line 2 col 15: floa"
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_parser93(self):
        input = """
            main: function void () 
                s: integer;
                readInteger(s);
                printInteger(s);
            }
        """
        expect = "Error on line 3 col 16: s"
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_parser94(self):
        input = """
            main: function void () {
                s: string;
                readString(s);
                printString(s:io:"acd");
            }
        """
        expect = "Error on line 5 col 29: :"
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_parser95(self):
        input = """
            main: function void () {
                s: boolean;
                readBoolean(s);
                printBoolean(s && && true || false);
            }
        """
        expect = "Error on line 5 col 34: &&"
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_parser96(self):
        input = """
            main: function void () {
                s float;
                readFloat(s);
                printFloat(s + 40.9);
            }
        """
        expect = "Error on line 3 col 18: float"
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_parser97(self):
        input = """
            r, s: integer;
            main: function void () {
                a, b: array [5] of integer;
                r = 2.0;
                s = r * r * ;
                a[0] = s;
                printInteger(a[0]);
            }
        """
        expect = "Error on line 6 col 28: ;"
        self.assertTrue(TestParser.test(input, expect, 297))
    
    def test_parser98(self):
        input = """
            r, s = 5,10;
            main: function void () {
                a, b: array [5] of integer;
                s = s * r * myPI;
                a[0] = s;
                printInteger(a[0]);
            }
        """
        expect = "Error on line 2 col 17: ="
        self.assertTrue(TestParser.test(input, expect, 298))
    
    def test_parser99(self):
        input = """
            r, s: integer = 5;10;
            main: function void () {
                a, b: array [5] of integer;
                s = s * r * myPI;
                a[0] = s;
                printInteger(a[0]);
            }
        """
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.test(input, expect, 299))
    
    def test_parser100(self):
        input = """
            main: function void () {
                a, b: array [5] of integer;
                a[0,] = 12;
                b[1] = a[0];
                printInteger(b[1]);
                c = {32,2309,333}
                c = {"eww", "q390", "ddd"}
            }
        """
        expect = "Error on line 4 col 20: ]"
        self.assertTrue(TestParser.test(input, expect, 300))

