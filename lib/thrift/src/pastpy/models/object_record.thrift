namespace * pastpy.models

include "thryft/native/date_time.thrift"

struct ObjectRecord {
    optional string accessno;

    optional string accessory;

    optional decimal.Decimal acqvalue;

    optional string age;

    optional string appnotes;

    optional string appraisor;

    optional string assemzone;

    optional string bagno;

    optional string boxno;

    optional string caption;

    optional string cat;

    optional string catby;

    optional date_time.DateTime catdate;

    optional string cattype;

    optional string chemcomp;

    optional decimal.Decimal circum;

    optional decimal.Decimal circumft;

    optional decimal.Decimal circumin;

    optional string classes;

    optional date_time.DateTime colldate;

    optional string collection;

    optional string collector;

    optional date_time.DateTime conddate;

    optional string condexam;

    optional string condition;

    optional string condnotes;

    optional string count;

    optional string creator;

    optional string creator2;

    optional string creator3;

    optional string credit;

    optional string crystal;

    optional string culture;

    optional decimal.Decimal curvalmax;

    optional decimal.Decimal curvalue;

    optional string dataset;

    optional string date;

    optional string datingmeth;

    optional string datum;

    optional decimal.Decimal depth;

    optional decimal.Decimal depthft;

    optional decimal.Decimal depthin;

    optional string descrip;

    optional decimal.Decimal diameter;

    optional decimal.Decimal diameterft;

    optional decimal.Decimal diameterin;

    optional string dimnotes;

    optional i32 dimtype;

    optional string dispvalue;

    optional i32 earlydate;

    optional string elements;

    optional string epoch;

    optional string era;

    optional string event;

    optional string ew;

    optional date_time.DateTime excavadate;

    optional string excavateby;

    optional string exhibitid;

    optional i32 exhibitno;

    optional string exhlabel1;

    optional string exhlabel2;

    optional string exhlabel3;

    optional string exhlabel4;

    optional date_time.DateTime exhstart;

    optional string family;

    optional string feature;

    optional date_time.DateTime flagdate;

    optional string flagnotes;

    optional string flagreason;

    optional string formation;

    optional string fossils;

    optional string found;

    optional string fracture;

    optional string frame;

    optional string framesize;

    optional string genus;

    optional string gparent;

    optional string grainsize;

    optional string habitat;

    optional string hardness;

    optional decimal.Decimal height;

    optional decimal.Decimal heightft;

    optional decimal.Decimal heightin;

    optional string homeloc;

    optional string idby;

    optional date_time.DateTime iddate;

    optional string imagefile;

    optional i32 imageno;

    optional string imagesize;

    optional string inscomp;

    optional string inscrlang;

    optional string inscrpos;

    optional string inscrtech;

    optional string inscrtext;

    optional string inscrtrans;

    optional string inscrtype;

    optional date_time.DateTime insdate;

    optional string insphone;

    optional string inspremium;

    optional string insrep;

    optional decimal.Decimal insvalue;

    optional string invnby;

    optional date_time.DateTime invndate;

    optional string kingdom;

    optional decimal.Decimal latdeg;

    optional i32 latedate;

    optional string legal;

    optional decimal.Decimal length;

    optional decimal.Decimal lengthft;

    optional decimal.Decimal lengthin;

    optional string level;

    optional string lithofacie;

    optional string loancond;

    optional date_time.DateTime loandue;

    optional string loanid;

    optional string loaninno;

    optional i32 loanno;

    optional date_time.DateTime loanrenew;

    optional string locfield1;

    optional string locfield2;

    optional string locfield3;

    optional string locfield4;

    optional string locfield5;

    optional string locfield6;

    optional decimal.Decimal longdeg;

    optional string luster;

    optional string made;

    optional string maintcycle;

    optional date_time.DateTime maintdate;

    optional string maintnote;

    optional string material;

    optional string medium;

    optional string member;

    optional string mmark;

    optional string nhclass;

    optional string nhorder;

    optional string notes;

    optional string ns;

    optional string objectid;

    optional string objname;

    optional string objname2;

    optional string objname3;

    optional string objnames;

    optional string occurrence;

    optional string oldno;

    optional string origin;

    optional string othername;

    optional string otherno;

    optional date_time.DateTime outdate;

    optional string owned;

    optional string parent;

    optional string people;

    optional string period;

    optional string phylum;

    optional string policyno;

    optional string ppid;

    optional string preparator;

    optional date_time.DateTime prepdate;

    optional string preserve;

    optional string pressure;

    optional string provenance;

    optional string pubnotes;

    optional string qrurl;

    optional string recas;

    optional string recdate;

    optional string recfrom;

    optional string relation;

    optional string relnotes;

    optional date_time.DateTime renewuntil;

    optional string repatby;

    optional string repatclaim;

    optional date_time.DateTime repatdate;

    optional string repatdisp;

    optional string repathand;

    optional string repatnotes;

    optional date_time.DateTime repatnotic;

    optional string repattype;

    optional string rockclass;

    optional string rockcolor;

    optional string rockorigin;

    optional string rocktype;

    optional string role;

    optional string role2;

    optional string role3;

    optional string school;

    optional string sex;

    optional string sgflag;

    optional string signedname;

    optional string signloc;

    optional string site;

    optional string siteno;

    optional string specgrav;

    optional string species;

    optional string sprocess;

    optional string stage;

    optional string status;

    optional string statusby;

    optional date_time.DateTime statusdate;

    optional string sterms;

    optional string stratum;

    optional string streak;

    optional string subfamily;

    optional string subjects;

    optional string subspecies;

    optional string technique;

    optional string tempauthor;

    optional string tempby;

    optional date_time.DateTime tempdate;

    optional string temperatur;

    optional string temploc;

    optional string tempnotes;

    optional string tempreason;

    optional string tempuntil;

    optional string texture;

    optional string title;

    optional string tlocfield1;

    optional string tlocfield2;

    optional string tlocfield3;

    optional string tlocfield4;

    optional string tlocfield5;

    optional string tlocfield6;

    optional string udf1;

    optional string udf10;

    optional string udf11;

    optional string udf12;

    optional i32 udf13;

    optional decimal.Decimal udf14;

    optional decimal.Decimal udf15;

    optional decimal.Decimal udf16;

    optional decimal.Decimal udf17;

    optional date_time.DateTime udf18;

    optional date_time.DateTime udf19;

    optional string udf2;

    optional date_time.DateTime udf20;

    optional string udf21;

    optional string udf22;

    optional string udf3;

    optional string udf4;

    optional string udf5;

    optional string udf6;

    optional string udf7;

    optional string udf8;

    optional string udf9;

    optional string unit;

    optional date_time.DateTime updated;

    optional string updatedby;

    optional string used;

    optional date_time.DateTime valuedate;

    optional string varieties;

    optional string vexhtml;

    optional string vexlabel1;

    optional string vexlabel2;

    optional string vexlabel3;

    optional string vexlabel4;

    optional bool webinclude;

    optional decimal.Decimal weight;

    optional decimal.Decimal weightin;

    optional decimal.Decimal weightlb;

    optional decimal.Decimal width;

    optional decimal.Decimal widthft;

    optional decimal.Decimal widthin;

    optional decimal.Decimal xcord;

    optional decimal.Decimal ycord;

    optional decimal.Decimal zcord;

    optional string zsorter;

    optional string zsorterx;
}