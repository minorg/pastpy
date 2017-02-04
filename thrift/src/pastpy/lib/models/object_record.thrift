namespace * pastpy.lib.models

include "pastpy/lib/models/cardinal_direction.thrift"
include "pastpy/lib/models/cat.thrift"
include "pastpy/lib/models/condition.thrift"
include "thryft/native/date_time.thrift"
include "thryft/native/decimal.thrift"
include "thryft/native/variant.thrift"

struct ObjectRecord {
    // @validation {"blank": false, "minLength": 1}
    optional string accessno;

    // @validation {"blank": false, "minLength": 1}
    optional string accessory;

    optional decimal.Decimal acqvalue;

    // @validation {"blank": false, "minLength": 1}
    optional string age;

    // @validation {"blank": false, "minLength": 1}
    optional string appnotes;

    // @validation {"blank": false, "minLength": 1}
    optional string appraisor;

    // @validation {"blank": false, "minLength": 1}
    optional string assemzone;

    optional i32 bagno;

    optional i32 boxno;

    // @validation {"blank": false, "minLength": 1}
    optional string caption;

    optional cat.Cat cat;

    // @validation {"blank": false, "minLength": 1}
    optional string catby;

    optional date_time.DateTime catdate;

    // @validation {"blank": false, "minLength": 1}
    optional string cattype;

    // @validation {"blank": false, "minLength": 1}
    optional string chemcomp;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal circum;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal circumft;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal circumin;

    // @validation {"blank": false, "minLength": 1}
    optional string classes;

    optional date_time.DateTime colldate;

    // @validation {"blank": false, "minLength": 1}
    optional string collection;

    // @validation {"blank": false, "minLength": 1}
    optional string collector;

    optional date_time.DateTime conddate;

    // @validation {"blank": false, "minLength": 1}
    optional string condexam;

    optional condition.Condition condition;

    // @validation {"blank": false, "minLength": 1}
    optional string condnotes;

    // @validation {"blank": false, "minLength": 1}
    optional string count;

    // @validation {"blank": false, "minLength": 1}
    optional string creator;

    // @validation {"blank": false, "minLength": 1}
    optional string creator2;

    // @validation {"blank": false, "minLength": 1}
    optional string creator3;

    // @validation {"blank": false, "minLength": 1}
    optional string credit;

    // @validation {"blank": false, "minLength": 1}
    optional string crystal;

    // @validation {"blank": false, "minLength": 1}
    optional string culture;

    optional decimal.Decimal curvalmax;

    optional decimal.Decimal curvalue;

    // @validation {"blank": false, "minLength": 1}
    optional string dataset;

    // @validation {"blank": false, "minLength": 1}
    optional string date;

    // @validation {"blank": false, "minLength": 1}
    optional string datingmeth;

    // @validation {"blank": false, "minLength": 1}
    optional string datum;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal depth;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal depthft;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal depthin;

    // @validation {"blank": false, "minLength": 1}
    optional string descrip;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal diameter;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal diameterft;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal diameterin;

    // @validation {"blank": false, "minLength": 1}
    optional string dimnotes;

    optional i32 dimtype;

    // @validation {"blank": false, "minLength": 1}
    optional string dispvalue;

    // @validation {"blank": false, "minLength": 1}
    optional string earlydate;

    // @validation {"blank": false, "minLength": 1}
    optional string elements;

    // @validation {"blank": false, "minLength": 1}
    optional string epoch;

    // @validation {"blank": false, "minLength": 1}
    optional string era;

    // @validation {"blank": false, "minLength": 1}
    optional string event;

    optional cardinal_direction.CardinalDirection ew;

    optional date_time.DateTime excavadate;

    // @validation {"blank": false, "minLength": 1}
    optional string excavateby;

    // @validation {"blank": false, "minLength": 1}
    optional string exhibitid;

    optional i32 exhibitno;

    // @validation {"minLength": 1}
    optional map<i32, string> exhlabel;

    // @validation {"blank": false, "minLength": 1}
    optional string exhstart;

    // @validation {"blank": false, "minLength": 1}
    optional string family;

    // @validation {"blank": false, "minLength": 1}
    optional string feature;

    optional date_time.DateTime flagdate;

    // @validation {"blank": false, "minLength": 1}
    optional string flagnotes;

    // @validation {"blank": false, "minLength": 1}
    optional string flagreason;

    // @validation {"blank": false, "minLength": 1}
    optional string formation;

    // @validation {"blank": false, "minLength": 1}
    optional string fossils;

    // @validation {"blank": false, "minLength": 1}
    optional string found;

    // @validation {"blank": false, "minLength": 1}
    optional string fracture;

    // @validation {"blank": false, "minLength": 1}
    optional string frame;

    // @validation {"blank": false, "minLength": 1}
    optional string framesize;

    // @validation {"blank": false, "minLength": 1}
    optional string genus;

    // @validation {"blank": false, "minLength": 1}
    optional string gparent;

    // @validation {"blank": false, "minLength": 1}
    optional string grainsize;

    // @validation {"blank": false, "minLength": 1}
    optional string habitat;

    // @validation {"blank": false, "minLength": 1}
    optional string hardness;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal height;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal heightft;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal heightin;

    // @validation {"blank": false, "minLength": 1}
    optional string homeloc;

    // @validation {"blank": false, "minLength": 1}
    optional string idby;

    optional date_time.DateTime iddate;

    // @validation {"blank": false, "minLength": 1}
    optional string imagefile;

    optional i32 imageno;

    // @validation {"blank": false, "minLength": 1}
    optional string imagesize;

    // @validation {"blank": false, "minLength": 1}
    optional string inscomp;

    // @validation {"blank": false, "minLength": 1}
    optional string inscrlang;

    // @validation {"blank": false, "minLength": 1}
    optional string inscrpos;

    // @validation {"blank": false, "minLength": 1}
    optional string inscrtech;

    // @validation {"blank": false, "minLength": 1}
    optional string inscrtext;

    // @validation {"blank": false, "minLength": 1}
    optional string inscrtrans;

    optional variant.Variant inscrtype;

    optional date_time.DateTime insdate;

    // @validation {"blank": false, "minLength": 1}
    optional string insphone;

    // @validation {"blank": false, "minLength": 1}
    optional string inspremium;

    // @validation {"blank": false, "minLength": 1}
    optional string insrep;

    optional decimal.Decimal insvalue;

    // @validation {"blank": false, "minLength": 1}
    optional string invnby;

    optional date_time.DateTime invndate;

    // @validation {"blank": false, "minLength": 1}
    optional string kingdom;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal latdeg;

    // @validation {"blank": false, "minLength": 1}
    optional string latedate;

    // @validation {"blank": false, "minLength": 1}
    optional string legal;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal length;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal lengthft;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal lengthin;

    // @validation {"blank": false, "minLength": 1}
    optional string level;

    // @validation {"blank": false, "minLength": 1}
    optional string lithofacie;

    // @validation {"blank": false, "minLength": 1}
    optional string loancond;

    // @validation {"blank": false, "minLength": 1}
    optional string loandue;

    // @validation {"blank": false, "minLength": 1}
    optional string loanid;

    // @validation {"blank": false, "minLength": 1}
    optional string loaninno;

    optional i32 loanno;

    optional date_time.DateTime loanrenew;

    // @validation {"minLength": 1}
    optional map<i32, string> locfield;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal longdeg;

    // @validation {"blank": false, "minLength": 1}
    optional string luster;

    // @validation {"blank": false, "minLength": 1}
    optional string made;

    // @validation {"blank": false, "minLength": 1}
    optional string maintcycle;

    optional date_time.DateTime maintdate;

    // @validation {"blank": false, "minLength": 1}
    optional string maintnote;

    // @validation {"blank": false, "minLength": 1}
    optional string material;

    // @validation {"blank": false, "minLength": 1}
    optional string medium;

    // @validation {"blank": false, "minLength": 1}
    optional string member;

    // @validation {"blank": false, "minLength": 1}
    optional string mmark;

    // @validation {"blank": false, "minLength": 1}
    optional string nhclass;

    // @validation {"blank": false, "minLength": 1}
    optional string nhorder;

    // @validation {"blank": false, "minLength": 1}
    optional string notes;

    optional cardinal_direction.CardinalDirection ns;

    // @validation {"blank": false, "minLength": 1}
    optional string objectid;

    // @validation {"blank": false, "minLength": 1}
    optional string objname;

    // @validation {"blank": false, "minLength": 1}
    optional string objname2;

    // @validation {"blank": false, "minLength": 1}
    optional string objname3;

    // @validation {"blank": false, "minLength": 1}
    optional string objnames;

    // @validation {"blank": false, "minLength": 1}
    optional string occurrence;

    // @validation {"blank": false, "minLength": 1}
    optional string oldno;

    // @validation {"blank": false, "minLength": 1}
    optional string origin;

    // @validation {"blank": false, "minLength": 1}
    optional string othername;

    // @validation {"blank": false, "minLength": 1}
    optional string otherno;

    optional date_time.DateTime outdate;

    // @validation {"blank": false, "minLength": 1}
    optional string owned;

    // @validation {"blank": false, "minLength": 1}
    optional string parent;

    // @validation {"blank": false, "minLength": 1}
    optional string people;

    // @validation {"blank": false, "minLength": 1}
    optional string period;

    // @validation {"blank": false, "minLength": 1}
    optional string phylum;

    // @validation {"blank": false, "minLength": 1}
    optional string policyno;

    // @validation {"blank": false, "minLength": 1}
    optional string ppid;

    // @validation {"blank": false, "minLength": 1}
    optional string preparator;

    optional date_time.DateTime prepdate;

    // @validation {"blank": false, "minLength": 1}
    optional string preserve;

    // @validation {"blank": false, "minLength": 1}
    optional string pressure;

    // @validation {"blank": false, "minLength": 1}
    optional string provenance;

    // @validation {"blank": false, "minLength": 1}
    optional string pubnotes;

    // @validation {"blank": false, "minLength": 1}
    optional string recas;

    optional date_time.DateTime recdate;

    // @validation {"blank": false, "minLength": 1}
    optional string recfrom;

    // @validation {"blank": false, "minLength": 1}
    optional string relation;

    // @validation {"blank": false, "minLength": 1}
    optional string relnotes;

    optional date_time.DateTime renewuntil;

    // @validation {"blank": false, "minLength": 1}
    optional string repatby;

    // @validation {"blank": false, "minLength": 1}
    optional string repatclaim;

    optional date_time.DateTime repatdate;

    // @validation {"blank": false, "minLength": 1}
    optional string repatdisp;

    // @validation {"blank": false, "minLength": 1}
    optional string repathand;

    // @validation {"blank": false, "minLength": 1}
    optional string repatnotes;

    // @validation {"blank": false, "minLength": 1}
    optional string repatnotic;

    optional i32 repattype;

    // @validation {"blank": false, "minLength": 1}
    optional string rockclass;

    // @validation {"blank": false, "minLength": 1}
    optional string rockcolor;

    // @validation {"blank": false, "minLength": 1}
    optional string rockorigin;

    optional i32 rocktype;

    // @validation {"blank": false, "minLength": 1}
    optional string role;

    // @validation {"blank": false, "minLength": 1}
    optional string role2;

    // @validation {"blank": false, "minLength": 1}
    optional string role3;

    // @validation {"blank": false, "minLength": 1}
    optional string school;

    // @validation {"blank": false, "minLength": 1}
    optional string sex;

    // @validation {"blank": false, "minLength": 1}
    optional string signedname;

    // @validation {"blank": false, "minLength": 1}
    optional string signloc;

    // @validation {"blank": false, "minLength": 1}
    optional string site;

    // @validation {"blank": false, "minLength": 1}
    optional string siteno;

    // @validation {"blank": false, "minLength": 1}
    optional string specgrav;

    // @validation {"blank": false, "minLength": 1}
    optional string species;

    // @validation {"blank": false, "minLength": 1}
    optional string sprocess;

    // @validation {"blank": false, "minLength": 1}
    optional string stage;

    // @validation {"blank": false, "minLength": 1}
    optional string status;

    // @validation {"blank": false, "minLength": 1}
    optional string statusby;

    optional date_time.DateTime statusdate;

    // @validation {"blank": false, "minLength": 1}
    optional string sterms;

    // @validation {"blank": false, "minLength": 1}
    optional string stratum;

    // @validation {"blank": false, "minLength": 1}
    optional string streak;

    // @validation {"blank": false, "minLength": 1}
    optional string subfamily;

    // @validation {"blank": false, "minLength": 1}
    optional string subjects;

    // @validation {"blank": false, "minLength": 1}
    optional string subspecies;

    // @validation {"blank": false, "minLength": 1}
    optional string technique;

    // @validation {"blank": false, "minLength": 1}
    optional string tempauthor;

    // @validation {"blank": false, "minLength": 1}
    optional string tempby;

    optional date_time.DateTime tempdate;

    // @validation {"blank": false, "minLength": 1}
    optional string temperatur;

    // @validation {"blank": false, "minLength": 1}
    optional string temploc;

    // @validation {"blank": false, "minLength": 1}
    optional string tempnotes;

    // @validation {"blank": false, "minLength": 1}
    optional string tempreason;

    // @validation {"blank": false, "minLength": 1}
    optional string tempuntil;

    // @validation {"blank": false, "minLength": 1}
    optional string texture;

    // @validation {"blank": false, "minLength": 1}
    optional string title;

    // @validation {"minLength": 1}
    optional map<i32, string> tlocfield;

     // @validation {"minLength": 1}
    optional map<i32, variant.Variant> udf;

    // @validation {"blank": false, "minLength": 1}
    optional string unit;

    optional date_time.DateTime updated;

    // @validation {"blank": false, "minLength": 1}
    optional string updatedby;

    // @validation {"blank": false, "minLength": 1}
    optional string used;

    optional date_time.DateTime valuedate;

    // @validation {"blank": false, "minLength": 1}
    optional string varieties;

    optional bool webinclude;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal weight;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal weightin;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal weightlb;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal width;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal widthft;

    // @validation {"minExclusive": 0}
    optional decimal.Decimal widthin;

    // @validation {"blank": false, "minLength": 1}
    optional string xcord;

    // @validation {"blank": false, "minLength": 1}
    optional string ycord;

    // @validation {"blank": false, "minLength": 1}
    optional string zcord;

    // @validation {"blank": false, "minLength": 1}
    optional string zsorter;

    // @validation {"blank": false, "minLength": 1}
    optional string zsorterx;
}
