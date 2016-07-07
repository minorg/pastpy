namespace * pastpy.models

include "pastpy/models/condition.thrift"
include "pastpy/models/recas.thrift"
include "pastpy/models/status.thrift"
include "thryft/native/date_time.thrift"
include "thryft/native/decimal.thrift"

struct Object {
    // @validation {"minLength": 1}
    optional string accessno;

    // @validation {"minLength": 1}
    optional string accessory;

    optional decimal.Decimal acqvalue;

    // @validation {"minLength": 1}
    optional string age;

    // @validation {"minLength": 1}
    optional string appnotes;

    // @validation {"minLength": 1}
    optional string appraisor;

    // @validation {"minLength": 1}
    optional string assemzone;

    // @validation {"minLength": 1}
    optional string bagno;

    // @validation {"minLength": 1}
    optional string boxno;

    // @validation {"minLength": 1}
    optional string caption;

    // @validation {"minLength": 1}
    optional string catby;

    optional date_time.DateTime catdate;

    // @validation {"minLength": 1}
    optional string cattype;

    // @validation {"minLength": 1}
    optional string chemcomp;

    // @validation {"minLength": 1}
    optional string circum;

    optional decimal.Decimal circumft;

    optional decimal.Decimal circumin;

    // @validation {"minLength": 1}
    optional string classes;

    optional date_time.DateTime colldate;

    // @validation {"minLength": 1}
    optional string collection;

    // @validation {"minLength": 1}
    optional string collector;

    optional date_time.DateTime conddate;

    // @validation {"minLength": 1}
    optional string condexam;

    optional condition.Condition condition;

    // @validation {"minLength": 1}
    optional string condnotes;

    // @validation {"minLength": 1}
    optional string count;

    // @validation {"minLength": 1}
    optional string creator;

    // @validation {"minLength": 1}
    optional string creator2;

    // @validation {"minLength": 1}
    optional string creator3;

    // @validation {"minLength": 1}
    optional string credit;

    // @validation {"minLength": 1}
    optional string crystal;

    // @validation {"minLength": 1}
    optional string culture;

    optional decimal.Decimal curvalmax;

    optional decimal.Decimal curvalue;

    // @validation {"minLength": 1}
    optional string dataset;

    // @validation {"minLength": 1}
    optional string date;

    // @validation {"minLength": 1}
    optional string datingmeth;

    // @validation {"minLength": 1}
    optional string datum;

    // @validation {"minLength": 1}
    optional string depth;

    optional decimal.Decimal depthft;

    optional decimal.Decimal depthin;

    // @validation {"minLength": 1}
    optional string descrip;

    // @validation {"minLength": 1}
    optional string diameter;

    optional decimal.Decimal diameterft;

    optional decimal.Decimal diameterin;

    // @validation {"minLength": 1}
    optional string dimnotes;

    // @validation {"minLength": 1}
    optional string dimtype;

    // @validation {"minLength": 1}
    optional string dispvalue;

    // @validation {"minLength": 1}
    optional string earlydate;

    // @validation {"minLength": 1}
    optional string elements;

    // @validation {"minLength": 1}
    optional string epoch;

    // @validation {"minLength": 1}
    optional string era;

    // @validation {"minLength": 1}
    optional string event;

    // @validation {"minLength": 1}
    optional string excavadate;

    // @validation {"minLength": 1}
    optional string excavateby;

    optional i32 exhibitno;

    // @validation {"minLength": 1}
    optional string exhlabel1;

    // @validation {"minLength": 1}
    optional string exhlabel2;

    // @validation {"minLength": 1}
    optional string exhlabel3;

    // @validation {"minLength": 1}
    optional string exhlabel4;

    // @validation {"minLength": 1}
    optional string exhstart;

    // @validation {"minLength": 1}
    optional string family;

    // @validation {"minLength": 1}
    optional string feature;

    // @validation {"minLength": 1}
    optional string flagdate;

    // @validation {"minLength": 1}
    optional string flagnotes;

    // @validation {"minLength": 1}
    optional string flagreason;

    // @validation {"minLength": 1}
    optional string formation;

    // @validation {"minLength": 1}
    optional string fossils;

    // @validation {"minLength": 1}
    optional string found;

    // @validation {"minLength": 1}
    optional string fracture;

    // @validation {"minLength": 1}
    optional string frame;

    // @validation {"minLength": 1}
    optional string framesize;

    // @validation {"minLength": 1}
    optional string genus;

    // @validation {"minLength": 1}
    optional string gparent;

    // @validation {"minLength": 1}
    optional string grainsize;

    // @validation {"minLength": 1}
    optional string habitat;

    // @validation {"minLength": 1}
    optional string hardness;

    // @validation {"minLength": 1}
    optional string height;

    optional decimal.Decimal heightft;

    optional decimal.Decimal heightin;

    // @validation {"minLength": 1}
    optional string homeloc;

    // @validation {"minLength": 1}
    optional string idby;

    // @validation {"minLength": 1}
    optional string iddate;

    // @validation {"minLength": 1}
    optional string imagefile;

    optional i32 imageno;

    // @validation {"minLength": 1}
    optional string imagesize;

    // @validation {"minLength": 1}
    optional string inscomp;

    // @validation {"minLength": 1}
    optional string inscrlang;

    // @validation {"minLength": 1}
    optional string inscrpos;

    // @validation {"minLength": 1}
    optional string inscrtech;

    // @validation {"minLength": 1}
    optional string inscrtext;

    // @validation {"minLength": 1}
    optional string inscrtrans;

    // @validation {"minLength": 1}
    optional string inscrtype;

    // @validation {"minLength": 1}
    optional string insdate;

    // @validation {"minLength": 1}
    optional string insphone;

    // @validation {"minLength": 1}
    optional string inspremium;

    // @validation {"minLength": 1}
    optional string insrep;

    optional decimal.Decimal insvalue;

    // @validation {"minLength": 1}
    optional string invnby;

    // @validation {"minLength": 1}
    optional string invndate;

    // @validation {"minLength": 1}
    optional string kingdom;

    // @validation {"minLength": 1}
    optional string latedate;

    // @validation {"minLength": 1}
    optional string legal;

    // @validation {"minLength": 1}
    optional string length;

    optional decimal.Decimal lengthft;

    optional decimal.Decimal lengthin;

    // @validation {"minLength": 1}
    optional string level;

    // @validation {"minLength": 1}
    optional string lithofacie;

    // @validation {"minLength": 1}
    optional string loancond;

    // @validation {"minLength": 1}
    optional string loandue;

    // @validation {"minLength": 1}
    optional string loaninno;

    // @validation {"minLength": 1}
    optional string loanno;

    // @validation {"minLength": 1}
    optional string locfield1;

    // @validation {"minLength": 1}
    optional string locfield2;

    // @validation {"minLength": 1}
    optional string locfield3;

    // @validation {"minLength": 1}
    optional string locfield4;

    // @validation {"minLength": 1}
    optional string locfield5;

    // @validation {"minLength": 1}
    optional string locfield6;

    // @validation {"minLength": 1}
    optional string luster;

    // @validation {"minLength": 1}
    optional string made;

    // @validation {"minLength": 1}
    optional string maintcycle;

    // @validation {"minLength": 1}
    optional string maintdate;

    // @validation {"minLength": 1}
    optional string maintnote;

    // @validation {"minLength": 1}
    optional string material;

    // @validation {"minLength": 1}
    optional string medium;

    // @validation {"minLength": 1}
    optional string member;

    // @validation {"minLength": 1}
    optional string mmark;

    // @validation {"minLength": 1}
    optional string nhclass;

    // @validation {"minLength": 1}
    optional string nhorder;

    // @validation {"minLength": 1}
    optional string notes;

    // @validation {"minLength": 1}
    optional string objectid;

    // @validation {"minLength": 1}
    optional string objname;

    // @validation {"minLength": 1}
    optional string objname2;

    // @validation {"minLength": 1}
    optional string objname3;

    // @validation {"minLength": 1}
    optional string objnames;

    // @validation {"minLength": 1}
    optional string occurrence;

    optional i32 oldno;

    // @validation {"minLength": 1}
    optional string origin;

    // @validation {"minLength": 1}
    optional string othername;

    optional i32 otherno;

    // @validation {"minLength": 1}
    optional string outdate;

    // @validation {"minLength": 1}
    optional string owned;

    // @validation {"minLength": 1}
    optional string parent;

    // @validation {"minLength": 1}
    optional string people;

    // @validation {"minLength": 1}
    optional string period;

    // @validation {"minLength": 1}
    optional string phylum;

    // @validation {"minLength": 1}
    optional string policyno;

    // @validation {"minLength": 1}
    optional string preparator;

    // @validation {"minLength": 1}
    optional string prepdate;

    // @validation {"minLength": 1}
    optional string preserve;

    // @validation {"minLength": 1}
    optional string pressure;

    // @validation {"minLength": 1}
    optional string provenance;

    // @validation {"minLength": 1}
    optional string pubnotes;

    optional recas.Recas recas;

    // @validation {"minLength": 1}
    optional string recdate;

    // @validation {"minLength": 1}
    optional string recfrom;

    // @validation {"minLength": 1}
    optional string relnotes;

    // @validation {"minLength": 1}
    optional string repatby;

    // @validation {"minLength": 1}
    optional string repatclaim;

    // @validation {"minLength": 1}
    optional string repatdate;

    // @validation {"minLength": 1}
    optional string repatdisp;

    // @validation {"minLength": 1}
    optional string repathand;

    // @validation {"minLength": 1}
    optional string repatnotes;

    // @validation {"minLength": 1}
    optional string repatnotic;

    // @validation {"minLength": 1}
    optional string repattype;

    // @validation {"minLength": 1}
    optional string rockclass;

    // @validation {"minLength": 1}
    optional string rockcolor;

    // @validation {"minLength": 1}
    optional string rockorigin;

    // @validation {"minLength": 1}
    optional string rocktype;

    // @validation {"minLength": 1}
    optional string role;

    // @validation {"minLength": 1}
    optional string role2;

    // @validation {"minLength": 1}
    optional string role3;

    // @validation {"minLength": 1}
    optional string school;

    // @validation {"minLength": 1}
    optional string sex;

    // @validation {"minLength": 1}
    optional string signedname;

    // @validation {"minLength": 1}
    optional string signloc;

    // @validation {"minLength": 1}
    optional string site;

    // @validation {"minLength": 1}
    optional string siteno;

    // @validation {"minLength": 1}
    optional string specgrav;

    // @validation {"minLength": 1}
    optional string species;

    // @validation {"minLength": 1}
    optional string sprocess;

    // @validation {"minLength": 1}
    optional string stage;

    optional status.Status status;

    // @validation {"minLength": 1}
    optional string statusby;

    optional date_time.DateTime statusdate;

    // @validation {"minLength": 1}
    optional string sterms;

    // @validation {"minLength": 1}
    optional string stratum;

    // @validation {"minLength": 1}
    optional string streak;

    // @validation {"minLength": 1}
    optional string subfamily;

    // @validation {"minLength": 1}
    optional string subjects;

    // @validation {"minLength": 1}
    optional string subspecies;

    // @validation {"minLength": 1}
    optional string technique;

    // @validation {"minLength": 1}
    optional string tempauthor;

    // @validation {"minLength": 1}
    optional string tempby;

    // @validation {"minLength": 1}
    optional string tempdate;

    // @validation {"minLength": 1}
    optional string temperatur;

    // @validation {"minLength": 1}
    optional string temploc;

    // @validation {"minLength": 1}
    optional string tempnotes;

    // @validation {"minLength": 1}
    optional string tempreason;

    // @validation {"minLength": 1}
    optional string tempuntil;

    // @validation {"minLength": 1}
    optional string texture;

    // @validation {"minLength": 1}
    optional string title;

    // @validation {"minLength": 1}
    optional string tlocfield1;

    // @validation {"minLength": 1}
    optional string tlocfield2;

    // @validation {"minLength": 1}
    optional string tlocfield3;

    // @validation {"minLength": 1}
    optional string tlocfield4;

    // @validation {"minLength": 1}
    optional string tlocfield5;

    // @validation {"minLength": 1}
    optional string tlocfield6;

    // @validation {"minLength": 1}
    optional string udf1;

    // @validation {"minLength": 1}
    optional string udf10;

    // @validation {"minLength": 1}
    optional string udf11;

    // @validation {"minLength": 1}
    optional string udf12;

    // @validation {"minLength": 1}
    optional string udf13;

    // @validation {"minLength": 1}
    optional string udf14;

    // @validation {"minLength": 1}
    optional string udf15;

    // @validation {"minLength": 1}
    optional string udf16;

    // @validation {"minLength": 1}
    optional string udf17;

    // @validation {"minLength": 1}
    optional string udf18;

    // @validation {"minLength": 1}
    optional string udf19;

    // @validation {"minLength": 1}
    optional string udf2;

    // @validation {"minLength": 1}
    optional string udf20;

    // @validation {"minLength": 1}
    optional string udf21;

    // @validation {"minLength": 1}
    optional string udf22;

    // @validation {"minLength": 1}
    optional string udf3;

    // @validation {"minLength": 1}
    optional string udf4;

    // @validation {"minLength": 1}
    optional string udf5;

    // @validation {"minLength": 1}
    optional string udf6;

    // @validation {"minLength": 1}
    optional string udf7;

    // @validation {"minLength": 1}
    optional string udf8;

    // @validation {"minLength": 1}
    optional string udf9;

    // @validation {"minLength": 1}
    optional string unit;

    // @validation {"minLength": 1}
    optional string updated;

    // @validation {"minLength": 1}
    optional string updatedby;

    // @validation {"minLength": 1}
    optional string used;

    // @validation {"minLength": 1}
    optional string valuedate;

    // @validation {"minLength": 1}
    optional string varieties;

    // @validation {"minLength": 1}
    optional string webinclude;

    // @validation {"minLength": 1}
    optional string weight;

    // @validation {"minLength": 1}
    optional string weightin;

    optional decimal.Decimal weightlb;

    // @validation {"minLength": 1}
    optional string width;

    optional decimal.Decimal widthft;

    optional decimal.Decimal widthin;

    // @validation {"minLength": 1}
    optional string xcord;

    // @validation {"minLength": 1}
    optional string ycord;

    // @validation {"minLength": 1}
    optional string zcord;
}
