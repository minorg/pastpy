from datetime import datetime
from decimal import Decimal
from typing import NamedTuple, Optional


class ObjectsDbfRecord(NamedTuple):
    # C,15
    accessno: Optional[str] = None

    # M,4
    accessory: Optional[str] = None

    # N,12,2
    acqvalue: Optional[Decimal] = None

    # C,10
    age: Optional[str] = None

    # M,4
    appnotes: Optional[str] = None

    # M,4
    appraisor: Optional[str] = None

    # C,25
    assemzone: Optional[str] = None

    # C,15
    bagno: Optional[str] = None

    # C,15
    boxno: Optional[str] = None

    # M,4
    caption: Optional[str] = None

    # C,1
    cat: Optional[str] = None

    # C,25
    catby: Optional[str] = None

    # D,8
    catdate: Optional[date] = None

    # C,15
    cattype: Optional[str] = None

    # C,25
    chemcomp: Optional[str] = None

    # N,16,10
    circum: Optional[Decimal] = None

    # N,16,10
    circumft: Optional[Decimal] = None

    # N,16,10
    circumin: Optional[Decimal] = None

    # M,4
    classes: Optional[str] = None

    # D,8
    colldate: Optional[date] = None

    # C,75
    collection: Optional[str] = None

    # M,4
    collector: Optional[str] = None

    # D,8
    conddate: Optional[date] = None

    # C,25
    condexam: Optional[str] = None

    # C,35
    condition: Optional[str] = None

    # M,4
    condnotes: Optional[str] = None

    # C,20
    count: Optional[str] = None

    # M,4
    creator: Optional[str] = None

    # M,4
    creator2: Optional[str] = None

    # M,4
    creator3: Optional[str] = None

    # M,4
    credit: Optional[str] = None

    # C,20
    crystal: Optional[str] = None

    # M,4
    culture: Optional[str] = None

    # N,12,2
    curvalmax: Optional[Decimal] = None

    # N,12,2
    curvalue: Optional[Decimal] = None

    # C,15
    dataset: Optional[str] = None

    # C,50
    date: Optional[str] = None

    # M,4
    datingmeth: Optional[str] = None

    # C,15
    datum: Optional[str] = None

    # N,16,10
    depth: Optional[Decimal] = None

    # N,16,10
    depthft: Optional[Decimal] = None

    # N,16,10
    depthin: Optional[Decimal] = None

    # M,4
    descrip: Optional[str] = None

    # N,16,10
    diameter: Optional[Decimal] = None

    # N,16,10
    diameterft: Optional[Decimal] = None

    # N,16,10
    diameterin: Optional[Decimal] = None

    # M,4
    dimnotes: Optional[str] = None

    # N,1
    dimtype: Optional[int] = None

    # C,10
    dispvalue: Optional[str] = None

    # N,4
    earlydate: Optional[int] = None

    # M,4
    elements: Optional[str] = None

    # C,25
    epoch: Optional[str] = None

    # C,25
    era: Optional[str] = None

    # M,4
    event: Optional[str] = None

    # C,1
    ew: Optional[str] = None

    # D,8
    excavadate: Optional[date] = None

    # M,4
    excavateby: Optional[str] = None

    # C,36
    exhibitid: Optional[str] = None

    # N,7
    exhibitno: Optional[int] = None

    # M,4
    exhlabel1: Optional[str] = None

    # M,4
    exhlabel2: Optional[str] = None

    # M,4
    exhlabel3: Optional[str] = None

    # M,4
    exhlabel4: Optional[str] = None

    # D,8
    exhstart: Optional[date] = None

    # C,35
    family: Optional[str] = None

    # M,4
    feature: Optional[str] = None

    # T,8
    flagdate: Optional[datetime] = None

    # M,4
    flagnotes: Optional[str] = None

    # C,20
    flagreason: Optional[str] = None

    # C,25
    formation: Optional[str] = None

    # C,25
    fossils: Optional[str] = None

    # M,4
    found: Optional[str] = None

    # C,20
    fracture: Optional[str] = None

    # M,4
    frame: Optional[str] = None

    # C,35
    framesize: Optional[str] = None

    # C,35
    genus: Optional[str] = None

    # C,45
    gparent: Optional[str] = None

    # C,25
    grainsize: Optional[str] = None

    # M,4
    habitat: Optional[str] = None

    # C,15
    hardness: Optional[str] = None

    # N,16,10
    height: Optional[Decimal] = None

    # N,16,10
    heightft: Optional[Decimal] = None

    # N,16,10
    heightin: Optional[Decimal] = None

    # C,60
    homeloc: Optional[str] = None

    # M,4
    idby: Optional[str] = None

    # D,8
    iddate: Optional[date] = None

    # M,4
    imagefile: Optional[str] = None

    # N,3
    imageno: Optional[int] = None

    # C,35
    imagesize: Optional[str] = None

    # C,30
    inscomp: Optional[str] = None

    # C,20
    inscrlang: Optional[str] = None

    # C,40
    inscrpos: Optional[str] = None

    # C,20
    inscrtech: Optional[str] = None

    # M,4
    inscrtext: Optional[str] = None

    # M,4
    inscrtrans: Optional[str] = None

    # C,20
    inscrtype: Optional[str] = None

    # D,8
    insdate: Optional[date] = None

    # C,25
    insphone: Optional[str] = None

    # C,20
    inspremium: Optional[str] = None

    # C,30
    insrep: Optional[str] = None

    # N,10,2
    insvalue: Optional[Decimal] = None

    # C,25
    invnby: Optional[str] = None

    # D,8
    invndate: Optional[date] = None

    # C,20
    kingdom: Optional[str] = None

    # N,9,6
    latdeg: Optional[Decimal] = None

    # N,4
    latedate: Optional[str] = None

    # M,4
    legal: Optional[str] = None

    # N,16,10
    length: Optional[Decimal] = None

    # N,16,10
    lengthft: Optional[Decimal] = None

    # N,16,10
    lengthin: Optional[Decimal] = None

    # M,4
    level: Optional[str] = None

    # C,25
    lithofacie: Optional[str] = None

    # M,4
    loancond: Optional[str] = None

    # D,8
    loandue: Optional[date] = None

    # C,36
    loanid: Optional[str] = None

    # C,15
    loaninno: Optional[str] = None

    # N,7
    loanno: Optional[int] = None

    # D,8
    loanrenew: Optional[date] = None

    # C,25
    locfield1: Optional[str] = None

    # C,25
    locfield2: Optional[str] = None

    # C,25
    locfield3: Optional[str] = None

    # C,25
    locfield4: Optional[str] = None

    # C,25
    locfield5: Optional[str] = None

    # C,40
    locfield6: Optional[str] = None

    # N,10,6
    longdeg: Optional[Decimal] = None

    # C,15
    luster: Optional[str] = None

    # M,4
    made: Optional[str] = None

    # C,10
    maintcycle: Optional[str] = None

    # D,8
    maintdate: Optional[date] = None

    # M,4
    maintnote: Optional[str] = None

    # M,4
    material: Optional[str] = None

    # M,4
    medium: Optional[str] = None

    # C,25
    member: Optional[str] = None

    # M,4
    mmark: Optional[str] = None

    # C,35
    nhclass: Optional[str] = None

    # M,4
    nhorder: Optional[str] = None

    # M,4
    notes: Optional[str] = None

    # C,1
    ns: Optional[str] = None

    # C,25
    objectid: Optional[str] = None

    # C,40
    objname: Optional[str] = None

    # C,40
    objname2: Optional[str] = None

    # C,40
    objname3: Optional[str] = None

    # M,4
    objnames: Optional[str] = None

    # M,4
    occurrence: Optional[str] = None

    # C,25
    oldno: Optional[str] = None

    # M,4
    origin: Optional[str] = None

    # C,40
    othername: Optional[str] = None

    # C,25
    otherno: Optional[str] = None

    # D,8
    outdate: Optional[date] = None

    # M,4
    owned: Optional[str] = None

    # C,40
    parent: Optional[str] = None

    # M,4
    people: Optional[str] = None

    # C,25
    period: Optional[str] = None

    # C,35
    phylum: Optional[str] = None

    # C,20
    policyno: Optional[str] = None

    # C,36
    ppid: Optional[str] = None

    # M,4
    preparator: Optional[str] = None

    # D,8
    prepdate: Optional[date] = None

    # M,4
    preserve: Optional[str] = None

    # C,25
    pressure: Optional[str] = None

    # M,4
    provenance: Optional[str] = None

    # M,4
    pubnotes: Optional[str] = None

    # M,4
    qrurl: Optional[str] = None

    # C,30
    recas: Optional[str] = None

    # C,10
    recdate: Optional[str] = None

    # M,4
    recfrom: Optional[str] = None

    # C,36
    relation: Optional[str] = None

    # M,4
    relnotes: Optional[str] = None

    # D,8
    renewuntil: Optional[date] = None

    # C,40
    repatby: Optional[str] = None

    # M,4
    repatclaim: Optional[str] = None

    # D,8
    repatdate: Optional[date] = None

    # M,4
    repatdisp: Optional[str] = None

    # M,4
    repathand: Optional[str] = None

    # M,4
    repatnotes: Optional[str] = None

    # D,8
    repatnotic: Optional[date] = None

    # C,40
    repattype: Optional[str] = None

    # C,25
    rockclass: Optional[str] = None

    # C,25
    rockcolor: Optional[str] = None

    # C,25
    rockorigin: Optional[str] = None

    # C,20
    rocktype: Optional[str] = None

    # C,15
    role: Optional[str] = None

    # C,15
    role2: Optional[str] = None

    # C,15
    role3: Optional[str] = None

    # M,4
    school: Optional[str] = None

    # C,13
    sex: Optional[str] = None

    # C,1
    sgflag: Optional[str] = None

    # M,4
    signedname: Optional[str] = None

    # M,4
    signloc: Optional[str] = None

    # C,40
    site: Optional[str] = None

    # C,30
    siteno: Optional[str] = None

    # C,10
    specgrav: Optional[str] = None

    # C,40
    species: Optional[str] = None

    # C,20
    sprocess: Optional[str] = None

    # C,25
    stage: Optional[str] = None

    # C,20
    status: Optional[str] = None

    # C,25
    statusby: Optional[str] = None

    # D,8
    statusdate: Optional[date] = None

    # M,4
    sterms: Optional[str] = None

    # C,35
    stratum: Optional[str] = None

    # C,20
    streak: Optional[str] = None

    # C,35
    subfamily: Optional[str] = None

    # M,4
    subjects: Optional[str] = None

    # M,4
    subspecies: Optional[str] = None

    # M,4
    technique: Optional[str] = None

    # C,25
    tempauthor: Optional[str] = None

    # C,25
    tempby: Optional[str] = None

    # D,8
    tempdate: Optional[date] = None

    # C,25
    temperatur: Optional[str] = None

    # M,4
    temploc: Optional[str] = None

    # M,4
    tempnotes: Optional[str] = None

    # M,4
    tempreason: Optional[str] = None

    # C,10
    tempuntil: Optional[str] = None

    # M,4
    texture: Optional[str] = None

    # M,4
    title: Optional[str] = None

    # C,25
    tlocfield1: Optional[str] = None

    # C,25
    tlocfield2: Optional[str] = None

    # C,25
    tlocfield3: Optional[str] = None

    # C,25
    tlocfield4: Optional[str] = None

    # C,25
    tlocfield5: Optional[str] = None

    # C,40
    tlocfield6: Optional[str] = None

    # M,4
    udf1: Optional[str] = None

    # M,4
    udf10: Optional[str] = None

    # C,20
    udf11: Optional[str] = None

    # C,20
    udf12: Optional[str] = None

    # N,12
    udf13: Optional[Decimal] = None

    # N,12,2
    udf14: Optional[Decimal] = None

    # N,12,2
    udf15: Optional[Decimal] = None

    # N,12,3
    udf16: Optional[Decimal] = None

    # N,12,3
    udf17: Optional[Decimal] = None

    # D,8
    udf18: Optional[date] = None

    # D,8
    udf19: Optional[date] = None

    # M,4
    udf2: Optional[str] = None

    # D,8
    udf20: Optional[date] = None

    # M,4
    udf21: Optional[str] = None

    # M,4
    udf22: Optional[str] = None

    # M,4
    udf3: Optional[str] = None

    # M,4
    udf4: Optional[str] = None

    # M,4
    udf5: Optional[str] = None

    # M,4
    udf6: Optional[str] = None

    # M,4
    udf7: Optional[str] = None

    # M,4
    udf8: Optional[str] = None

    # M,4
    udf9: Optional[str] = None

    # C,35
    unit: Optional[str] = None

    # T,8
    updated: Optional[datetime] = None

    # C,25
    updatedby: Optional[str] = None

    # M,4
    used: Optional[str] = None

    # D,8
    valuedate: Optional[date] = None

    # M,4
    varieties: Optional[str] = None

    # M,4
    vexhtml: Optional[str] = None

    # M,4
    vexlabel1: Optional[str] = None

    # M,4
    vexlabel2: Optional[str] = None

    # M,4
    vexlabel3: Optional[str] = None

    # M,4
    vexlabel4: Optional[str] = None

    # L,1
    webinclude: Optional[bool] = None

    # N,16,10
    weight: Optional[Decimal] = None

    # N,16,10
    weightin: Optional[Decimal] = None

    # N,16,10
    weightlb: Optional[Decimal] = None

    # N,16,10
    width: Optional[Decimal] = None

    # N,16,10
    widthft: Optional[Decimal] = None

    # N,16,10
    widthin: Optional[Decimal] = None

    # N,7,2
    xcord: Optional[Decimal] = None

    # N,7,2
    ycord: Optional[Decimal] = None

    # N,7,2
    zcord: Optional[Decimal] = None

    # C,69
    zsorter: Optional[str] = None

    # C,44
    zsorterx: Optional[str] = None
