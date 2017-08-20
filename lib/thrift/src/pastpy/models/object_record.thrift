namespace * pastpy.models

include "thryft/native/date_time.thrift"

struct ObjectRecord {
    // C,15
    optional string accessno;

    // M,4
    optional string accessory;

    // N,12,2
    optional decimal.Decimal acqvalue;

    // C,10
    optional string age;

    // M,4
    optional string appnotes;

    // M,4
    optional string appraisor;

    // C,25
    optional string assemzone;

    // C,15
    optional string bagno;

    // C,15
    optional string boxno;

    // M,4
    optional string caption;

    // C,1
    optional string cat;

    // C,25
    optional string catby;

    // D,8
    optional date_time.DateTime catdate;

    // C,15
    optional string cattype;

    // C,25
    optional string chemcomp;

    // N,16,10
    optional decimal.Decimal circum;

    // N,16,10
    optional decimal.Decimal circumft;

    // N,16,10
    optional decimal.Decimal circumin;

    // M,4
    optional string classes;

    // D,8
    optional date_time.DateTime colldate;

    // C,75
    optional string collection;

    // M,4
    optional string collector;

    // D,8
    optional date_time.DateTime conddate;

    // C,25
    optional string condexam;

    // C,35
    optional string condition;

    // M,4
    optional string condnotes;

    // C,20
    optional string count;

    // M,4
    optional string creator;

    // M,4
    optional string creator2;

    // M,4
    optional string creator3;

    // M,4
    optional string credit;

    // C,20
    optional string crystal;

    // M,4
    optional string culture;

    // N,12,2
    optional decimal.Decimal curvalmax;

    // N,12,2
    optional decimal.Decimal curvalue;

    // C,15
    optional string dataset;

    // C,50
    optional string date;

    // M,4
    optional string datingmeth;

    // C,15
    optional string datum;

    // N,16,10
    optional decimal.Decimal depth;

    // N,16,10
    optional decimal.Decimal depthft;

    // N,16,10
    optional decimal.Decimal depthin;

    // M,4
    optional string descrip;

    // N,16,10
    optional decimal.Decimal diameter;

    // N,16,10
    optional decimal.Decimal diameterft;

    // N,16,10
    optional decimal.Decimal diameterin;

    // M,4
    optional string dimnotes;

    // N,1
    optional i32 dimtype;

    // C,10
    optional string dispvalue;

    // N,4
    optional i32 earlydate;

    // M,4
    optional string elements;

    // C,25
    optional string epoch;

    // C,25
    optional string era;

    // M,4
    optional string event;

    // C,1
    optional string ew;

    // D,8
    optional date_time.DateTime excavadate;

    // M,4
    optional string excavateby;

    // C,36
    optional string exhibitid;

    // N,7
    optional i32 exhibitno;

    // M,4
    optional string exhlabel1;

    // M,4
    optional string exhlabel2;

    // M,4
    optional string exhlabel3;

    // M,4
    optional string exhlabel4;

    // D,8
    optional date_time.DateTime exhstart;

    // C,35
    optional string family;

    // M,4
    optional string feature;

    // T,8
    optional date_time.DateTime flagdate;

    // M,4
    optional string flagnotes;

    // C,20
    optional string flagreason;

    // C,25
    optional string formation;

    // C,25
    optional string fossils;

    // M,4
    optional string found;

    // C,20
    optional string fracture;

    // M,4
    optional string frame;

    // C,35
    optional string framesize;

    // C,35
    optional string genus;

    // C,45
    optional string gparent;

    // C,25
    optional string grainsize;

    // M,4
    optional string habitat;

    // C,15
    optional string hardness;

    // N,16,10
    optional decimal.Decimal height;

    // N,16,10
    optional decimal.Decimal heightft;

    // N,16,10
    optional decimal.Decimal heightin;

    // C,60
    optional string homeloc;

    // M,4
    optional string idby;

    // D,8
    optional date_time.DateTime iddate;

    // M,4
    optional string imagefile;

    // N,3
    optional i32 imageno;

    // C,35
    optional string imagesize;

    // C,30
    optional string inscomp;

    // C,20
    optional string inscrlang;

    // C,40
    optional string inscrpos;

    // C,20
    optional string inscrtech;

    // M,4
    optional string inscrtext;

    // M,4
    optional string inscrtrans;

    // C,20
    optional string inscrtype;

    // D,8
    optional date_time.DateTime insdate;

    // C,25
    optional string insphone;

    // C,20
    optional string inspremium;

    // C,30
    optional string insrep;

    // N,10,2
    optional decimal.Decimal insvalue;

    // C,25
    optional string invnby;

    // D,8
    optional date_time.DateTime invndate;

    // C,20
    optional string kingdom;

    // N,9,6
    optional decimal.Decimal latdeg;

    // N,4
    optional i32 latedate;

    // M,4
    optional string legal;

    // N,16,10
    optional decimal.Decimal length;

    // N,16,10
    optional decimal.Decimal lengthft;

    // N,16,10
    optional decimal.Decimal lengthin;

    // M,4
    optional string level;

    // C,25
    optional string lithofacie;

    // M,4
    optional string loancond;

    // D,8
    optional date_time.DateTime loandue;

    // C,36
    optional string loanid;

    // C,15
    optional string loaninno;

    // N,7
    optional i32 loanno;

    // D,8
    optional date_time.DateTime loanrenew;

    // C,25
    optional string locfield1;

    // C,25
    optional string locfield2;

    // C,25
    optional string locfield3;

    // C,25
    optional string locfield4;

    // C,25
    optional string locfield5;

    // C,40
    optional string locfield6;

    // N,10,6
    optional decimal.Decimal longdeg;

    // C,15
    optional string luster;

    // M,4
    optional string made;

    // C,10
    optional string maintcycle;

    // D,8
    optional date_time.DateTime maintdate;

    // M,4
    optional string maintnote;

    // M,4
    optional string material;

    // M,4
    optional string medium;

    // C,25
    optional string member;

    // M,4
    optional string mmark;

    // C,35
    optional string nhclass;

    // M,4
    optional string nhorder;

    // M,4
    optional string notes;

    // C,1
    optional string ns;

    // C,25
    optional string objectid;

    // C,40
    optional string objname;

    // C,40
    optional string objname2;

    // C,40
    optional string objname3;

    // M,4
    optional string objnames;

    // M,4
    optional string occurrence;

    // C,25
    optional string oldno;

    // M,4
    optional string origin;

    // C,40
    optional string othername;

    // C,25
    optional string otherno;

    // D,8
    optional date_time.DateTime outdate;

    // M,4
    optional string owned;

    // C,40
    optional string parent;

    // M,4
    optional string people;

    // C,25
    optional string period;

    // C,35
    optional string phylum;

    // C,20
    optional string policyno;

    // C,36
    optional string ppid;

    // M,4
    optional string preparator;

    // D,8
    optional date_time.DateTime prepdate;

    // M,4
    optional string preserve;

    // C,25
    optional string pressure;

    // M,4
    optional string provenance;

    // M,4
    optional string pubnotes;

    // M,4
    optional string qrurl;

    // C,30
    optional string recas;

    // C,10
    optional string recdate;

    // M,4
    optional string recfrom;

    // C,36
    optional string relation;

    // M,4
    optional string relnotes;

    // D,8
    optional date_time.DateTime renewuntil;

    // C,40
    optional string repatby;

    // M,4
    optional string repatclaim;

    // D,8
    optional date_time.DateTime repatdate;

    // M,4
    optional string repatdisp;

    // M,4
    optional string repathand;

    // M,4
    optional string repatnotes;

    // D,8
    optional date_time.DateTime repatnotic;

    // C,40
    optional string repattype;

    // C,25
    optional string rockclass;

    // C,25
    optional string rockcolor;

    // C,25
    optional string rockorigin;

    // C,20
    optional string rocktype;

    // C,15
    optional string role;

    // C,15
    optional string role2;

    // C,15
    optional string role3;

    // M,4
    optional string school;

    // C,13
    optional string sex;

    // C,1
    optional string sgflag;

    // M,4
    optional string signedname;

    // M,4
    optional string signloc;

    // C,40
    optional string site;

    // C,30
    optional string siteno;

    // C,10
    optional string specgrav;

    // C,40
    optional string species;

    // C,20
    optional string sprocess;

    // C,25
    optional string stage;

    // C,20
    optional string status;

    // C,25
    optional string statusby;

    // D,8
    optional date_time.DateTime statusdate;

    // M,4
    optional string sterms;

    // C,35
    optional string stratum;

    // C,20
    optional string streak;

    // C,35
    optional string subfamily;

    // M,4
    optional string subjects;

    // M,4
    optional string subspecies;

    // M,4
    optional string technique;

    // C,25
    optional string tempauthor;

    // C,25
    optional string tempby;

    // D,8
    optional date_time.DateTime tempdate;

    // C,25
    optional string temperatur;

    // M,4
    optional string temploc;

    // M,4
    optional string tempnotes;

    // M,4
    optional string tempreason;

    // C,10
    optional string tempuntil;

    // M,4
    optional string texture;

    // M,4
    optional string title;

    // C,25
    optional string tlocfield1;

    // C,25
    optional string tlocfield2;

    // C,25
    optional string tlocfield3;

    // C,25
    optional string tlocfield4;

    // C,25
    optional string tlocfield5;

    // C,40
    optional string tlocfield6;

    // M,4
    optional string udf1;

    // M,4
    optional string udf10;

    // C,20
    optional string udf11;

    // C,20
    optional string udf12;

    // N,12
    optional i32 udf13;

    // N,12,2
    optional decimal.Decimal udf14;

    // N,12,2
    optional decimal.Decimal udf15;

    // N,12,3
    optional decimal.Decimal udf16;

    // N,12,3
    optional decimal.Decimal udf17;

    // D,8
    optional date_time.DateTime udf18;

    // D,8
    optional date_time.DateTime udf19;

    // M,4
    optional string udf2;

    // D,8
    optional date_time.DateTime udf20;

    // M,4
    optional string udf21;

    // M,4
    optional string udf22;

    // M,4
    optional string udf3;

    // M,4
    optional string udf4;

    // M,4
    optional string udf5;

    // M,4
    optional string udf6;

    // M,4
    optional string udf7;

    // M,4
    optional string udf8;

    // M,4
    optional string udf9;

    // C,35
    optional string unit;

    // T,8
    optional date_time.DateTime updated;

    // C,25
    optional string updatedby;

    // M,4
    optional string used;

    // D,8
    optional date_time.DateTime valuedate;

    // M,4
    optional string varieties;

    // M,4
    optional string vexhtml;

    // M,4
    optional string vexlabel1;

    // M,4
    optional string vexlabel2;

    // M,4
    optional string vexlabel3;

    // M,4
    optional string vexlabel4;

    // L,1
    optional bool webinclude;

    // N,16,10
    optional decimal.Decimal weight;

    // N,16,10
    optional decimal.Decimal weightin;

    // N,16,10
    optional decimal.Decimal weightlb;

    // N,16,10
    optional decimal.Decimal width;

    // N,16,10
    optional decimal.Decimal widthft;

    // N,16,10
    optional decimal.Decimal widthin;

    // N,7,2
    optional decimal.Decimal xcord;

    // N,7,2
    optional decimal.Decimal ycord;

    // N,7,2
    optional decimal.Decimal zcord;

    // C,69
    optional string zsorter;

    // C,44
    optional string zsorterx;
}
