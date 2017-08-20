from __future__ import absolute_import; import decimal
from collections import OrderedDict
import builtins
import datetime


class ObjectRecord(object):
    class Builder(object):
        def __init__(
            self,
            accessno=None,
            accessory=None,
            acqvalue=None,
            age=None,
            appnotes=None,
            appraisor=None,
            assemzone=None,
            bagno=None,
            boxno=None,
            caption=None,
            cat=None,
            catby=None,
            catdate=None,
            cattype=None,
            chemcomp=None,
            circum=None,
            circumft=None,
            circumin=None,
            classes=None,
            colldate=None,
            collection=None,
            collector=None,
            conddate=None,
            condexam=None,
            condition=None,
            condnotes=None,
            count=None,
            creator=None,
            creator2=None,
            creator3=None,
            credit=None,
            crystal=None,
            culture=None,
            curvalmax=None,
            curvalue=None,
            dataset=None,
            date=None,
            datingmeth=None,
            datum=None,
            depth=None,
            depthft=None,
            depthin=None,
            descrip=None,
            diameter=None,
            diameterft=None,
            diameterin=None,
            dimnotes=None,
            dimtype=None,
            dispvalue=None,
            earlydate=None,
            elements=None,
            epoch=None,
            era=None,
            event=None,
            ew=None,
            excavadate=None,
            excavateby=None,
            exhibitid=None,
            exhibitno=None,
            exhlabel1=None,
            exhlabel2=None,
            exhlabel3=None,
            exhlabel4=None,
            exhstart=None,
            family=None,
            feature=None,
            flagdate=None,
            flagnotes=None,
            flagreason=None,
            formation=None,
            fossils=None,
            found=None,
            fracture=None,
            frame=None,
            framesize=None,
            genus=None,
            gparent=None,
            grainsize=None,
            habitat=None,
            hardness=None,
            height=None,
            heightft=None,
            heightin=None,
            homeloc=None,
            idby=None,
            iddate=None,
            imagefile=None,
            imageno=None,
            imagesize=None,
            inscomp=None,
            inscrlang=None,
            inscrpos=None,
            inscrtech=None,
            inscrtext=None,
            inscrtrans=None,
            inscrtype=None,
            insdate=None,
            insphone=None,
            inspremium=None,
            insrep=None,
            insvalue=None,
            invnby=None,
            invndate=None,
            kingdom=None,
            latdeg=None,
            latedate=None,
            legal=None,
            length=None,
            lengthft=None,
            lengthin=None,
            level=None,
            lithofacie=None,
            loancond=None,
            loandue=None,
            loanid=None,
            loaninno=None,
            loanno=None,
            loanrenew=None,
            locfield1=None,
            locfield2=None,
            locfield3=None,
            locfield4=None,
            locfield5=None,
            locfield6=None,
            longdeg=None,
            luster=None,
            made=None,
            maintcycle=None,
            maintdate=None,
            maintnote=None,
            material=None,
            medium=None,
            member=None,
            mmark=None,
            nhclass=None,
            nhorder=None,
            notes=None,
            ns=None,
            objectid=None,
            objname=None,
            objname2=None,
            objname3=None,
            objnames=None,
            occurrence=None,
            oldno=None,
            origin=None,
            othername=None,
            otherno=None,
            outdate=None,
            owned=None,
            parent=None,
            people=None,
            period=None,
            phylum=None,
            policyno=None,
            ppid=None,
            preparator=None,
            prepdate=None,
            preserve=None,
            pressure=None,
            provenance=None,
            pubnotes=None,
            qrurl=None,
            recas=None,
            recdate=None,
            recfrom=None,
            relation=None,
            relnotes=None,
            renewuntil=None,
            repatby=None,
            repatclaim=None,
            repatdate=None,
            repatdisp=None,
            repathand=None,
            repatnotes=None,
            repatnotic=None,
            repattype=None,
            rockclass=None,
            rockcolor=None,
            rockorigin=None,
            rocktype=None,
            role=None,
            role2=None,
            role3=None,
            school=None,
            sex=None,
            sgflag=None,
            signedname=None,
            signloc=None,
            site=None,
            siteno=None,
            specgrav=None,
            species=None,
            sprocess=None,
            stage=None,
            status=None,
            statusby=None,
            statusdate=None,
            sterms=None,
            stratum=None,
            streak=None,
            subfamily=None,
            subjects=None,
            subspecies=None,
            technique=None,
            tempauthor=None,
            tempby=None,
            tempdate=None,
            temperatur=None,
            temploc=None,
            tempnotes=None,
            tempreason=None,
            tempuntil=None,
            texture=None,
            title=None,
            tlocfield1=None,
            tlocfield2=None,
            tlocfield3=None,
            tlocfield4=None,
            tlocfield5=None,
            tlocfield6=None,
            udf1=None,
            udf10=None,
            udf11=None,
            udf12=None,
            udf13=None,
            udf14=None,
            udf15=None,
            udf16=None,
            udf17=None,
            udf18=None,
            udf19=None,
            udf2=None,
            udf20=None,
            udf21=None,
            udf22=None,
            udf3=None,
            udf4=None,
            udf5=None,
            udf6=None,
            udf7=None,
            udf8=None,
            udf9=None,
            unit=None,
            updated=None,
            updatedby=None,
            used=None,
            valuedate=None,
            varieties=None,
            vexhtml=None,
            vexlabel1=None,
            vexlabel2=None,
            vexlabel3=None,
            vexlabel4=None,
            webinclude=None,
            weight=None,
            weightin=None,
            weightlb=None,
            width=None,
            widthft=None,
            widthin=None,
            xcord=None,
            ycord=None,
            zcord=None,
            zsorter=None,
            zsorterx=None,
        ):
            '''
            :type accessno: str or None
            :type accessory: str or None
            :type acqvalue: Decimal or None
            :type age: str or None
            :type appnotes: str or None
            :type appraisor: str or None
            :type assemzone: str or None
            :type bagno: str or None
            :type boxno: str or None
            :type caption: str or None
            :type cat: str or None
            :type catby: str or None
            :type catdate: datetime.datetime or None
            :type cattype: str or None
            :type chemcomp: str or None
            :type circum: Decimal or None
            :type circumft: Decimal or None
            :type circumin: Decimal or None
            :type classes: str or None
            :type colldate: datetime.datetime or None
            :type collection: str or None
            :type collector: str or None
            :type conddate: datetime.datetime or None
            :type condexam: str or None
            :type condition: str or None
            :type condnotes: str or None
            :type count: str or None
            :type creator: str or None
            :type creator2: str or None
            :type creator3: str or None
            :type credit: str or None
            :type crystal: str or None
            :type culture: str or None
            :type curvalmax: Decimal or None
            :type curvalue: Decimal or None
            :type dataset: str or None
            :type date: str or None
            :type datingmeth: str or None
            :type datum: str or None
            :type depth: Decimal or None
            :type depthft: Decimal or None
            :type depthin: Decimal or None
            :type descrip: str or None
            :type diameter: Decimal or None
            :type diameterft: Decimal or None
            :type diameterin: Decimal or None
            :type dimnotes: str or None
            :type dimtype: int or None
            :type dispvalue: str or None
            :type earlydate: int or None
            :type elements: str or None
            :type epoch: str or None
            :type era: str or None
            :type event: str or None
            :type ew: str or None
            :type excavadate: datetime.datetime or None
            :type excavateby: str or None
            :type exhibitid: str or None
            :type exhibitno: int or None
            :type exhlabel1: str or None
            :type exhlabel2: str or None
            :type exhlabel3: str or None
            :type exhlabel4: str or None
            :type exhstart: datetime.datetime or None
            :type family: str or None
            :type feature: str or None
            :type flagdate: datetime.datetime or None
            :type flagnotes: str or None
            :type flagreason: str or None
            :type formation: str or None
            :type fossils: str or None
            :type found: str or None
            :type fracture: str or None
            :type frame: str or None
            :type framesize: str or None
            :type genus: str or None
            :type gparent: str or None
            :type grainsize: str or None
            :type habitat: str or None
            :type hardness: str or None
            :type height: Decimal or None
            :type heightft: Decimal or None
            :type heightin: Decimal or None
            :type homeloc: str or None
            :type idby: str or None
            :type iddate: datetime.datetime or None
            :type imagefile: str or None
            :type imageno: int or None
            :type imagesize: str or None
            :type inscomp: str or None
            :type inscrlang: str or None
            :type inscrpos: str or None
            :type inscrtech: str or None
            :type inscrtext: str or None
            :type inscrtrans: str or None
            :type inscrtype: str or None
            :type insdate: datetime.datetime or None
            :type insphone: str or None
            :type inspremium: str or None
            :type insrep: str or None
            :type insvalue: Decimal or None
            :type invnby: str or None
            :type invndate: datetime.datetime or None
            :type kingdom: str or None
            :type latdeg: Decimal or None
            :type latedate: int or None
            :type legal: str or None
            :type length: Decimal or None
            :type lengthft: Decimal or None
            :type lengthin: Decimal or None
            :type level: str or None
            :type lithofacie: str or None
            :type loancond: str or None
            :type loandue: datetime.datetime or None
            :type loanid: str or None
            :type loaninno: str or None
            :type loanno: int or None
            :type loanrenew: datetime.datetime or None
            :type locfield1: str or None
            :type locfield2: str or None
            :type locfield3: str or None
            :type locfield4: str or None
            :type locfield5: str or None
            :type locfield6: str or None
            :type longdeg: Decimal or None
            :type luster: str or None
            :type made: str or None
            :type maintcycle: str or None
            :type maintdate: datetime.datetime or None
            :type maintnote: str or None
            :type material: str or None
            :type medium: str or None
            :type member: str or None
            :type mmark: str or None
            :type nhclass: str or None
            :type nhorder: str or None
            :type notes: str or None
            :type ns: str or None
            :type objectid: str or None
            :type objname: str or None
            :type objname2: str or None
            :type objname3: str or None
            :type objnames: str or None
            :type occurrence: str or None
            :type oldno: str or None
            :type origin: str or None
            :type othername: str or None
            :type otherno: str or None
            :type outdate: datetime.datetime or None
            :type owned: str or None
            :type parent: str or None
            :type people: str or None
            :type period: str or None
            :type phylum: str or None
            :type policyno: str or None
            :type ppid: str or None
            :type preparator: str or None
            :type prepdate: datetime.datetime or None
            :type preserve: str or None
            :type pressure: str or None
            :type provenance: str or None
            :type pubnotes: str or None
            :type qrurl: str or None
            :type recas: str or None
            :type recdate: str or None
            :type recfrom: str or None
            :type relation: str or None
            :type relnotes: str or None
            :type renewuntil: datetime.datetime or None
            :type repatby: str or None
            :type repatclaim: str or None
            :type repatdate: datetime.datetime or None
            :type repatdisp: str or None
            :type repathand: str or None
            :type repatnotes: str or None
            :type repatnotic: datetime.datetime or None
            :type repattype: str or None
            :type rockclass: str or None
            :type rockcolor: str or None
            :type rockorigin: str or None
            :type rocktype: str or None
            :type role: str or None
            :type role2: str or None
            :type role3: str or None
            :type school: str or None
            :type sex: str or None
            :type sgflag: str or None
            :type signedname: str or None
            :type signloc: str or None
            :type site: str or None
            :type siteno: str or None
            :type specgrav: str or None
            :type species: str or None
            :type sprocess: str or None
            :type stage: str or None
            :type status: str or None
            :type statusby: str or None
            :type statusdate: datetime.datetime or None
            :type sterms: str or None
            :type stratum: str or None
            :type streak: str or None
            :type subfamily: str or None
            :type subjects: str or None
            :type subspecies: str or None
            :type technique: str or None
            :type tempauthor: str or None
            :type tempby: str or None
            :type tempdate: datetime.datetime or None
            :type temperatur: str or None
            :type temploc: str or None
            :type tempnotes: str or None
            :type tempreason: str or None
            :type tempuntil: str or None
            :type texture: str or None
            :type title: str or None
            :type tlocfield1: str or None
            :type tlocfield2: str or None
            :type tlocfield3: str or None
            :type tlocfield4: str or None
            :type tlocfield5: str or None
            :type tlocfield6: str or None
            :type udf1: str or None
            :type udf10: str or None
            :type udf11: str or None
            :type udf12: str or None
            :type udf13: int or None
            :type udf14: Decimal or None
            :type udf15: Decimal or None
            :type udf16: Decimal or None
            :type udf17: Decimal or None
            :type udf18: datetime.datetime or None
            :type udf19: datetime.datetime or None
            :type udf2: str or None
            :type udf20: datetime.datetime or None
            :type udf21: str or None
            :type udf22: str or None
            :type udf3: str or None
            :type udf4: str or None
            :type udf5: str or None
            :type udf6: str or None
            :type udf7: str or None
            :type udf8: str or None
            :type udf9: str or None
            :type unit: str or None
            :type updated: datetime.datetime or None
            :type updatedby: str or None
            :type used: str or None
            :type valuedate: datetime.datetime or None
            :type varieties: str or None
            :type vexhtml: str or None
            :type vexlabel1: str or None
            :type vexlabel2: str or None
            :type vexlabel3: str or None
            :type vexlabel4: str or None
            :type webinclude: bool or None
            :type weight: Decimal or None
            :type weightin: Decimal or None
            :type weightlb: Decimal or None
            :type width: Decimal or None
            :type widthft: Decimal or None
            :type widthin: Decimal or None
            :type xcord: Decimal or None
            :type ycord: Decimal or None
            :type zcord: Decimal or None
            :type zsorter: str or None
            :type zsorterx: str or None
            '''

            self.__accessno = accessno
            self.__accessory = accessory
            self.__acqvalue = acqvalue
            self.__age = age
            self.__appnotes = appnotes
            self.__appraisor = appraisor
            self.__assemzone = assemzone
            self.__bagno = bagno
            self.__boxno = boxno
            self.__caption = caption
            self.__cat = cat
            self.__catby = catby
            self.__catdate = catdate
            self.__cattype = cattype
            self.__chemcomp = chemcomp
            self.__circum = circum
            self.__circumft = circumft
            self.__circumin = circumin
            self.__classes = classes
            self.__colldate = colldate
            self.__collection = collection
            self.__collector = collector
            self.__conddate = conddate
            self.__condexam = condexam
            self.__condition = condition
            self.__condnotes = condnotes
            self.__count = count
            self.__creator = creator
            self.__creator2 = creator2
            self.__creator3 = creator3
            self.__credit = credit
            self.__crystal = crystal
            self.__culture = culture
            self.__curvalmax = curvalmax
            self.__curvalue = curvalue
            self.__dataset = dataset
            self.__date = date
            self.__datingmeth = datingmeth
            self.__datum = datum
            self.__depth = depth
            self.__depthft = depthft
            self.__depthin = depthin
            self.__descrip = descrip
            self.__diameter = diameter
            self.__diameterft = diameterft
            self.__diameterin = diameterin
            self.__dimnotes = dimnotes
            self.__dimtype = dimtype
            self.__dispvalue = dispvalue
            self.__earlydate = earlydate
            self.__elements = elements
            self.__epoch = epoch
            self.__era = era
            self.__event = event
            self.__ew = ew
            self.__excavadate = excavadate
            self.__excavateby = excavateby
            self.__exhibitid = exhibitid
            self.__exhibitno = exhibitno
            self.__exhlabel1 = exhlabel1
            self.__exhlabel2 = exhlabel2
            self.__exhlabel3 = exhlabel3
            self.__exhlabel4 = exhlabel4
            self.__exhstart = exhstart
            self.__family = family
            self.__feature = feature
            self.__flagdate = flagdate
            self.__flagnotes = flagnotes
            self.__flagreason = flagreason
            self.__formation = formation
            self.__fossils = fossils
            self.__found = found
            self.__fracture = fracture
            self.__frame = frame
            self.__framesize = framesize
            self.__genus = genus
            self.__gparent = gparent
            self.__grainsize = grainsize
            self.__habitat = habitat
            self.__hardness = hardness
            self.__height = height
            self.__heightft = heightft
            self.__heightin = heightin
            self.__homeloc = homeloc
            self.__idby = idby
            self.__iddate = iddate
            self.__imagefile = imagefile
            self.__imageno = imageno
            self.__imagesize = imagesize
            self.__inscomp = inscomp
            self.__inscrlang = inscrlang
            self.__inscrpos = inscrpos
            self.__inscrtech = inscrtech
            self.__inscrtext = inscrtext
            self.__inscrtrans = inscrtrans
            self.__inscrtype = inscrtype
            self.__insdate = insdate
            self.__insphone = insphone
            self.__inspremium = inspremium
            self.__insrep = insrep
            self.__insvalue = insvalue
            self.__invnby = invnby
            self.__invndate = invndate
            self.__kingdom = kingdom
            self.__latdeg = latdeg
            self.__latedate = latedate
            self.__legal = legal
            self.__length = length
            self.__lengthft = lengthft
            self.__lengthin = lengthin
            self.__level = level
            self.__lithofacie = lithofacie
            self.__loancond = loancond
            self.__loandue = loandue
            self.__loanid = loanid
            self.__loaninno = loaninno
            self.__loanno = loanno
            self.__loanrenew = loanrenew
            self.__locfield1 = locfield1
            self.__locfield2 = locfield2
            self.__locfield3 = locfield3
            self.__locfield4 = locfield4
            self.__locfield5 = locfield5
            self.__locfield6 = locfield6
            self.__longdeg = longdeg
            self.__luster = luster
            self.__made = made
            self.__maintcycle = maintcycle
            self.__maintdate = maintdate
            self.__maintnote = maintnote
            self.__material = material
            self.__medium = medium
            self.__member = member
            self.__mmark = mmark
            self.__nhclass = nhclass
            self.__nhorder = nhorder
            self.__notes = notes
            self.__ns = ns
            self.__objectid = objectid
            self.__objname = objname
            self.__objname2 = objname2
            self.__objname3 = objname3
            self.__objnames = objnames
            self.__occurrence = occurrence
            self.__oldno = oldno
            self.__origin = origin
            self.__othername = othername
            self.__otherno = otherno
            self.__outdate = outdate
            self.__owned = owned
            self.__parent = parent
            self.__people = people
            self.__period = period
            self.__phylum = phylum
            self.__policyno = policyno
            self.__ppid = ppid
            self.__preparator = preparator
            self.__prepdate = prepdate
            self.__preserve = preserve
            self.__pressure = pressure
            self.__provenance = provenance
            self.__pubnotes = pubnotes
            self.__qrurl = qrurl
            self.__recas = recas
            self.__recdate = recdate
            self.__recfrom = recfrom
            self.__relation = relation
            self.__relnotes = relnotes
            self.__renewuntil = renewuntil
            self.__repatby = repatby
            self.__repatclaim = repatclaim
            self.__repatdate = repatdate
            self.__repatdisp = repatdisp
            self.__repathand = repathand
            self.__repatnotes = repatnotes
            self.__repatnotic = repatnotic
            self.__repattype = repattype
            self.__rockclass = rockclass
            self.__rockcolor = rockcolor
            self.__rockorigin = rockorigin
            self.__rocktype = rocktype
            self.__role = role
            self.__role2 = role2
            self.__role3 = role3
            self.__school = school
            self.__sex = sex
            self.__sgflag = sgflag
            self.__signedname = signedname
            self.__signloc = signloc
            self.__site = site
            self.__siteno = siteno
            self.__specgrav = specgrav
            self.__species = species
            self.__sprocess = sprocess
            self.__stage = stage
            self.__status = status
            self.__statusby = statusby
            self.__statusdate = statusdate
            self.__sterms = sterms
            self.__stratum = stratum
            self.__streak = streak
            self.__subfamily = subfamily
            self.__subjects = subjects
            self.__subspecies = subspecies
            self.__technique = technique
            self.__tempauthor = tempauthor
            self.__tempby = tempby
            self.__tempdate = tempdate
            self.__temperatur = temperatur
            self.__temploc = temploc
            self.__tempnotes = tempnotes
            self.__tempreason = tempreason
            self.__tempuntil = tempuntil
            self.__texture = texture
            self.__title = title
            self.__tlocfield1 = tlocfield1
            self.__tlocfield2 = tlocfield2
            self.__tlocfield3 = tlocfield3
            self.__tlocfield4 = tlocfield4
            self.__tlocfield5 = tlocfield5
            self.__tlocfield6 = tlocfield6
            self.__udf1 = udf1
            self.__udf10 = udf10
            self.__udf11 = udf11
            self.__udf12 = udf12
            self.__udf13 = udf13
            self.__udf14 = udf14
            self.__udf15 = udf15
            self.__udf16 = udf16
            self.__udf17 = udf17
            self.__udf18 = udf18
            self.__udf19 = udf19
            self.__udf2 = udf2
            self.__udf20 = udf20
            self.__udf21 = udf21
            self.__udf22 = udf22
            self.__udf3 = udf3
            self.__udf4 = udf4
            self.__udf5 = udf5
            self.__udf6 = udf6
            self.__udf7 = udf7
            self.__udf8 = udf8
            self.__udf9 = udf9
            self.__unit = unit
            self.__updated = updated
            self.__updatedby = updatedby
            self.__used = used
            self.__valuedate = valuedate
            self.__varieties = varieties
            self.__vexhtml = vexhtml
            self.__vexlabel1 = vexlabel1
            self.__vexlabel2 = vexlabel2
            self.__vexlabel3 = vexlabel3
            self.__vexlabel4 = vexlabel4
            self.__webinclude = webinclude
            self.__weight = weight
            self.__weightin = weightin
            self.__weightlb = weightlb
            self.__width = width
            self.__widthft = widthft
            self.__widthin = widthin
            self.__xcord = xcord
            self.__ycord = ycord
            self.__zcord = zcord
            self.__zsorter = zsorter
            self.__zsorterx = zsorterx

        def build(self):
            return ObjectRecord(accessno=self.__accessno, accessory=self.__accessory, acqvalue=self.__acqvalue, age=self.__age, appnotes=self.__appnotes, appraisor=self.__appraisor, assemzone=self.__assemzone, bagno=self.__bagno, boxno=self.__boxno, caption=self.__caption, cat=self.__cat, catby=self.__catby, catdate=self.__catdate, cattype=self.__cattype, chemcomp=self.__chemcomp, circum=self.__circum, circumft=self.__circumft, circumin=self.__circumin, classes=self.__classes, colldate=self.__colldate, collection=self.__collection, collector=self.__collector, conddate=self.__conddate, condexam=self.__condexam, condition=self.__condition, condnotes=self.__condnotes, count=self.__count, creator=self.__creator, creator2=self.__creator2, creator3=self.__creator3, credit=self.__credit, crystal=self.__crystal, culture=self.__culture, curvalmax=self.__curvalmax, curvalue=self.__curvalue, dataset=self.__dataset, date=self.__date, datingmeth=self.__datingmeth, datum=self.__datum, depth=self.__depth, depthft=self.__depthft, depthin=self.__depthin, descrip=self.__descrip, diameter=self.__diameter, diameterft=self.__diameterft, diameterin=self.__diameterin, dimnotes=self.__dimnotes, dimtype=self.__dimtype, dispvalue=self.__dispvalue, earlydate=self.__earlydate, elements=self.__elements, epoch=self.__epoch, era=self.__era, event=self.__event, ew=self.__ew, excavadate=self.__excavadate, excavateby=self.__excavateby, exhibitid=self.__exhibitid, exhibitno=self.__exhibitno, exhlabel1=self.__exhlabel1, exhlabel2=self.__exhlabel2, exhlabel3=self.__exhlabel3, exhlabel4=self.__exhlabel4, exhstart=self.__exhstart, family=self.__family, feature=self.__feature, flagdate=self.__flagdate, flagnotes=self.__flagnotes, flagreason=self.__flagreason, formation=self.__formation, fossils=self.__fossils, found=self.__found, fracture=self.__fracture, frame=self.__frame, framesize=self.__framesize, genus=self.__genus, gparent=self.__gparent, grainsize=self.__grainsize, habitat=self.__habitat, hardness=self.__hardness, height=self.__height, heightft=self.__heightft, heightin=self.__heightin, homeloc=self.__homeloc, idby=self.__idby, iddate=self.__iddate, imagefile=self.__imagefile, imageno=self.__imageno, imagesize=self.__imagesize, inscomp=self.__inscomp, inscrlang=self.__inscrlang, inscrpos=self.__inscrpos, inscrtech=self.__inscrtech, inscrtext=self.__inscrtext, inscrtrans=self.__inscrtrans, inscrtype=self.__inscrtype, insdate=self.__insdate, insphone=self.__insphone, inspremium=self.__inspremium, insrep=self.__insrep, insvalue=self.__insvalue, invnby=self.__invnby, invndate=self.__invndate, kingdom=self.__kingdom, latdeg=self.__latdeg, latedate=self.__latedate, legal=self.__legal, length=self.__length, lengthft=self.__lengthft, lengthin=self.__lengthin, level=self.__level, lithofacie=self.__lithofacie, loancond=self.__loancond, loandue=self.__loandue, loanid=self.__loanid, loaninno=self.__loaninno, loanno=self.__loanno, loanrenew=self.__loanrenew, locfield1=self.__locfield1, locfield2=self.__locfield2, locfield3=self.__locfield3, locfield4=self.__locfield4, locfield5=self.__locfield5, locfield6=self.__locfield6, longdeg=self.__longdeg, luster=self.__luster, made=self.__made, maintcycle=self.__maintcycle, maintdate=self.__maintdate, maintnote=self.__maintnote, material=self.__material, medium=self.__medium, member=self.__member, mmark=self.__mmark, nhclass=self.__nhclass, nhorder=self.__nhorder, notes=self.__notes, ns=self.__ns, objectid=self.__objectid, objname=self.__objname, objname2=self.__objname2, objname3=self.__objname3, objnames=self.__objnames, occurrence=self.__occurrence, oldno=self.__oldno, origin=self.__origin, othername=self.__othername, otherno=self.__otherno, outdate=self.__outdate, owned=self.__owned, parent=self.__parent, people=self.__people, period=self.__period, phylum=self.__phylum, policyno=self.__policyno, ppid=self.__ppid, preparator=self.__preparator, prepdate=self.__prepdate, preserve=self.__preserve, pressure=self.__pressure, provenance=self.__provenance, pubnotes=self.__pubnotes, qrurl=self.__qrurl, recas=self.__recas, recdate=self.__recdate, recfrom=self.__recfrom, relation=self.__relation, relnotes=self.__relnotes, renewuntil=self.__renewuntil, repatby=self.__repatby, repatclaim=self.__repatclaim, repatdate=self.__repatdate, repatdisp=self.__repatdisp, repathand=self.__repathand, repatnotes=self.__repatnotes, repatnotic=self.__repatnotic, repattype=self.__repattype, rockclass=self.__rockclass, rockcolor=self.__rockcolor, rockorigin=self.__rockorigin, rocktype=self.__rocktype, role=self.__role, role2=self.__role2, role3=self.__role3, school=self.__school, sex=self.__sex, sgflag=self.__sgflag, signedname=self.__signedname, signloc=self.__signloc, site=self.__site, siteno=self.__siteno, specgrav=self.__specgrav, species=self.__species, sprocess=self.__sprocess, stage=self.__stage, status=self.__status, statusby=self.__statusby, statusdate=self.__statusdate, sterms=self.__sterms, stratum=self.__stratum, streak=self.__streak, subfamily=self.__subfamily, subjects=self.__subjects, subspecies=self.__subspecies, technique=self.__technique, tempauthor=self.__tempauthor, tempby=self.__tempby, tempdate=self.__tempdate, temperatur=self.__temperatur, temploc=self.__temploc, tempnotes=self.__tempnotes, tempreason=self.__tempreason, tempuntil=self.__tempuntil, texture=self.__texture, title=self.__title, tlocfield1=self.__tlocfield1, tlocfield2=self.__tlocfield2, tlocfield3=self.__tlocfield3, tlocfield4=self.__tlocfield4, tlocfield5=self.__tlocfield5, tlocfield6=self.__tlocfield6, udf1=self.__udf1, udf10=self.__udf10, udf11=self.__udf11, udf12=self.__udf12, udf13=self.__udf13, udf14=self.__udf14, udf15=self.__udf15, udf16=self.__udf16, udf17=self.__udf17, udf18=self.__udf18, udf19=self.__udf19, udf2=self.__udf2, udf20=self.__udf20, udf21=self.__udf21, udf22=self.__udf22, udf3=self.__udf3, udf4=self.__udf4, udf5=self.__udf5, udf6=self.__udf6, udf7=self.__udf7, udf8=self.__udf8, udf9=self.__udf9, unit=self.__unit, updated=self.__updated, updatedby=self.__updatedby, used=self.__used, valuedate=self.__valuedate, varieties=self.__varieties, vexhtml=self.__vexhtml, vexlabel1=self.__vexlabel1, vexlabel2=self.__vexlabel2, vexlabel3=self.__vexlabel3, vexlabel4=self.__vexlabel4, webinclude=self.__webinclude, weight=self.__weight, weightin=self.__weightin, weightlb=self.__weightlb, width=self.__width, widthft=self.__widthft, widthin=self.__widthin, xcord=self.__xcord, ycord=self.__ycord, zcord=self.__zcord, zsorter=self.__zsorter, zsorterx=self.__zsorterx)

        @property
        def accessno(self):
            '''
            :rtype: str
            '''

            return self.__accessno

        @property
        def accessory(self):
            '''
            :rtype: str
            '''

            return self.__accessory

        @property
        def acqvalue(self):
            '''
            :rtype: Decimal
            '''

            return self.__acqvalue

        @property
        def age(self):
            '''
            :rtype: str
            '''

            return self.__age

        @property
        def appnotes(self):
            '''
            :rtype: str
            '''

            return self.__appnotes

        @property
        def appraisor(self):
            '''
            :rtype: str
            '''

            return self.__appraisor

        @property
        def assemzone(self):
            '''
            :rtype: str
            '''

            return self.__assemzone

        @property
        def bagno(self):
            '''
            :rtype: str
            '''

            return self.__bagno

        @property
        def boxno(self):
            '''
            :rtype: str
            '''

            return self.__boxno

        @property
        def caption(self):
            '''
            :rtype: str
            '''

            return self.__caption

        @property
        def cat(self):
            '''
            :rtype: str
            '''

            return self.__cat

        @property
        def catby(self):
            '''
            :rtype: str
            '''

            return self.__catby

        @property
        def catdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__catdate

        @property
        def cattype(self):
            '''
            :rtype: str
            '''

            return self.__cattype

        @property
        def chemcomp(self):
            '''
            :rtype: str
            '''

            return self.__chemcomp

        @property
        def circum(self):
            '''
            :rtype: Decimal
            '''

            return self.__circum

        @property
        def circumft(self):
            '''
            :rtype: Decimal
            '''

            return self.__circumft

        @property
        def circumin(self):
            '''
            :rtype: Decimal
            '''

            return self.__circumin

        @property
        def classes(self):
            '''
            :rtype: str
            '''

            return self.__classes

        @property
        def colldate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__colldate

        @property
        def collection(self):
            '''
            :rtype: str
            '''

            return self.__collection

        @property
        def collector(self):
            '''
            :rtype: str
            '''

            return self.__collector

        @property
        def conddate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__conddate

        @property
        def condexam(self):
            '''
            :rtype: str
            '''

            return self.__condexam

        @property
        def condition(self):
            '''
            :rtype: str
            '''

            return self.__condition

        @property
        def condnotes(self):
            '''
            :rtype: str
            '''

            return self.__condnotes

        @property
        def count(self):
            '''
            :rtype: str
            '''

            return self.__count

        @property
        def creator(self):
            '''
            :rtype: str
            '''

            return self.__creator

        @property
        def creator2(self):
            '''
            :rtype: str
            '''

            return self.__creator2

        @property
        def creator3(self):
            '''
            :rtype: str
            '''

            return self.__creator3

        @property
        def credit(self):
            '''
            :rtype: str
            '''

            return self.__credit

        @property
        def crystal(self):
            '''
            :rtype: str
            '''

            return self.__crystal

        @property
        def culture(self):
            '''
            :rtype: str
            '''

            return self.__culture

        @property
        def curvalmax(self):
            '''
            :rtype: Decimal
            '''

            return self.__curvalmax

        @property
        def curvalue(self):
            '''
            :rtype: Decimal
            '''

            return self.__curvalue

        @property
        def dataset(self):
            '''
            :rtype: str
            '''

            return self.__dataset

        @property
        def date(self):
            '''
            :rtype: str
            '''

            return self.__date

        @property
        def datingmeth(self):
            '''
            :rtype: str
            '''

            return self.__datingmeth

        @property
        def datum(self):
            '''
            :rtype: str
            '''

            return self.__datum

        @property
        def depth(self):
            '''
            :rtype: Decimal
            '''

            return self.__depth

        @property
        def depthft(self):
            '''
            :rtype: Decimal
            '''

            return self.__depthft

        @property
        def depthin(self):
            '''
            :rtype: Decimal
            '''

            return self.__depthin

        @property
        def descrip(self):
            '''
            :rtype: str
            '''

            return self.__descrip

        @property
        def diameter(self):
            '''
            :rtype: Decimal
            '''

            return self.__diameter

        @property
        def diameterft(self):
            '''
            :rtype: Decimal
            '''

            return self.__diameterft

        @property
        def diameterin(self):
            '''
            :rtype: Decimal
            '''

            return self.__diameterin

        @property
        def dimnotes(self):
            '''
            :rtype: str
            '''

            return self.__dimnotes

        @property
        def dimtype(self):
            '''
            :rtype: int
            '''

            return self.__dimtype

        @property
        def dispvalue(self):
            '''
            :rtype: str
            '''

            return self.__dispvalue

        @property
        def earlydate(self):
            '''
            :rtype: int
            '''

            return self.__earlydate

        @property
        def elements(self):
            '''
            :rtype: str
            '''

            return self.__elements

        @property
        def epoch(self):
            '''
            :rtype: str
            '''

            return self.__epoch

        @property
        def era(self):
            '''
            :rtype: str
            '''

            return self.__era

        @property
        def event(self):
            '''
            :rtype: str
            '''

            return self.__event

        @property
        def ew(self):
            '''
            :rtype: str
            '''

            return self.__ew

        @property
        def excavadate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__excavadate

        @property
        def excavateby(self):
            '''
            :rtype: str
            '''

            return self.__excavateby

        @property
        def exhibitid(self):
            '''
            :rtype: str
            '''

            return self.__exhibitid

        @property
        def exhibitno(self):
            '''
            :rtype: int
            '''

            return self.__exhibitno

        @property
        def exhlabel1(self):
            '''
            :rtype: str
            '''

            return self.__exhlabel1

        @property
        def exhlabel2(self):
            '''
            :rtype: str
            '''

            return self.__exhlabel2

        @property
        def exhlabel3(self):
            '''
            :rtype: str
            '''

            return self.__exhlabel3

        @property
        def exhlabel4(self):
            '''
            :rtype: str
            '''

            return self.__exhlabel4

        @property
        def exhstart(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__exhstart

        @property
        def family(self):
            '''
            :rtype: str
            '''

            return self.__family

        @property
        def feature(self):
            '''
            :rtype: str
            '''

            return self.__feature

        @property
        def flagdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__flagdate

        @property
        def flagnotes(self):
            '''
            :rtype: str
            '''

            return self.__flagnotes

        @property
        def flagreason(self):
            '''
            :rtype: str
            '''

            return self.__flagreason

        @property
        def formation(self):
            '''
            :rtype: str
            '''

            return self.__formation

        @property
        def fossils(self):
            '''
            :rtype: str
            '''

            return self.__fossils

        @property
        def found(self):
            '''
            :rtype: str
            '''

            return self.__found

        @property
        def fracture(self):
            '''
            :rtype: str
            '''

            return self.__fracture

        @property
        def frame(self):
            '''
            :rtype: str
            '''

            return self.__frame

        @property
        def framesize(self):
            '''
            :rtype: str
            '''

            return self.__framesize

        @property
        def genus(self):
            '''
            :rtype: str
            '''

            return self.__genus

        @property
        def gparent(self):
            '''
            :rtype: str
            '''

            return self.__gparent

        @property
        def grainsize(self):
            '''
            :rtype: str
            '''

            return self.__grainsize

        @property
        def habitat(self):
            '''
            :rtype: str
            '''

            return self.__habitat

        @property
        def hardness(self):
            '''
            :rtype: str
            '''

            return self.__hardness

        @property
        def height(self):
            '''
            :rtype: Decimal
            '''

            return self.__height

        @property
        def heightft(self):
            '''
            :rtype: Decimal
            '''

            return self.__heightft

        @property
        def heightin(self):
            '''
            :rtype: Decimal
            '''

            return self.__heightin

        @property
        def homeloc(self):
            '''
            :rtype: str
            '''

            return self.__homeloc

        @property
        def idby(self):
            '''
            :rtype: str
            '''

            return self.__idby

        @property
        def iddate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__iddate

        @property
        def imagefile(self):
            '''
            :rtype: str
            '''

            return self.__imagefile

        @property
        def imageno(self):
            '''
            :rtype: int
            '''

            return self.__imageno

        @property
        def imagesize(self):
            '''
            :rtype: str
            '''

            return self.__imagesize

        @property
        def inscomp(self):
            '''
            :rtype: str
            '''

            return self.__inscomp

        @property
        def inscrlang(self):
            '''
            :rtype: str
            '''

            return self.__inscrlang

        @property
        def inscrpos(self):
            '''
            :rtype: str
            '''

            return self.__inscrpos

        @property
        def inscrtech(self):
            '''
            :rtype: str
            '''

            return self.__inscrtech

        @property
        def inscrtext(self):
            '''
            :rtype: str
            '''

            return self.__inscrtext

        @property
        def inscrtrans(self):
            '''
            :rtype: str
            '''

            return self.__inscrtrans

        @property
        def inscrtype(self):
            '''
            :rtype: str
            '''

            return self.__inscrtype

        @property
        def insdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__insdate

        @property
        def insphone(self):
            '''
            :rtype: str
            '''

            return self.__insphone

        @property
        def inspremium(self):
            '''
            :rtype: str
            '''

            return self.__inspremium

        @property
        def insrep(self):
            '''
            :rtype: str
            '''

            return self.__insrep

        @property
        def insvalue(self):
            '''
            :rtype: Decimal
            '''

            return self.__insvalue

        @property
        def invnby(self):
            '''
            :rtype: str
            '''

            return self.__invnby

        @property
        def invndate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__invndate

        @property
        def kingdom(self):
            '''
            :rtype: str
            '''

            return self.__kingdom

        @property
        def latdeg(self):
            '''
            :rtype: Decimal
            '''

            return self.__latdeg

        @property
        def latedate(self):
            '''
            :rtype: int
            '''

            return self.__latedate

        @property
        def legal(self):
            '''
            :rtype: str
            '''

            return self.__legal

        @property
        def length(self):
            '''
            :rtype: Decimal
            '''

            return self.__length

        @property
        def lengthft(self):
            '''
            :rtype: Decimal
            '''

            return self.__lengthft

        @property
        def lengthin(self):
            '''
            :rtype: Decimal
            '''

            return self.__lengthin

        @property
        def level(self):
            '''
            :rtype: str
            '''

            return self.__level

        @property
        def lithofacie(self):
            '''
            :rtype: str
            '''

            return self.__lithofacie

        @property
        def loancond(self):
            '''
            :rtype: str
            '''

            return self.__loancond

        @property
        def loandue(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__loandue

        @property
        def loanid(self):
            '''
            :rtype: str
            '''

            return self.__loanid

        @property
        def loaninno(self):
            '''
            :rtype: str
            '''

            return self.__loaninno

        @property
        def loanno(self):
            '''
            :rtype: int
            '''

            return self.__loanno

        @property
        def loanrenew(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__loanrenew

        @property
        def locfield1(self):
            '''
            :rtype: str
            '''

            return self.__locfield1

        @property
        def locfield2(self):
            '''
            :rtype: str
            '''

            return self.__locfield2

        @property
        def locfield3(self):
            '''
            :rtype: str
            '''

            return self.__locfield3

        @property
        def locfield4(self):
            '''
            :rtype: str
            '''

            return self.__locfield4

        @property
        def locfield5(self):
            '''
            :rtype: str
            '''

            return self.__locfield5

        @property
        def locfield6(self):
            '''
            :rtype: str
            '''

            return self.__locfield6

        @property
        def longdeg(self):
            '''
            :rtype: Decimal
            '''

            return self.__longdeg

        @property
        def luster(self):
            '''
            :rtype: str
            '''

            return self.__luster

        @property
        def made(self):
            '''
            :rtype: str
            '''

            return self.__made

        @property
        def maintcycle(self):
            '''
            :rtype: str
            '''

            return self.__maintcycle

        @property
        def maintdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__maintdate

        @property
        def maintnote(self):
            '''
            :rtype: str
            '''

            return self.__maintnote

        @property
        def material(self):
            '''
            :rtype: str
            '''

            return self.__material

        @property
        def medium(self):
            '''
            :rtype: str
            '''

            return self.__medium

        @property
        def member(self):
            '''
            :rtype: str
            '''

            return self.__member

        @property
        def mmark(self):
            '''
            :rtype: str
            '''

            return self.__mmark

        @property
        def nhclass(self):
            '''
            :rtype: str
            '''

            return self.__nhclass

        @property
        def nhorder(self):
            '''
            :rtype: str
            '''

            return self.__nhorder

        @property
        def notes(self):
            '''
            :rtype: str
            '''

            return self.__notes

        @property
        def ns(self):
            '''
            :rtype: str
            '''

            return self.__ns

        @property
        def objectid(self):
            '''
            :rtype: str
            '''

            return self.__objectid

        @property
        def objname(self):
            '''
            :rtype: str
            '''

            return self.__objname

        @property
        def objname2(self):
            '''
            :rtype: str
            '''

            return self.__objname2

        @property
        def objname3(self):
            '''
            :rtype: str
            '''

            return self.__objname3

        @property
        def objnames(self):
            '''
            :rtype: str
            '''

            return self.__objnames

        @property
        def occurrence(self):
            '''
            :rtype: str
            '''

            return self.__occurrence

        @property
        def oldno(self):
            '''
            :rtype: str
            '''

            return self.__oldno

        @property
        def origin(self):
            '''
            :rtype: str
            '''

            return self.__origin

        @property
        def othername(self):
            '''
            :rtype: str
            '''

            return self.__othername

        @property
        def otherno(self):
            '''
            :rtype: str
            '''

            return self.__otherno

        @property
        def outdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__outdate

        @property
        def owned(self):
            '''
            :rtype: str
            '''

            return self.__owned

        @property
        def parent(self):
            '''
            :rtype: str
            '''

            return self.__parent

        @property
        def people(self):
            '''
            :rtype: str
            '''

            return self.__people

        @property
        def period(self):
            '''
            :rtype: str
            '''

            return self.__period

        @property
        def phylum(self):
            '''
            :rtype: str
            '''

            return self.__phylum

        @property
        def policyno(self):
            '''
            :rtype: str
            '''

            return self.__policyno

        @property
        def ppid(self):
            '''
            :rtype: str
            '''

            return self.__ppid

        @property
        def preparator(self):
            '''
            :rtype: str
            '''

            return self.__preparator

        @property
        def prepdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__prepdate

        @property
        def preserve(self):
            '''
            :rtype: str
            '''

            return self.__preserve

        @property
        def pressure(self):
            '''
            :rtype: str
            '''

            return self.__pressure

        @property
        def provenance(self):
            '''
            :rtype: str
            '''

            return self.__provenance

        @property
        def pubnotes(self):
            '''
            :rtype: str
            '''

            return self.__pubnotes

        @property
        def qrurl(self):
            '''
            :rtype: str
            '''

            return self.__qrurl

        @property
        def recas(self):
            '''
            :rtype: str
            '''

            return self.__recas

        @property
        def recdate(self):
            '''
            :rtype: str
            '''

            return self.__recdate

        @property
        def recfrom(self):
            '''
            :rtype: str
            '''

            return self.__recfrom

        @property
        def relation(self):
            '''
            :rtype: str
            '''

            return self.__relation

        @property
        def relnotes(self):
            '''
            :rtype: str
            '''

            return self.__relnotes

        @property
        def renewuntil(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__renewuntil

        @property
        def repatby(self):
            '''
            :rtype: str
            '''

            return self.__repatby

        @property
        def repatclaim(self):
            '''
            :rtype: str
            '''

            return self.__repatclaim

        @property
        def repatdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__repatdate

        @property
        def repatdisp(self):
            '''
            :rtype: str
            '''

            return self.__repatdisp

        @property
        def repathand(self):
            '''
            :rtype: str
            '''

            return self.__repathand

        @property
        def repatnotes(self):
            '''
            :rtype: str
            '''

            return self.__repatnotes

        @property
        def repatnotic(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__repatnotic

        @property
        def repattype(self):
            '''
            :rtype: str
            '''

            return self.__repattype

        @property
        def rockclass(self):
            '''
            :rtype: str
            '''

            return self.__rockclass

        @property
        def rockcolor(self):
            '''
            :rtype: str
            '''

            return self.__rockcolor

        @property
        def rockorigin(self):
            '''
            :rtype: str
            '''

            return self.__rockorigin

        @property
        def rocktype(self):
            '''
            :rtype: str
            '''

            return self.__rocktype

        @property
        def role(self):
            '''
            :rtype: str
            '''

            return self.__role

        @property
        def role2(self):
            '''
            :rtype: str
            '''

            return self.__role2

        @property
        def role3(self):
            '''
            :rtype: str
            '''

            return self.__role3

        @property
        def school(self):
            '''
            :rtype: str
            '''

            return self.__school

        def set_accessno(self, accessno):
            '''
            :type accessno: str or None
            '''

            if accessno is not None:
                if not isinstance(accessno, str):
                    raise TypeError("expected accessno to be a str but it is a %s" % builtins.type(accessno))
            self.__accessno = accessno
            return self

        def set_accessory(self, accessory):
            '''
            :type accessory: str or None
            '''

            if accessory is not None:
                if not isinstance(accessory, str):
                    raise TypeError("expected accessory to be a str but it is a %s" % builtins.type(accessory))
            self.__accessory = accessory
            return self

        def set_acqvalue(self, acqvalue):
            '''
            :type acqvalue: Decimal or None
            '''

            if acqvalue is not None:
                if not isinstance(acqvalue, decimal.Decimal):
                    raise TypeError("expected acqvalue to be a Decimal but it is a %s" % builtins.type(acqvalue))
            self.__acqvalue = acqvalue
            return self

        def set_age(self, age):
            '''
            :type age: str or None
            '''

            if age is not None:
                if not isinstance(age, str):
                    raise TypeError("expected age to be a str but it is a %s" % builtins.type(age))
            self.__age = age
            return self

        def set_appnotes(self, appnotes):
            '''
            :type appnotes: str or None
            '''

            if appnotes is not None:
                if not isinstance(appnotes, str):
                    raise TypeError("expected appnotes to be a str but it is a %s" % builtins.type(appnotes))
            self.__appnotes = appnotes
            return self

        def set_appraisor(self, appraisor):
            '''
            :type appraisor: str or None
            '''

            if appraisor is not None:
                if not isinstance(appraisor, str):
                    raise TypeError("expected appraisor to be a str but it is a %s" % builtins.type(appraisor))
            self.__appraisor = appraisor
            return self

        def set_assemzone(self, assemzone):
            '''
            :type assemzone: str or None
            '''

            if assemzone is not None:
                if not isinstance(assemzone, str):
                    raise TypeError("expected assemzone to be a str but it is a %s" % builtins.type(assemzone))
            self.__assemzone = assemzone
            return self

        def set_bagno(self, bagno):
            '''
            :type bagno: str or None
            '''

            if bagno is not None:
                if not isinstance(bagno, str):
                    raise TypeError("expected bagno to be a str but it is a %s" % builtins.type(bagno))
            self.__bagno = bagno
            return self

        def set_boxno(self, boxno):
            '''
            :type boxno: str or None
            '''

            if boxno is not None:
                if not isinstance(boxno, str):
                    raise TypeError("expected boxno to be a str but it is a %s" % builtins.type(boxno))
            self.__boxno = boxno
            return self

        def set_caption(self, caption):
            '''
            :type caption: str or None
            '''

            if caption is not None:
                if not isinstance(caption, str):
                    raise TypeError("expected caption to be a str but it is a %s" % builtins.type(caption))
            self.__caption = caption
            return self

        def set_cat(self, cat):
            '''
            :type cat: str or None
            '''

            if cat is not None:
                if not isinstance(cat, str):
                    raise TypeError("expected cat to be a str but it is a %s" % builtins.type(cat))
            self.__cat = cat
            return self

        def set_catby(self, catby):
            '''
            :type catby: str or None
            '''

            if catby is not None:
                if not isinstance(catby, str):
                    raise TypeError("expected catby to be a str but it is a %s" % builtins.type(catby))
            self.__catby = catby
            return self

        def set_catdate(self, catdate):
            '''
            :type catdate: datetime.datetime or None
            '''

            if catdate is not None:
                if not isinstance(catdate, datetime.datetime):
                    raise TypeError("expected catdate to be a datetime.datetime but it is a %s" % builtins.type(catdate))
            self.__catdate = catdate
            return self

        def set_cattype(self, cattype):
            '''
            :type cattype: str or None
            '''

            if cattype is not None:
                if not isinstance(cattype, str):
                    raise TypeError("expected cattype to be a str but it is a %s" % builtins.type(cattype))
            self.__cattype = cattype
            return self

        def set_chemcomp(self, chemcomp):
            '''
            :type chemcomp: str or None
            '''

            if chemcomp is not None:
                if not isinstance(chemcomp, str):
                    raise TypeError("expected chemcomp to be a str but it is a %s" % builtins.type(chemcomp))
            self.__chemcomp = chemcomp
            return self

        def set_circum(self, circum):
            '''
            :type circum: Decimal or None
            '''

            if circum is not None:
                if not isinstance(circum, decimal.Decimal):
                    raise TypeError("expected circum to be a Decimal but it is a %s" % builtins.type(circum))
            self.__circum = circum
            return self

        def set_circumft(self, circumft):
            '''
            :type circumft: Decimal or None
            '''

            if circumft is not None:
                if not isinstance(circumft, decimal.Decimal):
                    raise TypeError("expected circumft to be a Decimal but it is a %s" % builtins.type(circumft))
            self.__circumft = circumft
            return self

        def set_circumin(self, circumin):
            '''
            :type circumin: Decimal or None
            '''

            if circumin is not None:
                if not isinstance(circumin, decimal.Decimal):
                    raise TypeError("expected circumin to be a Decimal but it is a %s" % builtins.type(circumin))
            self.__circumin = circumin
            return self

        def set_classes(self, classes):
            '''
            :type classes: str or None
            '''

            if classes is not None:
                if not isinstance(classes, str):
                    raise TypeError("expected classes to be a str but it is a %s" % builtins.type(classes))
            self.__classes = classes
            return self

        def set_colldate(self, colldate):
            '''
            :type colldate: datetime.datetime or None
            '''

            if colldate is not None:
                if not isinstance(colldate, datetime.datetime):
                    raise TypeError("expected colldate to be a datetime.datetime but it is a %s" % builtins.type(colldate))
            self.__colldate = colldate
            return self

        def set_collection(self, collection):
            '''
            :type collection: str or None
            '''

            if collection is not None:
                if not isinstance(collection, str):
                    raise TypeError("expected collection to be a str but it is a %s" % builtins.type(collection))
            self.__collection = collection
            return self

        def set_collector(self, collector):
            '''
            :type collector: str or None
            '''

            if collector is not None:
                if not isinstance(collector, str):
                    raise TypeError("expected collector to be a str but it is a %s" % builtins.type(collector))
            self.__collector = collector
            return self

        def set_conddate(self, conddate):
            '''
            :type conddate: datetime.datetime or None
            '''

            if conddate is not None:
                if not isinstance(conddate, datetime.datetime):
                    raise TypeError("expected conddate to be a datetime.datetime but it is a %s" % builtins.type(conddate))
            self.__conddate = conddate
            return self

        def set_condexam(self, condexam):
            '''
            :type condexam: str or None
            '''

            if condexam is not None:
                if not isinstance(condexam, str):
                    raise TypeError("expected condexam to be a str but it is a %s" % builtins.type(condexam))
            self.__condexam = condexam
            return self

        def set_condition(self, condition):
            '''
            :type condition: str or None
            '''

            if condition is not None:
                if not isinstance(condition, str):
                    raise TypeError("expected condition to be a str but it is a %s" % builtins.type(condition))
            self.__condition = condition
            return self

        def set_condnotes(self, condnotes):
            '''
            :type condnotes: str or None
            '''

            if condnotes is not None:
                if not isinstance(condnotes, str):
                    raise TypeError("expected condnotes to be a str but it is a %s" % builtins.type(condnotes))
            self.__condnotes = condnotes
            return self

        def set_count(self, count):
            '''
            :type count: str or None
            '''

            if count is not None:
                if not isinstance(count, str):
                    raise TypeError("expected count to be a str but it is a %s" % builtins.type(count))
            self.__count = count
            return self

        def set_creator(self, creator):
            '''
            :type creator: str or None
            '''

            if creator is not None:
                if not isinstance(creator, str):
                    raise TypeError("expected creator to be a str but it is a %s" % builtins.type(creator))
            self.__creator = creator
            return self

        def set_creator2(self, creator2):
            '''
            :type creator2: str or None
            '''

            if creator2 is not None:
                if not isinstance(creator2, str):
                    raise TypeError("expected creator2 to be a str but it is a %s" % builtins.type(creator2))
            self.__creator2 = creator2
            return self

        def set_creator3(self, creator3):
            '''
            :type creator3: str or None
            '''

            if creator3 is not None:
                if not isinstance(creator3, str):
                    raise TypeError("expected creator3 to be a str but it is a %s" % builtins.type(creator3))
            self.__creator3 = creator3
            return self

        def set_credit(self, credit):
            '''
            :type credit: str or None
            '''

            if credit is not None:
                if not isinstance(credit, str):
                    raise TypeError("expected credit to be a str but it is a %s" % builtins.type(credit))
            self.__credit = credit
            return self

        def set_crystal(self, crystal):
            '''
            :type crystal: str or None
            '''

            if crystal is not None:
                if not isinstance(crystal, str):
                    raise TypeError("expected crystal to be a str but it is a %s" % builtins.type(crystal))
            self.__crystal = crystal
            return self

        def set_culture(self, culture):
            '''
            :type culture: str or None
            '''

            if culture is not None:
                if not isinstance(culture, str):
                    raise TypeError("expected culture to be a str but it is a %s" % builtins.type(culture))
            self.__culture = culture
            return self

        def set_curvalmax(self, curvalmax):
            '''
            :type curvalmax: Decimal or None
            '''

            if curvalmax is not None:
                if not isinstance(curvalmax, decimal.Decimal):
                    raise TypeError("expected curvalmax to be a Decimal but it is a %s" % builtins.type(curvalmax))
            self.__curvalmax = curvalmax
            return self

        def set_curvalue(self, curvalue):
            '''
            :type curvalue: Decimal or None
            '''

            if curvalue is not None:
                if not isinstance(curvalue, decimal.Decimal):
                    raise TypeError("expected curvalue to be a Decimal but it is a %s" % builtins.type(curvalue))
            self.__curvalue = curvalue
            return self

        def set_dataset(self, dataset):
            '''
            :type dataset: str or None
            '''

            if dataset is not None:
                if not isinstance(dataset, str):
                    raise TypeError("expected dataset to be a str but it is a %s" % builtins.type(dataset))
            self.__dataset = dataset
            return self

        def set_date(self, date):
            '''
            :type date: str or None
            '''

            if date is not None:
                if not isinstance(date, str):
                    raise TypeError("expected date to be a str but it is a %s" % builtins.type(date))
            self.__date = date
            return self

        def set_datingmeth(self, datingmeth):
            '''
            :type datingmeth: str or None
            '''

            if datingmeth is not None:
                if not isinstance(datingmeth, str):
                    raise TypeError("expected datingmeth to be a str but it is a %s" % builtins.type(datingmeth))
            self.__datingmeth = datingmeth
            return self

        def set_datum(self, datum):
            '''
            :type datum: str or None
            '''

            if datum is not None:
                if not isinstance(datum, str):
                    raise TypeError("expected datum to be a str but it is a %s" % builtins.type(datum))
            self.__datum = datum
            return self

        def set_depth(self, depth):
            '''
            :type depth: Decimal or None
            '''

            if depth is not None:
                if not isinstance(depth, decimal.Decimal):
                    raise TypeError("expected depth to be a Decimal but it is a %s" % builtins.type(depth))
            self.__depth = depth
            return self

        def set_depthft(self, depthft):
            '''
            :type depthft: Decimal or None
            '''

            if depthft is not None:
                if not isinstance(depthft, decimal.Decimal):
                    raise TypeError("expected depthft to be a Decimal but it is a %s" % builtins.type(depthft))
            self.__depthft = depthft
            return self

        def set_depthin(self, depthin):
            '''
            :type depthin: Decimal or None
            '''

            if depthin is not None:
                if not isinstance(depthin, decimal.Decimal):
                    raise TypeError("expected depthin to be a Decimal but it is a %s" % builtins.type(depthin))
            self.__depthin = depthin
            return self

        def set_descrip(self, descrip):
            '''
            :type descrip: str or None
            '''

            if descrip is not None:
                if not isinstance(descrip, str):
                    raise TypeError("expected descrip to be a str but it is a %s" % builtins.type(descrip))
            self.__descrip = descrip
            return self

        def set_diameter(self, diameter):
            '''
            :type diameter: Decimal or None
            '''

            if diameter is not None:
                if not isinstance(diameter, decimal.Decimal):
                    raise TypeError("expected diameter to be a Decimal but it is a %s" % builtins.type(diameter))
            self.__diameter = diameter
            return self

        def set_diameterft(self, diameterft):
            '''
            :type diameterft: Decimal or None
            '''

            if diameterft is not None:
                if not isinstance(diameterft, decimal.Decimal):
                    raise TypeError("expected diameterft to be a Decimal but it is a %s" % builtins.type(diameterft))
            self.__diameterft = diameterft
            return self

        def set_diameterin(self, diameterin):
            '''
            :type diameterin: Decimal or None
            '''

            if diameterin is not None:
                if not isinstance(diameterin, decimal.Decimal):
                    raise TypeError("expected diameterin to be a Decimal but it is a %s" % builtins.type(diameterin))
            self.__diameterin = diameterin
            return self

        def set_dimnotes(self, dimnotes):
            '''
            :type dimnotes: str or None
            '''

            if dimnotes is not None:
                if not isinstance(dimnotes, str):
                    raise TypeError("expected dimnotes to be a str but it is a %s" % builtins.type(dimnotes))
            self.__dimnotes = dimnotes
            return self

        def set_dimtype(self, dimtype):
            '''
            :type dimtype: int or None
            '''

            if dimtype is not None:
                if not isinstance(dimtype, int):
                    raise TypeError("expected dimtype to be a int but it is a %s" % builtins.type(dimtype))
            self.__dimtype = dimtype
            return self

        def set_dispvalue(self, dispvalue):
            '''
            :type dispvalue: str or None
            '''

            if dispvalue is not None:
                if not isinstance(dispvalue, str):
                    raise TypeError("expected dispvalue to be a str but it is a %s" % builtins.type(dispvalue))
            self.__dispvalue = dispvalue
            return self

        def set_earlydate(self, earlydate):
            '''
            :type earlydate: int or None
            '''

            if earlydate is not None:
                if not isinstance(earlydate, int):
                    raise TypeError("expected earlydate to be a int but it is a %s" % builtins.type(earlydate))
            self.__earlydate = earlydate
            return self

        def set_elements(self, elements):
            '''
            :type elements: str or None
            '''

            if elements is not None:
                if not isinstance(elements, str):
                    raise TypeError("expected elements to be a str but it is a %s" % builtins.type(elements))
            self.__elements = elements
            return self

        def set_epoch(self, epoch):
            '''
            :type epoch: str or None
            '''

            if epoch is not None:
                if not isinstance(epoch, str):
                    raise TypeError("expected epoch to be a str but it is a %s" % builtins.type(epoch))
            self.__epoch = epoch
            return self

        def set_era(self, era):
            '''
            :type era: str or None
            '''

            if era is not None:
                if not isinstance(era, str):
                    raise TypeError("expected era to be a str but it is a %s" % builtins.type(era))
            self.__era = era
            return self

        def set_event(self, event):
            '''
            :type event: str or None
            '''

            if event is not None:
                if not isinstance(event, str):
                    raise TypeError("expected event to be a str but it is a %s" % builtins.type(event))
            self.__event = event
            return self

        def set_ew(self, ew):
            '''
            :type ew: str or None
            '''

            if ew is not None:
                if not isinstance(ew, str):
                    raise TypeError("expected ew to be a str but it is a %s" % builtins.type(ew))
            self.__ew = ew
            return self

        def set_excavadate(self, excavadate):
            '''
            :type excavadate: datetime.datetime or None
            '''

            if excavadate is not None:
                if not isinstance(excavadate, datetime.datetime):
                    raise TypeError("expected excavadate to be a datetime.datetime but it is a %s" % builtins.type(excavadate))
            self.__excavadate = excavadate
            return self

        def set_excavateby(self, excavateby):
            '''
            :type excavateby: str or None
            '''

            if excavateby is not None:
                if not isinstance(excavateby, str):
                    raise TypeError("expected excavateby to be a str but it is a %s" % builtins.type(excavateby))
            self.__excavateby = excavateby
            return self

        def set_exhibitid(self, exhibitid):
            '''
            :type exhibitid: str or None
            '''

            if exhibitid is not None:
                if not isinstance(exhibitid, str):
                    raise TypeError("expected exhibitid to be a str but it is a %s" % builtins.type(exhibitid))
            self.__exhibitid = exhibitid
            return self

        def set_exhibitno(self, exhibitno):
            '''
            :type exhibitno: int or None
            '''

            if exhibitno is not None:
                if not isinstance(exhibitno, int):
                    raise TypeError("expected exhibitno to be a int but it is a %s" % builtins.type(exhibitno))
            self.__exhibitno = exhibitno
            return self

        def set_exhlabel1(self, exhlabel1):
            '''
            :type exhlabel1: str or None
            '''

            if exhlabel1 is not None:
                if not isinstance(exhlabel1, str):
                    raise TypeError("expected exhlabel1 to be a str but it is a %s" % builtins.type(exhlabel1))
            self.__exhlabel1 = exhlabel1
            return self

        def set_exhlabel2(self, exhlabel2):
            '''
            :type exhlabel2: str or None
            '''

            if exhlabel2 is not None:
                if not isinstance(exhlabel2, str):
                    raise TypeError("expected exhlabel2 to be a str but it is a %s" % builtins.type(exhlabel2))
            self.__exhlabel2 = exhlabel2
            return self

        def set_exhlabel3(self, exhlabel3):
            '''
            :type exhlabel3: str or None
            '''

            if exhlabel3 is not None:
                if not isinstance(exhlabel3, str):
                    raise TypeError("expected exhlabel3 to be a str but it is a %s" % builtins.type(exhlabel3))
            self.__exhlabel3 = exhlabel3
            return self

        def set_exhlabel4(self, exhlabel4):
            '''
            :type exhlabel4: str or None
            '''

            if exhlabel4 is not None:
                if not isinstance(exhlabel4, str):
                    raise TypeError("expected exhlabel4 to be a str but it is a %s" % builtins.type(exhlabel4))
            self.__exhlabel4 = exhlabel4
            return self

        def set_exhstart(self, exhstart):
            '''
            :type exhstart: datetime.datetime or None
            '''

            if exhstart is not None:
                if not isinstance(exhstart, datetime.datetime):
                    raise TypeError("expected exhstart to be a datetime.datetime but it is a %s" % builtins.type(exhstart))
            self.__exhstart = exhstart
            return self

        def set_family(self, family):
            '''
            :type family: str or None
            '''

            if family is not None:
                if not isinstance(family, str):
                    raise TypeError("expected family to be a str but it is a %s" % builtins.type(family))
            self.__family = family
            return self

        def set_feature(self, feature):
            '''
            :type feature: str or None
            '''

            if feature is not None:
                if not isinstance(feature, str):
                    raise TypeError("expected feature to be a str but it is a %s" % builtins.type(feature))
            self.__feature = feature
            return self

        def set_flagdate(self, flagdate):
            '''
            :type flagdate: datetime.datetime or None
            '''

            if flagdate is not None:
                if not isinstance(flagdate, datetime.datetime):
                    raise TypeError("expected flagdate to be a datetime.datetime but it is a %s" % builtins.type(flagdate))
            self.__flagdate = flagdate
            return self

        def set_flagnotes(self, flagnotes):
            '''
            :type flagnotes: str or None
            '''

            if flagnotes is not None:
                if not isinstance(flagnotes, str):
                    raise TypeError("expected flagnotes to be a str but it is a %s" % builtins.type(flagnotes))
            self.__flagnotes = flagnotes
            return self

        def set_flagreason(self, flagreason):
            '''
            :type flagreason: str or None
            '''

            if flagreason is not None:
                if not isinstance(flagreason, str):
                    raise TypeError("expected flagreason to be a str but it is a %s" % builtins.type(flagreason))
            self.__flagreason = flagreason
            return self

        def set_formation(self, formation):
            '''
            :type formation: str or None
            '''

            if formation is not None:
                if not isinstance(formation, str):
                    raise TypeError("expected formation to be a str but it is a %s" % builtins.type(formation))
            self.__formation = formation
            return self

        def set_fossils(self, fossils):
            '''
            :type fossils: str or None
            '''

            if fossils is not None:
                if not isinstance(fossils, str):
                    raise TypeError("expected fossils to be a str but it is a %s" % builtins.type(fossils))
            self.__fossils = fossils
            return self

        def set_found(self, found):
            '''
            :type found: str or None
            '''

            if found is not None:
                if not isinstance(found, str):
                    raise TypeError("expected found to be a str but it is a %s" % builtins.type(found))
            self.__found = found
            return self

        def set_fracture(self, fracture):
            '''
            :type fracture: str or None
            '''

            if fracture is not None:
                if not isinstance(fracture, str):
                    raise TypeError("expected fracture to be a str but it is a %s" % builtins.type(fracture))
            self.__fracture = fracture
            return self

        def set_frame(self, frame):
            '''
            :type frame: str or None
            '''

            if frame is not None:
                if not isinstance(frame, str):
                    raise TypeError("expected frame to be a str but it is a %s" % builtins.type(frame))
            self.__frame = frame
            return self

        def set_framesize(self, framesize):
            '''
            :type framesize: str or None
            '''

            if framesize is not None:
                if not isinstance(framesize, str):
                    raise TypeError("expected framesize to be a str but it is a %s" % builtins.type(framesize))
            self.__framesize = framesize
            return self

        def set_genus(self, genus):
            '''
            :type genus: str or None
            '''

            if genus is not None:
                if not isinstance(genus, str):
                    raise TypeError("expected genus to be a str but it is a %s" % builtins.type(genus))
            self.__genus = genus
            return self

        def set_gparent(self, gparent):
            '''
            :type gparent: str or None
            '''

            if gparent is not None:
                if not isinstance(gparent, str):
                    raise TypeError("expected gparent to be a str but it is a %s" % builtins.type(gparent))
            self.__gparent = gparent
            return self

        def set_grainsize(self, grainsize):
            '''
            :type grainsize: str or None
            '''

            if grainsize is not None:
                if not isinstance(grainsize, str):
                    raise TypeError("expected grainsize to be a str but it is a %s" % builtins.type(grainsize))
            self.__grainsize = grainsize
            return self

        def set_habitat(self, habitat):
            '''
            :type habitat: str or None
            '''

            if habitat is not None:
                if not isinstance(habitat, str):
                    raise TypeError("expected habitat to be a str but it is a %s" % builtins.type(habitat))
            self.__habitat = habitat
            return self

        def set_hardness(self, hardness):
            '''
            :type hardness: str or None
            '''

            if hardness is not None:
                if not isinstance(hardness, str):
                    raise TypeError("expected hardness to be a str but it is a %s" % builtins.type(hardness))
            self.__hardness = hardness
            return self

        def set_height(self, height):
            '''
            :type height: Decimal or None
            '''

            if height is not None:
                if not isinstance(height, decimal.Decimal):
                    raise TypeError("expected height to be a Decimal but it is a %s" % builtins.type(height))
            self.__height = height
            return self

        def set_heightft(self, heightft):
            '''
            :type heightft: Decimal or None
            '''

            if heightft is not None:
                if not isinstance(heightft, decimal.Decimal):
                    raise TypeError("expected heightft to be a Decimal but it is a %s" % builtins.type(heightft))
            self.__heightft = heightft
            return self

        def set_heightin(self, heightin):
            '''
            :type heightin: Decimal or None
            '''

            if heightin is not None:
                if not isinstance(heightin, decimal.Decimal):
                    raise TypeError("expected heightin to be a Decimal but it is a %s" % builtins.type(heightin))
            self.__heightin = heightin
            return self

        def set_homeloc(self, homeloc):
            '''
            :type homeloc: str or None
            '''

            if homeloc is not None:
                if not isinstance(homeloc, str):
                    raise TypeError("expected homeloc to be a str but it is a %s" % builtins.type(homeloc))
            self.__homeloc = homeloc
            return self

        def set_idby(self, idby):
            '''
            :type idby: str or None
            '''

            if idby is not None:
                if not isinstance(idby, str):
                    raise TypeError("expected idby to be a str but it is a %s" % builtins.type(idby))
            self.__idby = idby
            return self

        def set_iddate(self, iddate):
            '''
            :type iddate: datetime.datetime or None
            '''

            if iddate is not None:
                if not isinstance(iddate, datetime.datetime):
                    raise TypeError("expected iddate to be a datetime.datetime but it is a %s" % builtins.type(iddate))
            self.__iddate = iddate
            return self

        def set_imagefile(self, imagefile):
            '''
            :type imagefile: str or None
            '''

            if imagefile is not None:
                if not isinstance(imagefile, str):
                    raise TypeError("expected imagefile to be a str but it is a %s" % builtins.type(imagefile))
            self.__imagefile = imagefile
            return self

        def set_imageno(self, imageno):
            '''
            :type imageno: int or None
            '''

            if imageno is not None:
                if not isinstance(imageno, int):
                    raise TypeError("expected imageno to be a int but it is a %s" % builtins.type(imageno))
            self.__imageno = imageno
            return self

        def set_imagesize(self, imagesize):
            '''
            :type imagesize: str or None
            '''

            if imagesize is not None:
                if not isinstance(imagesize, str):
                    raise TypeError("expected imagesize to be a str but it is a %s" % builtins.type(imagesize))
            self.__imagesize = imagesize
            return self

        def set_inscomp(self, inscomp):
            '''
            :type inscomp: str or None
            '''

            if inscomp is not None:
                if not isinstance(inscomp, str):
                    raise TypeError("expected inscomp to be a str but it is a %s" % builtins.type(inscomp))
            self.__inscomp = inscomp
            return self

        def set_inscrlang(self, inscrlang):
            '''
            :type inscrlang: str or None
            '''

            if inscrlang is not None:
                if not isinstance(inscrlang, str):
                    raise TypeError("expected inscrlang to be a str but it is a %s" % builtins.type(inscrlang))
            self.__inscrlang = inscrlang
            return self

        def set_inscrpos(self, inscrpos):
            '''
            :type inscrpos: str or None
            '''

            if inscrpos is not None:
                if not isinstance(inscrpos, str):
                    raise TypeError("expected inscrpos to be a str but it is a %s" % builtins.type(inscrpos))
            self.__inscrpos = inscrpos
            return self

        def set_inscrtech(self, inscrtech):
            '''
            :type inscrtech: str or None
            '''

            if inscrtech is not None:
                if not isinstance(inscrtech, str):
                    raise TypeError("expected inscrtech to be a str but it is a %s" % builtins.type(inscrtech))
            self.__inscrtech = inscrtech
            return self

        def set_inscrtext(self, inscrtext):
            '''
            :type inscrtext: str or None
            '''

            if inscrtext is not None:
                if not isinstance(inscrtext, str):
                    raise TypeError("expected inscrtext to be a str but it is a %s" % builtins.type(inscrtext))
            self.__inscrtext = inscrtext
            return self

        def set_inscrtrans(self, inscrtrans):
            '''
            :type inscrtrans: str or None
            '''

            if inscrtrans is not None:
                if not isinstance(inscrtrans, str):
                    raise TypeError("expected inscrtrans to be a str but it is a %s" % builtins.type(inscrtrans))
            self.__inscrtrans = inscrtrans
            return self

        def set_inscrtype(self, inscrtype):
            '''
            :type inscrtype: str or None
            '''

            if inscrtype is not None:
                if not isinstance(inscrtype, str):
                    raise TypeError("expected inscrtype to be a str but it is a %s" % builtins.type(inscrtype))
            self.__inscrtype = inscrtype
            return self

        def set_insdate(self, insdate):
            '''
            :type insdate: datetime.datetime or None
            '''

            if insdate is not None:
                if not isinstance(insdate, datetime.datetime):
                    raise TypeError("expected insdate to be a datetime.datetime but it is a %s" % builtins.type(insdate))
            self.__insdate = insdate
            return self

        def set_insphone(self, insphone):
            '''
            :type insphone: str or None
            '''

            if insphone is not None:
                if not isinstance(insphone, str):
                    raise TypeError("expected insphone to be a str but it is a %s" % builtins.type(insphone))
            self.__insphone = insphone
            return self

        def set_inspremium(self, inspremium):
            '''
            :type inspremium: str or None
            '''

            if inspremium is not None:
                if not isinstance(inspremium, str):
                    raise TypeError("expected inspremium to be a str but it is a %s" % builtins.type(inspremium))
            self.__inspremium = inspremium
            return self

        def set_insrep(self, insrep):
            '''
            :type insrep: str or None
            '''

            if insrep is not None:
                if not isinstance(insrep, str):
                    raise TypeError("expected insrep to be a str but it is a %s" % builtins.type(insrep))
            self.__insrep = insrep
            return self

        def set_insvalue(self, insvalue):
            '''
            :type insvalue: Decimal or None
            '''

            if insvalue is not None:
                if not isinstance(insvalue, decimal.Decimal):
                    raise TypeError("expected insvalue to be a Decimal but it is a %s" % builtins.type(insvalue))
            self.__insvalue = insvalue
            return self

        def set_invnby(self, invnby):
            '''
            :type invnby: str or None
            '''

            if invnby is not None:
                if not isinstance(invnby, str):
                    raise TypeError("expected invnby to be a str but it is a %s" % builtins.type(invnby))
            self.__invnby = invnby
            return self

        def set_invndate(self, invndate):
            '''
            :type invndate: datetime.datetime or None
            '''

            if invndate is not None:
                if not isinstance(invndate, datetime.datetime):
                    raise TypeError("expected invndate to be a datetime.datetime but it is a %s" % builtins.type(invndate))
            self.__invndate = invndate
            return self

        def set_kingdom(self, kingdom):
            '''
            :type kingdom: str or None
            '''

            if kingdom is not None:
                if not isinstance(kingdom, str):
                    raise TypeError("expected kingdom to be a str but it is a %s" % builtins.type(kingdom))
            self.__kingdom = kingdom
            return self

        def set_latdeg(self, latdeg):
            '''
            :type latdeg: Decimal or None
            '''

            if latdeg is not None:
                if not isinstance(latdeg, decimal.Decimal):
                    raise TypeError("expected latdeg to be a Decimal but it is a %s" % builtins.type(latdeg))
            self.__latdeg = latdeg
            return self

        def set_latedate(self, latedate):
            '''
            :type latedate: int or None
            '''

            if latedate is not None:
                if not isinstance(latedate, int):
                    raise TypeError("expected latedate to be a int but it is a %s" % builtins.type(latedate))
            self.__latedate = latedate
            return self

        def set_legal(self, legal):
            '''
            :type legal: str or None
            '''

            if legal is not None:
                if not isinstance(legal, str):
                    raise TypeError("expected legal to be a str but it is a %s" % builtins.type(legal))
            self.__legal = legal
            return self

        def set_length(self, length):
            '''
            :type length: Decimal or None
            '''

            if length is not None:
                if not isinstance(length, decimal.Decimal):
                    raise TypeError("expected length to be a Decimal but it is a %s" % builtins.type(length))
            self.__length = length
            return self

        def set_lengthft(self, lengthft):
            '''
            :type lengthft: Decimal or None
            '''

            if lengthft is not None:
                if not isinstance(lengthft, decimal.Decimal):
                    raise TypeError("expected lengthft to be a Decimal but it is a %s" % builtins.type(lengthft))
            self.__lengthft = lengthft
            return self

        def set_lengthin(self, lengthin):
            '''
            :type lengthin: Decimal or None
            '''

            if lengthin is not None:
                if not isinstance(lengthin, decimal.Decimal):
                    raise TypeError("expected lengthin to be a Decimal but it is a %s" % builtins.type(lengthin))
            self.__lengthin = lengthin
            return self

        def set_level(self, level):
            '''
            :type level: str or None
            '''

            if level is not None:
                if not isinstance(level, str):
                    raise TypeError("expected level to be a str but it is a %s" % builtins.type(level))
            self.__level = level
            return self

        def set_lithofacie(self, lithofacie):
            '''
            :type lithofacie: str or None
            '''

            if lithofacie is not None:
                if not isinstance(lithofacie, str):
                    raise TypeError("expected lithofacie to be a str but it is a %s" % builtins.type(lithofacie))
            self.__lithofacie = lithofacie
            return self

        def set_loancond(self, loancond):
            '''
            :type loancond: str or None
            '''

            if loancond is not None:
                if not isinstance(loancond, str):
                    raise TypeError("expected loancond to be a str but it is a %s" % builtins.type(loancond))
            self.__loancond = loancond
            return self

        def set_loandue(self, loandue):
            '''
            :type loandue: datetime.datetime or None
            '''

            if loandue is not None:
                if not isinstance(loandue, datetime.datetime):
                    raise TypeError("expected loandue to be a datetime.datetime but it is a %s" % builtins.type(loandue))
            self.__loandue = loandue
            return self

        def set_loanid(self, loanid):
            '''
            :type loanid: str or None
            '''

            if loanid is not None:
                if not isinstance(loanid, str):
                    raise TypeError("expected loanid to be a str but it is a %s" % builtins.type(loanid))
            self.__loanid = loanid
            return self

        def set_loaninno(self, loaninno):
            '''
            :type loaninno: str or None
            '''

            if loaninno is not None:
                if not isinstance(loaninno, str):
                    raise TypeError("expected loaninno to be a str but it is a %s" % builtins.type(loaninno))
            self.__loaninno = loaninno
            return self

        def set_loanno(self, loanno):
            '''
            :type loanno: int or None
            '''

            if loanno is not None:
                if not isinstance(loanno, int):
                    raise TypeError("expected loanno to be a int but it is a %s" % builtins.type(loanno))
            self.__loanno = loanno
            return self

        def set_loanrenew(self, loanrenew):
            '''
            :type loanrenew: datetime.datetime or None
            '''

            if loanrenew is not None:
                if not isinstance(loanrenew, datetime.datetime):
                    raise TypeError("expected loanrenew to be a datetime.datetime but it is a %s" % builtins.type(loanrenew))
            self.__loanrenew = loanrenew
            return self

        def set_locfield1(self, locfield1):
            '''
            :type locfield1: str or None
            '''

            if locfield1 is not None:
                if not isinstance(locfield1, str):
                    raise TypeError("expected locfield1 to be a str but it is a %s" % builtins.type(locfield1))
            self.__locfield1 = locfield1
            return self

        def set_locfield2(self, locfield2):
            '''
            :type locfield2: str or None
            '''

            if locfield2 is not None:
                if not isinstance(locfield2, str):
                    raise TypeError("expected locfield2 to be a str but it is a %s" % builtins.type(locfield2))
            self.__locfield2 = locfield2
            return self

        def set_locfield3(self, locfield3):
            '''
            :type locfield3: str or None
            '''

            if locfield3 is not None:
                if not isinstance(locfield3, str):
                    raise TypeError("expected locfield3 to be a str but it is a %s" % builtins.type(locfield3))
            self.__locfield3 = locfield3
            return self

        def set_locfield4(self, locfield4):
            '''
            :type locfield4: str or None
            '''

            if locfield4 is not None:
                if not isinstance(locfield4, str):
                    raise TypeError("expected locfield4 to be a str but it is a %s" % builtins.type(locfield4))
            self.__locfield4 = locfield4
            return self

        def set_locfield5(self, locfield5):
            '''
            :type locfield5: str or None
            '''

            if locfield5 is not None:
                if not isinstance(locfield5, str):
                    raise TypeError("expected locfield5 to be a str but it is a %s" % builtins.type(locfield5))
            self.__locfield5 = locfield5
            return self

        def set_locfield6(self, locfield6):
            '''
            :type locfield6: str or None
            '''

            if locfield6 is not None:
                if not isinstance(locfield6, str):
                    raise TypeError("expected locfield6 to be a str but it is a %s" % builtins.type(locfield6))
            self.__locfield6 = locfield6
            return self

        def set_longdeg(self, longdeg):
            '''
            :type longdeg: Decimal or None
            '''

            if longdeg is not None:
                if not isinstance(longdeg, decimal.Decimal):
                    raise TypeError("expected longdeg to be a Decimal but it is a %s" % builtins.type(longdeg))
            self.__longdeg = longdeg
            return self

        def set_luster(self, luster):
            '''
            :type luster: str or None
            '''

            if luster is not None:
                if not isinstance(luster, str):
                    raise TypeError("expected luster to be a str but it is a %s" % builtins.type(luster))
            self.__luster = luster
            return self

        def set_made(self, made):
            '''
            :type made: str or None
            '''

            if made is not None:
                if not isinstance(made, str):
                    raise TypeError("expected made to be a str but it is a %s" % builtins.type(made))
            self.__made = made
            return self

        def set_maintcycle(self, maintcycle):
            '''
            :type maintcycle: str or None
            '''

            if maintcycle is not None:
                if not isinstance(maintcycle, str):
                    raise TypeError("expected maintcycle to be a str but it is a %s" % builtins.type(maintcycle))
            self.__maintcycle = maintcycle
            return self

        def set_maintdate(self, maintdate):
            '''
            :type maintdate: datetime.datetime or None
            '''

            if maintdate is not None:
                if not isinstance(maintdate, datetime.datetime):
                    raise TypeError("expected maintdate to be a datetime.datetime but it is a %s" % builtins.type(maintdate))
            self.__maintdate = maintdate
            return self

        def set_maintnote(self, maintnote):
            '''
            :type maintnote: str or None
            '''

            if maintnote is not None:
                if not isinstance(maintnote, str):
                    raise TypeError("expected maintnote to be a str but it is a %s" % builtins.type(maintnote))
            self.__maintnote = maintnote
            return self

        def set_material(self, material):
            '''
            :type material: str or None
            '''

            if material is not None:
                if not isinstance(material, str):
                    raise TypeError("expected material to be a str but it is a %s" % builtins.type(material))
            self.__material = material
            return self

        def set_medium(self, medium):
            '''
            :type medium: str or None
            '''

            if medium is not None:
                if not isinstance(medium, str):
                    raise TypeError("expected medium to be a str but it is a %s" % builtins.type(medium))
            self.__medium = medium
            return self

        def set_member(self, member):
            '''
            :type member: str or None
            '''

            if member is not None:
                if not isinstance(member, str):
                    raise TypeError("expected member to be a str but it is a %s" % builtins.type(member))
            self.__member = member
            return self

        def set_mmark(self, mmark):
            '''
            :type mmark: str or None
            '''

            if mmark is not None:
                if not isinstance(mmark, str):
                    raise TypeError("expected mmark to be a str but it is a %s" % builtins.type(mmark))
            self.__mmark = mmark
            return self

        def set_nhclass(self, nhclass):
            '''
            :type nhclass: str or None
            '''

            if nhclass is not None:
                if not isinstance(nhclass, str):
                    raise TypeError("expected nhclass to be a str but it is a %s" % builtins.type(nhclass))
            self.__nhclass = nhclass
            return self

        def set_nhorder(self, nhorder):
            '''
            :type nhorder: str or None
            '''

            if nhorder is not None:
                if not isinstance(nhorder, str):
                    raise TypeError("expected nhorder to be a str but it is a %s" % builtins.type(nhorder))
            self.__nhorder = nhorder
            return self

        def set_notes(self, notes):
            '''
            :type notes: str or None
            '''

            if notes is not None:
                if not isinstance(notes, str):
                    raise TypeError("expected notes to be a str but it is a %s" % builtins.type(notes))
            self.__notes = notes
            return self

        def set_ns(self, ns):
            '''
            :type ns: str or None
            '''

            if ns is not None:
                if not isinstance(ns, str):
                    raise TypeError("expected ns to be a str but it is a %s" % builtins.type(ns))
            self.__ns = ns
            return self

        def set_objectid(self, objectid):
            '''
            :type objectid: str or None
            '''

            if objectid is not None:
                if not isinstance(objectid, str):
                    raise TypeError("expected objectid to be a str but it is a %s" % builtins.type(objectid))
            self.__objectid = objectid
            return self

        def set_objname(self, objname):
            '''
            :type objname: str or None
            '''

            if objname is not None:
                if not isinstance(objname, str):
                    raise TypeError("expected objname to be a str but it is a %s" % builtins.type(objname))
            self.__objname = objname
            return self

        def set_objname2(self, objname2):
            '''
            :type objname2: str or None
            '''

            if objname2 is not None:
                if not isinstance(objname2, str):
                    raise TypeError("expected objname2 to be a str but it is a %s" % builtins.type(objname2))
            self.__objname2 = objname2
            return self

        def set_objname3(self, objname3):
            '''
            :type objname3: str or None
            '''

            if objname3 is not None:
                if not isinstance(objname3, str):
                    raise TypeError("expected objname3 to be a str but it is a %s" % builtins.type(objname3))
            self.__objname3 = objname3
            return self

        def set_objnames(self, objnames):
            '''
            :type objnames: str or None
            '''

            if objnames is not None:
                if not isinstance(objnames, str):
                    raise TypeError("expected objnames to be a str but it is a %s" % builtins.type(objnames))
            self.__objnames = objnames
            return self

        def set_occurrence(self, occurrence):
            '''
            :type occurrence: str or None
            '''

            if occurrence is not None:
                if not isinstance(occurrence, str):
                    raise TypeError("expected occurrence to be a str but it is a %s" % builtins.type(occurrence))
            self.__occurrence = occurrence
            return self

        def set_oldno(self, oldno):
            '''
            :type oldno: str or None
            '''

            if oldno is not None:
                if not isinstance(oldno, str):
                    raise TypeError("expected oldno to be a str but it is a %s" % builtins.type(oldno))
            self.__oldno = oldno
            return self

        def set_origin(self, origin):
            '''
            :type origin: str or None
            '''

            if origin is not None:
                if not isinstance(origin, str):
                    raise TypeError("expected origin to be a str but it is a %s" % builtins.type(origin))
            self.__origin = origin
            return self

        def set_othername(self, othername):
            '''
            :type othername: str or None
            '''

            if othername is not None:
                if not isinstance(othername, str):
                    raise TypeError("expected othername to be a str but it is a %s" % builtins.type(othername))
            self.__othername = othername
            return self

        def set_otherno(self, otherno):
            '''
            :type otherno: str or None
            '''

            if otherno is not None:
                if not isinstance(otherno, str):
                    raise TypeError("expected otherno to be a str but it is a %s" % builtins.type(otherno))
            self.__otherno = otherno
            return self

        def set_outdate(self, outdate):
            '''
            :type outdate: datetime.datetime or None
            '''

            if outdate is not None:
                if not isinstance(outdate, datetime.datetime):
                    raise TypeError("expected outdate to be a datetime.datetime but it is a %s" % builtins.type(outdate))
            self.__outdate = outdate
            return self

        def set_owned(self, owned):
            '''
            :type owned: str or None
            '''

            if owned is not None:
                if not isinstance(owned, str):
                    raise TypeError("expected owned to be a str but it is a %s" % builtins.type(owned))
            self.__owned = owned
            return self

        def set_parent(self, parent):
            '''
            :type parent: str or None
            '''

            if parent is not None:
                if not isinstance(parent, str):
                    raise TypeError("expected parent to be a str but it is a %s" % builtins.type(parent))
            self.__parent = parent
            return self

        def set_people(self, people):
            '''
            :type people: str or None
            '''

            if people is not None:
                if not isinstance(people, str):
                    raise TypeError("expected people to be a str but it is a %s" % builtins.type(people))
            self.__people = people
            return self

        def set_period(self, period):
            '''
            :type period: str or None
            '''

            if period is not None:
                if not isinstance(period, str):
                    raise TypeError("expected period to be a str but it is a %s" % builtins.type(period))
            self.__period = period
            return self

        def set_phylum(self, phylum):
            '''
            :type phylum: str or None
            '''

            if phylum is not None:
                if not isinstance(phylum, str):
                    raise TypeError("expected phylum to be a str but it is a %s" % builtins.type(phylum))
            self.__phylum = phylum
            return self

        def set_policyno(self, policyno):
            '''
            :type policyno: str or None
            '''

            if policyno is not None:
                if not isinstance(policyno, str):
                    raise TypeError("expected policyno to be a str but it is a %s" % builtins.type(policyno))
            self.__policyno = policyno
            return self

        def set_ppid(self, ppid):
            '''
            :type ppid: str or None
            '''

            if ppid is not None:
                if not isinstance(ppid, str):
                    raise TypeError("expected ppid to be a str but it is a %s" % builtins.type(ppid))
            self.__ppid = ppid
            return self

        def set_preparator(self, preparator):
            '''
            :type preparator: str or None
            '''

            if preparator is not None:
                if not isinstance(preparator, str):
                    raise TypeError("expected preparator to be a str but it is a %s" % builtins.type(preparator))
            self.__preparator = preparator
            return self

        def set_prepdate(self, prepdate):
            '''
            :type prepdate: datetime.datetime or None
            '''

            if prepdate is not None:
                if not isinstance(prepdate, datetime.datetime):
                    raise TypeError("expected prepdate to be a datetime.datetime but it is a %s" % builtins.type(prepdate))
            self.__prepdate = prepdate
            return self

        def set_preserve(self, preserve):
            '''
            :type preserve: str or None
            '''

            if preserve is not None:
                if not isinstance(preserve, str):
                    raise TypeError("expected preserve to be a str but it is a %s" % builtins.type(preserve))
            self.__preserve = preserve
            return self

        def set_pressure(self, pressure):
            '''
            :type pressure: str or None
            '''

            if pressure is not None:
                if not isinstance(pressure, str):
                    raise TypeError("expected pressure to be a str but it is a %s" % builtins.type(pressure))
            self.__pressure = pressure
            return self

        def set_provenance(self, provenance):
            '''
            :type provenance: str or None
            '''

            if provenance is not None:
                if not isinstance(provenance, str):
                    raise TypeError("expected provenance to be a str but it is a %s" % builtins.type(provenance))
            self.__provenance = provenance
            return self

        def set_pubnotes(self, pubnotes):
            '''
            :type pubnotes: str or None
            '''

            if pubnotes is not None:
                if not isinstance(pubnotes, str):
                    raise TypeError("expected pubnotes to be a str but it is a %s" % builtins.type(pubnotes))
            self.__pubnotes = pubnotes
            return self

        def set_qrurl(self, qrurl):
            '''
            :type qrurl: str or None
            '''

            if qrurl is not None:
                if not isinstance(qrurl, str):
                    raise TypeError("expected qrurl to be a str but it is a %s" % builtins.type(qrurl))
            self.__qrurl = qrurl
            return self

        def set_recas(self, recas):
            '''
            :type recas: str or None
            '''

            if recas is not None:
                if not isinstance(recas, str):
                    raise TypeError("expected recas to be a str but it is a %s" % builtins.type(recas))
            self.__recas = recas
            return self

        def set_recdate(self, recdate):
            '''
            :type recdate: str or None
            '''

            if recdate is not None:
                if not isinstance(recdate, str):
                    raise TypeError("expected recdate to be a str but it is a %s" % builtins.type(recdate))
            self.__recdate = recdate
            return self

        def set_recfrom(self, recfrom):
            '''
            :type recfrom: str or None
            '''

            if recfrom is not None:
                if not isinstance(recfrom, str):
                    raise TypeError("expected recfrom to be a str but it is a %s" % builtins.type(recfrom))
            self.__recfrom = recfrom
            return self

        def set_relation(self, relation):
            '''
            :type relation: str or None
            '''

            if relation is not None:
                if not isinstance(relation, str):
                    raise TypeError("expected relation to be a str but it is a %s" % builtins.type(relation))
            self.__relation = relation
            return self

        def set_relnotes(self, relnotes):
            '''
            :type relnotes: str or None
            '''

            if relnotes is not None:
                if not isinstance(relnotes, str):
                    raise TypeError("expected relnotes to be a str but it is a %s" % builtins.type(relnotes))
            self.__relnotes = relnotes
            return self

        def set_renewuntil(self, renewuntil):
            '''
            :type renewuntil: datetime.datetime or None
            '''

            if renewuntil is not None:
                if not isinstance(renewuntil, datetime.datetime):
                    raise TypeError("expected renewuntil to be a datetime.datetime but it is a %s" % builtins.type(renewuntil))
            self.__renewuntil = renewuntil
            return self

        def set_repatby(self, repatby):
            '''
            :type repatby: str or None
            '''

            if repatby is not None:
                if not isinstance(repatby, str):
                    raise TypeError("expected repatby to be a str but it is a %s" % builtins.type(repatby))
            self.__repatby = repatby
            return self

        def set_repatclaim(self, repatclaim):
            '''
            :type repatclaim: str or None
            '''

            if repatclaim is not None:
                if not isinstance(repatclaim, str):
                    raise TypeError("expected repatclaim to be a str but it is a %s" % builtins.type(repatclaim))
            self.__repatclaim = repatclaim
            return self

        def set_repatdate(self, repatdate):
            '''
            :type repatdate: datetime.datetime or None
            '''

            if repatdate is not None:
                if not isinstance(repatdate, datetime.datetime):
                    raise TypeError("expected repatdate to be a datetime.datetime but it is a %s" % builtins.type(repatdate))
            self.__repatdate = repatdate
            return self

        def set_repatdisp(self, repatdisp):
            '''
            :type repatdisp: str or None
            '''

            if repatdisp is not None:
                if not isinstance(repatdisp, str):
                    raise TypeError("expected repatdisp to be a str but it is a %s" % builtins.type(repatdisp))
            self.__repatdisp = repatdisp
            return self

        def set_repathand(self, repathand):
            '''
            :type repathand: str or None
            '''

            if repathand is not None:
                if not isinstance(repathand, str):
                    raise TypeError("expected repathand to be a str but it is a %s" % builtins.type(repathand))
            self.__repathand = repathand
            return self

        def set_repatnotes(self, repatnotes):
            '''
            :type repatnotes: str or None
            '''

            if repatnotes is not None:
                if not isinstance(repatnotes, str):
                    raise TypeError("expected repatnotes to be a str but it is a %s" % builtins.type(repatnotes))
            self.__repatnotes = repatnotes
            return self

        def set_repatnotic(self, repatnotic):
            '''
            :type repatnotic: datetime.datetime or None
            '''

            if repatnotic is not None:
                if not isinstance(repatnotic, datetime.datetime):
                    raise TypeError("expected repatnotic to be a datetime.datetime but it is a %s" % builtins.type(repatnotic))
            self.__repatnotic = repatnotic
            return self

        def set_repattype(self, repattype):
            '''
            :type repattype: str or None
            '''

            if repattype is not None:
                if not isinstance(repattype, str):
                    raise TypeError("expected repattype to be a str but it is a %s" % builtins.type(repattype))
            self.__repattype = repattype
            return self

        def set_rockclass(self, rockclass):
            '''
            :type rockclass: str or None
            '''

            if rockclass is not None:
                if not isinstance(rockclass, str):
                    raise TypeError("expected rockclass to be a str but it is a %s" % builtins.type(rockclass))
            self.__rockclass = rockclass
            return self

        def set_rockcolor(self, rockcolor):
            '''
            :type rockcolor: str or None
            '''

            if rockcolor is not None:
                if not isinstance(rockcolor, str):
                    raise TypeError("expected rockcolor to be a str but it is a %s" % builtins.type(rockcolor))
            self.__rockcolor = rockcolor
            return self

        def set_rockorigin(self, rockorigin):
            '''
            :type rockorigin: str or None
            '''

            if rockorigin is not None:
                if not isinstance(rockorigin, str):
                    raise TypeError("expected rockorigin to be a str but it is a %s" % builtins.type(rockorigin))
            self.__rockorigin = rockorigin
            return self

        def set_rocktype(self, rocktype):
            '''
            :type rocktype: str or None
            '''

            if rocktype is not None:
                if not isinstance(rocktype, str):
                    raise TypeError("expected rocktype to be a str but it is a %s" % builtins.type(rocktype))
            self.__rocktype = rocktype
            return self

        def set_role(self, role):
            '''
            :type role: str or None
            '''

            if role is not None:
                if not isinstance(role, str):
                    raise TypeError("expected role to be a str but it is a %s" % builtins.type(role))
            self.__role = role
            return self

        def set_role2(self, role2):
            '''
            :type role2: str or None
            '''

            if role2 is not None:
                if not isinstance(role2, str):
                    raise TypeError("expected role2 to be a str but it is a %s" % builtins.type(role2))
            self.__role2 = role2
            return self

        def set_role3(self, role3):
            '''
            :type role3: str or None
            '''

            if role3 is not None:
                if not isinstance(role3, str):
                    raise TypeError("expected role3 to be a str but it is a %s" % builtins.type(role3))
            self.__role3 = role3
            return self

        def set_school(self, school):
            '''
            :type school: str or None
            '''

            if school is not None:
                if not isinstance(school, str):
                    raise TypeError("expected school to be a str but it is a %s" % builtins.type(school))
            self.__school = school
            return self

        def set_sex(self, sex):
            '''
            :type sex: str or None
            '''

            if sex is not None:
                if not isinstance(sex, str):
                    raise TypeError("expected sex to be a str but it is a %s" % builtins.type(sex))
            self.__sex = sex
            return self

        def set_sgflag(self, sgflag):
            '''
            :type sgflag: str or None
            '''

            if sgflag is not None:
                if not isinstance(sgflag, str):
                    raise TypeError("expected sgflag to be a str but it is a %s" % builtins.type(sgflag))
            self.__sgflag = sgflag
            return self

        def set_signedname(self, signedname):
            '''
            :type signedname: str or None
            '''

            if signedname is not None:
                if not isinstance(signedname, str):
                    raise TypeError("expected signedname to be a str but it is a %s" % builtins.type(signedname))
            self.__signedname = signedname
            return self

        def set_signloc(self, signloc):
            '''
            :type signloc: str or None
            '''

            if signloc is not None:
                if not isinstance(signloc, str):
                    raise TypeError("expected signloc to be a str but it is a %s" % builtins.type(signloc))
            self.__signloc = signloc
            return self

        def set_site(self, site):
            '''
            :type site: str or None
            '''

            if site is not None:
                if not isinstance(site, str):
                    raise TypeError("expected site to be a str but it is a %s" % builtins.type(site))
            self.__site = site
            return self

        def set_siteno(self, siteno):
            '''
            :type siteno: str or None
            '''

            if siteno is not None:
                if not isinstance(siteno, str):
                    raise TypeError("expected siteno to be a str but it is a %s" % builtins.type(siteno))
            self.__siteno = siteno
            return self

        def set_specgrav(self, specgrav):
            '''
            :type specgrav: str or None
            '''

            if specgrav is not None:
                if not isinstance(specgrav, str):
                    raise TypeError("expected specgrav to be a str but it is a %s" % builtins.type(specgrav))
            self.__specgrav = specgrav
            return self

        def set_species(self, species):
            '''
            :type species: str or None
            '''

            if species is not None:
                if not isinstance(species, str):
                    raise TypeError("expected species to be a str but it is a %s" % builtins.type(species))
            self.__species = species
            return self

        def set_sprocess(self, sprocess):
            '''
            :type sprocess: str or None
            '''

            if sprocess is not None:
                if not isinstance(sprocess, str):
                    raise TypeError("expected sprocess to be a str but it is a %s" % builtins.type(sprocess))
            self.__sprocess = sprocess
            return self

        def set_stage(self, stage):
            '''
            :type stage: str or None
            '''

            if stage is not None:
                if not isinstance(stage, str):
                    raise TypeError("expected stage to be a str but it is a %s" % builtins.type(stage))
            self.__stage = stage
            return self

        def set_status(self, status):
            '''
            :type status: str or None
            '''

            if status is not None:
                if not isinstance(status, str):
                    raise TypeError("expected status to be a str but it is a %s" % builtins.type(status))
            self.__status = status
            return self

        def set_statusby(self, statusby):
            '''
            :type statusby: str or None
            '''

            if statusby is not None:
                if not isinstance(statusby, str):
                    raise TypeError("expected statusby to be a str but it is a %s" % builtins.type(statusby))
            self.__statusby = statusby
            return self

        def set_statusdate(self, statusdate):
            '''
            :type statusdate: datetime.datetime or None
            '''

            if statusdate is not None:
                if not isinstance(statusdate, datetime.datetime):
                    raise TypeError("expected statusdate to be a datetime.datetime but it is a %s" % builtins.type(statusdate))
            self.__statusdate = statusdate
            return self

        def set_sterms(self, sterms):
            '''
            :type sterms: str or None
            '''

            if sterms is not None:
                if not isinstance(sterms, str):
                    raise TypeError("expected sterms to be a str but it is a %s" % builtins.type(sterms))
            self.__sterms = sterms
            return self

        def set_stratum(self, stratum):
            '''
            :type stratum: str or None
            '''

            if stratum is not None:
                if not isinstance(stratum, str):
                    raise TypeError("expected stratum to be a str but it is a %s" % builtins.type(stratum))
            self.__stratum = stratum
            return self

        def set_streak(self, streak):
            '''
            :type streak: str or None
            '''

            if streak is not None:
                if not isinstance(streak, str):
                    raise TypeError("expected streak to be a str but it is a %s" % builtins.type(streak))
            self.__streak = streak
            return self

        def set_subfamily(self, subfamily):
            '''
            :type subfamily: str or None
            '''

            if subfamily is not None:
                if not isinstance(subfamily, str):
                    raise TypeError("expected subfamily to be a str but it is a %s" % builtins.type(subfamily))
            self.__subfamily = subfamily
            return self

        def set_subjects(self, subjects):
            '''
            :type subjects: str or None
            '''

            if subjects is not None:
                if not isinstance(subjects, str):
                    raise TypeError("expected subjects to be a str but it is a %s" % builtins.type(subjects))
            self.__subjects = subjects
            return self

        def set_subspecies(self, subspecies):
            '''
            :type subspecies: str or None
            '''

            if subspecies is not None:
                if not isinstance(subspecies, str):
                    raise TypeError("expected subspecies to be a str but it is a %s" % builtins.type(subspecies))
            self.__subspecies = subspecies
            return self

        def set_technique(self, technique):
            '''
            :type technique: str or None
            '''

            if technique is not None:
                if not isinstance(technique, str):
                    raise TypeError("expected technique to be a str but it is a %s" % builtins.type(technique))
            self.__technique = technique
            return self

        def set_tempauthor(self, tempauthor):
            '''
            :type tempauthor: str or None
            '''

            if tempauthor is not None:
                if not isinstance(tempauthor, str):
                    raise TypeError("expected tempauthor to be a str but it is a %s" % builtins.type(tempauthor))
            self.__tempauthor = tempauthor
            return self

        def set_tempby(self, tempby):
            '''
            :type tempby: str or None
            '''

            if tempby is not None:
                if not isinstance(tempby, str):
                    raise TypeError("expected tempby to be a str but it is a %s" % builtins.type(tempby))
            self.__tempby = tempby
            return self

        def set_tempdate(self, tempdate):
            '''
            :type tempdate: datetime.datetime or None
            '''

            if tempdate is not None:
                if not isinstance(tempdate, datetime.datetime):
                    raise TypeError("expected tempdate to be a datetime.datetime but it is a %s" % builtins.type(tempdate))
            self.__tempdate = tempdate
            return self

        def set_temperatur(self, temperatur):
            '''
            :type temperatur: str or None
            '''

            if temperatur is not None:
                if not isinstance(temperatur, str):
                    raise TypeError("expected temperatur to be a str but it is a %s" % builtins.type(temperatur))
            self.__temperatur = temperatur
            return self

        def set_temploc(self, temploc):
            '''
            :type temploc: str or None
            '''

            if temploc is not None:
                if not isinstance(temploc, str):
                    raise TypeError("expected temploc to be a str but it is a %s" % builtins.type(temploc))
            self.__temploc = temploc
            return self

        def set_tempnotes(self, tempnotes):
            '''
            :type tempnotes: str or None
            '''

            if tempnotes is not None:
                if not isinstance(tempnotes, str):
                    raise TypeError("expected tempnotes to be a str but it is a %s" % builtins.type(tempnotes))
            self.__tempnotes = tempnotes
            return self

        def set_tempreason(self, tempreason):
            '''
            :type tempreason: str or None
            '''

            if tempreason is not None:
                if not isinstance(tempreason, str):
                    raise TypeError("expected tempreason to be a str but it is a %s" % builtins.type(tempreason))
            self.__tempreason = tempreason
            return self

        def set_tempuntil(self, tempuntil):
            '''
            :type tempuntil: str or None
            '''

            if tempuntil is not None:
                if not isinstance(tempuntil, str):
                    raise TypeError("expected tempuntil to be a str but it is a %s" % builtins.type(tempuntil))
            self.__tempuntil = tempuntil
            return self

        def set_texture(self, texture):
            '''
            :type texture: str or None
            '''

            if texture is not None:
                if not isinstance(texture, str):
                    raise TypeError("expected texture to be a str but it is a %s" % builtins.type(texture))
            self.__texture = texture
            return self

        def set_title(self, title):
            '''
            :type title: str or None
            '''

            if title is not None:
                if not isinstance(title, str):
                    raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
            self.__title = title
            return self

        def set_tlocfield1(self, tlocfield1):
            '''
            :type tlocfield1: str or None
            '''

            if tlocfield1 is not None:
                if not isinstance(tlocfield1, str):
                    raise TypeError("expected tlocfield1 to be a str but it is a %s" % builtins.type(tlocfield1))
            self.__tlocfield1 = tlocfield1
            return self

        def set_tlocfield2(self, tlocfield2):
            '''
            :type tlocfield2: str or None
            '''

            if tlocfield2 is not None:
                if not isinstance(tlocfield2, str):
                    raise TypeError("expected tlocfield2 to be a str but it is a %s" % builtins.type(tlocfield2))
            self.__tlocfield2 = tlocfield2
            return self

        def set_tlocfield3(self, tlocfield3):
            '''
            :type tlocfield3: str or None
            '''

            if tlocfield3 is not None:
                if not isinstance(tlocfield3, str):
                    raise TypeError("expected tlocfield3 to be a str but it is a %s" % builtins.type(tlocfield3))
            self.__tlocfield3 = tlocfield3
            return self

        def set_tlocfield4(self, tlocfield4):
            '''
            :type tlocfield4: str or None
            '''

            if tlocfield4 is not None:
                if not isinstance(tlocfield4, str):
                    raise TypeError("expected tlocfield4 to be a str but it is a %s" % builtins.type(tlocfield4))
            self.__tlocfield4 = tlocfield4
            return self

        def set_tlocfield5(self, tlocfield5):
            '''
            :type tlocfield5: str or None
            '''

            if tlocfield5 is not None:
                if not isinstance(tlocfield5, str):
                    raise TypeError("expected tlocfield5 to be a str but it is a %s" % builtins.type(tlocfield5))
            self.__tlocfield5 = tlocfield5
            return self

        def set_tlocfield6(self, tlocfield6):
            '''
            :type tlocfield6: str or None
            '''

            if tlocfield6 is not None:
                if not isinstance(tlocfield6, str):
                    raise TypeError("expected tlocfield6 to be a str but it is a %s" % builtins.type(tlocfield6))
            self.__tlocfield6 = tlocfield6
            return self

        def set_udf1(self, udf1):
            '''
            :type udf1: str or None
            '''

            if udf1 is not None:
                if not isinstance(udf1, str):
                    raise TypeError("expected udf1 to be a str but it is a %s" % builtins.type(udf1))
            self.__udf1 = udf1
            return self

        def set_udf10(self, udf10):
            '''
            :type udf10: str or None
            '''

            if udf10 is not None:
                if not isinstance(udf10, str):
                    raise TypeError("expected udf10 to be a str but it is a %s" % builtins.type(udf10))
            self.__udf10 = udf10
            return self

        def set_udf11(self, udf11):
            '''
            :type udf11: str or None
            '''

            if udf11 is not None:
                if not isinstance(udf11, str):
                    raise TypeError("expected udf11 to be a str but it is a %s" % builtins.type(udf11))
            self.__udf11 = udf11
            return self

        def set_udf12(self, udf12):
            '''
            :type udf12: str or None
            '''

            if udf12 is not None:
                if not isinstance(udf12, str):
                    raise TypeError("expected udf12 to be a str but it is a %s" % builtins.type(udf12))
            self.__udf12 = udf12
            return self

        def set_udf13(self, udf13):
            '''
            :type udf13: int or None
            '''

            if udf13 is not None:
                if not isinstance(udf13, int):
                    raise TypeError("expected udf13 to be a int but it is a %s" % builtins.type(udf13))
            self.__udf13 = udf13
            return self

        def set_udf14(self, udf14):
            '''
            :type udf14: Decimal or None
            '''

            if udf14 is not None:
                if not isinstance(udf14, decimal.Decimal):
                    raise TypeError("expected udf14 to be a Decimal but it is a %s" % builtins.type(udf14))
            self.__udf14 = udf14
            return self

        def set_udf15(self, udf15):
            '''
            :type udf15: Decimal or None
            '''

            if udf15 is not None:
                if not isinstance(udf15, decimal.Decimal):
                    raise TypeError("expected udf15 to be a Decimal but it is a %s" % builtins.type(udf15))
            self.__udf15 = udf15
            return self

        def set_udf16(self, udf16):
            '''
            :type udf16: Decimal or None
            '''

            if udf16 is not None:
                if not isinstance(udf16, decimal.Decimal):
                    raise TypeError("expected udf16 to be a Decimal but it is a %s" % builtins.type(udf16))
            self.__udf16 = udf16
            return self

        def set_udf17(self, udf17):
            '''
            :type udf17: Decimal or None
            '''

            if udf17 is not None:
                if not isinstance(udf17, decimal.Decimal):
                    raise TypeError("expected udf17 to be a Decimal but it is a %s" % builtins.type(udf17))
            self.__udf17 = udf17
            return self

        def set_udf18(self, udf18):
            '''
            :type udf18: datetime.datetime or None
            '''

            if udf18 is not None:
                if not isinstance(udf18, datetime.datetime):
                    raise TypeError("expected udf18 to be a datetime.datetime but it is a %s" % builtins.type(udf18))
            self.__udf18 = udf18
            return self

        def set_udf19(self, udf19):
            '''
            :type udf19: datetime.datetime or None
            '''

            if udf19 is not None:
                if not isinstance(udf19, datetime.datetime):
                    raise TypeError("expected udf19 to be a datetime.datetime but it is a %s" % builtins.type(udf19))
            self.__udf19 = udf19
            return self

        def set_udf2(self, udf2):
            '''
            :type udf2: str or None
            '''

            if udf2 is not None:
                if not isinstance(udf2, str):
                    raise TypeError("expected udf2 to be a str but it is a %s" % builtins.type(udf2))
            self.__udf2 = udf2
            return self

        def set_udf20(self, udf20):
            '''
            :type udf20: datetime.datetime or None
            '''

            if udf20 is not None:
                if not isinstance(udf20, datetime.datetime):
                    raise TypeError("expected udf20 to be a datetime.datetime but it is a %s" % builtins.type(udf20))
            self.__udf20 = udf20
            return self

        def set_udf21(self, udf21):
            '''
            :type udf21: str or None
            '''

            if udf21 is not None:
                if not isinstance(udf21, str):
                    raise TypeError("expected udf21 to be a str but it is a %s" % builtins.type(udf21))
            self.__udf21 = udf21
            return self

        def set_udf22(self, udf22):
            '''
            :type udf22: str or None
            '''

            if udf22 is not None:
                if not isinstance(udf22, str):
                    raise TypeError("expected udf22 to be a str but it is a %s" % builtins.type(udf22))
            self.__udf22 = udf22
            return self

        def set_udf3(self, udf3):
            '''
            :type udf3: str or None
            '''

            if udf3 is not None:
                if not isinstance(udf3, str):
                    raise TypeError("expected udf3 to be a str but it is a %s" % builtins.type(udf3))
            self.__udf3 = udf3
            return self

        def set_udf4(self, udf4):
            '''
            :type udf4: str or None
            '''

            if udf4 is not None:
                if not isinstance(udf4, str):
                    raise TypeError("expected udf4 to be a str but it is a %s" % builtins.type(udf4))
            self.__udf4 = udf4
            return self

        def set_udf5(self, udf5):
            '''
            :type udf5: str or None
            '''

            if udf5 is not None:
                if not isinstance(udf5, str):
                    raise TypeError("expected udf5 to be a str but it is a %s" % builtins.type(udf5))
            self.__udf5 = udf5
            return self

        def set_udf6(self, udf6):
            '''
            :type udf6: str or None
            '''

            if udf6 is not None:
                if not isinstance(udf6, str):
                    raise TypeError("expected udf6 to be a str but it is a %s" % builtins.type(udf6))
            self.__udf6 = udf6
            return self

        def set_udf7(self, udf7):
            '''
            :type udf7: str or None
            '''

            if udf7 is not None:
                if not isinstance(udf7, str):
                    raise TypeError("expected udf7 to be a str but it is a %s" % builtins.type(udf7))
            self.__udf7 = udf7
            return self

        def set_udf8(self, udf8):
            '''
            :type udf8: str or None
            '''

            if udf8 is not None:
                if not isinstance(udf8, str):
                    raise TypeError("expected udf8 to be a str but it is a %s" % builtins.type(udf8))
            self.__udf8 = udf8
            return self

        def set_udf9(self, udf9):
            '''
            :type udf9: str or None
            '''

            if udf9 is not None:
                if not isinstance(udf9, str):
                    raise TypeError("expected udf9 to be a str but it is a %s" % builtins.type(udf9))
            self.__udf9 = udf9
            return self

        def set_unit(self, unit):
            '''
            :type unit: str or None
            '''

            if unit is not None:
                if not isinstance(unit, str):
                    raise TypeError("expected unit to be a str but it is a %s" % builtins.type(unit))
            self.__unit = unit
            return self

        def set_updated(self, updated):
            '''
            :type updated: datetime.datetime or None
            '''

            if updated is not None:
                if not isinstance(updated, datetime.datetime):
                    raise TypeError("expected updated to be a datetime.datetime but it is a %s" % builtins.type(updated))
            self.__updated = updated
            return self

        def set_updatedby(self, updatedby):
            '''
            :type updatedby: str or None
            '''

            if updatedby is not None:
                if not isinstance(updatedby, str):
                    raise TypeError("expected updatedby to be a str but it is a %s" % builtins.type(updatedby))
            self.__updatedby = updatedby
            return self

        def set_used(self, used):
            '''
            :type used: str or None
            '''

            if used is not None:
                if not isinstance(used, str):
                    raise TypeError("expected used to be a str but it is a %s" % builtins.type(used))
            self.__used = used
            return self

        def set_valuedate(self, valuedate):
            '''
            :type valuedate: datetime.datetime or None
            '''

            if valuedate is not None:
                if not isinstance(valuedate, datetime.datetime):
                    raise TypeError("expected valuedate to be a datetime.datetime but it is a %s" % builtins.type(valuedate))
            self.__valuedate = valuedate
            return self

        def set_varieties(self, varieties):
            '''
            :type varieties: str or None
            '''

            if varieties is not None:
                if not isinstance(varieties, str):
                    raise TypeError("expected varieties to be a str but it is a %s" % builtins.type(varieties))
            self.__varieties = varieties
            return self

        def set_vexhtml(self, vexhtml):
            '''
            :type vexhtml: str or None
            '''

            if vexhtml is not None:
                if not isinstance(vexhtml, str):
                    raise TypeError("expected vexhtml to be a str but it is a %s" % builtins.type(vexhtml))
            self.__vexhtml = vexhtml
            return self

        def set_vexlabel1(self, vexlabel1):
            '''
            :type vexlabel1: str or None
            '''

            if vexlabel1 is not None:
                if not isinstance(vexlabel1, str):
                    raise TypeError("expected vexlabel1 to be a str but it is a %s" % builtins.type(vexlabel1))
            self.__vexlabel1 = vexlabel1
            return self

        def set_vexlabel2(self, vexlabel2):
            '''
            :type vexlabel2: str or None
            '''

            if vexlabel2 is not None:
                if not isinstance(vexlabel2, str):
                    raise TypeError("expected vexlabel2 to be a str but it is a %s" % builtins.type(vexlabel2))
            self.__vexlabel2 = vexlabel2
            return self

        def set_vexlabel3(self, vexlabel3):
            '''
            :type vexlabel3: str or None
            '''

            if vexlabel3 is not None:
                if not isinstance(vexlabel3, str):
                    raise TypeError("expected vexlabel3 to be a str but it is a %s" % builtins.type(vexlabel3))
            self.__vexlabel3 = vexlabel3
            return self

        def set_vexlabel4(self, vexlabel4):
            '''
            :type vexlabel4: str or None
            '''

            if vexlabel4 is not None:
                if not isinstance(vexlabel4, str):
                    raise TypeError("expected vexlabel4 to be a str but it is a %s" % builtins.type(vexlabel4))
            self.__vexlabel4 = vexlabel4
            return self

        def set_webinclude(self, webinclude):
            '''
            :type webinclude: bool or None
            '''

            if webinclude is not None:
                if not isinstance(webinclude, bool):
                    raise TypeError("expected webinclude to be a bool but it is a %s" % builtins.type(webinclude))
            self.__webinclude = webinclude
            return self

        def set_weight(self, weight):
            '''
            :type weight: Decimal or None
            '''

            if weight is not None:
                if not isinstance(weight, decimal.Decimal):
                    raise TypeError("expected weight to be a Decimal but it is a %s" % builtins.type(weight))
            self.__weight = weight
            return self

        def set_weightin(self, weightin):
            '''
            :type weightin: Decimal or None
            '''

            if weightin is not None:
                if not isinstance(weightin, decimal.Decimal):
                    raise TypeError("expected weightin to be a Decimal but it is a %s" % builtins.type(weightin))
            self.__weightin = weightin
            return self

        def set_weightlb(self, weightlb):
            '''
            :type weightlb: Decimal or None
            '''

            if weightlb is not None:
                if not isinstance(weightlb, decimal.Decimal):
                    raise TypeError("expected weightlb to be a Decimal but it is a %s" % builtins.type(weightlb))
            self.__weightlb = weightlb
            return self

        def set_width(self, width):
            '''
            :type width: Decimal or None
            '''

            if width is not None:
                if not isinstance(width, decimal.Decimal):
                    raise TypeError("expected width to be a Decimal but it is a %s" % builtins.type(width))
            self.__width = width
            return self

        def set_widthft(self, widthft):
            '''
            :type widthft: Decimal or None
            '''

            if widthft is not None:
                if not isinstance(widthft, decimal.Decimal):
                    raise TypeError("expected widthft to be a Decimal but it is a %s" % builtins.type(widthft))
            self.__widthft = widthft
            return self

        def set_widthin(self, widthin):
            '''
            :type widthin: Decimal or None
            '''

            if widthin is not None:
                if not isinstance(widthin, decimal.Decimal):
                    raise TypeError("expected widthin to be a Decimal but it is a %s" % builtins.type(widthin))
            self.__widthin = widthin
            return self

        def set_xcord(self, xcord):
            '''
            :type xcord: Decimal or None
            '''

            if xcord is not None:
                if not isinstance(xcord, decimal.Decimal):
                    raise TypeError("expected xcord to be a Decimal but it is a %s" % builtins.type(xcord))
            self.__xcord = xcord
            return self

        def set_ycord(self, ycord):
            '''
            :type ycord: Decimal or None
            '''

            if ycord is not None:
                if not isinstance(ycord, decimal.Decimal):
                    raise TypeError("expected ycord to be a Decimal but it is a %s" % builtins.type(ycord))
            self.__ycord = ycord
            return self

        def set_zcord(self, zcord):
            '''
            :type zcord: Decimal or None
            '''

            if zcord is not None:
                if not isinstance(zcord, decimal.Decimal):
                    raise TypeError("expected zcord to be a Decimal but it is a %s" % builtins.type(zcord))
            self.__zcord = zcord
            return self

        def set_zsorter(self, zsorter):
            '''
            :type zsorter: str or None
            '''

            if zsorter is not None:
                if not isinstance(zsorter, str):
                    raise TypeError("expected zsorter to be a str but it is a %s" % builtins.type(zsorter))
            self.__zsorter = zsorter
            return self

        def set_zsorterx(self, zsorterx):
            '''
            :type zsorterx: str or None
            '''

            if zsorterx is not None:
                if not isinstance(zsorterx, str):
                    raise TypeError("expected zsorterx to be a str but it is a %s" % builtins.type(zsorterx))
            self.__zsorterx = zsorterx
            return self

        @property
        def sex(self):
            '''
            :rtype: str
            '''

            return self.__sex

        @property
        def sgflag(self):
            '''
            :rtype: str
            '''

            return self.__sgflag

        @property
        def signedname(self):
            '''
            :rtype: str
            '''

            return self.__signedname

        @property
        def signloc(self):
            '''
            :rtype: str
            '''

            return self.__signloc

        @property
        def site(self):
            '''
            :rtype: str
            '''

            return self.__site

        @property
        def siteno(self):
            '''
            :rtype: str
            '''

            return self.__siteno

        @property
        def specgrav(self):
            '''
            :rtype: str
            '''

            return self.__specgrav

        @property
        def species(self):
            '''
            :rtype: str
            '''

            return self.__species

        @property
        def sprocess(self):
            '''
            :rtype: str
            '''

            return self.__sprocess

        @property
        def stage(self):
            '''
            :rtype: str
            '''

            return self.__stage

        @property
        def status(self):
            '''
            :rtype: str
            '''

            return self.__status

        @property
        def statusby(self):
            '''
            :rtype: str
            '''

            return self.__statusby

        @property
        def statusdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__statusdate

        @property
        def sterms(self):
            '''
            :rtype: str
            '''

            return self.__sterms

        @property
        def stratum(self):
            '''
            :rtype: str
            '''

            return self.__stratum

        @property
        def streak(self):
            '''
            :rtype: str
            '''

            return self.__streak

        @property
        def subfamily(self):
            '''
            :rtype: str
            '''

            return self.__subfamily

        @property
        def subjects(self):
            '''
            :rtype: str
            '''

            return self.__subjects

        @property
        def subspecies(self):
            '''
            :rtype: str
            '''

            return self.__subspecies

        @property
        def technique(self):
            '''
            :rtype: str
            '''

            return self.__technique

        @property
        def tempauthor(self):
            '''
            :rtype: str
            '''

            return self.__tempauthor

        @property
        def tempby(self):
            '''
            :rtype: str
            '''

            return self.__tempby

        @property
        def tempdate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__tempdate

        @property
        def temperatur(self):
            '''
            :rtype: str
            '''

            return self.__temperatur

        @property
        def temploc(self):
            '''
            :rtype: str
            '''

            return self.__temploc

        @property
        def tempnotes(self):
            '''
            :rtype: str
            '''

            return self.__tempnotes

        @property
        def tempreason(self):
            '''
            :rtype: str
            '''

            return self.__tempreason

        @property
        def tempuntil(self):
            '''
            :rtype: str
            '''

            return self.__tempuntil

        @property
        def texture(self):
            '''
            :rtype: str
            '''

            return self.__texture

        @property
        def title(self):
            '''
            :rtype: str
            '''

            return self.__title

        @property
        def tlocfield1(self):
            '''
            :rtype: str
            '''

            return self.__tlocfield1

        @property
        def tlocfield2(self):
            '''
            :rtype: str
            '''

            return self.__tlocfield2

        @property
        def tlocfield3(self):
            '''
            :rtype: str
            '''

            return self.__tlocfield3

        @property
        def tlocfield4(self):
            '''
            :rtype: str
            '''

            return self.__tlocfield4

        @property
        def tlocfield5(self):
            '''
            :rtype: str
            '''

            return self.__tlocfield5

        @property
        def tlocfield6(self):
            '''
            :rtype: str
            '''

            return self.__tlocfield6

        @property
        def udf1(self):
            '''
            :rtype: str
            '''

            return self.__udf1

        @property
        def udf10(self):
            '''
            :rtype: str
            '''

            return self.__udf10

        @property
        def udf11(self):
            '''
            :rtype: str
            '''

            return self.__udf11

        @property
        def udf12(self):
            '''
            :rtype: str
            '''

            return self.__udf12

        @property
        def udf13(self):
            '''
            :rtype: int
            '''

            return self.__udf13

        @property
        def udf14(self):
            '''
            :rtype: Decimal
            '''

            return self.__udf14

        @property
        def udf15(self):
            '''
            :rtype: Decimal
            '''

            return self.__udf15

        @property
        def udf16(self):
            '''
            :rtype: Decimal
            '''

            return self.__udf16

        @property
        def udf17(self):
            '''
            :rtype: Decimal
            '''

            return self.__udf17

        @property
        def udf18(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__udf18

        @property
        def udf19(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__udf19

        @property
        def udf2(self):
            '''
            :rtype: str
            '''

            return self.__udf2

        @property
        def udf20(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__udf20

        @property
        def udf21(self):
            '''
            :rtype: str
            '''

            return self.__udf21

        @property
        def udf22(self):
            '''
            :rtype: str
            '''

            return self.__udf22

        @property
        def udf3(self):
            '''
            :rtype: str
            '''

            return self.__udf3

        @property
        def udf4(self):
            '''
            :rtype: str
            '''

            return self.__udf4

        @property
        def udf5(self):
            '''
            :rtype: str
            '''

            return self.__udf5

        @property
        def udf6(self):
            '''
            :rtype: str
            '''

            return self.__udf6

        @property
        def udf7(self):
            '''
            :rtype: str
            '''

            return self.__udf7

        @property
        def udf8(self):
            '''
            :rtype: str
            '''

            return self.__udf8

        @property
        def udf9(self):
            '''
            :rtype: str
            '''

            return self.__udf9

        @property
        def unit(self):
            '''
            :rtype: str
            '''

            return self.__unit

        def update(self, object_record):
            '''
            :type accessno: str or None
            :type accessory: str or None
            :type acqvalue: Decimal or None
            :type age: str or None
            :type appnotes: str or None
            :type appraisor: str or None
            :type assemzone: str or None
            :type bagno: str or None
            :type boxno: str or None
            :type caption: str or None
            :type cat: str or None
            :type catby: str or None
            :type catdate: datetime.datetime or None
            :type cattype: str or None
            :type chemcomp: str or None
            :type circum: Decimal or None
            :type circumft: Decimal or None
            :type circumin: Decimal or None
            :type classes: str or None
            :type colldate: datetime.datetime or None
            :type collection: str or None
            :type collector: str or None
            :type conddate: datetime.datetime or None
            :type condexam: str or None
            :type condition: str or None
            :type condnotes: str or None
            :type count: str or None
            :type creator: str or None
            :type creator2: str or None
            :type creator3: str or None
            :type credit: str or None
            :type crystal: str or None
            :type culture: str or None
            :type curvalmax: Decimal or None
            :type curvalue: Decimal or None
            :type dataset: str or None
            :type date: str or None
            :type datingmeth: str or None
            :type datum: str or None
            :type depth: Decimal or None
            :type depthft: Decimal or None
            :type depthin: Decimal or None
            :type descrip: str or None
            :type diameter: Decimal or None
            :type diameterft: Decimal or None
            :type diameterin: Decimal or None
            :type dimnotes: str or None
            :type dimtype: int or None
            :type dispvalue: str or None
            :type earlydate: int or None
            :type elements: str or None
            :type epoch: str or None
            :type era: str or None
            :type event: str or None
            :type ew: str or None
            :type excavadate: datetime.datetime or None
            :type excavateby: str or None
            :type exhibitid: str or None
            :type exhibitno: int or None
            :type exhlabel1: str or None
            :type exhlabel2: str or None
            :type exhlabel3: str or None
            :type exhlabel4: str or None
            :type exhstart: datetime.datetime or None
            :type family: str or None
            :type feature: str or None
            :type flagdate: datetime.datetime or None
            :type flagnotes: str or None
            :type flagreason: str or None
            :type formation: str or None
            :type fossils: str or None
            :type found: str or None
            :type fracture: str or None
            :type frame: str or None
            :type framesize: str or None
            :type genus: str or None
            :type gparent: str or None
            :type grainsize: str or None
            :type habitat: str or None
            :type hardness: str or None
            :type height: Decimal or None
            :type heightft: Decimal or None
            :type heightin: Decimal or None
            :type homeloc: str or None
            :type idby: str or None
            :type iddate: datetime.datetime or None
            :type imagefile: str or None
            :type imageno: int or None
            :type imagesize: str or None
            :type inscomp: str or None
            :type inscrlang: str or None
            :type inscrpos: str or None
            :type inscrtech: str or None
            :type inscrtext: str or None
            :type inscrtrans: str or None
            :type inscrtype: str or None
            :type insdate: datetime.datetime or None
            :type insphone: str or None
            :type inspremium: str or None
            :type insrep: str or None
            :type insvalue: Decimal or None
            :type invnby: str or None
            :type invndate: datetime.datetime or None
            :type kingdom: str or None
            :type latdeg: Decimal or None
            :type latedate: int or None
            :type legal: str or None
            :type length: Decimal or None
            :type lengthft: Decimal or None
            :type lengthin: Decimal or None
            :type level: str or None
            :type lithofacie: str or None
            :type loancond: str or None
            :type loandue: datetime.datetime or None
            :type loanid: str or None
            :type loaninno: str or None
            :type loanno: int or None
            :type loanrenew: datetime.datetime or None
            :type locfield1: str or None
            :type locfield2: str or None
            :type locfield3: str or None
            :type locfield4: str or None
            :type locfield5: str or None
            :type locfield6: str or None
            :type longdeg: Decimal or None
            :type luster: str or None
            :type made: str or None
            :type maintcycle: str or None
            :type maintdate: datetime.datetime or None
            :type maintnote: str or None
            :type material: str or None
            :type medium: str or None
            :type member: str or None
            :type mmark: str or None
            :type nhclass: str or None
            :type nhorder: str or None
            :type notes: str or None
            :type ns: str or None
            :type objectid: str or None
            :type objname: str or None
            :type objname2: str or None
            :type objname3: str or None
            :type objnames: str or None
            :type occurrence: str or None
            :type oldno: str or None
            :type origin: str or None
            :type othername: str or None
            :type otherno: str or None
            :type outdate: datetime.datetime or None
            :type owned: str or None
            :type parent: str or None
            :type people: str or None
            :type period: str or None
            :type phylum: str or None
            :type policyno: str or None
            :type ppid: str or None
            :type preparator: str or None
            :type prepdate: datetime.datetime or None
            :type preserve: str or None
            :type pressure: str or None
            :type provenance: str or None
            :type pubnotes: str or None
            :type qrurl: str or None
            :type recas: str or None
            :type recdate: str or None
            :type recfrom: str or None
            :type relation: str or None
            :type relnotes: str or None
            :type renewuntil: datetime.datetime or None
            :type repatby: str or None
            :type repatclaim: str or None
            :type repatdate: datetime.datetime or None
            :type repatdisp: str or None
            :type repathand: str or None
            :type repatnotes: str or None
            :type repatnotic: datetime.datetime or None
            :type repattype: str or None
            :type rockclass: str or None
            :type rockcolor: str or None
            :type rockorigin: str or None
            :type rocktype: str or None
            :type role: str or None
            :type role2: str or None
            :type role3: str or None
            :type school: str or None
            :type sex: str or None
            :type sgflag: str or None
            :type signedname: str or None
            :type signloc: str or None
            :type site: str or None
            :type siteno: str or None
            :type specgrav: str or None
            :type species: str or None
            :type sprocess: str or None
            :type stage: str or None
            :type status: str or None
            :type statusby: str or None
            :type statusdate: datetime.datetime or None
            :type sterms: str or None
            :type stratum: str or None
            :type streak: str or None
            :type subfamily: str or None
            :type subjects: str or None
            :type subspecies: str or None
            :type technique: str or None
            :type tempauthor: str or None
            :type tempby: str or None
            :type tempdate: datetime.datetime or None
            :type temperatur: str or None
            :type temploc: str or None
            :type tempnotes: str or None
            :type tempreason: str or None
            :type tempuntil: str or None
            :type texture: str or None
            :type title: str or None
            :type tlocfield1: str or None
            :type tlocfield2: str or None
            :type tlocfield3: str or None
            :type tlocfield4: str or None
            :type tlocfield5: str or None
            :type tlocfield6: str or None
            :type udf1: str or None
            :type udf10: str or None
            :type udf11: str or None
            :type udf12: str or None
            :type udf13: int or None
            :type udf14: Decimal or None
            :type udf15: Decimal or None
            :type udf16: Decimal or None
            :type udf17: Decimal or None
            :type udf18: datetime.datetime or None
            :type udf19: datetime.datetime or None
            :type udf2: str or None
            :type udf20: datetime.datetime or None
            :type udf21: str or None
            :type udf22: str or None
            :type udf3: str or None
            :type udf4: str or None
            :type udf5: str or None
            :type udf6: str or None
            :type udf7: str or None
            :type udf8: str or None
            :type udf9: str or None
            :type unit: str or None
            :type updated: datetime.datetime or None
            :type updatedby: str or None
            :type used: str or None
            :type valuedate: datetime.datetime or None
            :type varieties: str or None
            :type vexhtml: str or None
            :type vexlabel1: str or None
            :type vexlabel2: str or None
            :type vexlabel3: str or None
            :type vexlabel4: str or None
            :type webinclude: bool or None
            :type weight: Decimal or None
            :type weightin: Decimal or None
            :type weightlb: Decimal or None
            :type width: Decimal or None
            :type widthft: Decimal or None
            :type widthin: Decimal or None
            :type xcord: Decimal or None
            :type ycord: Decimal or None
            :type zcord: Decimal or None
            :type zsorter: str or None
            :type zsorterx: str or None
            '''

            if isinstance(object_record, ObjectRecord):
                self.set_accessno(object_record.accessno)
                self.set_accessory(object_record.accessory)
                self.set_acqvalue(object_record.acqvalue)
                self.set_age(object_record.age)
                self.set_appnotes(object_record.appnotes)
                self.set_appraisor(object_record.appraisor)
                self.set_assemzone(object_record.assemzone)
                self.set_bagno(object_record.bagno)
                self.set_boxno(object_record.boxno)
                self.set_caption(object_record.caption)
                self.set_cat(object_record.cat)
                self.set_catby(object_record.catby)
                self.set_catdate(object_record.catdate)
                self.set_cattype(object_record.cattype)
                self.set_chemcomp(object_record.chemcomp)
                self.set_circum(object_record.circum)
                self.set_circumft(object_record.circumft)
                self.set_circumin(object_record.circumin)
                self.set_classes(object_record.classes)
                self.set_colldate(object_record.colldate)
                self.set_collection(object_record.collection)
                self.set_collector(object_record.collector)
                self.set_conddate(object_record.conddate)
                self.set_condexam(object_record.condexam)
                self.set_condition(object_record.condition)
                self.set_condnotes(object_record.condnotes)
                self.set_count(object_record.count)
                self.set_creator(object_record.creator)
                self.set_creator2(object_record.creator2)
                self.set_creator3(object_record.creator3)
                self.set_credit(object_record.credit)
                self.set_crystal(object_record.crystal)
                self.set_culture(object_record.culture)
                self.set_curvalmax(object_record.curvalmax)
                self.set_curvalue(object_record.curvalue)
                self.set_dataset(object_record.dataset)
                self.set_date(object_record.date)
                self.set_datingmeth(object_record.datingmeth)
                self.set_datum(object_record.datum)
                self.set_depth(object_record.depth)
                self.set_depthft(object_record.depthft)
                self.set_depthin(object_record.depthin)
                self.set_descrip(object_record.descrip)
                self.set_diameter(object_record.diameter)
                self.set_diameterft(object_record.diameterft)
                self.set_diameterin(object_record.diameterin)
                self.set_dimnotes(object_record.dimnotes)
                self.set_dimtype(object_record.dimtype)
                self.set_dispvalue(object_record.dispvalue)
                self.set_earlydate(object_record.earlydate)
                self.set_elements(object_record.elements)
                self.set_epoch(object_record.epoch)
                self.set_era(object_record.era)
                self.set_event(object_record.event)
                self.set_ew(object_record.ew)
                self.set_excavadate(object_record.excavadate)
                self.set_excavateby(object_record.excavateby)
                self.set_exhibitid(object_record.exhibitid)
                self.set_exhibitno(object_record.exhibitno)
                self.set_exhlabel1(object_record.exhlabel1)
                self.set_exhlabel2(object_record.exhlabel2)
                self.set_exhlabel3(object_record.exhlabel3)
                self.set_exhlabel4(object_record.exhlabel4)
                self.set_exhstart(object_record.exhstart)
                self.set_family(object_record.family)
                self.set_feature(object_record.feature)
                self.set_flagdate(object_record.flagdate)
                self.set_flagnotes(object_record.flagnotes)
                self.set_flagreason(object_record.flagreason)
                self.set_formation(object_record.formation)
                self.set_fossils(object_record.fossils)
                self.set_found(object_record.found)
                self.set_fracture(object_record.fracture)
                self.set_frame(object_record.frame)
                self.set_framesize(object_record.framesize)
                self.set_genus(object_record.genus)
                self.set_gparent(object_record.gparent)
                self.set_grainsize(object_record.grainsize)
                self.set_habitat(object_record.habitat)
                self.set_hardness(object_record.hardness)
                self.set_height(object_record.height)
                self.set_heightft(object_record.heightft)
                self.set_heightin(object_record.heightin)
                self.set_homeloc(object_record.homeloc)
                self.set_idby(object_record.idby)
                self.set_iddate(object_record.iddate)
                self.set_imagefile(object_record.imagefile)
                self.set_imageno(object_record.imageno)
                self.set_imagesize(object_record.imagesize)
                self.set_inscomp(object_record.inscomp)
                self.set_inscrlang(object_record.inscrlang)
                self.set_inscrpos(object_record.inscrpos)
                self.set_inscrtech(object_record.inscrtech)
                self.set_inscrtext(object_record.inscrtext)
                self.set_inscrtrans(object_record.inscrtrans)
                self.set_inscrtype(object_record.inscrtype)
                self.set_insdate(object_record.insdate)
                self.set_insphone(object_record.insphone)
                self.set_inspremium(object_record.inspremium)
                self.set_insrep(object_record.insrep)
                self.set_insvalue(object_record.insvalue)
                self.set_invnby(object_record.invnby)
                self.set_invndate(object_record.invndate)
                self.set_kingdom(object_record.kingdom)
                self.set_latdeg(object_record.latdeg)
                self.set_latedate(object_record.latedate)
                self.set_legal(object_record.legal)
                self.set_length(object_record.length)
                self.set_lengthft(object_record.lengthft)
                self.set_lengthin(object_record.lengthin)
                self.set_level(object_record.level)
                self.set_lithofacie(object_record.lithofacie)
                self.set_loancond(object_record.loancond)
                self.set_loandue(object_record.loandue)
                self.set_loanid(object_record.loanid)
                self.set_loaninno(object_record.loaninno)
                self.set_loanno(object_record.loanno)
                self.set_loanrenew(object_record.loanrenew)
                self.set_locfield1(object_record.locfield1)
                self.set_locfield2(object_record.locfield2)
                self.set_locfield3(object_record.locfield3)
                self.set_locfield4(object_record.locfield4)
                self.set_locfield5(object_record.locfield5)
                self.set_locfield6(object_record.locfield6)
                self.set_longdeg(object_record.longdeg)
                self.set_luster(object_record.luster)
                self.set_made(object_record.made)
                self.set_maintcycle(object_record.maintcycle)
                self.set_maintdate(object_record.maintdate)
                self.set_maintnote(object_record.maintnote)
                self.set_material(object_record.material)
                self.set_medium(object_record.medium)
                self.set_member(object_record.member)
                self.set_mmark(object_record.mmark)
                self.set_nhclass(object_record.nhclass)
                self.set_nhorder(object_record.nhorder)
                self.set_notes(object_record.notes)
                self.set_ns(object_record.ns)
                self.set_objectid(object_record.objectid)
                self.set_objname(object_record.objname)
                self.set_objname2(object_record.objname2)
                self.set_objname3(object_record.objname3)
                self.set_objnames(object_record.objnames)
                self.set_occurrence(object_record.occurrence)
                self.set_oldno(object_record.oldno)
                self.set_origin(object_record.origin)
                self.set_othername(object_record.othername)
                self.set_otherno(object_record.otherno)
                self.set_outdate(object_record.outdate)
                self.set_owned(object_record.owned)
                self.set_parent(object_record.parent)
                self.set_people(object_record.people)
                self.set_period(object_record.period)
                self.set_phylum(object_record.phylum)
                self.set_policyno(object_record.policyno)
                self.set_ppid(object_record.ppid)
                self.set_preparator(object_record.preparator)
                self.set_prepdate(object_record.prepdate)
                self.set_preserve(object_record.preserve)
                self.set_pressure(object_record.pressure)
                self.set_provenance(object_record.provenance)
                self.set_pubnotes(object_record.pubnotes)
                self.set_qrurl(object_record.qrurl)
                self.set_recas(object_record.recas)
                self.set_recdate(object_record.recdate)
                self.set_recfrom(object_record.recfrom)
                self.set_relation(object_record.relation)
                self.set_relnotes(object_record.relnotes)
                self.set_renewuntil(object_record.renewuntil)
                self.set_repatby(object_record.repatby)
                self.set_repatclaim(object_record.repatclaim)
                self.set_repatdate(object_record.repatdate)
                self.set_repatdisp(object_record.repatdisp)
                self.set_repathand(object_record.repathand)
                self.set_repatnotes(object_record.repatnotes)
                self.set_repatnotic(object_record.repatnotic)
                self.set_repattype(object_record.repattype)
                self.set_rockclass(object_record.rockclass)
                self.set_rockcolor(object_record.rockcolor)
                self.set_rockorigin(object_record.rockorigin)
                self.set_rocktype(object_record.rocktype)
                self.set_role(object_record.role)
                self.set_role2(object_record.role2)
                self.set_role3(object_record.role3)
                self.set_school(object_record.school)
                self.set_sex(object_record.sex)
                self.set_sgflag(object_record.sgflag)
                self.set_signedname(object_record.signedname)
                self.set_signloc(object_record.signloc)
                self.set_site(object_record.site)
                self.set_siteno(object_record.siteno)
                self.set_specgrav(object_record.specgrav)
                self.set_species(object_record.species)
                self.set_sprocess(object_record.sprocess)
                self.set_stage(object_record.stage)
                self.set_status(object_record.status)
                self.set_statusby(object_record.statusby)
                self.set_statusdate(object_record.statusdate)
                self.set_sterms(object_record.sterms)
                self.set_stratum(object_record.stratum)
                self.set_streak(object_record.streak)
                self.set_subfamily(object_record.subfamily)
                self.set_subjects(object_record.subjects)
                self.set_subspecies(object_record.subspecies)
                self.set_technique(object_record.technique)
                self.set_tempauthor(object_record.tempauthor)
                self.set_tempby(object_record.tempby)
                self.set_tempdate(object_record.tempdate)
                self.set_temperatur(object_record.temperatur)
                self.set_temploc(object_record.temploc)
                self.set_tempnotes(object_record.tempnotes)
                self.set_tempreason(object_record.tempreason)
                self.set_tempuntil(object_record.tempuntil)
                self.set_texture(object_record.texture)
                self.set_title(object_record.title)
                self.set_tlocfield1(object_record.tlocfield1)
                self.set_tlocfield2(object_record.tlocfield2)
                self.set_tlocfield3(object_record.tlocfield3)
                self.set_tlocfield4(object_record.tlocfield4)
                self.set_tlocfield5(object_record.tlocfield5)
                self.set_tlocfield6(object_record.tlocfield6)
                self.set_udf1(object_record.udf1)
                self.set_udf10(object_record.udf10)
                self.set_udf11(object_record.udf11)
                self.set_udf12(object_record.udf12)
                self.set_udf13(object_record.udf13)
                self.set_udf14(object_record.udf14)
                self.set_udf15(object_record.udf15)
                self.set_udf16(object_record.udf16)
                self.set_udf17(object_record.udf17)
                self.set_udf18(object_record.udf18)
                self.set_udf19(object_record.udf19)
                self.set_udf2(object_record.udf2)
                self.set_udf20(object_record.udf20)
                self.set_udf21(object_record.udf21)
                self.set_udf22(object_record.udf22)
                self.set_udf3(object_record.udf3)
                self.set_udf4(object_record.udf4)
                self.set_udf5(object_record.udf5)
                self.set_udf6(object_record.udf6)
                self.set_udf7(object_record.udf7)
                self.set_udf8(object_record.udf8)
                self.set_udf9(object_record.udf9)
                self.set_unit(object_record.unit)
                self.set_updated(object_record.updated)
                self.set_updatedby(object_record.updatedby)
                self.set_used(object_record.used)
                self.set_valuedate(object_record.valuedate)
                self.set_varieties(object_record.varieties)
                self.set_vexhtml(object_record.vexhtml)
                self.set_vexlabel1(object_record.vexlabel1)
                self.set_vexlabel2(object_record.vexlabel2)
                self.set_vexlabel3(object_record.vexlabel3)
                self.set_vexlabel4(object_record.vexlabel4)
                self.set_webinclude(object_record.webinclude)
                self.set_weight(object_record.weight)
                self.set_weightin(object_record.weightin)
                self.set_weightlb(object_record.weightlb)
                self.set_width(object_record.width)
                self.set_widthft(object_record.widthft)
                self.set_widthin(object_record.widthin)
                self.set_xcord(object_record.xcord)
                self.set_ycord(object_record.ycord)
                self.set_zcord(object_record.zcord)
                self.set_zsorter(object_record.zsorter)
                self.set_zsorterx(object_record.zsorterx)
            elif isinstance(object_record, dict):
                for key, value in object_record.items():
                    getattr(self, 'set_' + key)(value)
            else:
                raise TypeError(object_record)
            return self

        @property
        def updated(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__updated

        @property
        def updatedby(self):
            '''
            :rtype: str
            '''

            return self.__updatedby

        @property
        def used(self):
            '''
            :rtype: str
            '''

            return self.__used

        @property
        def valuedate(self):
            '''
            :rtype: datetime.datetime
            '''

            return self.__valuedate

        @property
        def varieties(self):
            '''
            :rtype: str
            '''

            return self.__varieties

        @property
        def vexhtml(self):
            '''
            :rtype: str
            '''

            return self.__vexhtml

        @property
        def vexlabel1(self):
            '''
            :rtype: str
            '''

            return self.__vexlabel1

        @property
        def vexlabel2(self):
            '''
            :rtype: str
            '''

            return self.__vexlabel2

        @property
        def vexlabel3(self):
            '''
            :rtype: str
            '''

            return self.__vexlabel3

        @property
        def vexlabel4(self):
            '''
            :rtype: str
            '''

            return self.__vexlabel4

        @property
        def webinclude(self):
            '''
            :rtype: bool
            '''

            return self.__webinclude

        @property
        def weight(self):
            '''
            :rtype: Decimal
            '''

            return self.__weight

        @property
        def weightin(self):
            '''
            :rtype: Decimal
            '''

            return self.__weightin

        @property
        def weightlb(self):
            '''
            :rtype: Decimal
            '''

            return self.__weightlb

        @property
        def width(self):
            '''
            :rtype: Decimal
            '''

            return self.__width

        @property
        def widthft(self):
            '''
            :rtype: Decimal
            '''

            return self.__widthft

        @property
        def widthin(self):
            '''
            :rtype: Decimal
            '''

            return self.__widthin

        @property
        def xcord(self):
            '''
            :rtype: Decimal
            '''

            return self.__xcord

        @property
        def ycord(self):
            '''
            :rtype: Decimal
            '''

            return self.__ycord

        @property
        def zcord(self):
            '''
            :rtype: Decimal
            '''

            return self.__zcord

        @property
        def zsorter(self):
            '''
            :rtype: str
            '''

            return self.__zsorter

        @property
        def zsorterx(self):
            '''
            :rtype: str
            '''

            return self.__zsorterx

        @accessno.setter
        def accessno(self, accessno):
            '''
            :type accessno: str or None
            '''

            self.set_accessno(accessno)

        @accessory.setter
        def accessory(self, accessory):
            '''
            :type accessory: str or None
            '''

            self.set_accessory(accessory)

        @acqvalue.setter
        def acqvalue(self, acqvalue):
            '''
            :type acqvalue: Decimal or None
            '''

            self.set_acqvalue(acqvalue)

        @age.setter
        def age(self, age):
            '''
            :type age: str or None
            '''

            self.set_age(age)

        @appnotes.setter
        def appnotes(self, appnotes):
            '''
            :type appnotes: str or None
            '''

            self.set_appnotes(appnotes)

        @appraisor.setter
        def appraisor(self, appraisor):
            '''
            :type appraisor: str or None
            '''

            self.set_appraisor(appraisor)

        @assemzone.setter
        def assemzone(self, assemzone):
            '''
            :type assemzone: str or None
            '''

            self.set_assemzone(assemzone)

        @bagno.setter
        def bagno(self, bagno):
            '''
            :type bagno: str or None
            '''

            self.set_bagno(bagno)

        @boxno.setter
        def boxno(self, boxno):
            '''
            :type boxno: str or None
            '''

            self.set_boxno(boxno)

        @caption.setter
        def caption(self, caption):
            '''
            :type caption: str or None
            '''

            self.set_caption(caption)

        @cat.setter
        def cat(self, cat):
            '''
            :type cat: str or None
            '''

            self.set_cat(cat)

        @catby.setter
        def catby(self, catby):
            '''
            :type catby: str or None
            '''

            self.set_catby(catby)

        @catdate.setter
        def catdate(self, catdate):
            '''
            :type catdate: datetime.datetime or None
            '''

            self.set_catdate(catdate)

        @cattype.setter
        def cattype(self, cattype):
            '''
            :type cattype: str or None
            '''

            self.set_cattype(cattype)

        @chemcomp.setter
        def chemcomp(self, chemcomp):
            '''
            :type chemcomp: str or None
            '''

            self.set_chemcomp(chemcomp)

        @circum.setter
        def circum(self, circum):
            '''
            :type circum: Decimal or None
            '''

            self.set_circum(circum)

        @circumft.setter
        def circumft(self, circumft):
            '''
            :type circumft: Decimal or None
            '''

            self.set_circumft(circumft)

        @circumin.setter
        def circumin(self, circumin):
            '''
            :type circumin: Decimal or None
            '''

            self.set_circumin(circumin)

        @classes.setter
        def classes(self, classes):
            '''
            :type classes: str or None
            '''

            self.set_classes(classes)

        @colldate.setter
        def colldate(self, colldate):
            '''
            :type colldate: datetime.datetime or None
            '''

            self.set_colldate(colldate)

        @collection.setter
        def collection(self, collection):
            '''
            :type collection: str or None
            '''

            self.set_collection(collection)

        @collector.setter
        def collector(self, collector):
            '''
            :type collector: str or None
            '''

            self.set_collector(collector)

        @conddate.setter
        def conddate(self, conddate):
            '''
            :type conddate: datetime.datetime or None
            '''

            self.set_conddate(conddate)

        @condexam.setter
        def condexam(self, condexam):
            '''
            :type condexam: str or None
            '''

            self.set_condexam(condexam)

        @condition.setter
        def condition(self, condition):
            '''
            :type condition: str or None
            '''

            self.set_condition(condition)

        @condnotes.setter
        def condnotes(self, condnotes):
            '''
            :type condnotes: str or None
            '''

            self.set_condnotes(condnotes)

        @count.setter
        def count(self, count):
            '''
            :type count: str or None
            '''

            self.set_count(count)

        @creator.setter
        def creator(self, creator):
            '''
            :type creator: str or None
            '''

            self.set_creator(creator)

        @creator2.setter
        def creator2(self, creator2):
            '''
            :type creator2: str or None
            '''

            self.set_creator2(creator2)

        @creator3.setter
        def creator3(self, creator3):
            '''
            :type creator3: str or None
            '''

            self.set_creator3(creator3)

        @credit.setter
        def credit(self, credit):
            '''
            :type credit: str or None
            '''

            self.set_credit(credit)

        @crystal.setter
        def crystal(self, crystal):
            '''
            :type crystal: str or None
            '''

            self.set_crystal(crystal)

        @culture.setter
        def culture(self, culture):
            '''
            :type culture: str or None
            '''

            self.set_culture(culture)

        @curvalmax.setter
        def curvalmax(self, curvalmax):
            '''
            :type curvalmax: Decimal or None
            '''

            self.set_curvalmax(curvalmax)

        @curvalue.setter
        def curvalue(self, curvalue):
            '''
            :type curvalue: Decimal or None
            '''

            self.set_curvalue(curvalue)

        @dataset.setter
        def dataset(self, dataset):
            '''
            :type dataset: str or None
            '''

            self.set_dataset(dataset)

        @date.setter
        def date(self, date):
            '''
            :type date: str or None
            '''

            self.set_date(date)

        @datingmeth.setter
        def datingmeth(self, datingmeth):
            '''
            :type datingmeth: str or None
            '''

            self.set_datingmeth(datingmeth)

        @datum.setter
        def datum(self, datum):
            '''
            :type datum: str or None
            '''

            self.set_datum(datum)

        @depth.setter
        def depth(self, depth):
            '''
            :type depth: Decimal or None
            '''

            self.set_depth(depth)

        @depthft.setter
        def depthft(self, depthft):
            '''
            :type depthft: Decimal or None
            '''

            self.set_depthft(depthft)

        @depthin.setter
        def depthin(self, depthin):
            '''
            :type depthin: Decimal or None
            '''

            self.set_depthin(depthin)

        @descrip.setter
        def descrip(self, descrip):
            '''
            :type descrip: str or None
            '''

            self.set_descrip(descrip)

        @diameter.setter
        def diameter(self, diameter):
            '''
            :type diameter: Decimal or None
            '''

            self.set_diameter(diameter)

        @diameterft.setter
        def diameterft(self, diameterft):
            '''
            :type diameterft: Decimal or None
            '''

            self.set_diameterft(diameterft)

        @diameterin.setter
        def diameterin(self, diameterin):
            '''
            :type diameterin: Decimal or None
            '''

            self.set_diameterin(diameterin)

        @dimnotes.setter
        def dimnotes(self, dimnotes):
            '''
            :type dimnotes: str or None
            '''

            self.set_dimnotes(dimnotes)

        @dimtype.setter
        def dimtype(self, dimtype):
            '''
            :type dimtype: int or None
            '''

            self.set_dimtype(dimtype)

        @dispvalue.setter
        def dispvalue(self, dispvalue):
            '''
            :type dispvalue: str or None
            '''

            self.set_dispvalue(dispvalue)

        @earlydate.setter
        def earlydate(self, earlydate):
            '''
            :type earlydate: int or None
            '''

            self.set_earlydate(earlydate)

        @elements.setter
        def elements(self, elements):
            '''
            :type elements: str or None
            '''

            self.set_elements(elements)

        @epoch.setter
        def epoch(self, epoch):
            '''
            :type epoch: str or None
            '''

            self.set_epoch(epoch)

        @era.setter
        def era(self, era):
            '''
            :type era: str or None
            '''

            self.set_era(era)

        @event.setter
        def event(self, event):
            '''
            :type event: str or None
            '''

            self.set_event(event)

        @ew.setter
        def ew(self, ew):
            '''
            :type ew: str or None
            '''

            self.set_ew(ew)

        @excavadate.setter
        def excavadate(self, excavadate):
            '''
            :type excavadate: datetime.datetime or None
            '''

            self.set_excavadate(excavadate)

        @excavateby.setter
        def excavateby(self, excavateby):
            '''
            :type excavateby: str or None
            '''

            self.set_excavateby(excavateby)

        @exhibitid.setter
        def exhibitid(self, exhibitid):
            '''
            :type exhibitid: str or None
            '''

            self.set_exhibitid(exhibitid)

        @exhibitno.setter
        def exhibitno(self, exhibitno):
            '''
            :type exhibitno: int or None
            '''

            self.set_exhibitno(exhibitno)

        @exhlabel1.setter
        def exhlabel1(self, exhlabel1):
            '''
            :type exhlabel1: str or None
            '''

            self.set_exhlabel1(exhlabel1)

        @exhlabel2.setter
        def exhlabel2(self, exhlabel2):
            '''
            :type exhlabel2: str or None
            '''

            self.set_exhlabel2(exhlabel2)

        @exhlabel3.setter
        def exhlabel3(self, exhlabel3):
            '''
            :type exhlabel3: str or None
            '''

            self.set_exhlabel3(exhlabel3)

        @exhlabel4.setter
        def exhlabel4(self, exhlabel4):
            '''
            :type exhlabel4: str or None
            '''

            self.set_exhlabel4(exhlabel4)

        @exhstart.setter
        def exhstart(self, exhstart):
            '''
            :type exhstart: datetime.datetime or None
            '''

            self.set_exhstart(exhstart)

        @family.setter
        def family(self, family):
            '''
            :type family: str or None
            '''

            self.set_family(family)

        @feature.setter
        def feature(self, feature):
            '''
            :type feature: str or None
            '''

            self.set_feature(feature)

        @flagdate.setter
        def flagdate(self, flagdate):
            '''
            :type flagdate: datetime.datetime or None
            '''

            self.set_flagdate(flagdate)

        @flagnotes.setter
        def flagnotes(self, flagnotes):
            '''
            :type flagnotes: str or None
            '''

            self.set_flagnotes(flagnotes)

        @flagreason.setter
        def flagreason(self, flagreason):
            '''
            :type flagreason: str or None
            '''

            self.set_flagreason(flagreason)

        @formation.setter
        def formation(self, formation):
            '''
            :type formation: str or None
            '''

            self.set_formation(formation)

        @fossils.setter
        def fossils(self, fossils):
            '''
            :type fossils: str or None
            '''

            self.set_fossils(fossils)

        @found.setter
        def found(self, found):
            '''
            :type found: str or None
            '''

            self.set_found(found)

        @fracture.setter
        def fracture(self, fracture):
            '''
            :type fracture: str or None
            '''

            self.set_fracture(fracture)

        @frame.setter
        def frame(self, frame):
            '''
            :type frame: str or None
            '''

            self.set_frame(frame)

        @framesize.setter
        def framesize(self, framesize):
            '''
            :type framesize: str or None
            '''

            self.set_framesize(framesize)

        @genus.setter
        def genus(self, genus):
            '''
            :type genus: str or None
            '''

            self.set_genus(genus)

        @gparent.setter
        def gparent(self, gparent):
            '''
            :type gparent: str or None
            '''

            self.set_gparent(gparent)

        @grainsize.setter
        def grainsize(self, grainsize):
            '''
            :type grainsize: str or None
            '''

            self.set_grainsize(grainsize)

        @habitat.setter
        def habitat(self, habitat):
            '''
            :type habitat: str or None
            '''

            self.set_habitat(habitat)

        @hardness.setter
        def hardness(self, hardness):
            '''
            :type hardness: str or None
            '''

            self.set_hardness(hardness)

        @height.setter
        def height(self, height):
            '''
            :type height: Decimal or None
            '''

            self.set_height(height)

        @heightft.setter
        def heightft(self, heightft):
            '''
            :type heightft: Decimal or None
            '''

            self.set_heightft(heightft)

        @heightin.setter
        def heightin(self, heightin):
            '''
            :type heightin: Decimal or None
            '''

            self.set_heightin(heightin)

        @homeloc.setter
        def homeloc(self, homeloc):
            '''
            :type homeloc: str or None
            '''

            self.set_homeloc(homeloc)

        @idby.setter
        def idby(self, idby):
            '''
            :type idby: str or None
            '''

            self.set_idby(idby)

        @iddate.setter
        def iddate(self, iddate):
            '''
            :type iddate: datetime.datetime or None
            '''

            self.set_iddate(iddate)

        @imagefile.setter
        def imagefile(self, imagefile):
            '''
            :type imagefile: str or None
            '''

            self.set_imagefile(imagefile)

        @imageno.setter
        def imageno(self, imageno):
            '''
            :type imageno: int or None
            '''

            self.set_imageno(imageno)

        @imagesize.setter
        def imagesize(self, imagesize):
            '''
            :type imagesize: str or None
            '''

            self.set_imagesize(imagesize)

        @inscomp.setter
        def inscomp(self, inscomp):
            '''
            :type inscomp: str or None
            '''

            self.set_inscomp(inscomp)

        @inscrlang.setter
        def inscrlang(self, inscrlang):
            '''
            :type inscrlang: str or None
            '''

            self.set_inscrlang(inscrlang)

        @inscrpos.setter
        def inscrpos(self, inscrpos):
            '''
            :type inscrpos: str or None
            '''

            self.set_inscrpos(inscrpos)

        @inscrtech.setter
        def inscrtech(self, inscrtech):
            '''
            :type inscrtech: str or None
            '''

            self.set_inscrtech(inscrtech)

        @inscrtext.setter
        def inscrtext(self, inscrtext):
            '''
            :type inscrtext: str or None
            '''

            self.set_inscrtext(inscrtext)

        @inscrtrans.setter
        def inscrtrans(self, inscrtrans):
            '''
            :type inscrtrans: str or None
            '''

            self.set_inscrtrans(inscrtrans)

        @inscrtype.setter
        def inscrtype(self, inscrtype):
            '''
            :type inscrtype: str or None
            '''

            self.set_inscrtype(inscrtype)

        @insdate.setter
        def insdate(self, insdate):
            '''
            :type insdate: datetime.datetime or None
            '''

            self.set_insdate(insdate)

        @insphone.setter
        def insphone(self, insphone):
            '''
            :type insphone: str or None
            '''

            self.set_insphone(insphone)

        @inspremium.setter
        def inspremium(self, inspremium):
            '''
            :type inspremium: str or None
            '''

            self.set_inspremium(inspremium)

        @insrep.setter
        def insrep(self, insrep):
            '''
            :type insrep: str or None
            '''

            self.set_insrep(insrep)

        @insvalue.setter
        def insvalue(self, insvalue):
            '''
            :type insvalue: Decimal or None
            '''

            self.set_insvalue(insvalue)

        @invnby.setter
        def invnby(self, invnby):
            '''
            :type invnby: str or None
            '''

            self.set_invnby(invnby)

        @invndate.setter
        def invndate(self, invndate):
            '''
            :type invndate: datetime.datetime or None
            '''

            self.set_invndate(invndate)

        @kingdom.setter
        def kingdom(self, kingdom):
            '''
            :type kingdom: str or None
            '''

            self.set_kingdom(kingdom)

        @latdeg.setter
        def latdeg(self, latdeg):
            '''
            :type latdeg: Decimal or None
            '''

            self.set_latdeg(latdeg)

        @latedate.setter
        def latedate(self, latedate):
            '''
            :type latedate: int or None
            '''

            self.set_latedate(latedate)

        @legal.setter
        def legal(self, legal):
            '''
            :type legal: str or None
            '''

            self.set_legal(legal)

        @length.setter
        def length(self, length):
            '''
            :type length: Decimal or None
            '''

            self.set_length(length)

        @lengthft.setter
        def lengthft(self, lengthft):
            '''
            :type lengthft: Decimal or None
            '''

            self.set_lengthft(lengthft)

        @lengthin.setter
        def lengthin(self, lengthin):
            '''
            :type lengthin: Decimal or None
            '''

            self.set_lengthin(lengthin)

        @level.setter
        def level(self, level):
            '''
            :type level: str or None
            '''

            self.set_level(level)

        @lithofacie.setter
        def lithofacie(self, lithofacie):
            '''
            :type lithofacie: str or None
            '''

            self.set_lithofacie(lithofacie)

        @loancond.setter
        def loancond(self, loancond):
            '''
            :type loancond: str or None
            '''

            self.set_loancond(loancond)

        @loandue.setter
        def loandue(self, loandue):
            '''
            :type loandue: datetime.datetime or None
            '''

            self.set_loandue(loandue)

        @loanid.setter
        def loanid(self, loanid):
            '''
            :type loanid: str or None
            '''

            self.set_loanid(loanid)

        @loaninno.setter
        def loaninno(self, loaninno):
            '''
            :type loaninno: str or None
            '''

            self.set_loaninno(loaninno)

        @loanno.setter
        def loanno(self, loanno):
            '''
            :type loanno: int or None
            '''

            self.set_loanno(loanno)

        @loanrenew.setter
        def loanrenew(self, loanrenew):
            '''
            :type loanrenew: datetime.datetime or None
            '''

            self.set_loanrenew(loanrenew)

        @locfield1.setter
        def locfield1(self, locfield1):
            '''
            :type locfield1: str or None
            '''

            self.set_locfield1(locfield1)

        @locfield2.setter
        def locfield2(self, locfield2):
            '''
            :type locfield2: str or None
            '''

            self.set_locfield2(locfield2)

        @locfield3.setter
        def locfield3(self, locfield3):
            '''
            :type locfield3: str or None
            '''

            self.set_locfield3(locfield3)

        @locfield4.setter
        def locfield4(self, locfield4):
            '''
            :type locfield4: str or None
            '''

            self.set_locfield4(locfield4)

        @locfield5.setter
        def locfield5(self, locfield5):
            '''
            :type locfield5: str or None
            '''

            self.set_locfield5(locfield5)

        @locfield6.setter
        def locfield6(self, locfield6):
            '''
            :type locfield6: str or None
            '''

            self.set_locfield6(locfield6)

        @longdeg.setter
        def longdeg(self, longdeg):
            '''
            :type longdeg: Decimal or None
            '''

            self.set_longdeg(longdeg)

        @luster.setter
        def luster(self, luster):
            '''
            :type luster: str or None
            '''

            self.set_luster(luster)

        @made.setter
        def made(self, made):
            '''
            :type made: str or None
            '''

            self.set_made(made)

        @maintcycle.setter
        def maintcycle(self, maintcycle):
            '''
            :type maintcycle: str or None
            '''

            self.set_maintcycle(maintcycle)

        @maintdate.setter
        def maintdate(self, maintdate):
            '''
            :type maintdate: datetime.datetime or None
            '''

            self.set_maintdate(maintdate)

        @maintnote.setter
        def maintnote(self, maintnote):
            '''
            :type maintnote: str or None
            '''

            self.set_maintnote(maintnote)

        @material.setter
        def material(self, material):
            '''
            :type material: str or None
            '''

            self.set_material(material)

        @medium.setter
        def medium(self, medium):
            '''
            :type medium: str or None
            '''

            self.set_medium(medium)

        @member.setter
        def member(self, member):
            '''
            :type member: str or None
            '''

            self.set_member(member)

        @mmark.setter
        def mmark(self, mmark):
            '''
            :type mmark: str or None
            '''

            self.set_mmark(mmark)

        @nhclass.setter
        def nhclass(self, nhclass):
            '''
            :type nhclass: str or None
            '''

            self.set_nhclass(nhclass)

        @nhorder.setter
        def nhorder(self, nhorder):
            '''
            :type nhorder: str or None
            '''

            self.set_nhorder(nhorder)

        @notes.setter
        def notes(self, notes):
            '''
            :type notes: str or None
            '''

            self.set_notes(notes)

        @ns.setter
        def ns(self, ns):
            '''
            :type ns: str or None
            '''

            self.set_ns(ns)

        @objectid.setter
        def objectid(self, objectid):
            '''
            :type objectid: str or None
            '''

            self.set_objectid(objectid)

        @objname.setter
        def objname(self, objname):
            '''
            :type objname: str or None
            '''

            self.set_objname(objname)

        @objname2.setter
        def objname2(self, objname2):
            '''
            :type objname2: str or None
            '''

            self.set_objname2(objname2)

        @objname3.setter
        def objname3(self, objname3):
            '''
            :type objname3: str or None
            '''

            self.set_objname3(objname3)

        @objnames.setter
        def objnames(self, objnames):
            '''
            :type objnames: str or None
            '''

            self.set_objnames(objnames)

        @occurrence.setter
        def occurrence(self, occurrence):
            '''
            :type occurrence: str or None
            '''

            self.set_occurrence(occurrence)

        @oldno.setter
        def oldno(self, oldno):
            '''
            :type oldno: str or None
            '''

            self.set_oldno(oldno)

        @origin.setter
        def origin(self, origin):
            '''
            :type origin: str or None
            '''

            self.set_origin(origin)

        @othername.setter
        def othername(self, othername):
            '''
            :type othername: str or None
            '''

            self.set_othername(othername)

        @otherno.setter
        def otherno(self, otherno):
            '''
            :type otherno: str or None
            '''

            self.set_otherno(otherno)

        @outdate.setter
        def outdate(self, outdate):
            '''
            :type outdate: datetime.datetime or None
            '''

            self.set_outdate(outdate)

        @owned.setter
        def owned(self, owned):
            '''
            :type owned: str or None
            '''

            self.set_owned(owned)

        @parent.setter
        def parent(self, parent):
            '''
            :type parent: str or None
            '''

            self.set_parent(parent)

        @people.setter
        def people(self, people):
            '''
            :type people: str or None
            '''

            self.set_people(people)

        @period.setter
        def period(self, period):
            '''
            :type period: str or None
            '''

            self.set_period(period)

        @phylum.setter
        def phylum(self, phylum):
            '''
            :type phylum: str or None
            '''

            self.set_phylum(phylum)

        @policyno.setter
        def policyno(self, policyno):
            '''
            :type policyno: str or None
            '''

            self.set_policyno(policyno)

        @ppid.setter
        def ppid(self, ppid):
            '''
            :type ppid: str or None
            '''

            self.set_ppid(ppid)

        @preparator.setter
        def preparator(self, preparator):
            '''
            :type preparator: str or None
            '''

            self.set_preparator(preparator)

        @prepdate.setter
        def prepdate(self, prepdate):
            '''
            :type prepdate: datetime.datetime or None
            '''

            self.set_prepdate(prepdate)

        @preserve.setter
        def preserve(self, preserve):
            '''
            :type preserve: str or None
            '''

            self.set_preserve(preserve)

        @pressure.setter
        def pressure(self, pressure):
            '''
            :type pressure: str or None
            '''

            self.set_pressure(pressure)

        @provenance.setter
        def provenance(self, provenance):
            '''
            :type provenance: str or None
            '''

            self.set_provenance(provenance)

        @pubnotes.setter
        def pubnotes(self, pubnotes):
            '''
            :type pubnotes: str or None
            '''

            self.set_pubnotes(pubnotes)

        @qrurl.setter
        def qrurl(self, qrurl):
            '''
            :type qrurl: str or None
            '''

            self.set_qrurl(qrurl)

        @recas.setter
        def recas(self, recas):
            '''
            :type recas: str or None
            '''

            self.set_recas(recas)

        @recdate.setter
        def recdate(self, recdate):
            '''
            :type recdate: str or None
            '''

            self.set_recdate(recdate)

        @recfrom.setter
        def recfrom(self, recfrom):
            '''
            :type recfrom: str or None
            '''

            self.set_recfrom(recfrom)

        @relation.setter
        def relation(self, relation):
            '''
            :type relation: str or None
            '''

            self.set_relation(relation)

        @relnotes.setter
        def relnotes(self, relnotes):
            '''
            :type relnotes: str or None
            '''

            self.set_relnotes(relnotes)

        @renewuntil.setter
        def renewuntil(self, renewuntil):
            '''
            :type renewuntil: datetime.datetime or None
            '''

            self.set_renewuntil(renewuntil)

        @repatby.setter
        def repatby(self, repatby):
            '''
            :type repatby: str or None
            '''

            self.set_repatby(repatby)

        @repatclaim.setter
        def repatclaim(self, repatclaim):
            '''
            :type repatclaim: str or None
            '''

            self.set_repatclaim(repatclaim)

        @repatdate.setter
        def repatdate(self, repatdate):
            '''
            :type repatdate: datetime.datetime or None
            '''

            self.set_repatdate(repatdate)

        @repatdisp.setter
        def repatdisp(self, repatdisp):
            '''
            :type repatdisp: str or None
            '''

            self.set_repatdisp(repatdisp)

        @repathand.setter
        def repathand(self, repathand):
            '''
            :type repathand: str or None
            '''

            self.set_repathand(repathand)

        @repatnotes.setter
        def repatnotes(self, repatnotes):
            '''
            :type repatnotes: str or None
            '''

            self.set_repatnotes(repatnotes)

        @repatnotic.setter
        def repatnotic(self, repatnotic):
            '''
            :type repatnotic: datetime.datetime or None
            '''

            self.set_repatnotic(repatnotic)

        @repattype.setter
        def repattype(self, repattype):
            '''
            :type repattype: str or None
            '''

            self.set_repattype(repattype)

        @rockclass.setter
        def rockclass(self, rockclass):
            '''
            :type rockclass: str or None
            '''

            self.set_rockclass(rockclass)

        @rockcolor.setter
        def rockcolor(self, rockcolor):
            '''
            :type rockcolor: str or None
            '''

            self.set_rockcolor(rockcolor)

        @rockorigin.setter
        def rockorigin(self, rockorigin):
            '''
            :type rockorigin: str or None
            '''

            self.set_rockorigin(rockorigin)

        @rocktype.setter
        def rocktype(self, rocktype):
            '''
            :type rocktype: str or None
            '''

            self.set_rocktype(rocktype)

        @role.setter
        def role(self, role):
            '''
            :type role: str or None
            '''

            self.set_role(role)

        @role2.setter
        def role2(self, role2):
            '''
            :type role2: str or None
            '''

            self.set_role2(role2)

        @role3.setter
        def role3(self, role3):
            '''
            :type role3: str or None
            '''

            self.set_role3(role3)

        @school.setter
        def school(self, school):
            '''
            :type school: str or None
            '''

            self.set_school(school)

        @sex.setter
        def sex(self, sex):
            '''
            :type sex: str or None
            '''

            self.set_sex(sex)

        @sgflag.setter
        def sgflag(self, sgflag):
            '''
            :type sgflag: str or None
            '''

            self.set_sgflag(sgflag)

        @signedname.setter
        def signedname(self, signedname):
            '''
            :type signedname: str or None
            '''

            self.set_signedname(signedname)

        @signloc.setter
        def signloc(self, signloc):
            '''
            :type signloc: str or None
            '''

            self.set_signloc(signloc)

        @site.setter
        def site(self, site):
            '''
            :type site: str or None
            '''

            self.set_site(site)

        @siteno.setter
        def siteno(self, siteno):
            '''
            :type siteno: str or None
            '''

            self.set_siteno(siteno)

        @specgrav.setter
        def specgrav(self, specgrav):
            '''
            :type specgrav: str or None
            '''

            self.set_specgrav(specgrav)

        @species.setter
        def species(self, species):
            '''
            :type species: str or None
            '''

            self.set_species(species)

        @sprocess.setter
        def sprocess(self, sprocess):
            '''
            :type sprocess: str or None
            '''

            self.set_sprocess(sprocess)

        @stage.setter
        def stage(self, stage):
            '''
            :type stage: str or None
            '''

            self.set_stage(stage)

        @status.setter
        def status(self, status):
            '''
            :type status: str or None
            '''

            self.set_status(status)

        @statusby.setter
        def statusby(self, statusby):
            '''
            :type statusby: str or None
            '''

            self.set_statusby(statusby)

        @statusdate.setter
        def statusdate(self, statusdate):
            '''
            :type statusdate: datetime.datetime or None
            '''

            self.set_statusdate(statusdate)

        @sterms.setter
        def sterms(self, sterms):
            '''
            :type sterms: str or None
            '''

            self.set_sterms(sterms)

        @stratum.setter
        def stratum(self, stratum):
            '''
            :type stratum: str or None
            '''

            self.set_stratum(stratum)

        @streak.setter
        def streak(self, streak):
            '''
            :type streak: str or None
            '''

            self.set_streak(streak)

        @subfamily.setter
        def subfamily(self, subfamily):
            '''
            :type subfamily: str or None
            '''

            self.set_subfamily(subfamily)

        @subjects.setter
        def subjects(self, subjects):
            '''
            :type subjects: str or None
            '''

            self.set_subjects(subjects)

        @subspecies.setter
        def subspecies(self, subspecies):
            '''
            :type subspecies: str or None
            '''

            self.set_subspecies(subspecies)

        @technique.setter
        def technique(self, technique):
            '''
            :type technique: str or None
            '''

            self.set_technique(technique)

        @tempauthor.setter
        def tempauthor(self, tempauthor):
            '''
            :type tempauthor: str or None
            '''

            self.set_tempauthor(tempauthor)

        @tempby.setter
        def tempby(self, tempby):
            '''
            :type tempby: str or None
            '''

            self.set_tempby(tempby)

        @tempdate.setter
        def tempdate(self, tempdate):
            '''
            :type tempdate: datetime.datetime or None
            '''

            self.set_tempdate(tempdate)

        @temperatur.setter
        def temperatur(self, temperatur):
            '''
            :type temperatur: str or None
            '''

            self.set_temperatur(temperatur)

        @temploc.setter
        def temploc(self, temploc):
            '''
            :type temploc: str or None
            '''

            self.set_temploc(temploc)

        @tempnotes.setter
        def tempnotes(self, tempnotes):
            '''
            :type tempnotes: str or None
            '''

            self.set_tempnotes(tempnotes)

        @tempreason.setter
        def tempreason(self, tempreason):
            '''
            :type tempreason: str or None
            '''

            self.set_tempreason(tempreason)

        @tempuntil.setter
        def tempuntil(self, tempuntil):
            '''
            :type tempuntil: str or None
            '''

            self.set_tempuntil(tempuntil)

        @texture.setter
        def texture(self, texture):
            '''
            :type texture: str or None
            '''

            self.set_texture(texture)

        @title.setter
        def title(self, title):
            '''
            :type title: str or None
            '''

            self.set_title(title)

        @tlocfield1.setter
        def tlocfield1(self, tlocfield1):
            '''
            :type tlocfield1: str or None
            '''

            self.set_tlocfield1(tlocfield1)

        @tlocfield2.setter
        def tlocfield2(self, tlocfield2):
            '''
            :type tlocfield2: str or None
            '''

            self.set_tlocfield2(tlocfield2)

        @tlocfield3.setter
        def tlocfield3(self, tlocfield3):
            '''
            :type tlocfield3: str or None
            '''

            self.set_tlocfield3(tlocfield3)

        @tlocfield4.setter
        def tlocfield4(self, tlocfield4):
            '''
            :type tlocfield4: str or None
            '''

            self.set_tlocfield4(tlocfield4)

        @tlocfield5.setter
        def tlocfield5(self, tlocfield5):
            '''
            :type tlocfield5: str or None
            '''

            self.set_tlocfield5(tlocfield5)

        @tlocfield6.setter
        def tlocfield6(self, tlocfield6):
            '''
            :type tlocfield6: str or None
            '''

            self.set_tlocfield6(tlocfield6)

        @udf1.setter
        def udf1(self, udf1):
            '''
            :type udf1: str or None
            '''

            self.set_udf1(udf1)

        @udf10.setter
        def udf10(self, udf10):
            '''
            :type udf10: str or None
            '''

            self.set_udf10(udf10)

        @udf11.setter
        def udf11(self, udf11):
            '''
            :type udf11: str or None
            '''

            self.set_udf11(udf11)

        @udf12.setter
        def udf12(self, udf12):
            '''
            :type udf12: str or None
            '''

            self.set_udf12(udf12)

        @udf13.setter
        def udf13(self, udf13):
            '''
            :type udf13: int or None
            '''

            self.set_udf13(udf13)

        @udf14.setter
        def udf14(self, udf14):
            '''
            :type udf14: Decimal or None
            '''

            self.set_udf14(udf14)

        @udf15.setter
        def udf15(self, udf15):
            '''
            :type udf15: Decimal or None
            '''

            self.set_udf15(udf15)

        @udf16.setter
        def udf16(self, udf16):
            '''
            :type udf16: Decimal or None
            '''

            self.set_udf16(udf16)

        @udf17.setter
        def udf17(self, udf17):
            '''
            :type udf17: Decimal or None
            '''

            self.set_udf17(udf17)

        @udf18.setter
        def udf18(self, udf18):
            '''
            :type udf18: datetime.datetime or None
            '''

            self.set_udf18(udf18)

        @udf19.setter
        def udf19(self, udf19):
            '''
            :type udf19: datetime.datetime or None
            '''

            self.set_udf19(udf19)

        @udf2.setter
        def udf2(self, udf2):
            '''
            :type udf2: str or None
            '''

            self.set_udf2(udf2)

        @udf20.setter
        def udf20(self, udf20):
            '''
            :type udf20: datetime.datetime or None
            '''

            self.set_udf20(udf20)

        @udf21.setter
        def udf21(self, udf21):
            '''
            :type udf21: str or None
            '''

            self.set_udf21(udf21)

        @udf22.setter
        def udf22(self, udf22):
            '''
            :type udf22: str or None
            '''

            self.set_udf22(udf22)

        @udf3.setter
        def udf3(self, udf3):
            '''
            :type udf3: str or None
            '''

            self.set_udf3(udf3)

        @udf4.setter
        def udf4(self, udf4):
            '''
            :type udf4: str or None
            '''

            self.set_udf4(udf4)

        @udf5.setter
        def udf5(self, udf5):
            '''
            :type udf5: str or None
            '''

            self.set_udf5(udf5)

        @udf6.setter
        def udf6(self, udf6):
            '''
            :type udf6: str or None
            '''

            self.set_udf6(udf6)

        @udf7.setter
        def udf7(self, udf7):
            '''
            :type udf7: str or None
            '''

            self.set_udf7(udf7)

        @udf8.setter
        def udf8(self, udf8):
            '''
            :type udf8: str or None
            '''

            self.set_udf8(udf8)

        @udf9.setter
        def udf9(self, udf9):
            '''
            :type udf9: str or None
            '''

            self.set_udf9(udf9)

        @unit.setter
        def unit(self, unit):
            '''
            :type unit: str or None
            '''

            self.set_unit(unit)

        @updated.setter
        def updated(self, updated):
            '''
            :type updated: datetime.datetime or None
            '''

            self.set_updated(updated)

        @updatedby.setter
        def updatedby(self, updatedby):
            '''
            :type updatedby: str or None
            '''

            self.set_updatedby(updatedby)

        @used.setter
        def used(self, used):
            '''
            :type used: str or None
            '''

            self.set_used(used)

        @valuedate.setter
        def valuedate(self, valuedate):
            '''
            :type valuedate: datetime.datetime or None
            '''

            self.set_valuedate(valuedate)

        @varieties.setter
        def varieties(self, varieties):
            '''
            :type varieties: str or None
            '''

            self.set_varieties(varieties)

        @vexhtml.setter
        def vexhtml(self, vexhtml):
            '''
            :type vexhtml: str or None
            '''

            self.set_vexhtml(vexhtml)

        @vexlabel1.setter
        def vexlabel1(self, vexlabel1):
            '''
            :type vexlabel1: str or None
            '''

            self.set_vexlabel1(vexlabel1)

        @vexlabel2.setter
        def vexlabel2(self, vexlabel2):
            '''
            :type vexlabel2: str or None
            '''

            self.set_vexlabel2(vexlabel2)

        @vexlabel3.setter
        def vexlabel3(self, vexlabel3):
            '''
            :type vexlabel3: str or None
            '''

            self.set_vexlabel3(vexlabel3)

        @vexlabel4.setter
        def vexlabel4(self, vexlabel4):
            '''
            :type vexlabel4: str or None
            '''

            self.set_vexlabel4(vexlabel4)

        @webinclude.setter
        def webinclude(self, webinclude):
            '''
            :type webinclude: bool or None
            '''

            self.set_webinclude(webinclude)

        @weight.setter
        def weight(self, weight):
            '''
            :type weight: Decimal or None
            '''

            self.set_weight(weight)

        @weightin.setter
        def weightin(self, weightin):
            '''
            :type weightin: Decimal or None
            '''

            self.set_weightin(weightin)

        @weightlb.setter
        def weightlb(self, weightlb):
            '''
            :type weightlb: Decimal or None
            '''

            self.set_weightlb(weightlb)

        @width.setter
        def width(self, width):
            '''
            :type width: Decimal or None
            '''

            self.set_width(width)

        @widthft.setter
        def widthft(self, widthft):
            '''
            :type widthft: Decimal or None
            '''

            self.set_widthft(widthft)

        @widthin.setter
        def widthin(self, widthin):
            '''
            :type widthin: Decimal or None
            '''

            self.set_widthin(widthin)

        @xcord.setter
        def xcord(self, xcord):
            '''
            :type xcord: Decimal or None
            '''

            self.set_xcord(xcord)

        @ycord.setter
        def ycord(self, ycord):
            '''
            :type ycord: Decimal or None
            '''

            self.set_ycord(ycord)

        @zcord.setter
        def zcord(self, zcord):
            '''
            :type zcord: Decimal or None
            '''

            self.set_zcord(zcord)

        @zsorter.setter
        def zsorter(self, zsorter):
            '''
            :type zsorter: str or None
            '''

            self.set_zsorter(zsorter)

        @zsorterx.setter
        def zsorterx(self, zsorterx):
            '''
            :type zsorterx: str or None
            '''

            self.set_zsorterx(zsorterx)

    class FieldMetadata(object):
        ACCESSNO = None
        ACCESSORY = None
        ACQVALUE = None
        AGE = None
        APPNOTES = None
        APPRAISOR = None
        ASSEMZONE = None
        BAGNO = None
        BOXNO = None
        CAPTION = None
        CAT = None
        CATBY = None
        CATDATE = None
        CATTYPE = None
        CHEMCOMP = None
        CIRCUM = None
        CIRCUMFT = None
        CIRCUMIN = None
        CLASSES = None
        COLLDATE = None
        COLLECTION = None
        COLLECTOR = None
        CONDDATE = None
        CONDEXAM = None
        CONDITION = None
        CONDNOTES = None
        COUNT = None
        CREATOR = None
        CREATOR2 = None
        CREATOR3 = None
        CREDIT = None
        CRYSTAL = None
        CULTURE = None
        CURVALMAX = None
        CURVALUE = None
        DATASET = None
        DATE = None
        DATINGMETH = None
        DATUM = None
        DEPTH = None
        DEPTHFT = None
        DEPTHIN = None
        DESCRIP = None
        DIAMETER = None
        DIAMETERFT = None
        DIAMETERIN = None
        DIMNOTES = None
        DIMTYPE = None
        DISPVALUE = None
        EARLYDATE = None
        ELEMENTS = None
        EPOCH = None
        ERA = None
        EVENT = None
        EW = None
        EXCAVADATE = None
        EXCAVATEBY = None
        EXHIBITID = None
        EXHIBITNO = None
        EXHLABEL1 = None
        EXHLABEL2 = None
        EXHLABEL3 = None
        EXHLABEL4 = None
        EXHSTART = None
        FAMILY = None
        FEATURE = None
        FLAGDATE = None
        FLAGNOTES = None
        FLAGREASON = None
        FORMATION = None
        FOSSILS = None
        FOUND = None
        FRACTURE = None
        FRAME = None
        FRAMESIZE = None
        GENUS = None
        GPARENT = None
        GRAINSIZE = None
        HABITAT = None
        HARDNESS = None
        HEIGHT = None
        HEIGHTFT = None
        HEIGHTIN = None
        HOMELOC = None
        IDBY = None
        IDDATE = None
        IMAGEFILE = None
        IMAGENO = None
        IMAGESIZE = None
        INSCOMP = None
        INSCRLANG = None
        INSCRPOS = None
        INSCRTECH = None
        INSCRTEXT = None
        INSCRTRANS = None
        INSCRTYPE = None
        INSDATE = None
        INSPHONE = None
        INSPREMIUM = None
        INSREP = None
        INSVALUE = None
        INVNBY = None
        INVNDATE = None
        KINGDOM = None
        LATDEG = None
        LATEDATE = None
        LEGAL = None
        LENGTH = None
        LENGTHFT = None
        LENGTHIN = None
        LEVEL = None
        LITHOFACIE = None
        LOANCOND = None
        LOANDUE = None
        LOANID = None
        LOANINNO = None
        LOANNO = None
        LOANRENEW = None
        LOCFIELD1 = None
        LOCFIELD2 = None
        LOCFIELD3 = None
        LOCFIELD4 = None
        LOCFIELD5 = None
        LOCFIELD6 = None
        LONGDEG = None
        LUSTER = None
        MADE = None
        MAINTCYCLE = None
        MAINTDATE = None
        MAINTNOTE = None
        MATERIAL = None
        MEDIUM = None
        MEMBER = None
        MMARK = None
        NHCLASS = None
        NHORDER = None
        NOTES = None
        NS = None
        OBJECTID = None
        OBJNAME = None
        OBJNAME2 = None
        OBJNAME3 = None
        OBJNAMES = None
        OCCURRENCE = None
        OLDNO = None
        ORIGIN = None
        OTHERNAME = None
        OTHERNO = None
        OUTDATE = None
        OWNED = None
        PARENT = None
        PEOPLE = None
        PERIOD = None
        PHYLUM = None
        POLICYNO = None
        PPID = None
        PREPARATOR = None
        PREPDATE = None
        PRESERVE = None
        PRESSURE = None
        PROVENANCE = None
        PUBNOTES = None
        QRURL = None
        RECAS = None
        RECDATE = None
        RECFROM = None
        RELATION = None
        RELNOTES = None
        RENEWUNTIL = None
        REPATBY = None
        REPATCLAIM = None
        REPATDATE = None
        REPATDISP = None
        REPATHAND = None
        REPATNOTES = None
        REPATNOTIC = None
        REPATTYPE = None
        ROCKCLASS = None
        ROCKCOLOR = None
        ROCKORIGIN = None
        ROCKTYPE = None
        ROLE = None
        ROLE2 = None
        ROLE3 = None
        SCHOOL = None
        SEX = None
        SGFLAG = None
        SIGNEDNAME = None
        SIGNLOC = None
        SITE = None
        SITENO = None
        SPECGRAV = None
        SPECIES = None
        SPROCESS = None
        STAGE = None
        STATUS = None
        STATUSBY = None
        STATUSDATE = None
        STERMS = None
        STRATUM = None
        STREAK = None
        SUBFAMILY = None
        SUBJECTS = None
        SUBSPECIES = None
        TECHNIQUE = None
        TEMPAUTHOR = None
        TEMPBY = None
        TEMPDATE = None
        TEMPERATUR = None
        TEMPLOC = None
        TEMPNOTES = None
        TEMPREASON = None
        TEMPUNTIL = None
        TEXTURE = None
        TITLE = None
        TLOCFIELD1 = None
        TLOCFIELD2 = None
        TLOCFIELD3 = None
        TLOCFIELD4 = None
        TLOCFIELD5 = None
        TLOCFIELD6 = None
        UDF1 = None
        UDF10 = None
        UDF11 = None
        UDF12 = None
        UDF13 = None
        UDF14 = None
        UDF15 = None
        UDF16 = None
        UDF17 = None
        UDF18 = None
        UDF19 = None
        UDF2 = None
        UDF20 = None
        UDF21 = None
        UDF22 = None
        UDF3 = None
        UDF4 = None
        UDF5 = None
        UDF6 = None
        UDF7 = None
        UDF8 = None
        UDF9 = None
        UNIT = None
        UPDATED = None
        UPDATEDBY = None
        USED = None
        VALUEDATE = None
        VARIETIES = None
        VEXHTML = None
        VEXLABEL1 = None
        VEXLABEL2 = None
        VEXLABEL3 = None
        VEXLABEL4 = None
        WEBINCLUDE = None
        WEIGHT = None
        WEIGHTIN = None
        WEIGHTLB = None
        WIDTH = None
        WIDTHFT = None
        WIDTHIN = None
        XCORD = None
        YCORD = None
        ZCORD = None
        ZSORTER = None
        ZSORTERX = None

        def __init__(self, name, type_, validation):
            object.__init__(self)
            self.__name = name
            self.__type = type_
            self.__validation = validation

        @property
        def name(self):
            return self.__name

        def __repr__(self):
            return self.__name

        def __str__(self):
            return self.__name

        @property
        def type(self):
            return self.__type

        @property
        def validation(self):
            return self.__validation

        @classmethod
        def values(cls):
            return (cls.ACCESSNO, cls.ACCESSORY, cls.ACQVALUE, cls.AGE, cls.APPNOTES, cls.APPRAISOR, cls.ASSEMZONE, cls.BAGNO, cls.BOXNO, cls.CAPTION, cls.CAT, cls.CATBY, cls.CATDATE, cls.CATTYPE, cls.CHEMCOMP, cls.CIRCUM, cls.CIRCUMFT, cls.CIRCUMIN, cls.CLASSES, cls.COLLDATE, cls.COLLECTION, cls.COLLECTOR, cls.CONDDATE, cls.CONDEXAM, cls.CONDITION, cls.CONDNOTES, cls.COUNT, cls.CREATOR, cls.CREATOR2, cls.CREATOR3, cls.CREDIT, cls.CRYSTAL, cls.CULTURE, cls.CURVALMAX, cls.CURVALUE, cls.DATASET, cls.DATE, cls.DATINGMETH, cls.DATUM, cls.DEPTH, cls.DEPTHFT, cls.DEPTHIN, cls.DESCRIP, cls.DIAMETER, cls.DIAMETERFT, cls.DIAMETERIN, cls.DIMNOTES, cls.DIMTYPE, cls.DISPVALUE, cls.EARLYDATE, cls.ELEMENTS, cls.EPOCH, cls.ERA, cls.EVENT, cls.EW, cls.EXCAVADATE, cls.EXCAVATEBY, cls.EXHIBITID, cls.EXHIBITNO, cls.EXHLABEL1, cls.EXHLABEL2, cls.EXHLABEL3, cls.EXHLABEL4, cls.EXHSTART, cls.FAMILY, cls.FEATURE, cls.FLAGDATE, cls.FLAGNOTES, cls.FLAGREASON, cls.FORMATION, cls.FOSSILS, cls.FOUND, cls.FRACTURE, cls.FRAME, cls.FRAMESIZE, cls.GENUS, cls.GPARENT, cls.GRAINSIZE, cls.HABITAT, cls.HARDNESS, cls.HEIGHT, cls.HEIGHTFT, cls.HEIGHTIN, cls.HOMELOC, cls.IDBY, cls.IDDATE, cls.IMAGEFILE, cls.IMAGENO, cls.IMAGESIZE, cls.INSCOMP, cls.INSCRLANG, cls.INSCRPOS, cls.INSCRTECH, cls.INSCRTEXT, cls.INSCRTRANS, cls.INSCRTYPE, cls.INSDATE, cls.INSPHONE, cls.INSPREMIUM, cls.INSREP, cls.INSVALUE, cls.INVNBY, cls.INVNDATE, cls.KINGDOM, cls.LATDEG, cls.LATEDATE, cls.LEGAL, cls.LENGTH, cls.LENGTHFT, cls.LENGTHIN, cls.LEVEL, cls.LITHOFACIE, cls.LOANCOND, cls.LOANDUE, cls.LOANID, cls.LOANINNO, cls.LOANNO, cls.LOANRENEW, cls.LOCFIELD1, cls.LOCFIELD2, cls.LOCFIELD3, cls.LOCFIELD4, cls.LOCFIELD5, cls.LOCFIELD6, cls.LONGDEG, cls.LUSTER, cls.MADE, cls.MAINTCYCLE, cls.MAINTDATE, cls.MAINTNOTE, cls.MATERIAL, cls.MEDIUM, cls.MEMBER, cls.MMARK, cls.NHCLASS, cls.NHORDER, cls.NOTES, cls.NS, cls.OBJECTID, cls.OBJNAME, cls.OBJNAME2, cls.OBJNAME3, cls.OBJNAMES, cls.OCCURRENCE, cls.OLDNO, cls.ORIGIN, cls.OTHERNAME, cls.OTHERNO, cls.OUTDATE, cls.OWNED, cls.PARENT, cls.PEOPLE, cls.PERIOD, cls.PHYLUM, cls.POLICYNO, cls.PPID, cls.PREPARATOR, cls.PREPDATE, cls.PRESERVE, cls.PRESSURE, cls.PROVENANCE, cls.PUBNOTES, cls.QRURL, cls.RECAS, cls.RECDATE, cls.RECFROM, cls.RELATION, cls.RELNOTES, cls.RENEWUNTIL, cls.REPATBY, cls.REPATCLAIM, cls.REPATDATE, cls.REPATDISP, cls.REPATHAND, cls.REPATNOTES, cls.REPATNOTIC, cls.REPATTYPE, cls.ROCKCLASS, cls.ROCKCOLOR, cls.ROCKORIGIN, cls.ROCKTYPE, cls.ROLE, cls.ROLE2, cls.ROLE3, cls.SCHOOL, cls.SEX, cls.SGFLAG, cls.SIGNEDNAME, cls.SIGNLOC, cls.SITE, cls.SITENO, cls.SPECGRAV, cls.SPECIES, cls.SPROCESS, cls.STAGE, cls.STATUS, cls.STATUSBY, cls.STATUSDATE, cls.STERMS, cls.STRATUM, cls.STREAK, cls.SUBFAMILY, cls.SUBJECTS, cls.SUBSPECIES, cls.TECHNIQUE, cls.TEMPAUTHOR, cls.TEMPBY, cls.TEMPDATE, cls.TEMPERATUR, cls.TEMPLOC, cls.TEMPNOTES, cls.TEMPREASON, cls.TEMPUNTIL, cls.TEXTURE, cls.TITLE, cls.TLOCFIELD1, cls.TLOCFIELD2, cls.TLOCFIELD3, cls.TLOCFIELD4, cls.TLOCFIELD5, cls.TLOCFIELD6, cls.UDF1, cls.UDF10, cls.UDF11, cls.UDF12, cls.UDF13, cls.UDF14, cls.UDF15, cls.UDF16, cls.UDF17, cls.UDF18, cls.UDF19, cls.UDF2, cls.UDF20, cls.UDF21, cls.UDF22, cls.UDF3, cls.UDF4, cls.UDF5, cls.UDF6, cls.UDF7, cls.UDF8, cls.UDF9, cls.UNIT, cls.UPDATED, cls.UPDATEDBY, cls.USED, cls.VALUEDATE, cls.VARIETIES, cls.VEXHTML, cls.VEXLABEL1, cls.VEXLABEL2, cls.VEXLABEL3, cls.VEXLABEL4, cls.WEBINCLUDE, cls.WEIGHT, cls.WEIGHTIN, cls.WEIGHTLB, cls.WIDTH, cls.WIDTHFT, cls.WIDTHIN, cls.XCORD, cls.YCORD, cls.ZCORD, cls.ZSORTER, cls.ZSORTERX,)

    FieldMetadata.ACCESSNO = FieldMetadata('accessno', str, None)
    FieldMetadata.ACCESSORY = FieldMetadata('accessory', str, None)
    FieldMetadata.ACQVALUE = FieldMetadata('acqvalue', decimal.Decimal, None)
    FieldMetadata.AGE = FieldMetadata('age', str, None)
    FieldMetadata.APPNOTES = FieldMetadata('appnotes', str, None)
    FieldMetadata.APPRAISOR = FieldMetadata('appraisor', str, None)
    FieldMetadata.ASSEMZONE = FieldMetadata('assemzone', str, None)
    FieldMetadata.BAGNO = FieldMetadata('bagno', str, None)
    FieldMetadata.BOXNO = FieldMetadata('boxno', str, None)
    FieldMetadata.CAPTION = FieldMetadata('caption', str, None)
    FieldMetadata.CAT = FieldMetadata('cat', str, None)
    FieldMetadata.CATBY = FieldMetadata('catby', str, None)
    FieldMetadata.CATDATE = FieldMetadata('catdate', datetime.datetime, None)
    FieldMetadata.CATTYPE = FieldMetadata('cattype', str, None)
    FieldMetadata.CHEMCOMP = FieldMetadata('chemcomp', str, None)
    FieldMetadata.CIRCUM = FieldMetadata('circum', decimal.Decimal, None)
    FieldMetadata.CIRCUMFT = FieldMetadata('circumft', decimal.Decimal, None)
    FieldMetadata.CIRCUMIN = FieldMetadata('circumin', decimal.Decimal, None)
    FieldMetadata.CLASSES = FieldMetadata('classes', str, None)
    FieldMetadata.COLLDATE = FieldMetadata('colldate', datetime.datetime, None)
    FieldMetadata.COLLECTION = FieldMetadata('collection', str, None)
    FieldMetadata.COLLECTOR = FieldMetadata('collector', str, None)
    FieldMetadata.CONDDATE = FieldMetadata('conddate', datetime.datetime, None)
    FieldMetadata.CONDEXAM = FieldMetadata('condexam', str, None)
    FieldMetadata.CONDITION = FieldMetadata('condition', str, None)
    FieldMetadata.CONDNOTES = FieldMetadata('condnotes', str, None)
    FieldMetadata.COUNT = FieldMetadata('count', str, None)
    FieldMetadata.CREATOR = FieldMetadata('creator', str, None)
    FieldMetadata.CREATOR2 = FieldMetadata('creator2', str, None)
    FieldMetadata.CREATOR3 = FieldMetadata('creator3', str, None)
    FieldMetadata.CREDIT = FieldMetadata('credit', str, None)
    FieldMetadata.CRYSTAL = FieldMetadata('crystal', str, None)
    FieldMetadata.CULTURE = FieldMetadata('culture', str, None)
    FieldMetadata.CURVALMAX = FieldMetadata('curvalmax', decimal.Decimal, None)
    FieldMetadata.CURVALUE = FieldMetadata('curvalue', decimal.Decimal, None)
    FieldMetadata.DATASET = FieldMetadata('dataset', str, None)
    FieldMetadata.DATE = FieldMetadata('date', str, None)
    FieldMetadata.DATINGMETH = FieldMetadata('datingmeth', str, None)
    FieldMetadata.DATUM = FieldMetadata('datum', str, None)
    FieldMetadata.DEPTH = FieldMetadata('depth', decimal.Decimal, None)
    FieldMetadata.DEPTHFT = FieldMetadata('depthft', decimal.Decimal, None)
    FieldMetadata.DEPTHIN = FieldMetadata('depthin', decimal.Decimal, None)
    FieldMetadata.DESCRIP = FieldMetadata('descrip', str, None)
    FieldMetadata.DIAMETER = FieldMetadata('diameter', decimal.Decimal, None)
    FieldMetadata.DIAMETERFT = FieldMetadata('diameterft', decimal.Decimal, None)
    FieldMetadata.DIAMETERIN = FieldMetadata('diameterin', decimal.Decimal, None)
    FieldMetadata.DIMNOTES = FieldMetadata('dimnotes', str, None)
    FieldMetadata.DIMTYPE = FieldMetadata('dimtype', int, None)
    FieldMetadata.DISPVALUE = FieldMetadata('dispvalue', str, None)
    FieldMetadata.EARLYDATE = FieldMetadata('earlydate', int, None)
    FieldMetadata.ELEMENTS = FieldMetadata('elements', str, None)
    FieldMetadata.EPOCH = FieldMetadata('epoch', str, None)
    FieldMetadata.ERA = FieldMetadata('era', str, None)
    FieldMetadata.EVENT = FieldMetadata('event', str, None)
    FieldMetadata.EW = FieldMetadata('ew', str, None)
    FieldMetadata.EXCAVADATE = FieldMetadata('excavadate', datetime.datetime, None)
    FieldMetadata.EXCAVATEBY = FieldMetadata('excavateby', str, None)
    FieldMetadata.EXHIBITID = FieldMetadata('exhibitid', str, None)
    FieldMetadata.EXHIBITNO = FieldMetadata('exhibitno', int, None)
    FieldMetadata.EXHLABEL1 = FieldMetadata('exhlabel1', str, None)
    FieldMetadata.EXHLABEL2 = FieldMetadata('exhlabel2', str, None)
    FieldMetadata.EXHLABEL3 = FieldMetadata('exhlabel3', str, None)
    FieldMetadata.EXHLABEL4 = FieldMetadata('exhlabel4', str, None)
    FieldMetadata.EXHSTART = FieldMetadata('exhstart', datetime.datetime, None)
    FieldMetadata.FAMILY = FieldMetadata('family', str, None)
    FieldMetadata.FEATURE = FieldMetadata('feature', str, None)
    FieldMetadata.FLAGDATE = FieldMetadata('flagdate', datetime.datetime, None)
    FieldMetadata.FLAGNOTES = FieldMetadata('flagnotes', str, None)
    FieldMetadata.FLAGREASON = FieldMetadata('flagreason', str, None)
    FieldMetadata.FORMATION = FieldMetadata('formation', str, None)
    FieldMetadata.FOSSILS = FieldMetadata('fossils', str, None)
    FieldMetadata.FOUND = FieldMetadata('found', str, None)
    FieldMetadata.FRACTURE = FieldMetadata('fracture', str, None)
    FieldMetadata.FRAME = FieldMetadata('frame', str, None)
    FieldMetadata.FRAMESIZE = FieldMetadata('framesize', str, None)
    FieldMetadata.GENUS = FieldMetadata('genus', str, None)
    FieldMetadata.GPARENT = FieldMetadata('gparent', str, None)
    FieldMetadata.GRAINSIZE = FieldMetadata('grainsize', str, None)
    FieldMetadata.HABITAT = FieldMetadata('habitat', str, None)
    FieldMetadata.HARDNESS = FieldMetadata('hardness', str, None)
    FieldMetadata.HEIGHT = FieldMetadata('height', decimal.Decimal, None)
    FieldMetadata.HEIGHTFT = FieldMetadata('heightft', decimal.Decimal, None)
    FieldMetadata.HEIGHTIN = FieldMetadata('heightin', decimal.Decimal, None)
    FieldMetadata.HOMELOC = FieldMetadata('homeloc', str, None)
    FieldMetadata.IDBY = FieldMetadata('idby', str, None)
    FieldMetadata.IDDATE = FieldMetadata('iddate', datetime.datetime, None)
    FieldMetadata.IMAGEFILE = FieldMetadata('imagefile', str, None)
    FieldMetadata.IMAGENO = FieldMetadata('imageno', int, None)
    FieldMetadata.IMAGESIZE = FieldMetadata('imagesize', str, None)
    FieldMetadata.INSCOMP = FieldMetadata('inscomp', str, None)
    FieldMetadata.INSCRLANG = FieldMetadata('inscrlang', str, None)
    FieldMetadata.INSCRPOS = FieldMetadata('inscrpos', str, None)
    FieldMetadata.INSCRTECH = FieldMetadata('inscrtech', str, None)
    FieldMetadata.INSCRTEXT = FieldMetadata('inscrtext', str, None)
    FieldMetadata.INSCRTRANS = FieldMetadata('inscrtrans', str, None)
    FieldMetadata.INSCRTYPE = FieldMetadata('inscrtype', str, None)
    FieldMetadata.INSDATE = FieldMetadata('insdate', datetime.datetime, None)
    FieldMetadata.INSPHONE = FieldMetadata('insphone', str, None)
    FieldMetadata.INSPREMIUM = FieldMetadata('inspremium', str, None)
    FieldMetadata.INSREP = FieldMetadata('insrep', str, None)
    FieldMetadata.INSVALUE = FieldMetadata('insvalue', decimal.Decimal, None)
    FieldMetadata.INVNBY = FieldMetadata('invnby', str, None)
    FieldMetadata.INVNDATE = FieldMetadata('invndate', datetime.datetime, None)
    FieldMetadata.KINGDOM = FieldMetadata('kingdom', str, None)
    FieldMetadata.LATDEG = FieldMetadata('latdeg', decimal.Decimal, None)
    FieldMetadata.LATEDATE = FieldMetadata('latedate', int, None)
    FieldMetadata.LEGAL = FieldMetadata('legal', str, None)
    FieldMetadata.LENGTH = FieldMetadata('length', decimal.Decimal, None)
    FieldMetadata.LENGTHFT = FieldMetadata('lengthft', decimal.Decimal, None)
    FieldMetadata.LENGTHIN = FieldMetadata('lengthin', decimal.Decimal, None)
    FieldMetadata.LEVEL = FieldMetadata('level', str, None)
    FieldMetadata.LITHOFACIE = FieldMetadata('lithofacie', str, None)
    FieldMetadata.LOANCOND = FieldMetadata('loancond', str, None)
    FieldMetadata.LOANDUE = FieldMetadata('loandue', datetime.datetime, None)
    FieldMetadata.LOANID = FieldMetadata('loanid', str, None)
    FieldMetadata.LOANINNO = FieldMetadata('loaninno', str, None)
    FieldMetadata.LOANNO = FieldMetadata('loanno', int, None)
    FieldMetadata.LOANRENEW = FieldMetadata('loanrenew', datetime.datetime, None)
    FieldMetadata.LOCFIELD1 = FieldMetadata('locfield1', str, None)
    FieldMetadata.LOCFIELD2 = FieldMetadata('locfield2', str, None)
    FieldMetadata.LOCFIELD3 = FieldMetadata('locfield3', str, None)
    FieldMetadata.LOCFIELD4 = FieldMetadata('locfield4', str, None)
    FieldMetadata.LOCFIELD5 = FieldMetadata('locfield5', str, None)
    FieldMetadata.LOCFIELD6 = FieldMetadata('locfield6', str, None)
    FieldMetadata.LONGDEG = FieldMetadata('longdeg', decimal.Decimal, None)
    FieldMetadata.LUSTER = FieldMetadata('luster', str, None)
    FieldMetadata.MADE = FieldMetadata('made', str, None)
    FieldMetadata.MAINTCYCLE = FieldMetadata('maintcycle', str, None)
    FieldMetadata.MAINTDATE = FieldMetadata('maintdate', datetime.datetime, None)
    FieldMetadata.MAINTNOTE = FieldMetadata('maintnote', str, None)
    FieldMetadata.MATERIAL = FieldMetadata('material', str, None)
    FieldMetadata.MEDIUM = FieldMetadata('medium', str, None)
    FieldMetadata.MEMBER = FieldMetadata('member', str, None)
    FieldMetadata.MMARK = FieldMetadata('mmark', str, None)
    FieldMetadata.NHCLASS = FieldMetadata('nhclass', str, None)
    FieldMetadata.NHORDER = FieldMetadata('nhorder', str, None)
    FieldMetadata.NOTES = FieldMetadata('notes', str, None)
    FieldMetadata.NS = FieldMetadata('ns', str, None)
    FieldMetadata.OBJECTID = FieldMetadata('objectid', str, None)
    FieldMetadata.OBJNAME = FieldMetadata('objname', str, None)
    FieldMetadata.OBJNAME2 = FieldMetadata('objname2', str, None)
    FieldMetadata.OBJNAME3 = FieldMetadata('objname3', str, None)
    FieldMetadata.OBJNAMES = FieldMetadata('objnames', str, None)
    FieldMetadata.OCCURRENCE = FieldMetadata('occurrence', str, None)
    FieldMetadata.OLDNO = FieldMetadata('oldno', str, None)
    FieldMetadata.ORIGIN = FieldMetadata('origin', str, None)
    FieldMetadata.OTHERNAME = FieldMetadata('othername', str, None)
    FieldMetadata.OTHERNO = FieldMetadata('otherno', str, None)
    FieldMetadata.OUTDATE = FieldMetadata('outdate', datetime.datetime, None)
    FieldMetadata.OWNED = FieldMetadata('owned', str, None)
    FieldMetadata.PARENT = FieldMetadata('parent', str, None)
    FieldMetadata.PEOPLE = FieldMetadata('people', str, None)
    FieldMetadata.PERIOD = FieldMetadata('period', str, None)
    FieldMetadata.PHYLUM = FieldMetadata('phylum', str, None)
    FieldMetadata.POLICYNO = FieldMetadata('policyno', str, None)
    FieldMetadata.PPID = FieldMetadata('ppid', str, None)
    FieldMetadata.PREPARATOR = FieldMetadata('preparator', str, None)
    FieldMetadata.PREPDATE = FieldMetadata('prepdate', datetime.datetime, None)
    FieldMetadata.PRESERVE = FieldMetadata('preserve', str, None)
    FieldMetadata.PRESSURE = FieldMetadata('pressure', str, None)
    FieldMetadata.PROVENANCE = FieldMetadata('provenance', str, None)
    FieldMetadata.PUBNOTES = FieldMetadata('pubnotes', str, None)
    FieldMetadata.QRURL = FieldMetadata('qrurl', str, None)
    FieldMetadata.RECAS = FieldMetadata('recas', str, None)
    FieldMetadata.RECDATE = FieldMetadata('recdate', str, None)
    FieldMetadata.RECFROM = FieldMetadata('recfrom', str, None)
    FieldMetadata.RELATION = FieldMetadata('relation', str, None)
    FieldMetadata.RELNOTES = FieldMetadata('relnotes', str, None)
    FieldMetadata.RENEWUNTIL = FieldMetadata('renewuntil', datetime.datetime, None)
    FieldMetadata.REPATBY = FieldMetadata('repatby', str, None)
    FieldMetadata.REPATCLAIM = FieldMetadata('repatclaim', str, None)
    FieldMetadata.REPATDATE = FieldMetadata('repatdate', datetime.datetime, None)
    FieldMetadata.REPATDISP = FieldMetadata('repatdisp', str, None)
    FieldMetadata.REPATHAND = FieldMetadata('repathand', str, None)
    FieldMetadata.REPATNOTES = FieldMetadata('repatnotes', str, None)
    FieldMetadata.REPATNOTIC = FieldMetadata('repatnotic', datetime.datetime, None)
    FieldMetadata.REPATTYPE = FieldMetadata('repattype', str, None)
    FieldMetadata.ROCKCLASS = FieldMetadata('rockclass', str, None)
    FieldMetadata.ROCKCOLOR = FieldMetadata('rockcolor', str, None)
    FieldMetadata.ROCKORIGIN = FieldMetadata('rockorigin', str, None)
    FieldMetadata.ROCKTYPE = FieldMetadata('rocktype', str, None)
    FieldMetadata.ROLE = FieldMetadata('role', str, None)
    FieldMetadata.ROLE2 = FieldMetadata('role2', str, None)
    FieldMetadata.ROLE3 = FieldMetadata('role3', str, None)
    FieldMetadata.SCHOOL = FieldMetadata('school', str, None)
    FieldMetadata.SEX = FieldMetadata('sex', str, None)
    FieldMetadata.SGFLAG = FieldMetadata('sgflag', str, None)
    FieldMetadata.SIGNEDNAME = FieldMetadata('signedname', str, None)
    FieldMetadata.SIGNLOC = FieldMetadata('signloc', str, None)
    FieldMetadata.SITE = FieldMetadata('site', str, None)
    FieldMetadata.SITENO = FieldMetadata('siteno', str, None)
    FieldMetadata.SPECGRAV = FieldMetadata('specgrav', str, None)
    FieldMetadata.SPECIES = FieldMetadata('species', str, None)
    FieldMetadata.SPROCESS = FieldMetadata('sprocess', str, None)
    FieldMetadata.STAGE = FieldMetadata('stage', str, None)
    FieldMetadata.STATUS = FieldMetadata('status', str, None)
    FieldMetadata.STATUSBY = FieldMetadata('statusby', str, None)
    FieldMetadata.STATUSDATE = FieldMetadata('statusdate', datetime.datetime, None)
    FieldMetadata.STERMS = FieldMetadata('sterms', str, None)
    FieldMetadata.STRATUM = FieldMetadata('stratum', str, None)
    FieldMetadata.STREAK = FieldMetadata('streak', str, None)
    FieldMetadata.SUBFAMILY = FieldMetadata('subfamily', str, None)
    FieldMetadata.SUBJECTS = FieldMetadata('subjects', str, None)
    FieldMetadata.SUBSPECIES = FieldMetadata('subspecies', str, None)
    FieldMetadata.TECHNIQUE = FieldMetadata('technique', str, None)
    FieldMetadata.TEMPAUTHOR = FieldMetadata('tempauthor', str, None)
    FieldMetadata.TEMPBY = FieldMetadata('tempby', str, None)
    FieldMetadata.TEMPDATE = FieldMetadata('tempdate', datetime.datetime, None)
    FieldMetadata.TEMPERATUR = FieldMetadata('temperatur', str, None)
    FieldMetadata.TEMPLOC = FieldMetadata('temploc', str, None)
    FieldMetadata.TEMPNOTES = FieldMetadata('tempnotes', str, None)
    FieldMetadata.TEMPREASON = FieldMetadata('tempreason', str, None)
    FieldMetadata.TEMPUNTIL = FieldMetadata('tempuntil', str, None)
    FieldMetadata.TEXTURE = FieldMetadata('texture', str, None)
    FieldMetadata.TITLE = FieldMetadata('title', str, None)
    FieldMetadata.TLOCFIELD1 = FieldMetadata('tlocfield1', str, None)
    FieldMetadata.TLOCFIELD2 = FieldMetadata('tlocfield2', str, None)
    FieldMetadata.TLOCFIELD3 = FieldMetadata('tlocfield3', str, None)
    FieldMetadata.TLOCFIELD4 = FieldMetadata('tlocfield4', str, None)
    FieldMetadata.TLOCFIELD5 = FieldMetadata('tlocfield5', str, None)
    FieldMetadata.TLOCFIELD6 = FieldMetadata('tlocfield6', str, None)
    FieldMetadata.UDF1 = FieldMetadata('udf1', str, None)
    FieldMetadata.UDF10 = FieldMetadata('udf10', str, None)
    FieldMetadata.UDF11 = FieldMetadata('udf11', str, None)
    FieldMetadata.UDF12 = FieldMetadata('udf12', str, None)
    FieldMetadata.UDF13 = FieldMetadata('udf13', int, None)
    FieldMetadata.UDF14 = FieldMetadata('udf14', decimal.Decimal, None)
    FieldMetadata.UDF15 = FieldMetadata('udf15', decimal.Decimal, None)
    FieldMetadata.UDF16 = FieldMetadata('udf16', decimal.Decimal, None)
    FieldMetadata.UDF17 = FieldMetadata('udf17', decimal.Decimal, None)
    FieldMetadata.UDF18 = FieldMetadata('udf18', datetime.datetime, None)
    FieldMetadata.UDF19 = FieldMetadata('udf19', datetime.datetime, None)
    FieldMetadata.UDF2 = FieldMetadata('udf2', str, None)
    FieldMetadata.UDF20 = FieldMetadata('udf20', datetime.datetime, None)
    FieldMetadata.UDF21 = FieldMetadata('udf21', str, None)
    FieldMetadata.UDF22 = FieldMetadata('udf22', str, None)
    FieldMetadata.UDF3 = FieldMetadata('udf3', str, None)
    FieldMetadata.UDF4 = FieldMetadata('udf4', str, None)
    FieldMetadata.UDF5 = FieldMetadata('udf5', str, None)
    FieldMetadata.UDF6 = FieldMetadata('udf6', str, None)
    FieldMetadata.UDF7 = FieldMetadata('udf7', str, None)
    FieldMetadata.UDF8 = FieldMetadata('udf8', str, None)
    FieldMetadata.UDF9 = FieldMetadata('udf9', str, None)
    FieldMetadata.UNIT = FieldMetadata('unit', str, None)
    FieldMetadata.UPDATED = FieldMetadata('updated', datetime.datetime, None)
    FieldMetadata.UPDATEDBY = FieldMetadata('updatedby', str, None)
    FieldMetadata.USED = FieldMetadata('used', str, None)
    FieldMetadata.VALUEDATE = FieldMetadata('valuedate', datetime.datetime, None)
    FieldMetadata.VARIETIES = FieldMetadata('varieties', str, None)
    FieldMetadata.VEXHTML = FieldMetadata('vexhtml', str, None)
    FieldMetadata.VEXLABEL1 = FieldMetadata('vexlabel1', str, None)
    FieldMetadata.VEXLABEL2 = FieldMetadata('vexlabel2', str, None)
    FieldMetadata.VEXLABEL3 = FieldMetadata('vexlabel3', str, None)
    FieldMetadata.VEXLABEL4 = FieldMetadata('vexlabel4', str, None)
    FieldMetadata.WEBINCLUDE = FieldMetadata('webinclude', bool, None)
    FieldMetadata.WEIGHT = FieldMetadata('weight', decimal.Decimal, None)
    FieldMetadata.WEIGHTIN = FieldMetadata('weightin', decimal.Decimal, None)
    FieldMetadata.WEIGHTLB = FieldMetadata('weightlb', decimal.Decimal, None)
    FieldMetadata.WIDTH = FieldMetadata('width', decimal.Decimal, None)
    FieldMetadata.WIDTHFT = FieldMetadata('widthft', decimal.Decimal, None)
    FieldMetadata.WIDTHIN = FieldMetadata('widthin', decimal.Decimal, None)
    FieldMetadata.XCORD = FieldMetadata('xcord', decimal.Decimal, None)
    FieldMetadata.YCORD = FieldMetadata('ycord', decimal.Decimal, None)
    FieldMetadata.ZCORD = FieldMetadata('zcord', decimal.Decimal, None)
    FieldMetadata.ZSORTER = FieldMetadata('zsorter', str, None)
    FieldMetadata.ZSORTERX = FieldMetadata('zsorterx', str, None)

    def __init__(
        self,
        accessno=None,
        accessory=None,
        acqvalue=None,
        age=None,
        appnotes=None,
        appraisor=None,
        assemzone=None,
        bagno=None,
        boxno=None,
        caption=None,
        cat=None,
        catby=None,
        catdate=None,
        cattype=None,
        chemcomp=None,
        circum=None,
        circumft=None,
        circumin=None,
        classes=None,
        colldate=None,
        collection=None,
        collector=None,
        conddate=None,
        condexam=None,
        condition=None,
        condnotes=None,
        count=None,
        creator=None,
        creator2=None,
        creator3=None,
        credit=None,
        crystal=None,
        culture=None,
        curvalmax=None,
        curvalue=None,
        dataset=None,
        date=None,
        datingmeth=None,
        datum=None,
        depth=None,
        depthft=None,
        depthin=None,
        descrip=None,
        diameter=None,
        diameterft=None,
        diameterin=None,
        dimnotes=None,
        dimtype=None,
        dispvalue=None,
        earlydate=None,
        elements=None,
        epoch=None,
        era=None,
        event=None,
        ew=None,
        excavadate=None,
        excavateby=None,
        exhibitid=None,
        exhibitno=None,
        exhlabel1=None,
        exhlabel2=None,
        exhlabel3=None,
        exhlabel4=None,
        exhstart=None,
        family=None,
        feature=None,
        flagdate=None,
        flagnotes=None,
        flagreason=None,
        formation=None,
        fossils=None,
        found=None,
        fracture=None,
        frame=None,
        framesize=None,
        genus=None,
        gparent=None,
        grainsize=None,
        habitat=None,
        hardness=None,
        height=None,
        heightft=None,
        heightin=None,
        homeloc=None,
        idby=None,
        iddate=None,
        imagefile=None,
        imageno=None,
        imagesize=None,
        inscomp=None,
        inscrlang=None,
        inscrpos=None,
        inscrtech=None,
        inscrtext=None,
        inscrtrans=None,
        inscrtype=None,
        insdate=None,
        insphone=None,
        inspremium=None,
        insrep=None,
        insvalue=None,
        invnby=None,
        invndate=None,
        kingdom=None,
        latdeg=None,
        latedate=None,
        legal=None,
        length=None,
        lengthft=None,
        lengthin=None,
        level=None,
        lithofacie=None,
        loancond=None,
        loandue=None,
        loanid=None,
        loaninno=None,
        loanno=None,
        loanrenew=None,
        locfield1=None,
        locfield2=None,
        locfield3=None,
        locfield4=None,
        locfield5=None,
        locfield6=None,
        longdeg=None,
        luster=None,
        made=None,
        maintcycle=None,
        maintdate=None,
        maintnote=None,
        material=None,
        medium=None,
        member=None,
        mmark=None,
        nhclass=None,
        nhorder=None,
        notes=None,
        ns=None,
        objectid=None,
        objname=None,
        objname2=None,
        objname3=None,
        objnames=None,
        occurrence=None,
        oldno=None,
        origin=None,
        othername=None,
        otherno=None,
        outdate=None,
        owned=None,
        parent=None,
        people=None,
        period=None,
        phylum=None,
        policyno=None,
        ppid=None,
        preparator=None,
        prepdate=None,
        preserve=None,
        pressure=None,
        provenance=None,
        pubnotes=None,
        qrurl=None,
        recas=None,
        recdate=None,
        recfrom=None,
        relation=None,
        relnotes=None,
        renewuntil=None,
        repatby=None,
        repatclaim=None,
        repatdate=None,
        repatdisp=None,
        repathand=None,
        repatnotes=None,
        repatnotic=None,
        repattype=None,
        rockclass=None,
        rockcolor=None,
        rockorigin=None,
        rocktype=None,
        role=None,
        role2=None,
        role3=None,
        school=None,
        sex=None,
        sgflag=None,
        signedname=None,
        signloc=None,
        site=None,
        siteno=None,
        specgrav=None,
        species=None,
        sprocess=None,
        stage=None,
        status=None,
        statusby=None,
        statusdate=None,
        sterms=None,
        stratum=None,
        streak=None,
        subfamily=None,
        subjects=None,
        subspecies=None,
        technique=None,
        tempauthor=None,
        tempby=None,
        tempdate=None,
        temperatur=None,
        temploc=None,
        tempnotes=None,
        tempreason=None,
        tempuntil=None,
        texture=None,
        title=None,
        tlocfield1=None,
        tlocfield2=None,
        tlocfield3=None,
        tlocfield4=None,
        tlocfield5=None,
        tlocfield6=None,
        udf1=None,
        udf10=None,
        udf11=None,
        udf12=None,
        udf13=None,
        udf14=None,
        udf15=None,
        udf16=None,
        udf17=None,
        udf18=None,
        udf19=None,
        udf2=None,
        udf20=None,
        udf21=None,
        udf22=None,
        udf3=None,
        udf4=None,
        udf5=None,
        udf6=None,
        udf7=None,
        udf8=None,
        udf9=None,
        unit=None,
        updated=None,
        updatedby=None,
        used=None,
        valuedate=None,
        varieties=None,
        vexhtml=None,
        vexlabel1=None,
        vexlabel2=None,
        vexlabel3=None,
        vexlabel4=None,
        webinclude=None,
        weight=None,
        weightin=None,
        weightlb=None,
        width=None,
        widthft=None,
        widthin=None,
        xcord=None,
        ycord=None,
        zcord=None,
        zsorter=None,
        zsorterx=None,
    ):
        '''
        :type accessno: str or None
        :type accessory: str or None
        :type acqvalue: Decimal or None
        :type age: str or None
        :type appnotes: str or None
        :type appraisor: str or None
        :type assemzone: str or None
        :type bagno: str or None
        :type boxno: str or None
        :type caption: str or None
        :type cat: str or None
        :type catby: str or None
        :type catdate: datetime.datetime or None
        :type cattype: str or None
        :type chemcomp: str or None
        :type circum: Decimal or None
        :type circumft: Decimal or None
        :type circumin: Decimal or None
        :type classes: str or None
        :type colldate: datetime.datetime or None
        :type collection: str or None
        :type collector: str or None
        :type conddate: datetime.datetime or None
        :type condexam: str or None
        :type condition: str or None
        :type condnotes: str or None
        :type count: str or None
        :type creator: str or None
        :type creator2: str or None
        :type creator3: str or None
        :type credit: str or None
        :type crystal: str or None
        :type culture: str or None
        :type curvalmax: Decimal or None
        :type curvalue: Decimal or None
        :type dataset: str or None
        :type date: str or None
        :type datingmeth: str or None
        :type datum: str or None
        :type depth: Decimal or None
        :type depthft: Decimal or None
        :type depthin: Decimal or None
        :type descrip: str or None
        :type diameter: Decimal or None
        :type diameterft: Decimal or None
        :type diameterin: Decimal or None
        :type dimnotes: str or None
        :type dimtype: int or None
        :type dispvalue: str or None
        :type earlydate: int or None
        :type elements: str or None
        :type epoch: str or None
        :type era: str or None
        :type event: str or None
        :type ew: str or None
        :type excavadate: datetime.datetime or None
        :type excavateby: str or None
        :type exhibitid: str or None
        :type exhibitno: int or None
        :type exhlabel1: str or None
        :type exhlabel2: str or None
        :type exhlabel3: str or None
        :type exhlabel4: str or None
        :type exhstart: datetime.datetime or None
        :type family: str or None
        :type feature: str or None
        :type flagdate: datetime.datetime or None
        :type flagnotes: str or None
        :type flagreason: str or None
        :type formation: str or None
        :type fossils: str or None
        :type found: str or None
        :type fracture: str or None
        :type frame: str or None
        :type framesize: str or None
        :type genus: str or None
        :type gparent: str or None
        :type grainsize: str or None
        :type habitat: str or None
        :type hardness: str or None
        :type height: Decimal or None
        :type heightft: Decimal or None
        :type heightin: Decimal or None
        :type homeloc: str or None
        :type idby: str or None
        :type iddate: datetime.datetime or None
        :type imagefile: str or None
        :type imageno: int or None
        :type imagesize: str or None
        :type inscomp: str or None
        :type inscrlang: str or None
        :type inscrpos: str or None
        :type inscrtech: str or None
        :type inscrtext: str or None
        :type inscrtrans: str or None
        :type inscrtype: str or None
        :type insdate: datetime.datetime or None
        :type insphone: str or None
        :type inspremium: str or None
        :type insrep: str or None
        :type insvalue: Decimal or None
        :type invnby: str or None
        :type invndate: datetime.datetime or None
        :type kingdom: str or None
        :type latdeg: Decimal or None
        :type latedate: int or None
        :type legal: str or None
        :type length: Decimal or None
        :type lengthft: Decimal or None
        :type lengthin: Decimal or None
        :type level: str or None
        :type lithofacie: str or None
        :type loancond: str or None
        :type loandue: datetime.datetime or None
        :type loanid: str or None
        :type loaninno: str or None
        :type loanno: int or None
        :type loanrenew: datetime.datetime or None
        :type locfield1: str or None
        :type locfield2: str or None
        :type locfield3: str or None
        :type locfield4: str or None
        :type locfield5: str or None
        :type locfield6: str or None
        :type longdeg: Decimal or None
        :type luster: str or None
        :type made: str or None
        :type maintcycle: str or None
        :type maintdate: datetime.datetime or None
        :type maintnote: str or None
        :type material: str or None
        :type medium: str or None
        :type member: str or None
        :type mmark: str or None
        :type nhclass: str or None
        :type nhorder: str or None
        :type notes: str or None
        :type ns: str or None
        :type objectid: str or None
        :type objname: str or None
        :type objname2: str or None
        :type objname3: str or None
        :type objnames: str or None
        :type occurrence: str or None
        :type oldno: str or None
        :type origin: str or None
        :type othername: str or None
        :type otherno: str or None
        :type outdate: datetime.datetime or None
        :type owned: str or None
        :type parent: str or None
        :type people: str or None
        :type period: str or None
        :type phylum: str or None
        :type policyno: str or None
        :type ppid: str or None
        :type preparator: str or None
        :type prepdate: datetime.datetime or None
        :type preserve: str or None
        :type pressure: str or None
        :type provenance: str or None
        :type pubnotes: str or None
        :type qrurl: str or None
        :type recas: str or None
        :type recdate: str or None
        :type recfrom: str or None
        :type relation: str or None
        :type relnotes: str or None
        :type renewuntil: datetime.datetime or None
        :type repatby: str or None
        :type repatclaim: str or None
        :type repatdate: datetime.datetime or None
        :type repatdisp: str or None
        :type repathand: str or None
        :type repatnotes: str or None
        :type repatnotic: datetime.datetime or None
        :type repattype: str or None
        :type rockclass: str or None
        :type rockcolor: str or None
        :type rockorigin: str or None
        :type rocktype: str or None
        :type role: str or None
        :type role2: str or None
        :type role3: str or None
        :type school: str or None
        :type sex: str or None
        :type sgflag: str or None
        :type signedname: str or None
        :type signloc: str or None
        :type site: str or None
        :type siteno: str or None
        :type specgrav: str or None
        :type species: str or None
        :type sprocess: str or None
        :type stage: str or None
        :type status: str or None
        :type statusby: str or None
        :type statusdate: datetime.datetime or None
        :type sterms: str or None
        :type stratum: str or None
        :type streak: str or None
        :type subfamily: str or None
        :type subjects: str or None
        :type subspecies: str or None
        :type technique: str or None
        :type tempauthor: str or None
        :type tempby: str or None
        :type tempdate: datetime.datetime or None
        :type temperatur: str or None
        :type temploc: str or None
        :type tempnotes: str or None
        :type tempreason: str or None
        :type tempuntil: str or None
        :type texture: str or None
        :type title: str or None
        :type tlocfield1: str or None
        :type tlocfield2: str or None
        :type tlocfield3: str or None
        :type tlocfield4: str or None
        :type tlocfield5: str or None
        :type tlocfield6: str or None
        :type udf1: str or None
        :type udf10: str or None
        :type udf11: str or None
        :type udf12: str or None
        :type udf13: int or None
        :type udf14: Decimal or None
        :type udf15: Decimal or None
        :type udf16: Decimal or None
        :type udf17: Decimal or None
        :type udf18: datetime.datetime or None
        :type udf19: datetime.datetime or None
        :type udf2: str or None
        :type udf20: datetime.datetime or None
        :type udf21: str or None
        :type udf22: str or None
        :type udf3: str or None
        :type udf4: str or None
        :type udf5: str or None
        :type udf6: str or None
        :type udf7: str or None
        :type udf8: str or None
        :type udf9: str or None
        :type unit: str or None
        :type updated: datetime.datetime or None
        :type updatedby: str or None
        :type used: str or None
        :type valuedate: datetime.datetime or None
        :type varieties: str or None
        :type vexhtml: str or None
        :type vexlabel1: str or None
        :type vexlabel2: str or None
        :type vexlabel3: str or None
        :type vexlabel4: str or None
        :type webinclude: bool or None
        :type weight: Decimal or None
        :type weightin: Decimal or None
        :type weightlb: Decimal or None
        :type width: Decimal or None
        :type widthft: Decimal or None
        :type widthin: Decimal or None
        :type xcord: Decimal or None
        :type ycord: Decimal or None
        :type zcord: Decimal or None
        :type zsorter: str or None
        :type zsorterx: str or None
        '''

        if accessno is not None:
            if not isinstance(accessno, str):
                raise TypeError("expected accessno to be a str but it is a %s" % builtins.type(accessno))
        self.__accessno = accessno

        if accessory is not None:
            if not isinstance(accessory, str):
                raise TypeError("expected accessory to be a str but it is a %s" % builtins.type(accessory))
        self.__accessory = accessory

        if acqvalue is not None:
            if not isinstance(acqvalue, decimal.Decimal):
                raise TypeError("expected acqvalue to be a Decimal but it is a %s" % builtins.type(acqvalue))
        self.__acqvalue = acqvalue

        if age is not None:
            if not isinstance(age, str):
                raise TypeError("expected age to be a str but it is a %s" % builtins.type(age))
        self.__age = age

        if appnotes is not None:
            if not isinstance(appnotes, str):
                raise TypeError("expected appnotes to be a str but it is a %s" % builtins.type(appnotes))
        self.__appnotes = appnotes

        if appraisor is not None:
            if not isinstance(appraisor, str):
                raise TypeError("expected appraisor to be a str but it is a %s" % builtins.type(appraisor))
        self.__appraisor = appraisor

        if assemzone is not None:
            if not isinstance(assemzone, str):
                raise TypeError("expected assemzone to be a str but it is a %s" % builtins.type(assemzone))
        self.__assemzone = assemzone

        if bagno is not None:
            if not isinstance(bagno, str):
                raise TypeError("expected bagno to be a str but it is a %s" % builtins.type(bagno))
        self.__bagno = bagno

        if boxno is not None:
            if not isinstance(boxno, str):
                raise TypeError("expected boxno to be a str but it is a %s" % builtins.type(boxno))
        self.__boxno = boxno

        if caption is not None:
            if not isinstance(caption, str):
                raise TypeError("expected caption to be a str but it is a %s" % builtins.type(caption))
        self.__caption = caption

        if cat is not None:
            if not isinstance(cat, str):
                raise TypeError("expected cat to be a str but it is a %s" % builtins.type(cat))
        self.__cat = cat

        if catby is not None:
            if not isinstance(catby, str):
                raise TypeError("expected catby to be a str but it is a %s" % builtins.type(catby))
        self.__catby = catby

        if catdate is not None:
            if not isinstance(catdate, datetime.datetime):
                raise TypeError("expected catdate to be a datetime.datetime but it is a %s" % builtins.type(catdate))
        self.__catdate = catdate

        if cattype is not None:
            if not isinstance(cattype, str):
                raise TypeError("expected cattype to be a str but it is a %s" % builtins.type(cattype))
        self.__cattype = cattype

        if chemcomp is not None:
            if not isinstance(chemcomp, str):
                raise TypeError("expected chemcomp to be a str but it is a %s" % builtins.type(chemcomp))
        self.__chemcomp = chemcomp

        if circum is not None:
            if not isinstance(circum, decimal.Decimal):
                raise TypeError("expected circum to be a Decimal but it is a %s" % builtins.type(circum))
        self.__circum = circum

        if circumft is not None:
            if not isinstance(circumft, decimal.Decimal):
                raise TypeError("expected circumft to be a Decimal but it is a %s" % builtins.type(circumft))
        self.__circumft = circumft

        if circumin is not None:
            if not isinstance(circumin, decimal.Decimal):
                raise TypeError("expected circumin to be a Decimal but it is a %s" % builtins.type(circumin))
        self.__circumin = circumin

        if classes is not None:
            if not isinstance(classes, str):
                raise TypeError("expected classes to be a str but it is a %s" % builtins.type(classes))
        self.__classes = classes

        if colldate is not None:
            if not isinstance(colldate, datetime.datetime):
                raise TypeError("expected colldate to be a datetime.datetime but it is a %s" % builtins.type(colldate))
        self.__colldate = colldate

        if collection is not None:
            if not isinstance(collection, str):
                raise TypeError("expected collection to be a str but it is a %s" % builtins.type(collection))
        self.__collection = collection

        if collector is not None:
            if not isinstance(collector, str):
                raise TypeError("expected collector to be a str but it is a %s" % builtins.type(collector))
        self.__collector = collector

        if conddate is not None:
            if not isinstance(conddate, datetime.datetime):
                raise TypeError("expected conddate to be a datetime.datetime but it is a %s" % builtins.type(conddate))
        self.__conddate = conddate

        if condexam is not None:
            if not isinstance(condexam, str):
                raise TypeError("expected condexam to be a str but it is a %s" % builtins.type(condexam))
        self.__condexam = condexam

        if condition is not None:
            if not isinstance(condition, str):
                raise TypeError("expected condition to be a str but it is a %s" % builtins.type(condition))
        self.__condition = condition

        if condnotes is not None:
            if not isinstance(condnotes, str):
                raise TypeError("expected condnotes to be a str but it is a %s" % builtins.type(condnotes))
        self.__condnotes = condnotes

        if count is not None:
            if not isinstance(count, str):
                raise TypeError("expected count to be a str but it is a %s" % builtins.type(count))
        self.__count = count

        if creator is not None:
            if not isinstance(creator, str):
                raise TypeError("expected creator to be a str but it is a %s" % builtins.type(creator))
        self.__creator = creator

        if creator2 is not None:
            if not isinstance(creator2, str):
                raise TypeError("expected creator2 to be a str but it is a %s" % builtins.type(creator2))
        self.__creator2 = creator2

        if creator3 is not None:
            if not isinstance(creator3, str):
                raise TypeError("expected creator3 to be a str but it is a %s" % builtins.type(creator3))
        self.__creator3 = creator3

        if credit is not None:
            if not isinstance(credit, str):
                raise TypeError("expected credit to be a str but it is a %s" % builtins.type(credit))
        self.__credit = credit

        if crystal is not None:
            if not isinstance(crystal, str):
                raise TypeError("expected crystal to be a str but it is a %s" % builtins.type(crystal))
        self.__crystal = crystal

        if culture is not None:
            if not isinstance(culture, str):
                raise TypeError("expected culture to be a str but it is a %s" % builtins.type(culture))
        self.__culture = culture

        if curvalmax is not None:
            if not isinstance(curvalmax, decimal.Decimal):
                raise TypeError("expected curvalmax to be a Decimal but it is a %s" % builtins.type(curvalmax))
        self.__curvalmax = curvalmax

        if curvalue is not None:
            if not isinstance(curvalue, decimal.Decimal):
                raise TypeError("expected curvalue to be a Decimal but it is a %s" % builtins.type(curvalue))
        self.__curvalue = curvalue

        if dataset is not None:
            if not isinstance(dataset, str):
                raise TypeError("expected dataset to be a str but it is a %s" % builtins.type(dataset))
        self.__dataset = dataset

        if date is not None:
            if not isinstance(date, str):
                raise TypeError("expected date to be a str but it is a %s" % builtins.type(date))
        self.__date = date

        if datingmeth is not None:
            if not isinstance(datingmeth, str):
                raise TypeError("expected datingmeth to be a str but it is a %s" % builtins.type(datingmeth))
        self.__datingmeth = datingmeth

        if datum is not None:
            if not isinstance(datum, str):
                raise TypeError("expected datum to be a str but it is a %s" % builtins.type(datum))
        self.__datum = datum

        if depth is not None:
            if not isinstance(depth, decimal.Decimal):
                raise TypeError("expected depth to be a Decimal but it is a %s" % builtins.type(depth))
        self.__depth = depth

        if depthft is not None:
            if not isinstance(depthft, decimal.Decimal):
                raise TypeError("expected depthft to be a Decimal but it is a %s" % builtins.type(depthft))
        self.__depthft = depthft

        if depthin is not None:
            if not isinstance(depthin, decimal.Decimal):
                raise TypeError("expected depthin to be a Decimal but it is a %s" % builtins.type(depthin))
        self.__depthin = depthin

        if descrip is not None:
            if not isinstance(descrip, str):
                raise TypeError("expected descrip to be a str but it is a %s" % builtins.type(descrip))
        self.__descrip = descrip

        if diameter is not None:
            if not isinstance(diameter, decimal.Decimal):
                raise TypeError("expected diameter to be a Decimal but it is a %s" % builtins.type(diameter))
        self.__diameter = diameter

        if diameterft is not None:
            if not isinstance(diameterft, decimal.Decimal):
                raise TypeError("expected diameterft to be a Decimal but it is a %s" % builtins.type(diameterft))
        self.__diameterft = diameterft

        if diameterin is not None:
            if not isinstance(diameterin, decimal.Decimal):
                raise TypeError("expected diameterin to be a Decimal but it is a %s" % builtins.type(diameterin))
        self.__diameterin = diameterin

        if dimnotes is not None:
            if not isinstance(dimnotes, str):
                raise TypeError("expected dimnotes to be a str but it is a %s" % builtins.type(dimnotes))
        self.__dimnotes = dimnotes

        if dimtype is not None:
            if not isinstance(dimtype, int):
                raise TypeError("expected dimtype to be a int but it is a %s" % builtins.type(dimtype))
        self.__dimtype = dimtype

        if dispvalue is not None:
            if not isinstance(dispvalue, str):
                raise TypeError("expected dispvalue to be a str but it is a %s" % builtins.type(dispvalue))
        self.__dispvalue = dispvalue

        if earlydate is not None:
            if not isinstance(earlydate, int):
                raise TypeError("expected earlydate to be a int but it is a %s" % builtins.type(earlydate))
        self.__earlydate = earlydate

        if elements is not None:
            if not isinstance(elements, str):
                raise TypeError("expected elements to be a str but it is a %s" % builtins.type(elements))
        self.__elements = elements

        if epoch is not None:
            if not isinstance(epoch, str):
                raise TypeError("expected epoch to be a str but it is a %s" % builtins.type(epoch))
        self.__epoch = epoch

        if era is not None:
            if not isinstance(era, str):
                raise TypeError("expected era to be a str but it is a %s" % builtins.type(era))
        self.__era = era

        if event is not None:
            if not isinstance(event, str):
                raise TypeError("expected event to be a str but it is a %s" % builtins.type(event))
        self.__event = event

        if ew is not None:
            if not isinstance(ew, str):
                raise TypeError("expected ew to be a str but it is a %s" % builtins.type(ew))
        self.__ew = ew

        if excavadate is not None:
            if not isinstance(excavadate, datetime.datetime):
                raise TypeError("expected excavadate to be a datetime.datetime but it is a %s" % builtins.type(excavadate))
        self.__excavadate = excavadate

        if excavateby is not None:
            if not isinstance(excavateby, str):
                raise TypeError("expected excavateby to be a str but it is a %s" % builtins.type(excavateby))
        self.__excavateby = excavateby

        if exhibitid is not None:
            if not isinstance(exhibitid, str):
                raise TypeError("expected exhibitid to be a str but it is a %s" % builtins.type(exhibitid))
        self.__exhibitid = exhibitid

        if exhibitno is not None:
            if not isinstance(exhibitno, int):
                raise TypeError("expected exhibitno to be a int but it is a %s" % builtins.type(exhibitno))
        self.__exhibitno = exhibitno

        if exhlabel1 is not None:
            if not isinstance(exhlabel1, str):
                raise TypeError("expected exhlabel1 to be a str but it is a %s" % builtins.type(exhlabel1))
        self.__exhlabel1 = exhlabel1

        if exhlabel2 is not None:
            if not isinstance(exhlabel2, str):
                raise TypeError("expected exhlabel2 to be a str but it is a %s" % builtins.type(exhlabel2))
        self.__exhlabel2 = exhlabel2

        if exhlabel3 is not None:
            if not isinstance(exhlabel3, str):
                raise TypeError("expected exhlabel3 to be a str but it is a %s" % builtins.type(exhlabel3))
        self.__exhlabel3 = exhlabel3

        if exhlabel4 is not None:
            if not isinstance(exhlabel4, str):
                raise TypeError("expected exhlabel4 to be a str but it is a %s" % builtins.type(exhlabel4))
        self.__exhlabel4 = exhlabel4

        if exhstart is not None:
            if not isinstance(exhstart, datetime.datetime):
                raise TypeError("expected exhstart to be a datetime.datetime but it is a %s" % builtins.type(exhstart))
        self.__exhstart = exhstart

        if family is not None:
            if not isinstance(family, str):
                raise TypeError("expected family to be a str but it is a %s" % builtins.type(family))
        self.__family = family

        if feature is not None:
            if not isinstance(feature, str):
                raise TypeError("expected feature to be a str but it is a %s" % builtins.type(feature))
        self.__feature = feature

        if flagdate is not None:
            if not isinstance(flagdate, datetime.datetime):
                raise TypeError("expected flagdate to be a datetime.datetime but it is a %s" % builtins.type(flagdate))
        self.__flagdate = flagdate

        if flagnotes is not None:
            if not isinstance(flagnotes, str):
                raise TypeError("expected flagnotes to be a str but it is a %s" % builtins.type(flagnotes))
        self.__flagnotes = flagnotes

        if flagreason is not None:
            if not isinstance(flagreason, str):
                raise TypeError("expected flagreason to be a str but it is a %s" % builtins.type(flagreason))
        self.__flagreason = flagreason

        if formation is not None:
            if not isinstance(formation, str):
                raise TypeError("expected formation to be a str but it is a %s" % builtins.type(formation))
        self.__formation = formation

        if fossils is not None:
            if not isinstance(fossils, str):
                raise TypeError("expected fossils to be a str but it is a %s" % builtins.type(fossils))
        self.__fossils = fossils

        if found is not None:
            if not isinstance(found, str):
                raise TypeError("expected found to be a str but it is a %s" % builtins.type(found))
        self.__found = found

        if fracture is not None:
            if not isinstance(fracture, str):
                raise TypeError("expected fracture to be a str but it is a %s" % builtins.type(fracture))
        self.__fracture = fracture

        if frame is not None:
            if not isinstance(frame, str):
                raise TypeError("expected frame to be a str but it is a %s" % builtins.type(frame))
        self.__frame = frame

        if framesize is not None:
            if not isinstance(framesize, str):
                raise TypeError("expected framesize to be a str but it is a %s" % builtins.type(framesize))
        self.__framesize = framesize

        if genus is not None:
            if not isinstance(genus, str):
                raise TypeError("expected genus to be a str but it is a %s" % builtins.type(genus))
        self.__genus = genus

        if gparent is not None:
            if not isinstance(gparent, str):
                raise TypeError("expected gparent to be a str but it is a %s" % builtins.type(gparent))
        self.__gparent = gparent

        if grainsize is not None:
            if not isinstance(grainsize, str):
                raise TypeError("expected grainsize to be a str but it is a %s" % builtins.type(grainsize))
        self.__grainsize = grainsize

        if habitat is not None:
            if not isinstance(habitat, str):
                raise TypeError("expected habitat to be a str but it is a %s" % builtins.type(habitat))
        self.__habitat = habitat

        if hardness is not None:
            if not isinstance(hardness, str):
                raise TypeError("expected hardness to be a str but it is a %s" % builtins.type(hardness))
        self.__hardness = hardness

        if height is not None:
            if not isinstance(height, decimal.Decimal):
                raise TypeError("expected height to be a Decimal but it is a %s" % builtins.type(height))
        self.__height = height

        if heightft is not None:
            if not isinstance(heightft, decimal.Decimal):
                raise TypeError("expected heightft to be a Decimal but it is a %s" % builtins.type(heightft))
        self.__heightft = heightft

        if heightin is not None:
            if not isinstance(heightin, decimal.Decimal):
                raise TypeError("expected heightin to be a Decimal but it is a %s" % builtins.type(heightin))
        self.__heightin = heightin

        if homeloc is not None:
            if not isinstance(homeloc, str):
                raise TypeError("expected homeloc to be a str but it is a %s" % builtins.type(homeloc))
        self.__homeloc = homeloc

        if idby is not None:
            if not isinstance(idby, str):
                raise TypeError("expected idby to be a str but it is a %s" % builtins.type(idby))
        self.__idby = idby

        if iddate is not None:
            if not isinstance(iddate, datetime.datetime):
                raise TypeError("expected iddate to be a datetime.datetime but it is a %s" % builtins.type(iddate))
        self.__iddate = iddate

        if imagefile is not None:
            if not isinstance(imagefile, str):
                raise TypeError("expected imagefile to be a str but it is a %s" % builtins.type(imagefile))
        self.__imagefile = imagefile

        if imageno is not None:
            if not isinstance(imageno, int):
                raise TypeError("expected imageno to be a int but it is a %s" % builtins.type(imageno))
        self.__imageno = imageno

        if imagesize is not None:
            if not isinstance(imagesize, str):
                raise TypeError("expected imagesize to be a str but it is a %s" % builtins.type(imagesize))
        self.__imagesize = imagesize

        if inscomp is not None:
            if not isinstance(inscomp, str):
                raise TypeError("expected inscomp to be a str but it is a %s" % builtins.type(inscomp))
        self.__inscomp = inscomp

        if inscrlang is not None:
            if not isinstance(inscrlang, str):
                raise TypeError("expected inscrlang to be a str but it is a %s" % builtins.type(inscrlang))
        self.__inscrlang = inscrlang

        if inscrpos is not None:
            if not isinstance(inscrpos, str):
                raise TypeError("expected inscrpos to be a str but it is a %s" % builtins.type(inscrpos))
        self.__inscrpos = inscrpos

        if inscrtech is not None:
            if not isinstance(inscrtech, str):
                raise TypeError("expected inscrtech to be a str but it is a %s" % builtins.type(inscrtech))
        self.__inscrtech = inscrtech

        if inscrtext is not None:
            if not isinstance(inscrtext, str):
                raise TypeError("expected inscrtext to be a str but it is a %s" % builtins.type(inscrtext))
        self.__inscrtext = inscrtext

        if inscrtrans is not None:
            if not isinstance(inscrtrans, str):
                raise TypeError("expected inscrtrans to be a str but it is a %s" % builtins.type(inscrtrans))
        self.__inscrtrans = inscrtrans

        if inscrtype is not None:
            if not isinstance(inscrtype, str):
                raise TypeError("expected inscrtype to be a str but it is a %s" % builtins.type(inscrtype))
        self.__inscrtype = inscrtype

        if insdate is not None:
            if not isinstance(insdate, datetime.datetime):
                raise TypeError("expected insdate to be a datetime.datetime but it is a %s" % builtins.type(insdate))
        self.__insdate = insdate

        if insphone is not None:
            if not isinstance(insphone, str):
                raise TypeError("expected insphone to be a str but it is a %s" % builtins.type(insphone))
        self.__insphone = insphone

        if inspremium is not None:
            if not isinstance(inspremium, str):
                raise TypeError("expected inspremium to be a str but it is a %s" % builtins.type(inspremium))
        self.__inspremium = inspremium

        if insrep is not None:
            if not isinstance(insrep, str):
                raise TypeError("expected insrep to be a str but it is a %s" % builtins.type(insrep))
        self.__insrep = insrep

        if insvalue is not None:
            if not isinstance(insvalue, decimal.Decimal):
                raise TypeError("expected insvalue to be a Decimal but it is a %s" % builtins.type(insvalue))
        self.__insvalue = insvalue

        if invnby is not None:
            if not isinstance(invnby, str):
                raise TypeError("expected invnby to be a str but it is a %s" % builtins.type(invnby))
        self.__invnby = invnby

        if invndate is not None:
            if not isinstance(invndate, datetime.datetime):
                raise TypeError("expected invndate to be a datetime.datetime but it is a %s" % builtins.type(invndate))
        self.__invndate = invndate

        if kingdom is not None:
            if not isinstance(kingdom, str):
                raise TypeError("expected kingdom to be a str but it is a %s" % builtins.type(kingdom))
        self.__kingdom = kingdom

        if latdeg is not None:
            if not isinstance(latdeg, decimal.Decimal):
                raise TypeError("expected latdeg to be a Decimal but it is a %s" % builtins.type(latdeg))
        self.__latdeg = latdeg

        if latedate is not None:
            if not isinstance(latedate, int):
                raise TypeError("expected latedate to be a int but it is a %s" % builtins.type(latedate))
        self.__latedate = latedate

        if legal is not None:
            if not isinstance(legal, str):
                raise TypeError("expected legal to be a str but it is a %s" % builtins.type(legal))
        self.__legal = legal

        if length is not None:
            if not isinstance(length, decimal.Decimal):
                raise TypeError("expected length to be a Decimal but it is a %s" % builtins.type(length))
        self.__length = length

        if lengthft is not None:
            if not isinstance(lengthft, decimal.Decimal):
                raise TypeError("expected lengthft to be a Decimal but it is a %s" % builtins.type(lengthft))
        self.__lengthft = lengthft

        if lengthin is not None:
            if not isinstance(lengthin, decimal.Decimal):
                raise TypeError("expected lengthin to be a Decimal but it is a %s" % builtins.type(lengthin))
        self.__lengthin = lengthin

        if level is not None:
            if not isinstance(level, str):
                raise TypeError("expected level to be a str but it is a %s" % builtins.type(level))
        self.__level = level

        if lithofacie is not None:
            if not isinstance(lithofacie, str):
                raise TypeError("expected lithofacie to be a str but it is a %s" % builtins.type(lithofacie))
        self.__lithofacie = lithofacie

        if loancond is not None:
            if not isinstance(loancond, str):
                raise TypeError("expected loancond to be a str but it is a %s" % builtins.type(loancond))
        self.__loancond = loancond

        if loandue is not None:
            if not isinstance(loandue, datetime.datetime):
                raise TypeError("expected loandue to be a datetime.datetime but it is a %s" % builtins.type(loandue))
        self.__loandue = loandue

        if loanid is not None:
            if not isinstance(loanid, str):
                raise TypeError("expected loanid to be a str but it is a %s" % builtins.type(loanid))
        self.__loanid = loanid

        if loaninno is not None:
            if not isinstance(loaninno, str):
                raise TypeError("expected loaninno to be a str but it is a %s" % builtins.type(loaninno))
        self.__loaninno = loaninno

        if loanno is not None:
            if not isinstance(loanno, int):
                raise TypeError("expected loanno to be a int but it is a %s" % builtins.type(loanno))
        self.__loanno = loanno

        if loanrenew is not None:
            if not isinstance(loanrenew, datetime.datetime):
                raise TypeError("expected loanrenew to be a datetime.datetime but it is a %s" % builtins.type(loanrenew))
        self.__loanrenew = loanrenew

        if locfield1 is not None:
            if not isinstance(locfield1, str):
                raise TypeError("expected locfield1 to be a str but it is a %s" % builtins.type(locfield1))
        self.__locfield1 = locfield1

        if locfield2 is not None:
            if not isinstance(locfield2, str):
                raise TypeError("expected locfield2 to be a str but it is a %s" % builtins.type(locfield2))
        self.__locfield2 = locfield2

        if locfield3 is not None:
            if not isinstance(locfield3, str):
                raise TypeError("expected locfield3 to be a str but it is a %s" % builtins.type(locfield3))
        self.__locfield3 = locfield3

        if locfield4 is not None:
            if not isinstance(locfield4, str):
                raise TypeError("expected locfield4 to be a str but it is a %s" % builtins.type(locfield4))
        self.__locfield4 = locfield4

        if locfield5 is not None:
            if not isinstance(locfield5, str):
                raise TypeError("expected locfield5 to be a str but it is a %s" % builtins.type(locfield5))
        self.__locfield5 = locfield5

        if locfield6 is not None:
            if not isinstance(locfield6, str):
                raise TypeError("expected locfield6 to be a str but it is a %s" % builtins.type(locfield6))
        self.__locfield6 = locfield6

        if longdeg is not None:
            if not isinstance(longdeg, decimal.Decimal):
                raise TypeError("expected longdeg to be a Decimal but it is a %s" % builtins.type(longdeg))
        self.__longdeg = longdeg

        if luster is not None:
            if not isinstance(luster, str):
                raise TypeError("expected luster to be a str but it is a %s" % builtins.type(luster))
        self.__luster = luster

        if made is not None:
            if not isinstance(made, str):
                raise TypeError("expected made to be a str but it is a %s" % builtins.type(made))
        self.__made = made

        if maintcycle is not None:
            if not isinstance(maintcycle, str):
                raise TypeError("expected maintcycle to be a str but it is a %s" % builtins.type(maintcycle))
        self.__maintcycle = maintcycle

        if maintdate is not None:
            if not isinstance(maintdate, datetime.datetime):
                raise TypeError("expected maintdate to be a datetime.datetime but it is a %s" % builtins.type(maintdate))
        self.__maintdate = maintdate

        if maintnote is not None:
            if not isinstance(maintnote, str):
                raise TypeError("expected maintnote to be a str but it is a %s" % builtins.type(maintnote))
        self.__maintnote = maintnote

        if material is not None:
            if not isinstance(material, str):
                raise TypeError("expected material to be a str but it is a %s" % builtins.type(material))
        self.__material = material

        if medium is not None:
            if not isinstance(medium, str):
                raise TypeError("expected medium to be a str but it is a %s" % builtins.type(medium))
        self.__medium = medium

        if member is not None:
            if not isinstance(member, str):
                raise TypeError("expected member to be a str but it is a %s" % builtins.type(member))
        self.__member = member

        if mmark is not None:
            if not isinstance(mmark, str):
                raise TypeError("expected mmark to be a str but it is a %s" % builtins.type(mmark))
        self.__mmark = mmark

        if nhclass is not None:
            if not isinstance(nhclass, str):
                raise TypeError("expected nhclass to be a str but it is a %s" % builtins.type(nhclass))
        self.__nhclass = nhclass

        if nhorder is not None:
            if not isinstance(nhorder, str):
                raise TypeError("expected nhorder to be a str but it is a %s" % builtins.type(nhorder))
        self.__nhorder = nhorder

        if notes is not None:
            if not isinstance(notes, str):
                raise TypeError("expected notes to be a str but it is a %s" % builtins.type(notes))
        self.__notes = notes

        if ns is not None:
            if not isinstance(ns, str):
                raise TypeError("expected ns to be a str but it is a %s" % builtins.type(ns))
        self.__ns = ns

        if objectid is not None:
            if not isinstance(objectid, str):
                raise TypeError("expected objectid to be a str but it is a %s" % builtins.type(objectid))
        self.__objectid = objectid

        if objname is not None:
            if not isinstance(objname, str):
                raise TypeError("expected objname to be a str but it is a %s" % builtins.type(objname))
        self.__objname = objname

        if objname2 is not None:
            if not isinstance(objname2, str):
                raise TypeError("expected objname2 to be a str but it is a %s" % builtins.type(objname2))
        self.__objname2 = objname2

        if objname3 is not None:
            if not isinstance(objname3, str):
                raise TypeError("expected objname3 to be a str but it is a %s" % builtins.type(objname3))
        self.__objname3 = objname3

        if objnames is not None:
            if not isinstance(objnames, str):
                raise TypeError("expected objnames to be a str but it is a %s" % builtins.type(objnames))
        self.__objnames = objnames

        if occurrence is not None:
            if not isinstance(occurrence, str):
                raise TypeError("expected occurrence to be a str but it is a %s" % builtins.type(occurrence))
        self.__occurrence = occurrence

        if oldno is not None:
            if not isinstance(oldno, str):
                raise TypeError("expected oldno to be a str but it is a %s" % builtins.type(oldno))
        self.__oldno = oldno

        if origin is not None:
            if not isinstance(origin, str):
                raise TypeError("expected origin to be a str but it is a %s" % builtins.type(origin))
        self.__origin = origin

        if othername is not None:
            if not isinstance(othername, str):
                raise TypeError("expected othername to be a str but it is a %s" % builtins.type(othername))
        self.__othername = othername

        if otherno is not None:
            if not isinstance(otherno, str):
                raise TypeError("expected otherno to be a str but it is a %s" % builtins.type(otherno))
        self.__otherno = otherno

        if outdate is not None:
            if not isinstance(outdate, datetime.datetime):
                raise TypeError("expected outdate to be a datetime.datetime but it is a %s" % builtins.type(outdate))
        self.__outdate = outdate

        if owned is not None:
            if not isinstance(owned, str):
                raise TypeError("expected owned to be a str but it is a %s" % builtins.type(owned))
        self.__owned = owned

        if parent is not None:
            if not isinstance(parent, str):
                raise TypeError("expected parent to be a str but it is a %s" % builtins.type(parent))
        self.__parent = parent

        if people is not None:
            if not isinstance(people, str):
                raise TypeError("expected people to be a str but it is a %s" % builtins.type(people))
        self.__people = people

        if period is not None:
            if not isinstance(period, str):
                raise TypeError("expected period to be a str but it is a %s" % builtins.type(period))
        self.__period = period

        if phylum is not None:
            if not isinstance(phylum, str):
                raise TypeError("expected phylum to be a str but it is a %s" % builtins.type(phylum))
        self.__phylum = phylum

        if policyno is not None:
            if not isinstance(policyno, str):
                raise TypeError("expected policyno to be a str but it is a %s" % builtins.type(policyno))
        self.__policyno = policyno

        if ppid is not None:
            if not isinstance(ppid, str):
                raise TypeError("expected ppid to be a str but it is a %s" % builtins.type(ppid))
        self.__ppid = ppid

        if preparator is not None:
            if not isinstance(preparator, str):
                raise TypeError("expected preparator to be a str but it is a %s" % builtins.type(preparator))
        self.__preparator = preparator

        if prepdate is not None:
            if not isinstance(prepdate, datetime.datetime):
                raise TypeError("expected prepdate to be a datetime.datetime but it is a %s" % builtins.type(prepdate))
        self.__prepdate = prepdate

        if preserve is not None:
            if not isinstance(preserve, str):
                raise TypeError("expected preserve to be a str but it is a %s" % builtins.type(preserve))
        self.__preserve = preserve

        if pressure is not None:
            if not isinstance(pressure, str):
                raise TypeError("expected pressure to be a str but it is a %s" % builtins.type(pressure))
        self.__pressure = pressure

        if provenance is not None:
            if not isinstance(provenance, str):
                raise TypeError("expected provenance to be a str but it is a %s" % builtins.type(provenance))
        self.__provenance = provenance

        if pubnotes is not None:
            if not isinstance(pubnotes, str):
                raise TypeError("expected pubnotes to be a str but it is a %s" % builtins.type(pubnotes))
        self.__pubnotes = pubnotes

        if qrurl is not None:
            if not isinstance(qrurl, str):
                raise TypeError("expected qrurl to be a str but it is a %s" % builtins.type(qrurl))
        self.__qrurl = qrurl

        if recas is not None:
            if not isinstance(recas, str):
                raise TypeError("expected recas to be a str but it is a %s" % builtins.type(recas))
        self.__recas = recas

        if recdate is not None:
            if not isinstance(recdate, str):
                raise TypeError("expected recdate to be a str but it is a %s" % builtins.type(recdate))
        self.__recdate = recdate

        if recfrom is not None:
            if not isinstance(recfrom, str):
                raise TypeError("expected recfrom to be a str but it is a %s" % builtins.type(recfrom))
        self.__recfrom = recfrom

        if relation is not None:
            if not isinstance(relation, str):
                raise TypeError("expected relation to be a str but it is a %s" % builtins.type(relation))
        self.__relation = relation

        if relnotes is not None:
            if not isinstance(relnotes, str):
                raise TypeError("expected relnotes to be a str but it is a %s" % builtins.type(relnotes))
        self.__relnotes = relnotes

        if renewuntil is not None:
            if not isinstance(renewuntil, datetime.datetime):
                raise TypeError("expected renewuntil to be a datetime.datetime but it is a %s" % builtins.type(renewuntil))
        self.__renewuntil = renewuntil

        if repatby is not None:
            if not isinstance(repatby, str):
                raise TypeError("expected repatby to be a str but it is a %s" % builtins.type(repatby))
        self.__repatby = repatby

        if repatclaim is not None:
            if not isinstance(repatclaim, str):
                raise TypeError("expected repatclaim to be a str but it is a %s" % builtins.type(repatclaim))
        self.__repatclaim = repatclaim

        if repatdate is not None:
            if not isinstance(repatdate, datetime.datetime):
                raise TypeError("expected repatdate to be a datetime.datetime but it is a %s" % builtins.type(repatdate))
        self.__repatdate = repatdate

        if repatdisp is not None:
            if not isinstance(repatdisp, str):
                raise TypeError("expected repatdisp to be a str but it is a %s" % builtins.type(repatdisp))
        self.__repatdisp = repatdisp

        if repathand is not None:
            if not isinstance(repathand, str):
                raise TypeError("expected repathand to be a str but it is a %s" % builtins.type(repathand))
        self.__repathand = repathand

        if repatnotes is not None:
            if not isinstance(repatnotes, str):
                raise TypeError("expected repatnotes to be a str but it is a %s" % builtins.type(repatnotes))
        self.__repatnotes = repatnotes

        if repatnotic is not None:
            if not isinstance(repatnotic, datetime.datetime):
                raise TypeError("expected repatnotic to be a datetime.datetime but it is a %s" % builtins.type(repatnotic))
        self.__repatnotic = repatnotic

        if repattype is not None:
            if not isinstance(repattype, str):
                raise TypeError("expected repattype to be a str but it is a %s" % builtins.type(repattype))
        self.__repattype = repattype

        if rockclass is not None:
            if not isinstance(rockclass, str):
                raise TypeError("expected rockclass to be a str but it is a %s" % builtins.type(rockclass))
        self.__rockclass = rockclass

        if rockcolor is not None:
            if not isinstance(rockcolor, str):
                raise TypeError("expected rockcolor to be a str but it is a %s" % builtins.type(rockcolor))
        self.__rockcolor = rockcolor

        if rockorigin is not None:
            if not isinstance(rockorigin, str):
                raise TypeError("expected rockorigin to be a str but it is a %s" % builtins.type(rockorigin))
        self.__rockorigin = rockorigin

        if rocktype is not None:
            if not isinstance(rocktype, str):
                raise TypeError("expected rocktype to be a str but it is a %s" % builtins.type(rocktype))
        self.__rocktype = rocktype

        if role is not None:
            if not isinstance(role, str):
                raise TypeError("expected role to be a str but it is a %s" % builtins.type(role))
        self.__role = role

        if role2 is not None:
            if not isinstance(role2, str):
                raise TypeError("expected role2 to be a str but it is a %s" % builtins.type(role2))
        self.__role2 = role2

        if role3 is not None:
            if not isinstance(role3, str):
                raise TypeError("expected role3 to be a str but it is a %s" % builtins.type(role3))
        self.__role3 = role3

        if school is not None:
            if not isinstance(school, str):
                raise TypeError("expected school to be a str but it is a %s" % builtins.type(school))
        self.__school = school

        if sex is not None:
            if not isinstance(sex, str):
                raise TypeError("expected sex to be a str but it is a %s" % builtins.type(sex))
        self.__sex = sex

        if sgflag is not None:
            if not isinstance(sgflag, str):
                raise TypeError("expected sgflag to be a str but it is a %s" % builtins.type(sgflag))
        self.__sgflag = sgflag

        if signedname is not None:
            if not isinstance(signedname, str):
                raise TypeError("expected signedname to be a str but it is a %s" % builtins.type(signedname))
        self.__signedname = signedname

        if signloc is not None:
            if not isinstance(signloc, str):
                raise TypeError("expected signloc to be a str but it is a %s" % builtins.type(signloc))
        self.__signloc = signloc

        if site is not None:
            if not isinstance(site, str):
                raise TypeError("expected site to be a str but it is a %s" % builtins.type(site))
        self.__site = site

        if siteno is not None:
            if not isinstance(siteno, str):
                raise TypeError("expected siteno to be a str but it is a %s" % builtins.type(siteno))
        self.__siteno = siteno

        if specgrav is not None:
            if not isinstance(specgrav, str):
                raise TypeError("expected specgrav to be a str but it is a %s" % builtins.type(specgrav))
        self.__specgrav = specgrav

        if species is not None:
            if not isinstance(species, str):
                raise TypeError("expected species to be a str but it is a %s" % builtins.type(species))
        self.__species = species

        if sprocess is not None:
            if not isinstance(sprocess, str):
                raise TypeError("expected sprocess to be a str but it is a %s" % builtins.type(sprocess))
        self.__sprocess = sprocess

        if stage is not None:
            if not isinstance(stage, str):
                raise TypeError("expected stage to be a str but it is a %s" % builtins.type(stage))
        self.__stage = stage

        if status is not None:
            if not isinstance(status, str):
                raise TypeError("expected status to be a str but it is a %s" % builtins.type(status))
        self.__status = status

        if statusby is not None:
            if not isinstance(statusby, str):
                raise TypeError("expected statusby to be a str but it is a %s" % builtins.type(statusby))
        self.__statusby = statusby

        if statusdate is not None:
            if not isinstance(statusdate, datetime.datetime):
                raise TypeError("expected statusdate to be a datetime.datetime but it is a %s" % builtins.type(statusdate))
        self.__statusdate = statusdate

        if sterms is not None:
            if not isinstance(sterms, str):
                raise TypeError("expected sterms to be a str but it is a %s" % builtins.type(sterms))
        self.__sterms = sterms

        if stratum is not None:
            if not isinstance(stratum, str):
                raise TypeError("expected stratum to be a str but it is a %s" % builtins.type(stratum))
        self.__stratum = stratum

        if streak is not None:
            if not isinstance(streak, str):
                raise TypeError("expected streak to be a str but it is a %s" % builtins.type(streak))
        self.__streak = streak

        if subfamily is not None:
            if not isinstance(subfamily, str):
                raise TypeError("expected subfamily to be a str but it is a %s" % builtins.type(subfamily))
        self.__subfamily = subfamily

        if subjects is not None:
            if not isinstance(subjects, str):
                raise TypeError("expected subjects to be a str but it is a %s" % builtins.type(subjects))
        self.__subjects = subjects

        if subspecies is not None:
            if not isinstance(subspecies, str):
                raise TypeError("expected subspecies to be a str but it is a %s" % builtins.type(subspecies))
        self.__subspecies = subspecies

        if technique is not None:
            if not isinstance(technique, str):
                raise TypeError("expected technique to be a str but it is a %s" % builtins.type(technique))
        self.__technique = technique

        if tempauthor is not None:
            if not isinstance(tempauthor, str):
                raise TypeError("expected tempauthor to be a str but it is a %s" % builtins.type(tempauthor))
        self.__tempauthor = tempauthor

        if tempby is not None:
            if not isinstance(tempby, str):
                raise TypeError("expected tempby to be a str but it is a %s" % builtins.type(tempby))
        self.__tempby = tempby

        if tempdate is not None:
            if not isinstance(tempdate, datetime.datetime):
                raise TypeError("expected tempdate to be a datetime.datetime but it is a %s" % builtins.type(tempdate))
        self.__tempdate = tempdate

        if temperatur is not None:
            if not isinstance(temperatur, str):
                raise TypeError("expected temperatur to be a str but it is a %s" % builtins.type(temperatur))
        self.__temperatur = temperatur

        if temploc is not None:
            if not isinstance(temploc, str):
                raise TypeError("expected temploc to be a str but it is a %s" % builtins.type(temploc))
        self.__temploc = temploc

        if tempnotes is not None:
            if not isinstance(tempnotes, str):
                raise TypeError("expected tempnotes to be a str but it is a %s" % builtins.type(tempnotes))
        self.__tempnotes = tempnotes

        if tempreason is not None:
            if not isinstance(tempreason, str):
                raise TypeError("expected tempreason to be a str but it is a %s" % builtins.type(tempreason))
        self.__tempreason = tempreason

        if tempuntil is not None:
            if not isinstance(tempuntil, str):
                raise TypeError("expected tempuntil to be a str but it is a %s" % builtins.type(tempuntil))
        self.__tempuntil = tempuntil

        if texture is not None:
            if not isinstance(texture, str):
                raise TypeError("expected texture to be a str but it is a %s" % builtins.type(texture))
        self.__texture = texture

        if title is not None:
            if not isinstance(title, str):
                raise TypeError("expected title to be a str but it is a %s" % builtins.type(title))
        self.__title = title

        if tlocfield1 is not None:
            if not isinstance(tlocfield1, str):
                raise TypeError("expected tlocfield1 to be a str but it is a %s" % builtins.type(tlocfield1))
        self.__tlocfield1 = tlocfield1

        if tlocfield2 is not None:
            if not isinstance(tlocfield2, str):
                raise TypeError("expected tlocfield2 to be a str but it is a %s" % builtins.type(tlocfield2))
        self.__tlocfield2 = tlocfield2

        if tlocfield3 is not None:
            if not isinstance(tlocfield3, str):
                raise TypeError("expected tlocfield3 to be a str but it is a %s" % builtins.type(tlocfield3))
        self.__tlocfield3 = tlocfield3

        if tlocfield4 is not None:
            if not isinstance(tlocfield4, str):
                raise TypeError("expected tlocfield4 to be a str but it is a %s" % builtins.type(tlocfield4))
        self.__tlocfield4 = tlocfield4

        if tlocfield5 is not None:
            if not isinstance(tlocfield5, str):
                raise TypeError("expected tlocfield5 to be a str but it is a %s" % builtins.type(tlocfield5))
        self.__tlocfield5 = tlocfield5

        if tlocfield6 is not None:
            if not isinstance(tlocfield6, str):
                raise TypeError("expected tlocfield6 to be a str but it is a %s" % builtins.type(tlocfield6))
        self.__tlocfield6 = tlocfield6

        if udf1 is not None:
            if not isinstance(udf1, str):
                raise TypeError("expected udf1 to be a str but it is a %s" % builtins.type(udf1))
        self.__udf1 = udf1

        if udf10 is not None:
            if not isinstance(udf10, str):
                raise TypeError("expected udf10 to be a str but it is a %s" % builtins.type(udf10))
        self.__udf10 = udf10

        if udf11 is not None:
            if not isinstance(udf11, str):
                raise TypeError("expected udf11 to be a str but it is a %s" % builtins.type(udf11))
        self.__udf11 = udf11

        if udf12 is not None:
            if not isinstance(udf12, str):
                raise TypeError("expected udf12 to be a str but it is a %s" % builtins.type(udf12))
        self.__udf12 = udf12

        if udf13 is not None:
            if not isinstance(udf13, int):
                raise TypeError("expected udf13 to be a int but it is a %s" % builtins.type(udf13))
        self.__udf13 = udf13

        if udf14 is not None:
            if not isinstance(udf14, decimal.Decimal):
                raise TypeError("expected udf14 to be a Decimal but it is a %s" % builtins.type(udf14))
        self.__udf14 = udf14

        if udf15 is not None:
            if not isinstance(udf15, decimal.Decimal):
                raise TypeError("expected udf15 to be a Decimal but it is a %s" % builtins.type(udf15))
        self.__udf15 = udf15

        if udf16 is not None:
            if not isinstance(udf16, decimal.Decimal):
                raise TypeError("expected udf16 to be a Decimal but it is a %s" % builtins.type(udf16))
        self.__udf16 = udf16

        if udf17 is not None:
            if not isinstance(udf17, decimal.Decimal):
                raise TypeError("expected udf17 to be a Decimal but it is a %s" % builtins.type(udf17))
        self.__udf17 = udf17

        if udf18 is not None:
            if not isinstance(udf18, datetime.datetime):
                raise TypeError("expected udf18 to be a datetime.datetime but it is a %s" % builtins.type(udf18))
        self.__udf18 = udf18

        if udf19 is not None:
            if not isinstance(udf19, datetime.datetime):
                raise TypeError("expected udf19 to be a datetime.datetime but it is a %s" % builtins.type(udf19))
        self.__udf19 = udf19

        if udf2 is not None:
            if not isinstance(udf2, str):
                raise TypeError("expected udf2 to be a str but it is a %s" % builtins.type(udf2))
        self.__udf2 = udf2

        if udf20 is not None:
            if not isinstance(udf20, datetime.datetime):
                raise TypeError("expected udf20 to be a datetime.datetime but it is a %s" % builtins.type(udf20))
        self.__udf20 = udf20

        if udf21 is not None:
            if not isinstance(udf21, str):
                raise TypeError("expected udf21 to be a str but it is a %s" % builtins.type(udf21))
        self.__udf21 = udf21

        if udf22 is not None:
            if not isinstance(udf22, str):
                raise TypeError("expected udf22 to be a str but it is a %s" % builtins.type(udf22))
        self.__udf22 = udf22

        if udf3 is not None:
            if not isinstance(udf3, str):
                raise TypeError("expected udf3 to be a str but it is a %s" % builtins.type(udf3))
        self.__udf3 = udf3

        if udf4 is not None:
            if not isinstance(udf4, str):
                raise TypeError("expected udf4 to be a str but it is a %s" % builtins.type(udf4))
        self.__udf4 = udf4

        if udf5 is not None:
            if not isinstance(udf5, str):
                raise TypeError("expected udf5 to be a str but it is a %s" % builtins.type(udf5))
        self.__udf5 = udf5

        if udf6 is not None:
            if not isinstance(udf6, str):
                raise TypeError("expected udf6 to be a str but it is a %s" % builtins.type(udf6))
        self.__udf6 = udf6

        if udf7 is not None:
            if not isinstance(udf7, str):
                raise TypeError("expected udf7 to be a str but it is a %s" % builtins.type(udf7))
        self.__udf7 = udf7

        if udf8 is not None:
            if not isinstance(udf8, str):
                raise TypeError("expected udf8 to be a str but it is a %s" % builtins.type(udf8))
        self.__udf8 = udf8

        if udf9 is not None:
            if not isinstance(udf9, str):
                raise TypeError("expected udf9 to be a str but it is a %s" % builtins.type(udf9))
        self.__udf9 = udf9

        if unit is not None:
            if not isinstance(unit, str):
                raise TypeError("expected unit to be a str but it is a %s" % builtins.type(unit))
        self.__unit = unit

        if updated is not None:
            if not isinstance(updated, datetime.datetime):
                raise TypeError("expected updated to be a datetime.datetime but it is a %s" % builtins.type(updated))
        self.__updated = updated

        if updatedby is not None:
            if not isinstance(updatedby, str):
                raise TypeError("expected updatedby to be a str but it is a %s" % builtins.type(updatedby))
        self.__updatedby = updatedby

        if used is not None:
            if not isinstance(used, str):
                raise TypeError("expected used to be a str but it is a %s" % builtins.type(used))
        self.__used = used

        if valuedate is not None:
            if not isinstance(valuedate, datetime.datetime):
                raise TypeError("expected valuedate to be a datetime.datetime but it is a %s" % builtins.type(valuedate))
        self.__valuedate = valuedate

        if varieties is not None:
            if not isinstance(varieties, str):
                raise TypeError("expected varieties to be a str but it is a %s" % builtins.type(varieties))
        self.__varieties = varieties

        if vexhtml is not None:
            if not isinstance(vexhtml, str):
                raise TypeError("expected vexhtml to be a str but it is a %s" % builtins.type(vexhtml))
        self.__vexhtml = vexhtml

        if vexlabel1 is not None:
            if not isinstance(vexlabel1, str):
                raise TypeError("expected vexlabel1 to be a str but it is a %s" % builtins.type(vexlabel1))
        self.__vexlabel1 = vexlabel1

        if vexlabel2 is not None:
            if not isinstance(vexlabel2, str):
                raise TypeError("expected vexlabel2 to be a str but it is a %s" % builtins.type(vexlabel2))
        self.__vexlabel2 = vexlabel2

        if vexlabel3 is not None:
            if not isinstance(vexlabel3, str):
                raise TypeError("expected vexlabel3 to be a str but it is a %s" % builtins.type(vexlabel3))
        self.__vexlabel3 = vexlabel3

        if vexlabel4 is not None:
            if not isinstance(vexlabel4, str):
                raise TypeError("expected vexlabel4 to be a str but it is a %s" % builtins.type(vexlabel4))
        self.__vexlabel4 = vexlabel4

        if webinclude is not None:
            if not isinstance(webinclude, bool):
                raise TypeError("expected webinclude to be a bool but it is a %s" % builtins.type(webinclude))
        self.__webinclude = webinclude

        if weight is not None:
            if not isinstance(weight, decimal.Decimal):
                raise TypeError("expected weight to be a Decimal but it is a %s" % builtins.type(weight))
        self.__weight = weight

        if weightin is not None:
            if not isinstance(weightin, decimal.Decimal):
                raise TypeError("expected weightin to be a Decimal but it is a %s" % builtins.type(weightin))
        self.__weightin = weightin

        if weightlb is not None:
            if not isinstance(weightlb, decimal.Decimal):
                raise TypeError("expected weightlb to be a Decimal but it is a %s" % builtins.type(weightlb))
        self.__weightlb = weightlb

        if width is not None:
            if not isinstance(width, decimal.Decimal):
                raise TypeError("expected width to be a Decimal but it is a %s" % builtins.type(width))
        self.__width = width

        if widthft is not None:
            if not isinstance(widthft, decimal.Decimal):
                raise TypeError("expected widthft to be a Decimal but it is a %s" % builtins.type(widthft))
        self.__widthft = widthft

        if widthin is not None:
            if not isinstance(widthin, decimal.Decimal):
                raise TypeError("expected widthin to be a Decimal but it is a %s" % builtins.type(widthin))
        self.__widthin = widthin

        if xcord is not None:
            if not isinstance(xcord, decimal.Decimal):
                raise TypeError("expected xcord to be a Decimal but it is a %s" % builtins.type(xcord))
        self.__xcord = xcord

        if ycord is not None:
            if not isinstance(ycord, decimal.Decimal):
                raise TypeError("expected ycord to be a Decimal but it is a %s" % builtins.type(ycord))
        self.__ycord = ycord

        if zcord is not None:
            if not isinstance(zcord, decimal.Decimal):
                raise TypeError("expected zcord to be a Decimal but it is a %s" % builtins.type(zcord))
        self.__zcord = zcord

        if zsorter is not None:
            if not isinstance(zsorter, str):
                raise TypeError("expected zsorter to be a str but it is a %s" % builtins.type(zsorter))
        self.__zsorter = zsorter

        if zsorterx is not None:
            if not isinstance(zsorterx, str):
                raise TypeError("expected zsorterx to be a str but it is a %s" % builtins.type(zsorterx))
        self.__zsorterx = zsorterx

    def __eq__(self, other):
        if self.accessno != other.accessno:
            return False
        if self.accessory != other.accessory:
            return False
        if self.acqvalue != other.acqvalue:
            return False
        if self.age != other.age:
            return False
        if self.appnotes != other.appnotes:
            return False
        if self.appraisor != other.appraisor:
            return False
        if self.assemzone != other.assemzone:
            return False
        if self.bagno != other.bagno:
            return False
        if self.boxno != other.boxno:
            return False
        if self.caption != other.caption:
            return False
        if self.cat != other.cat:
            return False
        if self.catby != other.catby:
            return False
        if self.catdate != other.catdate:
            return False
        if self.cattype != other.cattype:
            return False
        if self.chemcomp != other.chemcomp:
            return False
        if self.circum != other.circum:
            return False
        if self.circumft != other.circumft:
            return False
        if self.circumin != other.circumin:
            return False
        if self.classes != other.classes:
            return False
        if self.colldate != other.colldate:
            return False
        if self.collection != other.collection:
            return False
        if self.collector != other.collector:
            return False
        if self.conddate != other.conddate:
            return False
        if self.condexam != other.condexam:
            return False
        if self.condition != other.condition:
            return False
        if self.condnotes != other.condnotes:
            return False
        if self.count != other.count:
            return False
        if self.creator != other.creator:
            return False
        if self.creator2 != other.creator2:
            return False
        if self.creator3 != other.creator3:
            return False
        if self.credit != other.credit:
            return False
        if self.crystal != other.crystal:
            return False
        if self.culture != other.culture:
            return False
        if self.curvalmax != other.curvalmax:
            return False
        if self.curvalue != other.curvalue:
            return False
        if self.dataset != other.dataset:
            return False
        if self.date != other.date:
            return False
        if self.datingmeth != other.datingmeth:
            return False
        if self.datum != other.datum:
            return False
        if self.depth != other.depth:
            return False
        if self.depthft != other.depthft:
            return False
        if self.depthin != other.depthin:
            return False
        if self.descrip != other.descrip:
            return False
        if self.diameter != other.diameter:
            return False
        if self.diameterft != other.diameterft:
            return False
        if self.diameterin != other.diameterin:
            return False
        if self.dimnotes != other.dimnotes:
            return False
        if self.dimtype != other.dimtype:
            return False
        if self.dispvalue != other.dispvalue:
            return False
        if self.earlydate != other.earlydate:
            return False
        if self.elements != other.elements:
            return False
        if self.epoch != other.epoch:
            return False
        if self.era != other.era:
            return False
        if self.event != other.event:
            return False
        if self.ew != other.ew:
            return False
        if self.excavadate != other.excavadate:
            return False
        if self.excavateby != other.excavateby:
            return False
        if self.exhibitid != other.exhibitid:
            return False
        if self.exhibitno != other.exhibitno:
            return False
        if self.exhlabel1 != other.exhlabel1:
            return False
        if self.exhlabel2 != other.exhlabel2:
            return False
        if self.exhlabel3 != other.exhlabel3:
            return False
        if self.exhlabel4 != other.exhlabel4:
            return False
        if self.exhstart != other.exhstart:
            return False
        if self.family != other.family:
            return False
        if self.feature != other.feature:
            return False
        if self.flagdate != other.flagdate:
            return False
        if self.flagnotes != other.flagnotes:
            return False
        if self.flagreason != other.flagreason:
            return False
        if self.formation != other.formation:
            return False
        if self.fossils != other.fossils:
            return False
        if self.found != other.found:
            return False
        if self.fracture != other.fracture:
            return False
        if self.frame != other.frame:
            return False
        if self.framesize != other.framesize:
            return False
        if self.genus != other.genus:
            return False
        if self.gparent != other.gparent:
            return False
        if self.grainsize != other.grainsize:
            return False
        if self.habitat != other.habitat:
            return False
        if self.hardness != other.hardness:
            return False
        if self.height != other.height:
            return False
        if self.heightft != other.heightft:
            return False
        if self.heightin != other.heightin:
            return False
        if self.homeloc != other.homeloc:
            return False
        if self.idby != other.idby:
            return False
        if self.iddate != other.iddate:
            return False
        if self.imagefile != other.imagefile:
            return False
        if self.imageno != other.imageno:
            return False
        if self.imagesize != other.imagesize:
            return False
        if self.inscomp != other.inscomp:
            return False
        if self.inscrlang != other.inscrlang:
            return False
        if self.inscrpos != other.inscrpos:
            return False
        if self.inscrtech != other.inscrtech:
            return False
        if self.inscrtext != other.inscrtext:
            return False
        if self.inscrtrans != other.inscrtrans:
            return False
        if self.inscrtype != other.inscrtype:
            return False
        if self.insdate != other.insdate:
            return False
        if self.insphone != other.insphone:
            return False
        if self.inspremium != other.inspremium:
            return False
        if self.insrep != other.insrep:
            return False
        if self.insvalue != other.insvalue:
            return False
        if self.invnby != other.invnby:
            return False
        if self.invndate != other.invndate:
            return False
        if self.kingdom != other.kingdom:
            return False
        if self.latdeg != other.latdeg:
            return False
        if self.latedate != other.latedate:
            return False
        if self.legal != other.legal:
            return False
        if self.length != other.length:
            return False
        if self.lengthft != other.lengthft:
            return False
        if self.lengthin != other.lengthin:
            return False
        if self.level != other.level:
            return False
        if self.lithofacie != other.lithofacie:
            return False
        if self.loancond != other.loancond:
            return False
        if self.loandue != other.loandue:
            return False
        if self.loanid != other.loanid:
            return False
        if self.loaninno != other.loaninno:
            return False
        if self.loanno != other.loanno:
            return False
        if self.loanrenew != other.loanrenew:
            return False
        if self.locfield1 != other.locfield1:
            return False
        if self.locfield2 != other.locfield2:
            return False
        if self.locfield3 != other.locfield3:
            return False
        if self.locfield4 != other.locfield4:
            return False
        if self.locfield5 != other.locfield5:
            return False
        if self.locfield6 != other.locfield6:
            return False
        if self.longdeg != other.longdeg:
            return False
        if self.luster != other.luster:
            return False
        if self.made != other.made:
            return False
        if self.maintcycle != other.maintcycle:
            return False
        if self.maintdate != other.maintdate:
            return False
        if self.maintnote != other.maintnote:
            return False
        if self.material != other.material:
            return False
        if self.medium != other.medium:
            return False
        if self.member != other.member:
            return False
        if self.mmark != other.mmark:
            return False
        if self.nhclass != other.nhclass:
            return False
        if self.nhorder != other.nhorder:
            return False
        if self.notes != other.notes:
            return False
        if self.ns != other.ns:
            return False
        if self.objectid != other.objectid:
            return False
        if self.objname != other.objname:
            return False
        if self.objname2 != other.objname2:
            return False
        if self.objname3 != other.objname3:
            return False
        if self.objnames != other.objnames:
            return False
        if self.occurrence != other.occurrence:
            return False
        if self.oldno != other.oldno:
            return False
        if self.origin != other.origin:
            return False
        if self.othername != other.othername:
            return False
        if self.otherno != other.otherno:
            return False
        if self.outdate != other.outdate:
            return False
        if self.owned != other.owned:
            return False
        if self.parent != other.parent:
            return False
        if self.people != other.people:
            return False
        if self.period != other.period:
            return False
        if self.phylum != other.phylum:
            return False
        if self.policyno != other.policyno:
            return False
        if self.ppid != other.ppid:
            return False
        if self.preparator != other.preparator:
            return False
        if self.prepdate != other.prepdate:
            return False
        if self.preserve != other.preserve:
            return False
        if self.pressure != other.pressure:
            return False
        if self.provenance != other.provenance:
            return False
        if self.pubnotes != other.pubnotes:
            return False
        if self.qrurl != other.qrurl:
            return False
        if self.recas != other.recas:
            return False
        if self.recdate != other.recdate:
            return False
        if self.recfrom != other.recfrom:
            return False
        if self.relation != other.relation:
            return False
        if self.relnotes != other.relnotes:
            return False
        if self.renewuntil != other.renewuntil:
            return False
        if self.repatby != other.repatby:
            return False
        if self.repatclaim != other.repatclaim:
            return False
        if self.repatdate != other.repatdate:
            return False
        if self.repatdisp != other.repatdisp:
            return False
        if self.repathand != other.repathand:
            return False
        if self.repatnotes != other.repatnotes:
            return False
        if self.repatnotic != other.repatnotic:
            return False
        if self.repattype != other.repattype:
            return False
        if self.rockclass != other.rockclass:
            return False
        if self.rockcolor != other.rockcolor:
            return False
        if self.rockorigin != other.rockorigin:
            return False
        if self.rocktype != other.rocktype:
            return False
        if self.role != other.role:
            return False
        if self.role2 != other.role2:
            return False
        if self.role3 != other.role3:
            return False
        if self.school != other.school:
            return False
        if self.sex != other.sex:
            return False
        if self.sgflag != other.sgflag:
            return False
        if self.signedname != other.signedname:
            return False
        if self.signloc != other.signloc:
            return False
        if self.site != other.site:
            return False
        if self.siteno != other.siteno:
            return False
        if self.specgrav != other.specgrav:
            return False
        if self.species != other.species:
            return False
        if self.sprocess != other.sprocess:
            return False
        if self.stage != other.stage:
            return False
        if self.status != other.status:
            return False
        if self.statusby != other.statusby:
            return False
        if self.statusdate != other.statusdate:
            return False
        if self.sterms != other.sterms:
            return False
        if self.stratum != other.stratum:
            return False
        if self.streak != other.streak:
            return False
        if self.subfamily != other.subfamily:
            return False
        if self.subjects != other.subjects:
            return False
        if self.subspecies != other.subspecies:
            return False
        if self.technique != other.technique:
            return False
        if self.tempauthor != other.tempauthor:
            return False
        if self.tempby != other.tempby:
            return False
        if self.tempdate != other.tempdate:
            return False
        if self.temperatur != other.temperatur:
            return False
        if self.temploc != other.temploc:
            return False
        if self.tempnotes != other.tempnotes:
            return False
        if self.tempreason != other.tempreason:
            return False
        if self.tempuntil != other.tempuntil:
            return False
        if self.texture != other.texture:
            return False
        if self.title != other.title:
            return False
        if self.tlocfield1 != other.tlocfield1:
            return False
        if self.tlocfield2 != other.tlocfield2:
            return False
        if self.tlocfield3 != other.tlocfield3:
            return False
        if self.tlocfield4 != other.tlocfield4:
            return False
        if self.tlocfield5 != other.tlocfield5:
            return False
        if self.tlocfield6 != other.tlocfield6:
            return False
        if self.udf1 != other.udf1:
            return False
        if self.udf10 != other.udf10:
            return False
        if self.udf11 != other.udf11:
            return False
        if self.udf12 != other.udf12:
            return False
        if self.udf13 != other.udf13:
            return False
        if self.udf14 != other.udf14:
            return False
        if self.udf15 != other.udf15:
            return False
        if self.udf16 != other.udf16:
            return False
        if self.udf17 != other.udf17:
            return False
        if self.udf18 != other.udf18:
            return False
        if self.udf19 != other.udf19:
            return False
        if self.udf2 != other.udf2:
            return False
        if self.udf20 != other.udf20:
            return False
        if self.udf21 != other.udf21:
            return False
        if self.udf22 != other.udf22:
            return False
        if self.udf3 != other.udf3:
            return False
        if self.udf4 != other.udf4:
            return False
        if self.udf5 != other.udf5:
            return False
        if self.udf6 != other.udf6:
            return False
        if self.udf7 != other.udf7:
            return False
        if self.udf8 != other.udf8:
            return False
        if self.udf9 != other.udf9:
            return False
        if self.unit != other.unit:
            return False
        if self.updated != other.updated:
            return False
        if self.updatedby != other.updatedby:
            return False
        if self.used != other.used:
            return False
        if self.valuedate != other.valuedate:
            return False
        if self.varieties != other.varieties:
            return False
        if self.vexhtml != other.vexhtml:
            return False
        if self.vexlabel1 != other.vexlabel1:
            return False
        if self.vexlabel2 != other.vexlabel2:
            return False
        if self.vexlabel3 != other.vexlabel3:
            return False
        if self.vexlabel4 != other.vexlabel4:
            return False
        if self.webinclude != other.webinclude:
            return False
        if self.weight != other.weight:
            return False
        if self.weightin != other.weightin:
            return False
        if self.weightlb != other.weightlb:
            return False
        if self.width != other.width:
            return False
        if self.widthft != other.widthft:
            return False
        if self.widthin != other.widthin:
            return False
        if self.xcord != other.xcord:
            return False
        if self.ycord != other.ycord:
            return False
        if self.zcord != other.zcord:
            return False
        if self.zsorter != other.zsorter:
            return False
        if self.zsorterx != other.zsorterx:
            return False
        return True

    def __hash__(self):
        return hash((self.accessno,self.accessory,self.acqvalue,self.age,self.appnotes,self.appraisor,self.assemzone,self.bagno,self.boxno,self.caption,self.cat,self.catby,self.catdate,self.cattype,self.chemcomp,self.circum,self.circumft,self.circumin,self.classes,self.colldate,self.collection,self.collector,self.conddate,self.condexam,self.condition,self.condnotes,self.count,self.creator,self.creator2,self.creator3,self.credit,self.crystal,self.culture,self.curvalmax,self.curvalue,self.dataset,self.date,self.datingmeth,self.datum,self.depth,self.depthft,self.depthin,self.descrip,self.diameter,self.diameterft,self.diameterin,self.dimnotes,self.dimtype,self.dispvalue,self.earlydate,self.elements,self.epoch,self.era,self.event,self.ew,self.excavadate,self.excavateby,self.exhibitid,self.exhibitno,self.exhlabel1,self.exhlabel2,self.exhlabel3,self.exhlabel4,self.exhstart,self.family,self.feature,self.flagdate,self.flagnotes,self.flagreason,self.formation,self.fossils,self.found,self.fracture,self.frame,self.framesize,self.genus,self.gparent,self.grainsize,self.habitat,self.hardness,self.height,self.heightft,self.heightin,self.homeloc,self.idby,self.iddate,self.imagefile,self.imageno,self.imagesize,self.inscomp,self.inscrlang,self.inscrpos,self.inscrtech,self.inscrtext,self.inscrtrans,self.inscrtype,self.insdate,self.insphone,self.inspremium,self.insrep,self.insvalue,self.invnby,self.invndate,self.kingdom,self.latdeg,self.latedate,self.legal,self.length,self.lengthft,self.lengthin,self.level,self.lithofacie,self.loancond,self.loandue,self.loanid,self.loaninno,self.loanno,self.loanrenew,self.locfield1,self.locfield2,self.locfield3,self.locfield4,self.locfield5,self.locfield6,self.longdeg,self.luster,self.made,self.maintcycle,self.maintdate,self.maintnote,self.material,self.medium,self.member,self.mmark,self.nhclass,self.nhorder,self.notes,self.ns,self.objectid,self.objname,self.objname2,self.objname3,self.objnames,self.occurrence,self.oldno,self.origin,self.othername,self.otherno,self.outdate,self.owned,self.parent,self.people,self.period,self.phylum,self.policyno,self.ppid,self.preparator,self.prepdate,self.preserve,self.pressure,self.provenance,self.pubnotes,self.qrurl,self.recas,self.recdate,self.recfrom,self.relation,self.relnotes,self.renewuntil,self.repatby,self.repatclaim,self.repatdate,self.repatdisp,self.repathand,self.repatnotes,self.repatnotic,self.repattype,self.rockclass,self.rockcolor,self.rockorigin,self.rocktype,self.role,self.role2,self.role3,self.school,self.sex,self.sgflag,self.signedname,self.signloc,self.site,self.siteno,self.specgrav,self.species,self.sprocess,self.stage,self.status,self.statusby,self.statusdate,self.sterms,self.stratum,self.streak,self.subfamily,self.subjects,self.subspecies,self.technique,self.tempauthor,self.tempby,self.tempdate,self.temperatur,self.temploc,self.tempnotes,self.tempreason,self.tempuntil,self.texture,self.title,self.tlocfield1,self.tlocfield2,self.tlocfield3,self.tlocfield4,self.tlocfield5,self.tlocfield6,self.udf1,self.udf10,self.udf11,self.udf12,self.udf13,self.udf14,self.udf15,self.udf16,self.udf17,self.udf18,self.udf19,self.udf2,self.udf20,self.udf21,self.udf22,self.udf3,self.udf4,self.udf5,self.udf6,self.udf7,self.udf8,self.udf9,self.unit,self.updated,self.updatedby,self.used,self.valuedate,self.varieties,self.vexhtml,self.vexlabel1,self.vexlabel2,self.vexlabel3,self.vexlabel4,self.webinclude,self.weight,self.weightin,self.weightlb,self.width,self.widthft,self.widthin,self.xcord,self.ycord,self.zcord,self.zsorter,self.zsorterx,))

    def __iter__(self):
        return iter((self.accessno, self.accessory, self.acqvalue, self.age, self.appnotes, self.appraisor, self.assemzone, self.bagno, self.boxno, self.caption, self.cat, self.catby, self.catdate, self.cattype, self.chemcomp, self.circum, self.circumft, self.circumin, self.classes, self.colldate, self.collection, self.collector, self.conddate, self.condexam, self.condition, self.condnotes, self.count, self.creator, self.creator2, self.creator3, self.credit, self.crystal, self.culture, self.curvalmax, self.curvalue, self.dataset, self.date, self.datingmeth, self.datum, self.depth, self.depthft, self.depthin, self.descrip, self.diameter, self.diameterft, self.diameterin, self.dimnotes, self.dimtype, self.dispvalue, self.earlydate, self.elements, self.epoch, self.era, self.event, self.ew, self.excavadate, self.excavateby, self.exhibitid, self.exhibitno, self.exhlabel1, self.exhlabel2, self.exhlabel3, self.exhlabel4, self.exhstart, self.family, self.feature, self.flagdate, self.flagnotes, self.flagreason, self.formation, self.fossils, self.found, self.fracture, self.frame, self.framesize, self.genus, self.gparent, self.grainsize, self.habitat, self.hardness, self.height, self.heightft, self.heightin, self.homeloc, self.idby, self.iddate, self.imagefile, self.imageno, self.imagesize, self.inscomp, self.inscrlang, self.inscrpos, self.inscrtech, self.inscrtext, self.inscrtrans, self.inscrtype, self.insdate, self.insphone, self.inspremium, self.insrep, self.insvalue, self.invnby, self.invndate, self.kingdom, self.latdeg, self.latedate, self.legal, self.length, self.lengthft, self.lengthin, self.level, self.lithofacie, self.loancond, self.loandue, self.loanid, self.loaninno, self.loanno, self.loanrenew, self.locfield1, self.locfield2, self.locfield3, self.locfield4, self.locfield5, self.locfield6, self.longdeg, self.luster, self.made, self.maintcycle, self.maintdate, self.maintnote, self.material, self.medium, self.member, self.mmark, self.nhclass, self.nhorder, self.notes, self.ns, self.objectid, self.objname, self.objname2, self.objname3, self.objnames, self.occurrence, self.oldno, self.origin, self.othername, self.otherno, self.outdate, self.owned, self.parent, self.people, self.period, self.phylum, self.policyno, self.ppid, self.preparator, self.prepdate, self.preserve, self.pressure, self.provenance, self.pubnotes, self.qrurl, self.recas, self.recdate, self.recfrom, self.relation, self.relnotes, self.renewuntil, self.repatby, self.repatclaim, self.repatdate, self.repatdisp, self.repathand, self.repatnotes, self.repatnotic, self.repattype, self.rockclass, self.rockcolor, self.rockorigin, self.rocktype, self.role, self.role2, self.role3, self.school, self.sex, self.sgflag, self.signedname, self.signloc, self.site, self.siteno, self.specgrav, self.species, self.sprocess, self.stage, self.status, self.statusby, self.statusdate, self.sterms, self.stratum, self.streak, self.subfamily, self.subjects, self.subspecies, self.technique, self.tempauthor, self.tempby, self.tempdate, self.temperatur, self.temploc, self.tempnotes, self.tempreason, self.tempuntil, self.texture, self.title, self.tlocfield1, self.tlocfield2, self.tlocfield3, self.tlocfield4, self.tlocfield5, self.tlocfield6, self.udf1, self.udf10, self.udf11, self.udf12, self.udf13, self.udf14, self.udf15, self.udf16, self.udf17, self.udf18, self.udf19, self.udf2, self.udf20, self.udf21, self.udf22, self.udf3, self.udf4, self.udf5, self.udf6, self.udf7, self.udf8, self.udf9, self.unit, self.updated, self.updatedby, self.used, self.valuedate, self.varieties, self.vexhtml, self.vexlabel1, self.vexlabel2, self.vexlabel3, self.vexlabel4, self.webinclude, self.weight, self.weightin, self.weightlb, self.width, self.widthft, self.widthin, self.xcord, self.ycord, self.zcord, self.zsorter, self.zsorterx,))

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        field_reprs = []
        if self.accessno is not None:
            field_reprs.append('accessno=' + "'" + self.accessno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.accessory is not None:
            field_reprs.append('accessory=' + "'" + self.accessory.encode('ascii', 'replace').decode('ascii') + "'")
        if self.acqvalue is not None:
            field_reprs.append('acqvalue=' + repr(self.acqvalue))
        if self.age is not None:
            field_reprs.append('age=' + "'" + self.age.encode('ascii', 'replace').decode('ascii') + "'")
        if self.appnotes is not None:
            field_reprs.append('appnotes=' + "'" + self.appnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.appraisor is not None:
            field_reprs.append('appraisor=' + "'" + self.appraisor.encode('ascii', 'replace').decode('ascii') + "'")
        if self.assemzone is not None:
            field_reprs.append('assemzone=' + "'" + self.assemzone.encode('ascii', 'replace').decode('ascii') + "'")
        if self.bagno is not None:
            field_reprs.append('bagno=' + "'" + self.bagno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.boxno is not None:
            field_reprs.append('boxno=' + "'" + self.boxno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.caption is not None:
            field_reprs.append('caption=' + "'" + self.caption.encode('ascii', 'replace').decode('ascii') + "'")
        if self.cat is not None:
            field_reprs.append('cat=' + "'" + self.cat.encode('ascii', 'replace').decode('ascii') + "'")
        if self.catby is not None:
            field_reprs.append('catby=' + "'" + self.catby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.catdate is not None:
            field_reprs.append('catdate=' + repr(self.catdate))
        if self.cattype is not None:
            field_reprs.append('cattype=' + "'" + self.cattype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.chemcomp is not None:
            field_reprs.append('chemcomp=' + "'" + self.chemcomp.encode('ascii', 'replace').decode('ascii') + "'")
        if self.circum is not None:
            field_reprs.append('circum=' + repr(self.circum))
        if self.circumft is not None:
            field_reprs.append('circumft=' + repr(self.circumft))
        if self.circumin is not None:
            field_reprs.append('circumin=' + repr(self.circumin))
        if self.classes is not None:
            field_reprs.append('classes=' + "'" + self.classes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.colldate is not None:
            field_reprs.append('colldate=' + repr(self.colldate))
        if self.collection is not None:
            field_reprs.append('collection=' + "'" + self.collection.encode('ascii', 'replace').decode('ascii') + "'")
        if self.collector is not None:
            field_reprs.append('collector=' + "'" + self.collector.encode('ascii', 'replace').decode('ascii') + "'")
        if self.conddate is not None:
            field_reprs.append('conddate=' + repr(self.conddate))
        if self.condexam is not None:
            field_reprs.append('condexam=' + "'" + self.condexam.encode('ascii', 'replace').decode('ascii') + "'")
        if self.condition is not None:
            field_reprs.append('condition=' + "'" + self.condition.encode('ascii', 'replace').decode('ascii') + "'")
        if self.condnotes is not None:
            field_reprs.append('condnotes=' + "'" + self.condnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.count is not None:
            field_reprs.append('count=' + "'" + self.count.encode('ascii', 'replace').decode('ascii') + "'")
        if self.creator is not None:
            field_reprs.append('creator=' + "'" + self.creator.encode('ascii', 'replace').decode('ascii') + "'")
        if self.creator2 is not None:
            field_reprs.append('creator2=' + "'" + self.creator2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.creator3 is not None:
            field_reprs.append('creator3=' + "'" + self.creator3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.credit is not None:
            field_reprs.append('credit=' + "'" + self.credit.encode('ascii', 'replace').decode('ascii') + "'")
        if self.crystal is not None:
            field_reprs.append('crystal=' + "'" + self.crystal.encode('ascii', 'replace').decode('ascii') + "'")
        if self.culture is not None:
            field_reprs.append('culture=' + "'" + self.culture.encode('ascii', 'replace').decode('ascii') + "'")
        if self.curvalmax is not None:
            field_reprs.append('curvalmax=' + repr(self.curvalmax))
        if self.curvalue is not None:
            field_reprs.append('curvalue=' + repr(self.curvalue))
        if self.dataset is not None:
            field_reprs.append('dataset=' + "'" + self.dataset.encode('ascii', 'replace').decode('ascii') + "'")
        if self.date is not None:
            field_reprs.append('date=' + "'" + self.date.encode('ascii', 'replace').decode('ascii') + "'")
        if self.datingmeth is not None:
            field_reprs.append('datingmeth=' + "'" + self.datingmeth.encode('ascii', 'replace').decode('ascii') + "'")
        if self.datum is not None:
            field_reprs.append('datum=' + "'" + self.datum.encode('ascii', 'replace').decode('ascii') + "'")
        if self.depth is not None:
            field_reprs.append('depth=' + repr(self.depth))
        if self.depthft is not None:
            field_reprs.append('depthft=' + repr(self.depthft))
        if self.depthin is not None:
            field_reprs.append('depthin=' + repr(self.depthin))
        if self.descrip is not None:
            field_reprs.append('descrip=' + "'" + self.descrip.encode('ascii', 'replace').decode('ascii') + "'")
        if self.diameter is not None:
            field_reprs.append('diameter=' + repr(self.diameter))
        if self.diameterft is not None:
            field_reprs.append('diameterft=' + repr(self.diameterft))
        if self.diameterin is not None:
            field_reprs.append('diameterin=' + repr(self.diameterin))
        if self.dimnotes is not None:
            field_reprs.append('dimnotes=' + "'" + self.dimnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.dimtype is not None:
            field_reprs.append('dimtype=' + repr(self.dimtype))
        if self.dispvalue is not None:
            field_reprs.append('dispvalue=' + "'" + self.dispvalue.encode('ascii', 'replace').decode('ascii') + "'")
        if self.earlydate is not None:
            field_reprs.append('earlydate=' + repr(self.earlydate))
        if self.elements is not None:
            field_reprs.append('elements=' + "'" + self.elements.encode('ascii', 'replace').decode('ascii') + "'")
        if self.epoch is not None:
            field_reprs.append('epoch=' + "'" + self.epoch.encode('ascii', 'replace').decode('ascii') + "'")
        if self.era is not None:
            field_reprs.append('era=' + "'" + self.era.encode('ascii', 'replace').decode('ascii') + "'")
        if self.event is not None:
            field_reprs.append('event=' + "'" + self.event.encode('ascii', 'replace').decode('ascii') + "'")
        if self.ew is not None:
            field_reprs.append('ew=' + "'" + self.ew.encode('ascii', 'replace').decode('ascii') + "'")
        if self.excavadate is not None:
            field_reprs.append('excavadate=' + repr(self.excavadate))
        if self.excavateby is not None:
            field_reprs.append('excavateby=' + "'" + self.excavateby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhibitid is not None:
            field_reprs.append('exhibitid=' + "'" + self.exhibitid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhibitno is not None:
            field_reprs.append('exhibitno=' + repr(self.exhibitno))
        if self.exhlabel1 is not None:
            field_reprs.append('exhlabel1=' + "'" + self.exhlabel1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhlabel2 is not None:
            field_reprs.append('exhlabel2=' + "'" + self.exhlabel2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhlabel3 is not None:
            field_reprs.append('exhlabel3=' + "'" + self.exhlabel3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhlabel4 is not None:
            field_reprs.append('exhlabel4=' + "'" + self.exhlabel4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhstart is not None:
            field_reprs.append('exhstart=' + repr(self.exhstart))
        if self.family is not None:
            field_reprs.append('family=' + "'" + self.family.encode('ascii', 'replace').decode('ascii') + "'")
        if self.feature is not None:
            field_reprs.append('feature=' + "'" + self.feature.encode('ascii', 'replace').decode('ascii') + "'")
        if self.flagdate is not None:
            field_reprs.append('flagdate=' + repr(self.flagdate))
        if self.flagnotes is not None:
            field_reprs.append('flagnotes=' + "'" + self.flagnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.flagreason is not None:
            field_reprs.append('flagreason=' + "'" + self.flagreason.encode('ascii', 'replace').decode('ascii') + "'")
        if self.formation is not None:
            field_reprs.append('formation=' + "'" + self.formation.encode('ascii', 'replace').decode('ascii') + "'")
        if self.fossils is not None:
            field_reprs.append('fossils=' + "'" + self.fossils.encode('ascii', 'replace').decode('ascii') + "'")
        if self.found is not None:
            field_reprs.append('found=' + "'" + self.found.encode('ascii', 'replace').decode('ascii') + "'")
        if self.fracture is not None:
            field_reprs.append('fracture=' + "'" + self.fracture.encode('ascii', 'replace').decode('ascii') + "'")
        if self.frame is not None:
            field_reprs.append('frame=' + "'" + self.frame.encode('ascii', 'replace').decode('ascii') + "'")
        if self.framesize is not None:
            field_reprs.append('framesize=' + "'" + self.framesize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.genus is not None:
            field_reprs.append('genus=' + "'" + self.genus.encode('ascii', 'replace').decode('ascii') + "'")
        if self.gparent is not None:
            field_reprs.append('gparent=' + "'" + self.gparent.encode('ascii', 'replace').decode('ascii') + "'")
        if self.grainsize is not None:
            field_reprs.append('grainsize=' + "'" + self.grainsize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.habitat is not None:
            field_reprs.append('habitat=' + "'" + self.habitat.encode('ascii', 'replace').decode('ascii') + "'")
        if self.hardness is not None:
            field_reprs.append('hardness=' + "'" + self.hardness.encode('ascii', 'replace').decode('ascii') + "'")
        if self.height is not None:
            field_reprs.append('height=' + repr(self.height))
        if self.heightft is not None:
            field_reprs.append('heightft=' + repr(self.heightft))
        if self.heightin is not None:
            field_reprs.append('heightin=' + repr(self.heightin))
        if self.homeloc is not None:
            field_reprs.append('homeloc=' + "'" + self.homeloc.encode('ascii', 'replace').decode('ascii') + "'")
        if self.idby is not None:
            field_reprs.append('idby=' + "'" + self.idby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.iddate is not None:
            field_reprs.append('iddate=' + repr(self.iddate))
        if self.imagefile is not None:
            field_reprs.append('imagefile=' + "'" + self.imagefile.encode('ascii', 'replace').decode('ascii') + "'")
        if self.imageno is not None:
            field_reprs.append('imageno=' + repr(self.imageno))
        if self.imagesize is not None:
            field_reprs.append('imagesize=' + "'" + self.imagesize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscomp is not None:
            field_reprs.append('inscomp=' + "'" + self.inscomp.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrlang is not None:
            field_reprs.append('inscrlang=' + "'" + self.inscrlang.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrpos is not None:
            field_reprs.append('inscrpos=' + "'" + self.inscrpos.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtech is not None:
            field_reprs.append('inscrtech=' + "'" + self.inscrtech.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtext is not None:
            field_reprs.append('inscrtext=' + "'" + self.inscrtext.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtrans is not None:
            field_reprs.append('inscrtrans=' + "'" + self.inscrtrans.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtype is not None:
            field_reprs.append('inscrtype=' + "'" + self.inscrtype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.insdate is not None:
            field_reprs.append('insdate=' + repr(self.insdate))
        if self.insphone is not None:
            field_reprs.append('insphone=' + "'" + self.insphone.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inspremium is not None:
            field_reprs.append('inspremium=' + "'" + self.inspremium.encode('ascii', 'replace').decode('ascii') + "'")
        if self.insrep is not None:
            field_reprs.append('insrep=' + "'" + self.insrep.encode('ascii', 'replace').decode('ascii') + "'")
        if self.insvalue is not None:
            field_reprs.append('insvalue=' + repr(self.insvalue))
        if self.invnby is not None:
            field_reprs.append('invnby=' + "'" + self.invnby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.invndate is not None:
            field_reprs.append('invndate=' + repr(self.invndate))
        if self.kingdom is not None:
            field_reprs.append('kingdom=' + "'" + self.kingdom.encode('ascii', 'replace').decode('ascii') + "'")
        if self.latdeg is not None:
            field_reprs.append('latdeg=' + repr(self.latdeg))
        if self.latedate is not None:
            field_reprs.append('latedate=' + repr(self.latedate))
        if self.legal is not None:
            field_reprs.append('legal=' + "'" + self.legal.encode('ascii', 'replace').decode('ascii') + "'")
        if self.length is not None:
            field_reprs.append('length=' + repr(self.length))
        if self.lengthft is not None:
            field_reprs.append('lengthft=' + repr(self.lengthft))
        if self.lengthin is not None:
            field_reprs.append('lengthin=' + repr(self.lengthin))
        if self.level is not None:
            field_reprs.append('level=' + "'" + self.level.encode('ascii', 'replace').decode('ascii') + "'")
        if self.lithofacie is not None:
            field_reprs.append('lithofacie=' + "'" + self.lithofacie.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loancond is not None:
            field_reprs.append('loancond=' + "'" + self.loancond.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loandue is not None:
            field_reprs.append('loandue=' + repr(self.loandue))
        if self.loanid is not None:
            field_reprs.append('loanid=' + "'" + self.loanid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loaninno is not None:
            field_reprs.append('loaninno=' + "'" + self.loaninno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loanno is not None:
            field_reprs.append('loanno=' + repr(self.loanno))
        if self.loanrenew is not None:
            field_reprs.append('loanrenew=' + repr(self.loanrenew))
        if self.locfield1 is not None:
            field_reprs.append('locfield1=' + "'" + self.locfield1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield2 is not None:
            field_reprs.append('locfield2=' + "'" + self.locfield2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield3 is not None:
            field_reprs.append('locfield3=' + "'" + self.locfield3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield4 is not None:
            field_reprs.append('locfield4=' + "'" + self.locfield4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield5 is not None:
            field_reprs.append('locfield5=' + "'" + self.locfield5.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield6 is not None:
            field_reprs.append('locfield6=' + "'" + self.locfield6.encode('ascii', 'replace').decode('ascii') + "'")
        if self.longdeg is not None:
            field_reprs.append('longdeg=' + repr(self.longdeg))
        if self.luster is not None:
            field_reprs.append('luster=' + "'" + self.luster.encode('ascii', 'replace').decode('ascii') + "'")
        if self.made is not None:
            field_reprs.append('made=' + "'" + self.made.encode('ascii', 'replace').decode('ascii') + "'")
        if self.maintcycle is not None:
            field_reprs.append('maintcycle=' + "'" + self.maintcycle.encode('ascii', 'replace').decode('ascii') + "'")
        if self.maintdate is not None:
            field_reprs.append('maintdate=' + repr(self.maintdate))
        if self.maintnote is not None:
            field_reprs.append('maintnote=' + "'" + self.maintnote.encode('ascii', 'replace').decode('ascii') + "'")
        if self.material is not None:
            field_reprs.append('material=' + "'" + self.material.encode('ascii', 'replace').decode('ascii') + "'")
        if self.medium is not None:
            field_reprs.append('medium=' + "'" + self.medium.encode('ascii', 'replace').decode('ascii') + "'")
        if self.member is not None:
            field_reprs.append('member=' + "'" + self.member.encode('ascii', 'replace').decode('ascii') + "'")
        if self.mmark is not None:
            field_reprs.append('mmark=' + "'" + self.mmark.encode('ascii', 'replace').decode('ascii') + "'")
        if self.nhclass is not None:
            field_reprs.append('nhclass=' + "'" + self.nhclass.encode('ascii', 'replace').decode('ascii') + "'")
        if self.nhorder is not None:
            field_reprs.append('nhorder=' + "'" + self.nhorder.encode('ascii', 'replace').decode('ascii') + "'")
        if self.notes is not None:
            field_reprs.append('notes=' + "'" + self.notes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.ns is not None:
            field_reprs.append('ns=' + "'" + self.ns.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objectid is not None:
            field_reprs.append('objectid=' + "'" + self.objectid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objname is not None:
            field_reprs.append('objname=' + "'" + self.objname.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objname2 is not None:
            field_reprs.append('objname2=' + "'" + self.objname2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objname3 is not None:
            field_reprs.append('objname3=' + "'" + self.objname3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objnames is not None:
            field_reprs.append('objnames=' + "'" + self.objnames.encode('ascii', 'replace').decode('ascii') + "'")
        if self.occurrence is not None:
            field_reprs.append('occurrence=' + "'" + self.occurrence.encode('ascii', 'replace').decode('ascii') + "'")
        if self.oldno is not None:
            field_reprs.append('oldno=' + "'" + self.oldno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.origin is not None:
            field_reprs.append('origin=' + "'" + self.origin.encode('ascii', 'replace').decode('ascii') + "'")
        if self.othername is not None:
            field_reprs.append('othername=' + "'" + self.othername.encode('ascii', 'replace').decode('ascii') + "'")
        if self.otherno is not None:
            field_reprs.append('otherno=' + "'" + self.otherno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.outdate is not None:
            field_reprs.append('outdate=' + repr(self.outdate))
        if self.owned is not None:
            field_reprs.append('owned=' + "'" + self.owned.encode('ascii', 'replace').decode('ascii') + "'")
        if self.parent is not None:
            field_reprs.append('parent=' + "'" + self.parent.encode('ascii', 'replace').decode('ascii') + "'")
        if self.people is not None:
            field_reprs.append('people=' + "'" + self.people.encode('ascii', 'replace').decode('ascii') + "'")
        if self.period is not None:
            field_reprs.append('period=' + "'" + self.period.encode('ascii', 'replace').decode('ascii') + "'")
        if self.phylum is not None:
            field_reprs.append('phylum=' + "'" + self.phylum.encode('ascii', 'replace').decode('ascii') + "'")
        if self.policyno is not None:
            field_reprs.append('policyno=' + "'" + self.policyno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.ppid is not None:
            field_reprs.append('ppid=' + "'" + self.ppid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.preparator is not None:
            field_reprs.append('preparator=' + "'" + self.preparator.encode('ascii', 'replace').decode('ascii') + "'")
        if self.prepdate is not None:
            field_reprs.append('prepdate=' + repr(self.prepdate))
        if self.preserve is not None:
            field_reprs.append('preserve=' + "'" + self.preserve.encode('ascii', 'replace').decode('ascii') + "'")
        if self.pressure is not None:
            field_reprs.append('pressure=' + "'" + self.pressure.encode('ascii', 'replace').decode('ascii') + "'")
        if self.provenance is not None:
            field_reprs.append('provenance=' + "'" + self.provenance.encode('ascii', 'replace').decode('ascii') + "'")
        if self.pubnotes is not None:
            field_reprs.append('pubnotes=' + "'" + self.pubnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.qrurl is not None:
            field_reprs.append('qrurl=' + "'" + self.qrurl.encode('ascii', 'replace').decode('ascii') + "'")
        if self.recas is not None:
            field_reprs.append('recas=' + "'" + self.recas.encode('ascii', 'replace').decode('ascii') + "'")
        if self.recdate is not None:
            field_reprs.append('recdate=' + "'" + self.recdate.encode('ascii', 'replace').decode('ascii') + "'")
        if self.recfrom is not None:
            field_reprs.append('recfrom=' + "'" + self.recfrom.encode('ascii', 'replace').decode('ascii') + "'")
        if self.relation is not None:
            field_reprs.append('relation=' + "'" + self.relation.encode('ascii', 'replace').decode('ascii') + "'")
        if self.relnotes is not None:
            field_reprs.append('relnotes=' + "'" + self.relnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.renewuntil is not None:
            field_reprs.append('renewuntil=' + repr(self.renewuntil))
        if self.repatby is not None:
            field_reprs.append('repatby=' + "'" + self.repatby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatclaim is not None:
            field_reprs.append('repatclaim=' + "'" + self.repatclaim.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatdate is not None:
            field_reprs.append('repatdate=' + repr(self.repatdate))
        if self.repatdisp is not None:
            field_reprs.append('repatdisp=' + "'" + self.repatdisp.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repathand is not None:
            field_reprs.append('repathand=' + "'" + self.repathand.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatnotes is not None:
            field_reprs.append('repatnotes=' + "'" + self.repatnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatnotic is not None:
            field_reprs.append('repatnotic=' + repr(self.repatnotic))
        if self.repattype is not None:
            field_reprs.append('repattype=' + "'" + self.repattype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rockclass is not None:
            field_reprs.append('rockclass=' + "'" + self.rockclass.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rockcolor is not None:
            field_reprs.append('rockcolor=' + "'" + self.rockcolor.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rockorigin is not None:
            field_reprs.append('rockorigin=' + "'" + self.rockorigin.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rocktype is not None:
            field_reprs.append('rocktype=' + "'" + self.rocktype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.role is not None:
            field_reprs.append('role=' + "'" + self.role.encode('ascii', 'replace').decode('ascii') + "'")
        if self.role2 is not None:
            field_reprs.append('role2=' + "'" + self.role2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.role3 is not None:
            field_reprs.append('role3=' + "'" + self.role3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.school is not None:
            field_reprs.append('school=' + "'" + self.school.encode('ascii', 'replace').decode('ascii') + "'")
        if self.sex is not None:
            field_reprs.append('sex=' + "'" + self.sex.encode('ascii', 'replace').decode('ascii') + "'")
        if self.sgflag is not None:
            field_reprs.append('sgflag=' + "'" + self.sgflag.encode('ascii', 'replace').decode('ascii') + "'")
        if self.signedname is not None:
            field_reprs.append('signedname=' + "'" + self.signedname.encode('ascii', 'replace').decode('ascii') + "'")
        if self.signloc is not None:
            field_reprs.append('signloc=' + "'" + self.signloc.encode('ascii', 'replace').decode('ascii') + "'")
        if self.site is not None:
            field_reprs.append('site=' + "'" + self.site.encode('ascii', 'replace').decode('ascii') + "'")
        if self.siteno is not None:
            field_reprs.append('siteno=' + "'" + self.siteno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.specgrav is not None:
            field_reprs.append('specgrav=' + "'" + self.specgrav.encode('ascii', 'replace').decode('ascii') + "'")
        if self.species is not None:
            field_reprs.append('species=' + "'" + self.species.encode('ascii', 'replace').decode('ascii') + "'")
        if self.sprocess is not None:
            field_reprs.append('sprocess=' + "'" + self.sprocess.encode('ascii', 'replace').decode('ascii') + "'")
        if self.stage is not None:
            field_reprs.append('stage=' + "'" + self.stage.encode('ascii', 'replace').decode('ascii') + "'")
        if self.status is not None:
            field_reprs.append('status=' + "'" + self.status.encode('ascii', 'replace').decode('ascii') + "'")
        if self.statusby is not None:
            field_reprs.append('statusby=' + "'" + self.statusby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.statusdate is not None:
            field_reprs.append('statusdate=' + repr(self.statusdate))
        if self.sterms is not None:
            field_reprs.append('sterms=' + "'" + self.sterms.encode('ascii', 'replace').decode('ascii') + "'")
        if self.stratum is not None:
            field_reprs.append('stratum=' + "'" + self.stratum.encode('ascii', 'replace').decode('ascii') + "'")
        if self.streak is not None:
            field_reprs.append('streak=' + "'" + self.streak.encode('ascii', 'replace').decode('ascii') + "'")
        if self.subfamily is not None:
            field_reprs.append('subfamily=' + "'" + self.subfamily.encode('ascii', 'replace').decode('ascii') + "'")
        if self.subjects is not None:
            field_reprs.append('subjects=' + "'" + self.subjects.encode('ascii', 'replace').decode('ascii') + "'")
        if self.subspecies is not None:
            field_reprs.append('subspecies=' + "'" + self.subspecies.encode('ascii', 'replace').decode('ascii') + "'")
        if self.technique is not None:
            field_reprs.append('technique=' + "'" + self.technique.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempauthor is not None:
            field_reprs.append('tempauthor=' + "'" + self.tempauthor.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempby is not None:
            field_reprs.append('tempby=' + "'" + self.tempby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempdate is not None:
            field_reprs.append('tempdate=' + repr(self.tempdate))
        if self.temperatur is not None:
            field_reprs.append('temperatur=' + "'" + self.temperatur.encode('ascii', 'replace').decode('ascii') + "'")
        if self.temploc is not None:
            field_reprs.append('temploc=' + "'" + self.temploc.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempnotes is not None:
            field_reprs.append('tempnotes=' + "'" + self.tempnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempreason is not None:
            field_reprs.append('tempreason=' + "'" + self.tempreason.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempuntil is not None:
            field_reprs.append('tempuntil=' + "'" + self.tempuntil.encode('ascii', 'replace').decode('ascii') + "'")
        if self.texture is not None:
            field_reprs.append('texture=' + "'" + self.texture.encode('ascii', 'replace').decode('ascii') + "'")
        if self.title is not None:
            field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield1 is not None:
            field_reprs.append('tlocfield1=' + "'" + self.tlocfield1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield2 is not None:
            field_reprs.append('tlocfield2=' + "'" + self.tlocfield2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield3 is not None:
            field_reprs.append('tlocfield3=' + "'" + self.tlocfield3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield4 is not None:
            field_reprs.append('tlocfield4=' + "'" + self.tlocfield4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield5 is not None:
            field_reprs.append('tlocfield5=' + "'" + self.tlocfield5.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield6 is not None:
            field_reprs.append('tlocfield6=' + "'" + self.tlocfield6.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf1 is not None:
            field_reprs.append('udf1=' + "'" + self.udf1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf10 is not None:
            field_reprs.append('udf10=' + "'" + self.udf10.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf11 is not None:
            field_reprs.append('udf11=' + "'" + self.udf11.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf12 is not None:
            field_reprs.append('udf12=' + "'" + self.udf12.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf13 is not None:
            field_reprs.append('udf13=' + repr(self.udf13))
        if self.udf14 is not None:
            field_reprs.append('udf14=' + repr(self.udf14))
        if self.udf15 is not None:
            field_reprs.append('udf15=' + repr(self.udf15))
        if self.udf16 is not None:
            field_reprs.append('udf16=' + repr(self.udf16))
        if self.udf17 is not None:
            field_reprs.append('udf17=' + repr(self.udf17))
        if self.udf18 is not None:
            field_reprs.append('udf18=' + repr(self.udf18))
        if self.udf19 is not None:
            field_reprs.append('udf19=' + repr(self.udf19))
        if self.udf2 is not None:
            field_reprs.append('udf2=' + "'" + self.udf2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf20 is not None:
            field_reprs.append('udf20=' + repr(self.udf20))
        if self.udf21 is not None:
            field_reprs.append('udf21=' + "'" + self.udf21.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf22 is not None:
            field_reprs.append('udf22=' + "'" + self.udf22.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf3 is not None:
            field_reprs.append('udf3=' + "'" + self.udf3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf4 is not None:
            field_reprs.append('udf4=' + "'" + self.udf4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf5 is not None:
            field_reprs.append('udf5=' + "'" + self.udf5.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf6 is not None:
            field_reprs.append('udf6=' + "'" + self.udf6.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf7 is not None:
            field_reprs.append('udf7=' + "'" + self.udf7.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf8 is not None:
            field_reprs.append('udf8=' + "'" + self.udf8.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf9 is not None:
            field_reprs.append('udf9=' + "'" + self.udf9.encode('ascii', 'replace').decode('ascii') + "'")
        if self.unit is not None:
            field_reprs.append('unit=' + "'" + self.unit.encode('ascii', 'replace').decode('ascii') + "'")
        if self.updated is not None:
            field_reprs.append('updated=' + repr(self.updated))
        if self.updatedby is not None:
            field_reprs.append('updatedby=' + "'" + self.updatedby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.used is not None:
            field_reprs.append('used=' + "'" + self.used.encode('ascii', 'replace').decode('ascii') + "'")
        if self.valuedate is not None:
            field_reprs.append('valuedate=' + repr(self.valuedate))
        if self.varieties is not None:
            field_reprs.append('varieties=' + "'" + self.varieties.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexhtml is not None:
            field_reprs.append('vexhtml=' + "'" + self.vexhtml.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel1 is not None:
            field_reprs.append('vexlabel1=' + "'" + self.vexlabel1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel2 is not None:
            field_reprs.append('vexlabel2=' + "'" + self.vexlabel2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel3 is not None:
            field_reprs.append('vexlabel3=' + "'" + self.vexlabel3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel4 is not None:
            field_reprs.append('vexlabel4=' + "'" + self.vexlabel4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.webinclude is not None:
            field_reprs.append('webinclude=' + repr(self.webinclude))
        if self.weight is not None:
            field_reprs.append('weight=' + repr(self.weight))
        if self.weightin is not None:
            field_reprs.append('weightin=' + repr(self.weightin))
        if self.weightlb is not None:
            field_reprs.append('weightlb=' + repr(self.weightlb))
        if self.width is not None:
            field_reprs.append('width=' + repr(self.width))
        if self.widthft is not None:
            field_reprs.append('widthft=' + repr(self.widthft))
        if self.widthin is not None:
            field_reprs.append('widthin=' + repr(self.widthin))
        if self.xcord is not None:
            field_reprs.append('xcord=' + repr(self.xcord))
        if self.ycord is not None:
            field_reprs.append('ycord=' + repr(self.ycord))
        if self.zcord is not None:
            field_reprs.append('zcord=' + repr(self.zcord))
        if self.zsorter is not None:
            field_reprs.append('zsorter=' + "'" + self.zsorter.encode('ascii', 'replace').decode('ascii') + "'")
        if self.zsorterx is not None:
            field_reprs.append('zsorterx=' + "'" + self.zsorterx.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectRecord(' + ', '.join(field_reprs) + ')'

    def __str__(self):
        field_reprs = []
        if self.accessno is not None:
            field_reprs.append('accessno=' + "'" + self.accessno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.accessory is not None:
            field_reprs.append('accessory=' + "'" + self.accessory.encode('ascii', 'replace').decode('ascii') + "'")
        if self.acqvalue is not None:
            field_reprs.append('acqvalue=' + repr(self.acqvalue))
        if self.age is not None:
            field_reprs.append('age=' + "'" + self.age.encode('ascii', 'replace').decode('ascii') + "'")
        if self.appnotes is not None:
            field_reprs.append('appnotes=' + "'" + self.appnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.appraisor is not None:
            field_reprs.append('appraisor=' + "'" + self.appraisor.encode('ascii', 'replace').decode('ascii') + "'")
        if self.assemzone is not None:
            field_reprs.append('assemzone=' + "'" + self.assemzone.encode('ascii', 'replace').decode('ascii') + "'")
        if self.bagno is not None:
            field_reprs.append('bagno=' + "'" + self.bagno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.boxno is not None:
            field_reprs.append('boxno=' + "'" + self.boxno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.caption is not None:
            field_reprs.append('caption=' + "'" + self.caption.encode('ascii', 'replace').decode('ascii') + "'")
        if self.cat is not None:
            field_reprs.append('cat=' + "'" + self.cat.encode('ascii', 'replace').decode('ascii') + "'")
        if self.catby is not None:
            field_reprs.append('catby=' + "'" + self.catby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.catdate is not None:
            field_reprs.append('catdate=' + repr(self.catdate))
        if self.cattype is not None:
            field_reprs.append('cattype=' + "'" + self.cattype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.chemcomp is not None:
            field_reprs.append('chemcomp=' + "'" + self.chemcomp.encode('ascii', 'replace').decode('ascii') + "'")
        if self.circum is not None:
            field_reprs.append('circum=' + repr(self.circum))
        if self.circumft is not None:
            field_reprs.append('circumft=' + repr(self.circumft))
        if self.circumin is not None:
            field_reprs.append('circumin=' + repr(self.circumin))
        if self.classes is not None:
            field_reprs.append('classes=' + "'" + self.classes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.colldate is not None:
            field_reprs.append('colldate=' + repr(self.colldate))
        if self.collection is not None:
            field_reprs.append('collection=' + "'" + self.collection.encode('ascii', 'replace').decode('ascii') + "'")
        if self.collector is not None:
            field_reprs.append('collector=' + "'" + self.collector.encode('ascii', 'replace').decode('ascii') + "'")
        if self.conddate is not None:
            field_reprs.append('conddate=' + repr(self.conddate))
        if self.condexam is not None:
            field_reprs.append('condexam=' + "'" + self.condexam.encode('ascii', 'replace').decode('ascii') + "'")
        if self.condition is not None:
            field_reprs.append('condition=' + "'" + self.condition.encode('ascii', 'replace').decode('ascii') + "'")
        if self.condnotes is not None:
            field_reprs.append('condnotes=' + "'" + self.condnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.count is not None:
            field_reprs.append('count=' + "'" + self.count.encode('ascii', 'replace').decode('ascii') + "'")
        if self.creator is not None:
            field_reprs.append('creator=' + "'" + self.creator.encode('ascii', 'replace').decode('ascii') + "'")
        if self.creator2 is not None:
            field_reprs.append('creator2=' + "'" + self.creator2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.creator3 is not None:
            field_reprs.append('creator3=' + "'" + self.creator3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.credit is not None:
            field_reprs.append('credit=' + "'" + self.credit.encode('ascii', 'replace').decode('ascii') + "'")
        if self.crystal is not None:
            field_reprs.append('crystal=' + "'" + self.crystal.encode('ascii', 'replace').decode('ascii') + "'")
        if self.culture is not None:
            field_reprs.append('culture=' + "'" + self.culture.encode('ascii', 'replace').decode('ascii') + "'")
        if self.curvalmax is not None:
            field_reprs.append('curvalmax=' + repr(self.curvalmax))
        if self.curvalue is not None:
            field_reprs.append('curvalue=' + repr(self.curvalue))
        if self.dataset is not None:
            field_reprs.append('dataset=' + "'" + self.dataset.encode('ascii', 'replace').decode('ascii') + "'")
        if self.date is not None:
            field_reprs.append('date=' + "'" + self.date.encode('ascii', 'replace').decode('ascii') + "'")
        if self.datingmeth is not None:
            field_reprs.append('datingmeth=' + "'" + self.datingmeth.encode('ascii', 'replace').decode('ascii') + "'")
        if self.datum is not None:
            field_reprs.append('datum=' + "'" + self.datum.encode('ascii', 'replace').decode('ascii') + "'")
        if self.depth is not None:
            field_reprs.append('depth=' + repr(self.depth))
        if self.depthft is not None:
            field_reprs.append('depthft=' + repr(self.depthft))
        if self.depthin is not None:
            field_reprs.append('depthin=' + repr(self.depthin))
        if self.descrip is not None:
            field_reprs.append('descrip=' + "'" + self.descrip.encode('ascii', 'replace').decode('ascii') + "'")
        if self.diameter is not None:
            field_reprs.append('diameter=' + repr(self.diameter))
        if self.diameterft is not None:
            field_reprs.append('diameterft=' + repr(self.diameterft))
        if self.diameterin is not None:
            field_reprs.append('diameterin=' + repr(self.diameterin))
        if self.dimnotes is not None:
            field_reprs.append('dimnotes=' + "'" + self.dimnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.dimtype is not None:
            field_reprs.append('dimtype=' + repr(self.dimtype))
        if self.dispvalue is not None:
            field_reprs.append('dispvalue=' + "'" + self.dispvalue.encode('ascii', 'replace').decode('ascii') + "'")
        if self.earlydate is not None:
            field_reprs.append('earlydate=' + repr(self.earlydate))
        if self.elements is not None:
            field_reprs.append('elements=' + "'" + self.elements.encode('ascii', 'replace').decode('ascii') + "'")
        if self.epoch is not None:
            field_reprs.append('epoch=' + "'" + self.epoch.encode('ascii', 'replace').decode('ascii') + "'")
        if self.era is not None:
            field_reprs.append('era=' + "'" + self.era.encode('ascii', 'replace').decode('ascii') + "'")
        if self.event is not None:
            field_reprs.append('event=' + "'" + self.event.encode('ascii', 'replace').decode('ascii') + "'")
        if self.ew is not None:
            field_reprs.append('ew=' + "'" + self.ew.encode('ascii', 'replace').decode('ascii') + "'")
        if self.excavadate is not None:
            field_reprs.append('excavadate=' + repr(self.excavadate))
        if self.excavateby is not None:
            field_reprs.append('excavateby=' + "'" + self.excavateby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhibitid is not None:
            field_reprs.append('exhibitid=' + "'" + self.exhibitid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhibitno is not None:
            field_reprs.append('exhibitno=' + repr(self.exhibitno))
        if self.exhlabel1 is not None:
            field_reprs.append('exhlabel1=' + "'" + self.exhlabel1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhlabel2 is not None:
            field_reprs.append('exhlabel2=' + "'" + self.exhlabel2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhlabel3 is not None:
            field_reprs.append('exhlabel3=' + "'" + self.exhlabel3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhlabel4 is not None:
            field_reprs.append('exhlabel4=' + "'" + self.exhlabel4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.exhstart is not None:
            field_reprs.append('exhstart=' + repr(self.exhstart))
        if self.family is not None:
            field_reprs.append('family=' + "'" + self.family.encode('ascii', 'replace').decode('ascii') + "'")
        if self.feature is not None:
            field_reprs.append('feature=' + "'" + self.feature.encode('ascii', 'replace').decode('ascii') + "'")
        if self.flagdate is not None:
            field_reprs.append('flagdate=' + repr(self.flagdate))
        if self.flagnotes is not None:
            field_reprs.append('flagnotes=' + "'" + self.flagnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.flagreason is not None:
            field_reprs.append('flagreason=' + "'" + self.flagreason.encode('ascii', 'replace').decode('ascii') + "'")
        if self.formation is not None:
            field_reprs.append('formation=' + "'" + self.formation.encode('ascii', 'replace').decode('ascii') + "'")
        if self.fossils is not None:
            field_reprs.append('fossils=' + "'" + self.fossils.encode('ascii', 'replace').decode('ascii') + "'")
        if self.found is not None:
            field_reprs.append('found=' + "'" + self.found.encode('ascii', 'replace').decode('ascii') + "'")
        if self.fracture is not None:
            field_reprs.append('fracture=' + "'" + self.fracture.encode('ascii', 'replace').decode('ascii') + "'")
        if self.frame is not None:
            field_reprs.append('frame=' + "'" + self.frame.encode('ascii', 'replace').decode('ascii') + "'")
        if self.framesize is not None:
            field_reprs.append('framesize=' + "'" + self.framesize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.genus is not None:
            field_reprs.append('genus=' + "'" + self.genus.encode('ascii', 'replace').decode('ascii') + "'")
        if self.gparent is not None:
            field_reprs.append('gparent=' + "'" + self.gparent.encode('ascii', 'replace').decode('ascii') + "'")
        if self.grainsize is not None:
            field_reprs.append('grainsize=' + "'" + self.grainsize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.habitat is not None:
            field_reprs.append('habitat=' + "'" + self.habitat.encode('ascii', 'replace').decode('ascii') + "'")
        if self.hardness is not None:
            field_reprs.append('hardness=' + "'" + self.hardness.encode('ascii', 'replace').decode('ascii') + "'")
        if self.height is not None:
            field_reprs.append('height=' + repr(self.height))
        if self.heightft is not None:
            field_reprs.append('heightft=' + repr(self.heightft))
        if self.heightin is not None:
            field_reprs.append('heightin=' + repr(self.heightin))
        if self.homeloc is not None:
            field_reprs.append('homeloc=' + "'" + self.homeloc.encode('ascii', 'replace').decode('ascii') + "'")
        if self.idby is not None:
            field_reprs.append('idby=' + "'" + self.idby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.iddate is not None:
            field_reprs.append('iddate=' + repr(self.iddate))
        if self.imagefile is not None:
            field_reprs.append('imagefile=' + "'" + self.imagefile.encode('ascii', 'replace').decode('ascii') + "'")
        if self.imageno is not None:
            field_reprs.append('imageno=' + repr(self.imageno))
        if self.imagesize is not None:
            field_reprs.append('imagesize=' + "'" + self.imagesize.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscomp is not None:
            field_reprs.append('inscomp=' + "'" + self.inscomp.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrlang is not None:
            field_reprs.append('inscrlang=' + "'" + self.inscrlang.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrpos is not None:
            field_reprs.append('inscrpos=' + "'" + self.inscrpos.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtech is not None:
            field_reprs.append('inscrtech=' + "'" + self.inscrtech.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtext is not None:
            field_reprs.append('inscrtext=' + "'" + self.inscrtext.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtrans is not None:
            field_reprs.append('inscrtrans=' + "'" + self.inscrtrans.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inscrtype is not None:
            field_reprs.append('inscrtype=' + "'" + self.inscrtype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.insdate is not None:
            field_reprs.append('insdate=' + repr(self.insdate))
        if self.insphone is not None:
            field_reprs.append('insphone=' + "'" + self.insphone.encode('ascii', 'replace').decode('ascii') + "'")
        if self.inspremium is not None:
            field_reprs.append('inspremium=' + "'" + self.inspremium.encode('ascii', 'replace').decode('ascii') + "'")
        if self.insrep is not None:
            field_reprs.append('insrep=' + "'" + self.insrep.encode('ascii', 'replace').decode('ascii') + "'")
        if self.insvalue is not None:
            field_reprs.append('insvalue=' + repr(self.insvalue))
        if self.invnby is not None:
            field_reprs.append('invnby=' + "'" + self.invnby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.invndate is not None:
            field_reprs.append('invndate=' + repr(self.invndate))
        if self.kingdom is not None:
            field_reprs.append('kingdom=' + "'" + self.kingdom.encode('ascii', 'replace').decode('ascii') + "'")
        if self.latdeg is not None:
            field_reprs.append('latdeg=' + repr(self.latdeg))
        if self.latedate is not None:
            field_reprs.append('latedate=' + repr(self.latedate))
        if self.legal is not None:
            field_reprs.append('legal=' + "'" + self.legal.encode('ascii', 'replace').decode('ascii') + "'")
        if self.length is not None:
            field_reprs.append('length=' + repr(self.length))
        if self.lengthft is not None:
            field_reprs.append('lengthft=' + repr(self.lengthft))
        if self.lengthin is not None:
            field_reprs.append('lengthin=' + repr(self.lengthin))
        if self.level is not None:
            field_reprs.append('level=' + "'" + self.level.encode('ascii', 'replace').decode('ascii') + "'")
        if self.lithofacie is not None:
            field_reprs.append('lithofacie=' + "'" + self.lithofacie.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loancond is not None:
            field_reprs.append('loancond=' + "'" + self.loancond.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loandue is not None:
            field_reprs.append('loandue=' + repr(self.loandue))
        if self.loanid is not None:
            field_reprs.append('loanid=' + "'" + self.loanid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loaninno is not None:
            field_reprs.append('loaninno=' + "'" + self.loaninno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.loanno is not None:
            field_reprs.append('loanno=' + repr(self.loanno))
        if self.loanrenew is not None:
            field_reprs.append('loanrenew=' + repr(self.loanrenew))
        if self.locfield1 is not None:
            field_reprs.append('locfield1=' + "'" + self.locfield1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield2 is not None:
            field_reprs.append('locfield2=' + "'" + self.locfield2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield3 is not None:
            field_reprs.append('locfield3=' + "'" + self.locfield3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield4 is not None:
            field_reprs.append('locfield4=' + "'" + self.locfield4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield5 is not None:
            field_reprs.append('locfield5=' + "'" + self.locfield5.encode('ascii', 'replace').decode('ascii') + "'")
        if self.locfield6 is not None:
            field_reprs.append('locfield6=' + "'" + self.locfield6.encode('ascii', 'replace').decode('ascii') + "'")
        if self.longdeg is not None:
            field_reprs.append('longdeg=' + repr(self.longdeg))
        if self.luster is not None:
            field_reprs.append('luster=' + "'" + self.luster.encode('ascii', 'replace').decode('ascii') + "'")
        if self.made is not None:
            field_reprs.append('made=' + "'" + self.made.encode('ascii', 'replace').decode('ascii') + "'")
        if self.maintcycle is not None:
            field_reprs.append('maintcycle=' + "'" + self.maintcycle.encode('ascii', 'replace').decode('ascii') + "'")
        if self.maintdate is not None:
            field_reprs.append('maintdate=' + repr(self.maintdate))
        if self.maintnote is not None:
            field_reprs.append('maintnote=' + "'" + self.maintnote.encode('ascii', 'replace').decode('ascii') + "'")
        if self.material is not None:
            field_reprs.append('material=' + "'" + self.material.encode('ascii', 'replace').decode('ascii') + "'")
        if self.medium is not None:
            field_reprs.append('medium=' + "'" + self.medium.encode('ascii', 'replace').decode('ascii') + "'")
        if self.member is not None:
            field_reprs.append('member=' + "'" + self.member.encode('ascii', 'replace').decode('ascii') + "'")
        if self.mmark is not None:
            field_reprs.append('mmark=' + "'" + self.mmark.encode('ascii', 'replace').decode('ascii') + "'")
        if self.nhclass is not None:
            field_reprs.append('nhclass=' + "'" + self.nhclass.encode('ascii', 'replace').decode('ascii') + "'")
        if self.nhorder is not None:
            field_reprs.append('nhorder=' + "'" + self.nhorder.encode('ascii', 'replace').decode('ascii') + "'")
        if self.notes is not None:
            field_reprs.append('notes=' + "'" + self.notes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.ns is not None:
            field_reprs.append('ns=' + "'" + self.ns.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objectid is not None:
            field_reprs.append('objectid=' + "'" + self.objectid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objname is not None:
            field_reprs.append('objname=' + "'" + self.objname.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objname2 is not None:
            field_reprs.append('objname2=' + "'" + self.objname2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objname3 is not None:
            field_reprs.append('objname3=' + "'" + self.objname3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.objnames is not None:
            field_reprs.append('objnames=' + "'" + self.objnames.encode('ascii', 'replace').decode('ascii') + "'")
        if self.occurrence is not None:
            field_reprs.append('occurrence=' + "'" + self.occurrence.encode('ascii', 'replace').decode('ascii') + "'")
        if self.oldno is not None:
            field_reprs.append('oldno=' + "'" + self.oldno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.origin is not None:
            field_reprs.append('origin=' + "'" + self.origin.encode('ascii', 'replace').decode('ascii') + "'")
        if self.othername is not None:
            field_reprs.append('othername=' + "'" + self.othername.encode('ascii', 'replace').decode('ascii') + "'")
        if self.otherno is not None:
            field_reprs.append('otherno=' + "'" + self.otherno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.outdate is not None:
            field_reprs.append('outdate=' + repr(self.outdate))
        if self.owned is not None:
            field_reprs.append('owned=' + "'" + self.owned.encode('ascii', 'replace').decode('ascii') + "'")
        if self.parent is not None:
            field_reprs.append('parent=' + "'" + self.parent.encode('ascii', 'replace').decode('ascii') + "'")
        if self.people is not None:
            field_reprs.append('people=' + "'" + self.people.encode('ascii', 'replace').decode('ascii') + "'")
        if self.period is not None:
            field_reprs.append('period=' + "'" + self.period.encode('ascii', 'replace').decode('ascii') + "'")
        if self.phylum is not None:
            field_reprs.append('phylum=' + "'" + self.phylum.encode('ascii', 'replace').decode('ascii') + "'")
        if self.policyno is not None:
            field_reprs.append('policyno=' + "'" + self.policyno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.ppid is not None:
            field_reprs.append('ppid=' + "'" + self.ppid.encode('ascii', 'replace').decode('ascii') + "'")
        if self.preparator is not None:
            field_reprs.append('preparator=' + "'" + self.preparator.encode('ascii', 'replace').decode('ascii') + "'")
        if self.prepdate is not None:
            field_reprs.append('prepdate=' + repr(self.prepdate))
        if self.preserve is not None:
            field_reprs.append('preserve=' + "'" + self.preserve.encode('ascii', 'replace').decode('ascii') + "'")
        if self.pressure is not None:
            field_reprs.append('pressure=' + "'" + self.pressure.encode('ascii', 'replace').decode('ascii') + "'")
        if self.provenance is not None:
            field_reprs.append('provenance=' + "'" + self.provenance.encode('ascii', 'replace').decode('ascii') + "'")
        if self.pubnotes is not None:
            field_reprs.append('pubnotes=' + "'" + self.pubnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.qrurl is not None:
            field_reprs.append('qrurl=' + "'" + self.qrurl.encode('ascii', 'replace').decode('ascii') + "'")
        if self.recas is not None:
            field_reprs.append('recas=' + "'" + self.recas.encode('ascii', 'replace').decode('ascii') + "'")
        if self.recdate is not None:
            field_reprs.append('recdate=' + "'" + self.recdate.encode('ascii', 'replace').decode('ascii') + "'")
        if self.recfrom is not None:
            field_reprs.append('recfrom=' + "'" + self.recfrom.encode('ascii', 'replace').decode('ascii') + "'")
        if self.relation is not None:
            field_reprs.append('relation=' + "'" + self.relation.encode('ascii', 'replace').decode('ascii') + "'")
        if self.relnotes is not None:
            field_reprs.append('relnotes=' + "'" + self.relnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.renewuntil is not None:
            field_reprs.append('renewuntil=' + repr(self.renewuntil))
        if self.repatby is not None:
            field_reprs.append('repatby=' + "'" + self.repatby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatclaim is not None:
            field_reprs.append('repatclaim=' + "'" + self.repatclaim.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatdate is not None:
            field_reprs.append('repatdate=' + repr(self.repatdate))
        if self.repatdisp is not None:
            field_reprs.append('repatdisp=' + "'" + self.repatdisp.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repathand is not None:
            field_reprs.append('repathand=' + "'" + self.repathand.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatnotes is not None:
            field_reprs.append('repatnotes=' + "'" + self.repatnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.repatnotic is not None:
            field_reprs.append('repatnotic=' + repr(self.repatnotic))
        if self.repattype is not None:
            field_reprs.append('repattype=' + "'" + self.repattype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rockclass is not None:
            field_reprs.append('rockclass=' + "'" + self.rockclass.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rockcolor is not None:
            field_reprs.append('rockcolor=' + "'" + self.rockcolor.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rockorigin is not None:
            field_reprs.append('rockorigin=' + "'" + self.rockorigin.encode('ascii', 'replace').decode('ascii') + "'")
        if self.rocktype is not None:
            field_reprs.append('rocktype=' + "'" + self.rocktype.encode('ascii', 'replace').decode('ascii') + "'")
        if self.role is not None:
            field_reprs.append('role=' + "'" + self.role.encode('ascii', 'replace').decode('ascii') + "'")
        if self.role2 is not None:
            field_reprs.append('role2=' + "'" + self.role2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.role3 is not None:
            field_reprs.append('role3=' + "'" + self.role3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.school is not None:
            field_reprs.append('school=' + "'" + self.school.encode('ascii', 'replace').decode('ascii') + "'")
        if self.sex is not None:
            field_reprs.append('sex=' + "'" + self.sex.encode('ascii', 'replace').decode('ascii') + "'")
        if self.sgflag is not None:
            field_reprs.append('sgflag=' + "'" + self.sgflag.encode('ascii', 'replace').decode('ascii') + "'")
        if self.signedname is not None:
            field_reprs.append('signedname=' + "'" + self.signedname.encode('ascii', 'replace').decode('ascii') + "'")
        if self.signloc is not None:
            field_reprs.append('signloc=' + "'" + self.signloc.encode('ascii', 'replace').decode('ascii') + "'")
        if self.site is not None:
            field_reprs.append('site=' + "'" + self.site.encode('ascii', 'replace').decode('ascii') + "'")
        if self.siteno is not None:
            field_reprs.append('siteno=' + "'" + self.siteno.encode('ascii', 'replace').decode('ascii') + "'")
        if self.specgrav is not None:
            field_reprs.append('specgrav=' + "'" + self.specgrav.encode('ascii', 'replace').decode('ascii') + "'")
        if self.species is not None:
            field_reprs.append('species=' + "'" + self.species.encode('ascii', 'replace').decode('ascii') + "'")
        if self.sprocess is not None:
            field_reprs.append('sprocess=' + "'" + self.sprocess.encode('ascii', 'replace').decode('ascii') + "'")
        if self.stage is not None:
            field_reprs.append('stage=' + "'" + self.stage.encode('ascii', 'replace').decode('ascii') + "'")
        if self.status is not None:
            field_reprs.append('status=' + "'" + self.status.encode('ascii', 'replace').decode('ascii') + "'")
        if self.statusby is not None:
            field_reprs.append('statusby=' + "'" + self.statusby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.statusdate is not None:
            field_reprs.append('statusdate=' + repr(self.statusdate))
        if self.sterms is not None:
            field_reprs.append('sterms=' + "'" + self.sterms.encode('ascii', 'replace').decode('ascii') + "'")
        if self.stratum is not None:
            field_reprs.append('stratum=' + "'" + self.stratum.encode('ascii', 'replace').decode('ascii') + "'")
        if self.streak is not None:
            field_reprs.append('streak=' + "'" + self.streak.encode('ascii', 'replace').decode('ascii') + "'")
        if self.subfamily is not None:
            field_reprs.append('subfamily=' + "'" + self.subfamily.encode('ascii', 'replace').decode('ascii') + "'")
        if self.subjects is not None:
            field_reprs.append('subjects=' + "'" + self.subjects.encode('ascii', 'replace').decode('ascii') + "'")
        if self.subspecies is not None:
            field_reprs.append('subspecies=' + "'" + self.subspecies.encode('ascii', 'replace').decode('ascii') + "'")
        if self.technique is not None:
            field_reprs.append('technique=' + "'" + self.technique.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempauthor is not None:
            field_reprs.append('tempauthor=' + "'" + self.tempauthor.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempby is not None:
            field_reprs.append('tempby=' + "'" + self.tempby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempdate is not None:
            field_reprs.append('tempdate=' + repr(self.tempdate))
        if self.temperatur is not None:
            field_reprs.append('temperatur=' + "'" + self.temperatur.encode('ascii', 'replace').decode('ascii') + "'")
        if self.temploc is not None:
            field_reprs.append('temploc=' + "'" + self.temploc.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempnotes is not None:
            field_reprs.append('tempnotes=' + "'" + self.tempnotes.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempreason is not None:
            field_reprs.append('tempreason=' + "'" + self.tempreason.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tempuntil is not None:
            field_reprs.append('tempuntil=' + "'" + self.tempuntil.encode('ascii', 'replace').decode('ascii') + "'")
        if self.texture is not None:
            field_reprs.append('texture=' + "'" + self.texture.encode('ascii', 'replace').decode('ascii') + "'")
        if self.title is not None:
            field_reprs.append('title=' + "'" + self.title.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield1 is not None:
            field_reprs.append('tlocfield1=' + "'" + self.tlocfield1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield2 is not None:
            field_reprs.append('tlocfield2=' + "'" + self.tlocfield2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield3 is not None:
            field_reprs.append('tlocfield3=' + "'" + self.tlocfield3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield4 is not None:
            field_reprs.append('tlocfield4=' + "'" + self.tlocfield4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield5 is not None:
            field_reprs.append('tlocfield5=' + "'" + self.tlocfield5.encode('ascii', 'replace').decode('ascii') + "'")
        if self.tlocfield6 is not None:
            field_reprs.append('tlocfield6=' + "'" + self.tlocfield6.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf1 is not None:
            field_reprs.append('udf1=' + "'" + self.udf1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf10 is not None:
            field_reprs.append('udf10=' + "'" + self.udf10.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf11 is not None:
            field_reprs.append('udf11=' + "'" + self.udf11.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf12 is not None:
            field_reprs.append('udf12=' + "'" + self.udf12.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf13 is not None:
            field_reprs.append('udf13=' + repr(self.udf13))
        if self.udf14 is not None:
            field_reprs.append('udf14=' + repr(self.udf14))
        if self.udf15 is not None:
            field_reprs.append('udf15=' + repr(self.udf15))
        if self.udf16 is not None:
            field_reprs.append('udf16=' + repr(self.udf16))
        if self.udf17 is not None:
            field_reprs.append('udf17=' + repr(self.udf17))
        if self.udf18 is not None:
            field_reprs.append('udf18=' + repr(self.udf18))
        if self.udf19 is not None:
            field_reprs.append('udf19=' + repr(self.udf19))
        if self.udf2 is not None:
            field_reprs.append('udf2=' + "'" + self.udf2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf20 is not None:
            field_reprs.append('udf20=' + repr(self.udf20))
        if self.udf21 is not None:
            field_reprs.append('udf21=' + "'" + self.udf21.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf22 is not None:
            field_reprs.append('udf22=' + "'" + self.udf22.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf3 is not None:
            field_reprs.append('udf3=' + "'" + self.udf3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf4 is not None:
            field_reprs.append('udf4=' + "'" + self.udf4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf5 is not None:
            field_reprs.append('udf5=' + "'" + self.udf5.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf6 is not None:
            field_reprs.append('udf6=' + "'" + self.udf6.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf7 is not None:
            field_reprs.append('udf7=' + "'" + self.udf7.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf8 is not None:
            field_reprs.append('udf8=' + "'" + self.udf8.encode('ascii', 'replace').decode('ascii') + "'")
        if self.udf9 is not None:
            field_reprs.append('udf9=' + "'" + self.udf9.encode('ascii', 'replace').decode('ascii') + "'")
        if self.unit is not None:
            field_reprs.append('unit=' + "'" + self.unit.encode('ascii', 'replace').decode('ascii') + "'")
        if self.updated is not None:
            field_reprs.append('updated=' + repr(self.updated))
        if self.updatedby is not None:
            field_reprs.append('updatedby=' + "'" + self.updatedby.encode('ascii', 'replace').decode('ascii') + "'")
        if self.used is not None:
            field_reprs.append('used=' + "'" + self.used.encode('ascii', 'replace').decode('ascii') + "'")
        if self.valuedate is not None:
            field_reprs.append('valuedate=' + repr(self.valuedate))
        if self.varieties is not None:
            field_reprs.append('varieties=' + "'" + self.varieties.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexhtml is not None:
            field_reprs.append('vexhtml=' + "'" + self.vexhtml.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel1 is not None:
            field_reprs.append('vexlabel1=' + "'" + self.vexlabel1.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel2 is not None:
            field_reprs.append('vexlabel2=' + "'" + self.vexlabel2.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel3 is not None:
            field_reprs.append('vexlabel3=' + "'" + self.vexlabel3.encode('ascii', 'replace').decode('ascii') + "'")
        if self.vexlabel4 is not None:
            field_reprs.append('vexlabel4=' + "'" + self.vexlabel4.encode('ascii', 'replace').decode('ascii') + "'")
        if self.webinclude is not None:
            field_reprs.append('webinclude=' + repr(self.webinclude))
        if self.weight is not None:
            field_reprs.append('weight=' + repr(self.weight))
        if self.weightin is not None:
            field_reprs.append('weightin=' + repr(self.weightin))
        if self.weightlb is not None:
            field_reprs.append('weightlb=' + repr(self.weightlb))
        if self.width is not None:
            field_reprs.append('width=' + repr(self.width))
        if self.widthft is not None:
            field_reprs.append('widthft=' + repr(self.widthft))
        if self.widthin is not None:
            field_reprs.append('widthin=' + repr(self.widthin))
        if self.xcord is not None:
            field_reprs.append('xcord=' + repr(self.xcord))
        if self.ycord is not None:
            field_reprs.append('ycord=' + repr(self.ycord))
        if self.zcord is not None:
            field_reprs.append('zcord=' + repr(self.zcord))
        if self.zsorter is not None:
            field_reprs.append('zsorter=' + "'" + self.zsorter.encode('ascii', 'replace').decode('ascii') + "'")
        if self.zsorterx is not None:
            field_reprs.append('zsorterx=' + "'" + self.zsorterx.encode('ascii', 'replace').decode('ascii') + "'")
        return 'ObjectRecord(' + ', '.join(field_reprs) + ')'

    @property
    def accessno(self):
        '''
        :rtype: str
        '''

        return self.__accessno

    @property
    def accessory(self):
        '''
        :rtype: str
        '''

        return self.__accessory

    @property
    def acqvalue(self):
        '''
        :rtype: Decimal
        '''

        return self.__acqvalue

    @property
    def age(self):
        '''
        :rtype: str
        '''

        return self.__age

    @property
    def appnotes(self):
        '''
        :rtype: str
        '''

        return self.__appnotes

    @property
    def appraisor(self):
        '''
        :rtype: str
        '''

        return self.__appraisor

    @property
    def assemzone(self):
        '''
        :rtype: str
        '''

        return self.__assemzone

    @property
    def bagno(self):
        '''
        :rtype: str
        '''

        return self.__bagno

    @property
    def boxno(self):
        '''
        :rtype: str
        '''

        return self.__boxno

    @property
    def caption(self):
        '''
        :rtype: str
        '''

        return self.__caption

    @property
    def cat(self):
        '''
        :rtype: str
        '''

        return self.__cat

    @property
    def catby(self):
        '''
        :rtype: str
        '''

        return self.__catby

    @property
    def catdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__catdate

    @property
    def cattype(self):
        '''
        :rtype: str
        '''

        return self.__cattype

    @property
    def chemcomp(self):
        '''
        :rtype: str
        '''

        return self.__chemcomp

    @property
    def circum(self):
        '''
        :rtype: Decimal
        '''

        return self.__circum

    @property
    def circumft(self):
        '''
        :rtype: Decimal
        '''

        return self.__circumft

    @property
    def circumin(self):
        '''
        :rtype: Decimal
        '''

        return self.__circumin

    @property
    def classes(self):
        '''
        :rtype: str
        '''

        return self.__classes

    @property
    def colldate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__colldate

    @property
    def collection(self):
        '''
        :rtype: str
        '''

        return self.__collection

    @property
    def collector(self):
        '''
        :rtype: str
        '''

        return self.__collector

    @property
    def conddate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__conddate

    @property
    def condexam(self):
        '''
        :rtype: str
        '''

        return self.__condexam

    @property
    def condition(self):
        '''
        :rtype: str
        '''

        return self.__condition

    @property
    def condnotes(self):
        '''
        :rtype: str
        '''

        return self.__condnotes

    @property
    def count(self):
        '''
        :rtype: str
        '''

        return self.__count

    @property
    def creator(self):
        '''
        :rtype: str
        '''

        return self.__creator

    @property
    def creator2(self):
        '''
        :rtype: str
        '''

        return self.__creator2

    @property
    def creator3(self):
        '''
        :rtype: str
        '''

        return self.__creator3

    @property
    def credit(self):
        '''
        :rtype: str
        '''

        return self.__credit

    @property
    def crystal(self):
        '''
        :rtype: str
        '''

        return self.__crystal

    @property
    def culture(self):
        '''
        :rtype: str
        '''

        return self.__culture

    @property
    def curvalmax(self):
        '''
        :rtype: Decimal
        '''

        return self.__curvalmax

    @property
    def curvalue(self):
        '''
        :rtype: Decimal
        '''

        return self.__curvalue

    @property
    def dataset(self):
        '''
        :rtype: str
        '''

        return self.__dataset

    @property
    def date(self):
        '''
        :rtype: str
        '''

        return self.__date

    @property
    def datingmeth(self):
        '''
        :rtype: str
        '''

        return self.__datingmeth

    @property
    def datum(self):
        '''
        :rtype: str
        '''

        return self.__datum

    @property
    def depth(self):
        '''
        :rtype: Decimal
        '''

        return self.__depth

    @property
    def depthft(self):
        '''
        :rtype: Decimal
        '''

        return self.__depthft

    @property
    def depthin(self):
        '''
        :rtype: Decimal
        '''

        return self.__depthin

    @property
    def descrip(self):
        '''
        :rtype: str
        '''

        return self.__descrip

    @property
    def diameter(self):
        '''
        :rtype: Decimal
        '''

        return self.__diameter

    @property
    def diameterft(self):
        '''
        :rtype: Decimal
        '''

        return self.__diameterft

    @property
    def diameterin(self):
        '''
        :rtype: Decimal
        '''

        return self.__diameterin

    @property
    def dimnotes(self):
        '''
        :rtype: str
        '''

        return self.__dimnotes

    @property
    def dimtype(self):
        '''
        :rtype: int
        '''

        return self.__dimtype

    @property
    def dispvalue(self):
        '''
        :rtype: str
        '''

        return self.__dispvalue

    @property
    def earlydate(self):
        '''
        :rtype: int
        '''

        return self.__earlydate

    @property
    def elements(self):
        '''
        :rtype: str
        '''

        return self.__elements

    @property
    def epoch(self):
        '''
        :rtype: str
        '''

        return self.__epoch

    @property
    def era(self):
        '''
        :rtype: str
        '''

        return self.__era

    @property
    def event(self):
        '''
        :rtype: str
        '''

        return self.__event

    @property
    def ew(self):
        '''
        :rtype: str
        '''

        return self.__ew

    @property
    def excavadate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__excavadate

    @property
    def excavateby(self):
        '''
        :rtype: str
        '''

        return self.__excavateby

    @property
    def exhibitid(self):
        '''
        :rtype: str
        '''

        return self.__exhibitid

    @property
    def exhibitno(self):
        '''
        :rtype: int
        '''

        return self.__exhibitno

    @property
    def exhlabel1(self):
        '''
        :rtype: str
        '''

        return self.__exhlabel1

    @property
    def exhlabel2(self):
        '''
        :rtype: str
        '''

        return self.__exhlabel2

    @property
    def exhlabel3(self):
        '''
        :rtype: str
        '''

        return self.__exhlabel3

    @property
    def exhlabel4(self):
        '''
        :rtype: str
        '''

        return self.__exhlabel4

    @property
    def exhstart(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__exhstart

    @property
    def family(self):
        '''
        :rtype: str
        '''

        return self.__family

    @property
    def feature(self):
        '''
        :rtype: str
        '''

        return self.__feature

    @property
    def flagdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__flagdate

    @property
    def flagnotes(self):
        '''
        :rtype: str
        '''

        return self.__flagnotes

    @property
    def flagreason(self):
        '''
        :rtype: str
        '''

        return self.__flagreason

    @property
    def formation(self):
        '''
        :rtype: str
        '''

        return self.__formation

    @property
    def fossils(self):
        '''
        :rtype: str
        '''

        return self.__fossils

    @property
    def found(self):
        '''
        :rtype: str
        '''

        return self.__found

    @property
    def fracture(self):
        '''
        :rtype: str
        '''

        return self.__fracture

    @property
    def frame(self):
        '''
        :rtype: str
        '''

        return self.__frame

    @property
    def framesize(self):
        '''
        :rtype: str
        '''

        return self.__framesize

    @property
    def genus(self):
        '''
        :rtype: str
        '''

        return self.__genus

    @property
    def gparent(self):
        '''
        :rtype: str
        '''

        return self.__gparent

    @property
    def grainsize(self):
        '''
        :rtype: str
        '''

        return self.__grainsize

    @property
    def habitat(self):
        '''
        :rtype: str
        '''

        return self.__habitat

    @property
    def hardness(self):
        '''
        :rtype: str
        '''

        return self.__hardness

    @property
    def height(self):
        '''
        :rtype: Decimal
        '''

        return self.__height

    @property
    def heightft(self):
        '''
        :rtype: Decimal
        '''

        return self.__heightft

    @property
    def heightin(self):
        '''
        :rtype: Decimal
        '''

        return self.__heightin

    @property
    def homeloc(self):
        '''
        :rtype: str
        '''

        return self.__homeloc

    @property
    def idby(self):
        '''
        :rtype: str
        '''

        return self.__idby

    @property
    def iddate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__iddate

    @property
    def imagefile(self):
        '''
        :rtype: str
        '''

        return self.__imagefile

    @property
    def imageno(self):
        '''
        :rtype: int
        '''

        return self.__imageno

    @property
    def imagesize(self):
        '''
        :rtype: str
        '''

        return self.__imagesize

    @property
    def inscomp(self):
        '''
        :rtype: str
        '''

        return self.__inscomp

    @property
    def inscrlang(self):
        '''
        :rtype: str
        '''

        return self.__inscrlang

    @property
    def inscrpos(self):
        '''
        :rtype: str
        '''

        return self.__inscrpos

    @property
    def inscrtech(self):
        '''
        :rtype: str
        '''

        return self.__inscrtech

    @property
    def inscrtext(self):
        '''
        :rtype: str
        '''

        return self.__inscrtext

    @property
    def inscrtrans(self):
        '''
        :rtype: str
        '''

        return self.__inscrtrans

    @property
    def inscrtype(self):
        '''
        :rtype: str
        '''

        return self.__inscrtype

    @property
    def insdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__insdate

    @property
    def insphone(self):
        '''
        :rtype: str
        '''

        return self.__insphone

    @property
    def inspremium(self):
        '''
        :rtype: str
        '''

        return self.__inspremium

    @property
    def insrep(self):
        '''
        :rtype: str
        '''

        return self.__insrep

    @property
    def insvalue(self):
        '''
        :rtype: Decimal
        '''

        return self.__insvalue

    @property
    def invnby(self):
        '''
        :rtype: str
        '''

        return self.__invnby

    @property
    def invndate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__invndate

    @property
    def kingdom(self):
        '''
        :rtype: str
        '''

        return self.__kingdom

    @property
    def latdeg(self):
        '''
        :rtype: Decimal
        '''

        return self.__latdeg

    @property
    def latedate(self):
        '''
        :rtype: int
        '''

        return self.__latedate

    @property
    def legal(self):
        '''
        :rtype: str
        '''

        return self.__legal

    @property
    def length(self):
        '''
        :rtype: Decimal
        '''

        return self.__length

    @property
    def lengthft(self):
        '''
        :rtype: Decimal
        '''

        return self.__lengthft

    @property
    def lengthin(self):
        '''
        :rtype: Decimal
        '''

        return self.__lengthin

    @property
    def level(self):
        '''
        :rtype: str
        '''

        return self.__level

    @property
    def lithofacie(self):
        '''
        :rtype: str
        '''

        return self.__lithofacie

    @property
    def loancond(self):
        '''
        :rtype: str
        '''

        return self.__loancond

    @property
    def loandue(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__loandue

    @property
    def loanid(self):
        '''
        :rtype: str
        '''

        return self.__loanid

    @property
    def loaninno(self):
        '''
        :rtype: str
        '''

        return self.__loaninno

    @property
    def loanno(self):
        '''
        :rtype: int
        '''

        return self.__loanno

    @property
    def loanrenew(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__loanrenew

    @property
    def locfield1(self):
        '''
        :rtype: str
        '''

        return self.__locfield1

    @property
    def locfield2(self):
        '''
        :rtype: str
        '''

        return self.__locfield2

    @property
    def locfield3(self):
        '''
        :rtype: str
        '''

        return self.__locfield3

    @property
    def locfield4(self):
        '''
        :rtype: str
        '''

        return self.__locfield4

    @property
    def locfield5(self):
        '''
        :rtype: str
        '''

        return self.__locfield5

    @property
    def locfield6(self):
        '''
        :rtype: str
        '''

        return self.__locfield6

    @property
    def longdeg(self):
        '''
        :rtype: Decimal
        '''

        return self.__longdeg

    @property
    def luster(self):
        '''
        :rtype: str
        '''

        return self.__luster

    @property
    def made(self):
        '''
        :rtype: str
        '''

        return self.__made

    @property
    def maintcycle(self):
        '''
        :rtype: str
        '''

        return self.__maintcycle

    @property
    def maintdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__maintdate

    @property
    def maintnote(self):
        '''
        :rtype: str
        '''

        return self.__maintnote

    @property
    def material(self):
        '''
        :rtype: str
        '''

        return self.__material

    @property
    def medium(self):
        '''
        :rtype: str
        '''

        return self.__medium

    @property
    def member(self):
        '''
        :rtype: str
        '''

        return self.__member

    @property
    def mmark(self):
        '''
        :rtype: str
        '''

        return self.__mmark

    @property
    def nhclass(self):
        '''
        :rtype: str
        '''

        return self.__nhclass

    @property
    def nhorder(self):
        '''
        :rtype: str
        '''

        return self.__nhorder

    @property
    def notes(self):
        '''
        :rtype: str
        '''

        return self.__notes

    @property
    def ns(self):
        '''
        :rtype: str
        '''

        return self.__ns

    @property
    def objectid(self):
        '''
        :rtype: str
        '''

        return self.__objectid

    @property
    def objname(self):
        '''
        :rtype: str
        '''

        return self.__objname

    @property
    def objname2(self):
        '''
        :rtype: str
        '''

        return self.__objname2

    @property
    def objname3(self):
        '''
        :rtype: str
        '''

        return self.__objname3

    @property
    def objnames(self):
        '''
        :rtype: str
        '''

        return self.__objnames

    @property
    def occurrence(self):
        '''
        :rtype: str
        '''

        return self.__occurrence

    @property
    def oldno(self):
        '''
        :rtype: str
        '''

        return self.__oldno

    @property
    def origin(self):
        '''
        :rtype: str
        '''

        return self.__origin

    @property
    def othername(self):
        '''
        :rtype: str
        '''

        return self.__othername

    @property
    def otherno(self):
        '''
        :rtype: str
        '''

        return self.__otherno

    @property
    def outdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__outdate

    @property
    def owned(self):
        '''
        :rtype: str
        '''

        return self.__owned

    @property
    def parent(self):
        '''
        :rtype: str
        '''

        return self.__parent

    @property
    def people(self):
        '''
        :rtype: str
        '''

        return self.__people

    @property
    def period(self):
        '''
        :rtype: str
        '''

        return self.__period

    @property
    def phylum(self):
        '''
        :rtype: str
        '''

        return self.__phylum

    @property
    def policyno(self):
        '''
        :rtype: str
        '''

        return self.__policyno

    @property
    def ppid(self):
        '''
        :rtype: str
        '''

        return self.__ppid

    @property
    def preparator(self):
        '''
        :rtype: str
        '''

        return self.__preparator

    @property
    def prepdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__prepdate

    @property
    def preserve(self):
        '''
        :rtype: str
        '''

        return self.__preserve

    @property
    def pressure(self):
        '''
        :rtype: str
        '''

        return self.__pressure

    @property
    def provenance(self):
        '''
        :rtype: str
        '''

        return self.__provenance

    @property
    def pubnotes(self):
        '''
        :rtype: str
        '''

        return self.__pubnotes

    @property
    def qrurl(self):
        '''
        :rtype: str
        '''

        return self.__qrurl

    @classmethod
    def read(cls, iprot):
        '''
        Read a new object from the given input protocol and return the object.

        :type iprot: thryft.protocol._input_protocol._InputProtocol
        :rtype: pastpy.models.object_record.ObjectRecord
        '''

        init_kwds = {}

        iprot.read_struct_begin()
        while True:
            ifield_name, ifield_type, _ifield_id = iprot.read_field_begin()
            if ifield_type == 0: # STOP
                break
            elif ifield_name == 'accessno':
                try:
                    init_kwds['accessno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'accessory':
                try:
                    init_kwds['accessory'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'acqvalue':
                try:
                    init_kwds['acqvalue'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'age':
                try:
                    init_kwds['age'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'appnotes':
                try:
                    init_kwds['appnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'appraisor':
                try:
                    init_kwds['appraisor'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'assemzone':
                try:
                    init_kwds['assemzone'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'bagno':
                try:
                    init_kwds['bagno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'boxno':
                try:
                    init_kwds['boxno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'caption':
                try:
                    init_kwds['caption'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'cat':
                try:
                    init_kwds['cat'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'catby':
                try:
                    init_kwds['catby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'catdate':
                try:
                    init_kwds['catdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'cattype':
                try:
                    init_kwds['cattype'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'chemcomp':
                try:
                    init_kwds['chemcomp'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'circum':
                try:
                    init_kwds['circum'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'circumft':
                try:
                    init_kwds['circumft'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'circumin':
                try:
                    init_kwds['circumin'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'classes':
                try:
                    init_kwds['classes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'colldate':
                try:
                    init_kwds['colldate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'collection':
                try:
                    init_kwds['collection'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'collector':
                try:
                    init_kwds['collector'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'conddate':
                try:
                    init_kwds['conddate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'condexam':
                try:
                    init_kwds['condexam'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'condition':
                try:
                    init_kwds['condition'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'condnotes':
                try:
                    init_kwds['condnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'count':
                try:
                    init_kwds['count'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'creator':
                try:
                    init_kwds['creator'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'creator2':
                try:
                    init_kwds['creator2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'creator3':
                try:
                    init_kwds['creator3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'credit':
                try:
                    init_kwds['credit'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'crystal':
                try:
                    init_kwds['crystal'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'culture':
                try:
                    init_kwds['culture'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'curvalmax':
                try:
                    init_kwds['curvalmax'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'curvalue':
                try:
                    init_kwds['curvalue'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'dataset':
                try:
                    init_kwds['dataset'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'date':
                try:
                    init_kwds['date'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'datingmeth':
                try:
                    init_kwds['datingmeth'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'datum':
                try:
                    init_kwds['datum'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'depth':
                try:
                    init_kwds['depth'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'depthft':
                try:
                    init_kwds['depthft'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'depthin':
                try:
                    init_kwds['depthin'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'descrip':
                try:
                    init_kwds['descrip'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'diameter':
                try:
                    init_kwds['diameter'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'diameterft':
                try:
                    init_kwds['diameterft'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'diameterin':
                try:
                    init_kwds['diameterin'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'dimnotes':
                try:
                    init_kwds['dimnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'dimtype':
                try:
                    init_kwds['dimtype'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'dispvalue':
                try:
                    init_kwds['dispvalue'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'earlydate':
                try:
                    init_kwds['earlydate'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'elements':
                try:
                    init_kwds['elements'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'epoch':
                try:
                    init_kwds['epoch'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'era':
                try:
                    init_kwds['era'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'event':
                try:
                    init_kwds['event'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'ew':
                try:
                    init_kwds['ew'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'excavadate':
                try:
                    init_kwds['excavadate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'excavateby':
                try:
                    init_kwds['excavateby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'exhibitid':
                try:
                    init_kwds['exhibitid'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'exhibitno':
                try:
                    init_kwds['exhibitno'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'exhlabel1':
                try:
                    init_kwds['exhlabel1'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'exhlabel2':
                try:
                    init_kwds['exhlabel2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'exhlabel3':
                try:
                    init_kwds['exhlabel3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'exhlabel4':
                try:
                    init_kwds['exhlabel4'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'exhstart':
                try:
                    init_kwds['exhstart'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'family':
                try:
                    init_kwds['family'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'feature':
                try:
                    init_kwds['feature'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'flagdate':
                try:
                    init_kwds['flagdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'flagnotes':
                try:
                    init_kwds['flagnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'flagreason':
                try:
                    init_kwds['flagreason'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'formation':
                try:
                    init_kwds['formation'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'fossils':
                try:
                    init_kwds['fossils'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'found':
                try:
                    init_kwds['found'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'fracture':
                try:
                    init_kwds['fracture'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'frame':
                try:
                    init_kwds['frame'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'framesize':
                try:
                    init_kwds['framesize'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'genus':
                try:
                    init_kwds['genus'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'gparent':
                try:
                    init_kwds['gparent'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'grainsize':
                try:
                    init_kwds['grainsize'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'habitat':
                try:
                    init_kwds['habitat'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'hardness':
                try:
                    init_kwds['hardness'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'height':
                try:
                    init_kwds['height'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'heightft':
                try:
                    init_kwds['heightft'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'heightin':
                try:
                    init_kwds['heightin'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'homeloc':
                try:
                    init_kwds['homeloc'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'idby':
                try:
                    init_kwds['idby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'iddate':
                try:
                    init_kwds['iddate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'imagefile':
                try:
                    init_kwds['imagefile'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'imageno':
                try:
                    init_kwds['imageno'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'imagesize':
                try:
                    init_kwds['imagesize'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inscomp':
                try:
                    init_kwds['inscomp'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inscrlang':
                try:
                    init_kwds['inscrlang'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inscrpos':
                try:
                    init_kwds['inscrpos'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inscrtech':
                try:
                    init_kwds['inscrtech'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inscrtext':
                try:
                    init_kwds['inscrtext'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inscrtrans':
                try:
                    init_kwds['inscrtrans'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inscrtype':
                try:
                    init_kwds['inscrtype'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'insdate':
                try:
                    init_kwds['insdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'insphone':
                try:
                    init_kwds['insphone'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'inspremium':
                try:
                    init_kwds['inspremium'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'insrep':
                try:
                    init_kwds['insrep'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'insvalue':
                try:
                    init_kwds['insvalue'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'invnby':
                try:
                    init_kwds['invnby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'invndate':
                try:
                    init_kwds['invndate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'kingdom':
                try:
                    init_kwds['kingdom'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'latdeg':
                try:
                    init_kwds['latdeg'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'latedate':
                try:
                    init_kwds['latedate'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'legal':
                try:
                    init_kwds['legal'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'length':
                try:
                    init_kwds['length'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'lengthft':
                try:
                    init_kwds['lengthft'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'lengthin':
                try:
                    init_kwds['lengthin'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'level':
                try:
                    init_kwds['level'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'lithofacie':
                try:
                    init_kwds['lithofacie'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'loancond':
                try:
                    init_kwds['loancond'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'loandue':
                try:
                    init_kwds['loandue'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'loanid':
                try:
                    init_kwds['loanid'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'loaninno':
                try:
                    init_kwds['loaninno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'loanno':
                try:
                    init_kwds['loanno'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'loanrenew':
                try:
                    init_kwds['loanrenew'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'locfield1':
                try:
                    init_kwds['locfield1'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'locfield2':
                try:
                    init_kwds['locfield2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'locfield3':
                try:
                    init_kwds['locfield3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'locfield4':
                try:
                    init_kwds['locfield4'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'locfield5':
                try:
                    init_kwds['locfield5'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'locfield6':
                try:
                    init_kwds['locfield6'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'longdeg':
                try:
                    init_kwds['longdeg'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'luster':
                try:
                    init_kwds['luster'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'made':
                try:
                    init_kwds['made'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'maintcycle':
                try:
                    init_kwds['maintcycle'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'maintdate':
                try:
                    init_kwds['maintdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'maintnote':
                try:
                    init_kwds['maintnote'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'material':
                try:
                    init_kwds['material'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'medium':
                try:
                    init_kwds['medium'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'member':
                try:
                    init_kwds['member'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'mmark':
                try:
                    init_kwds['mmark'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'nhclass':
                try:
                    init_kwds['nhclass'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'nhorder':
                try:
                    init_kwds['nhorder'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'notes':
                try:
                    init_kwds['notes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'ns':
                try:
                    init_kwds['ns'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'objectid':
                try:
                    init_kwds['objectid'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'objname':
                try:
                    init_kwds['objname'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'objname2':
                try:
                    init_kwds['objname2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'objname3':
                try:
                    init_kwds['objname3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'objnames':
                try:
                    init_kwds['objnames'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'occurrence':
                try:
                    init_kwds['occurrence'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'oldno':
                try:
                    init_kwds['oldno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'origin':
                try:
                    init_kwds['origin'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'othername':
                try:
                    init_kwds['othername'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'otherno':
                try:
                    init_kwds['otherno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'outdate':
                try:
                    init_kwds['outdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'owned':
                try:
                    init_kwds['owned'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'parent':
                try:
                    init_kwds['parent'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'people':
                try:
                    init_kwds['people'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'period':
                try:
                    init_kwds['period'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'phylum':
                try:
                    init_kwds['phylum'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'policyno':
                try:
                    init_kwds['policyno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'ppid':
                try:
                    init_kwds['ppid'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'preparator':
                try:
                    init_kwds['preparator'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'prepdate':
                try:
                    init_kwds['prepdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'preserve':
                try:
                    init_kwds['preserve'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'pressure':
                try:
                    init_kwds['pressure'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'provenance':
                try:
                    init_kwds['provenance'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'pubnotes':
                try:
                    init_kwds['pubnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'qrurl':
                try:
                    init_kwds['qrurl'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'recas':
                try:
                    init_kwds['recas'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'recdate':
                try:
                    init_kwds['recdate'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'recfrom':
                try:
                    init_kwds['recfrom'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'relation':
                try:
                    init_kwds['relation'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'relnotes':
                try:
                    init_kwds['relnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'renewuntil':
                try:
                    init_kwds['renewuntil'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'repatby':
                try:
                    init_kwds['repatby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'repatclaim':
                try:
                    init_kwds['repatclaim'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'repatdate':
                try:
                    init_kwds['repatdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'repatdisp':
                try:
                    init_kwds['repatdisp'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'repathand':
                try:
                    init_kwds['repathand'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'repatnotes':
                try:
                    init_kwds['repatnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'repatnotic':
                try:
                    init_kwds['repatnotic'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'repattype':
                try:
                    init_kwds['repattype'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'rockclass':
                try:
                    init_kwds['rockclass'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'rockcolor':
                try:
                    init_kwds['rockcolor'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'rockorigin':
                try:
                    init_kwds['rockorigin'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'rocktype':
                try:
                    init_kwds['rocktype'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'role':
                try:
                    init_kwds['role'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'role2':
                try:
                    init_kwds['role2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'role3':
                try:
                    init_kwds['role3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'school':
                try:
                    init_kwds['school'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'sex':
                try:
                    init_kwds['sex'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'sgflag':
                try:
                    init_kwds['sgflag'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'signedname':
                try:
                    init_kwds['signedname'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'signloc':
                try:
                    init_kwds['signloc'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'site':
                try:
                    init_kwds['site'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'siteno':
                try:
                    init_kwds['siteno'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'specgrav':
                try:
                    init_kwds['specgrav'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'species':
                try:
                    init_kwds['species'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'sprocess':
                try:
                    init_kwds['sprocess'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'stage':
                try:
                    init_kwds['stage'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'status':
                try:
                    init_kwds['status'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'statusby':
                try:
                    init_kwds['statusby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'statusdate':
                try:
                    init_kwds['statusdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'sterms':
                try:
                    init_kwds['sterms'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'stratum':
                try:
                    init_kwds['stratum'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'streak':
                try:
                    init_kwds['streak'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'subfamily':
                try:
                    init_kwds['subfamily'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'subjects':
                try:
                    init_kwds['subjects'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'subspecies':
                try:
                    init_kwds['subspecies'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'technique':
                try:
                    init_kwds['technique'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tempauthor':
                try:
                    init_kwds['tempauthor'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tempby':
                try:
                    init_kwds['tempby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tempdate':
                try:
                    init_kwds['tempdate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'temperatur':
                try:
                    init_kwds['temperatur'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'temploc':
                try:
                    init_kwds['temploc'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tempnotes':
                try:
                    init_kwds['tempnotes'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tempreason':
                try:
                    init_kwds['tempreason'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tempuntil':
                try:
                    init_kwds['tempuntil'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'texture':
                try:
                    init_kwds['texture'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'title':
                try:
                    init_kwds['title'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tlocfield1':
                try:
                    init_kwds['tlocfield1'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tlocfield2':
                try:
                    init_kwds['tlocfield2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tlocfield3':
                try:
                    init_kwds['tlocfield3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tlocfield4':
                try:
                    init_kwds['tlocfield4'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tlocfield5':
                try:
                    init_kwds['tlocfield5'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'tlocfield6':
                try:
                    init_kwds['tlocfield6'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf1':
                try:
                    init_kwds['udf1'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf10':
                try:
                    init_kwds['udf10'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf11':
                try:
                    init_kwds['udf11'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf12':
                try:
                    init_kwds['udf12'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf13':
                try:
                    init_kwds['udf13'] = iprot.read_i32()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf14':
                try:
                    init_kwds['udf14'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'udf15':
                try:
                    init_kwds['udf15'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'udf16':
                try:
                    init_kwds['udf16'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'udf17':
                try:
                    init_kwds['udf17'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'udf18':
                try:
                    init_kwds['udf18'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'udf19':
                try:
                    init_kwds['udf19'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'udf2':
                try:
                    init_kwds['udf2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf20':
                try:
                    init_kwds['udf20'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'udf21':
                try:
                    init_kwds['udf21'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf22':
                try:
                    init_kwds['udf22'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf3':
                try:
                    init_kwds['udf3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf4':
                try:
                    init_kwds['udf4'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf5':
                try:
                    init_kwds['udf5'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf6':
                try:
                    init_kwds['udf6'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf7':
                try:
                    init_kwds['udf7'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf8':
                try:
                    init_kwds['udf8'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'udf9':
                try:
                    init_kwds['udf9'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'unit':
                try:
                    init_kwds['unit'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'updated':
                try:
                    init_kwds['updated'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'updatedby':
                try:
                    init_kwds['updatedby'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'used':
                try:
                    init_kwds['used'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'valuedate':
                try:
                    init_kwds['valuedate'] = iprot.read_date_time()
                except (TypeError,):
                    pass
            elif ifield_name == 'varieties':
                try:
                    init_kwds['varieties'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'vexhtml':
                try:
                    init_kwds['vexhtml'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'vexlabel1':
                try:
                    init_kwds['vexlabel1'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'vexlabel2':
                try:
                    init_kwds['vexlabel2'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'vexlabel3':
                try:
                    init_kwds['vexlabel3'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'vexlabel4':
                try:
                    init_kwds['vexlabel4'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'webinclude':
                try:
                    init_kwds['webinclude'] = iprot.read_bool()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'weight':
                try:
                    init_kwds['weight'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'weightin':
                try:
                    init_kwds['weightin'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'weightlb':
                try:
                    init_kwds['weightlb'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'width':
                try:
                    init_kwds['width'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'widthft':
                try:
                    init_kwds['widthft'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'widthin':
                try:
                    init_kwds['widthin'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'xcord':
                try:
                    init_kwds['xcord'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'ycord':
                try:
                    init_kwds['ycord'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'zcord':
                try:
                    init_kwds['zcord'] = iprot.read_decimal()
                except (decimal.InvalidOperation, TypeError,):
                    pass
            elif ifield_name == 'zsorter':
                try:
                    init_kwds['zsorter'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            elif ifield_name == 'zsorterx':
                try:
                    init_kwds['zsorterx'] = iprot.read_string()
                except (TypeError, ValueError,):
                    pass
            iprot.read_field_end()
        iprot.read_struct_end()

        return cls(**init_kwds)

    @property
    def recas(self):
        '''
        :rtype: str
        '''

        return self.__recas

    @property
    def recdate(self):
        '''
        :rtype: str
        '''

        return self.__recdate

    @property
    def recfrom(self):
        '''
        :rtype: str
        '''

        return self.__recfrom

    @property
    def relation(self):
        '''
        :rtype: str
        '''

        return self.__relation

    @property
    def relnotes(self):
        '''
        :rtype: str
        '''

        return self.__relnotes

    @property
    def renewuntil(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__renewuntil

    @property
    def repatby(self):
        '''
        :rtype: str
        '''

        return self.__repatby

    @property
    def repatclaim(self):
        '''
        :rtype: str
        '''

        return self.__repatclaim

    @property
    def repatdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__repatdate

    @property
    def repatdisp(self):
        '''
        :rtype: str
        '''

        return self.__repatdisp

    @property
    def repathand(self):
        '''
        :rtype: str
        '''

        return self.__repathand

    @property
    def repatnotes(self):
        '''
        :rtype: str
        '''

        return self.__repatnotes

    @property
    def repatnotic(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__repatnotic

    @property
    def repattype(self):
        '''
        :rtype: str
        '''

        return self.__repattype

    def replace(
        self,
        accessno=None,
        accessory=None,
        acqvalue=None,
        age=None,
        appnotes=None,
        appraisor=None,
        assemzone=None,
        bagno=None,
        boxno=None,
        caption=None,
        cat=None,
        catby=None,
        catdate=None,
        cattype=None,
        chemcomp=None,
        circum=None,
        circumft=None,
        circumin=None,
        classes=None,
        colldate=None,
        collection=None,
        collector=None,
        conddate=None,
        condexam=None,
        condition=None,
        condnotes=None,
        count=None,
        creator=None,
        creator2=None,
        creator3=None,
        credit=None,
        crystal=None,
        culture=None,
        curvalmax=None,
        curvalue=None,
        dataset=None,
        date=None,
        datingmeth=None,
        datum=None,
        depth=None,
        depthft=None,
        depthin=None,
        descrip=None,
        diameter=None,
        diameterft=None,
        diameterin=None,
        dimnotes=None,
        dimtype=None,
        dispvalue=None,
        earlydate=None,
        elements=None,
        epoch=None,
        era=None,
        event=None,
        ew=None,
        excavadate=None,
        excavateby=None,
        exhibitid=None,
        exhibitno=None,
        exhlabel1=None,
        exhlabel2=None,
        exhlabel3=None,
        exhlabel4=None,
        exhstart=None,
        family=None,
        feature=None,
        flagdate=None,
        flagnotes=None,
        flagreason=None,
        formation=None,
        fossils=None,
        found=None,
        fracture=None,
        frame=None,
        framesize=None,
        genus=None,
        gparent=None,
        grainsize=None,
        habitat=None,
        hardness=None,
        height=None,
        heightft=None,
        heightin=None,
        homeloc=None,
        idby=None,
        iddate=None,
        imagefile=None,
        imageno=None,
        imagesize=None,
        inscomp=None,
        inscrlang=None,
        inscrpos=None,
        inscrtech=None,
        inscrtext=None,
        inscrtrans=None,
        inscrtype=None,
        insdate=None,
        insphone=None,
        inspremium=None,
        insrep=None,
        insvalue=None,
        invnby=None,
        invndate=None,
        kingdom=None,
        latdeg=None,
        latedate=None,
        legal=None,
        length=None,
        lengthft=None,
        lengthin=None,
        level=None,
        lithofacie=None,
        loancond=None,
        loandue=None,
        loanid=None,
        loaninno=None,
        loanno=None,
        loanrenew=None,
        locfield1=None,
        locfield2=None,
        locfield3=None,
        locfield4=None,
        locfield5=None,
        locfield6=None,
        longdeg=None,
        luster=None,
        made=None,
        maintcycle=None,
        maintdate=None,
        maintnote=None,
        material=None,
        medium=None,
        member=None,
        mmark=None,
        nhclass=None,
        nhorder=None,
        notes=None,
        ns=None,
        objectid=None,
        objname=None,
        objname2=None,
        objname3=None,
        objnames=None,
        occurrence=None,
        oldno=None,
        origin=None,
        othername=None,
        otherno=None,
        outdate=None,
        owned=None,
        parent=None,
        people=None,
        period=None,
        phylum=None,
        policyno=None,
        ppid=None,
        preparator=None,
        prepdate=None,
        preserve=None,
        pressure=None,
        provenance=None,
        pubnotes=None,
        qrurl=None,
        recas=None,
        recdate=None,
        recfrom=None,
        relation=None,
        relnotes=None,
        renewuntil=None,
        repatby=None,
        repatclaim=None,
        repatdate=None,
        repatdisp=None,
        repathand=None,
        repatnotes=None,
        repatnotic=None,
        repattype=None,
        rockclass=None,
        rockcolor=None,
        rockorigin=None,
        rocktype=None,
        role=None,
        role2=None,
        role3=None,
        school=None,
        sex=None,
        sgflag=None,
        signedname=None,
        signloc=None,
        site=None,
        siteno=None,
        specgrav=None,
        species=None,
        sprocess=None,
        stage=None,
        status=None,
        statusby=None,
        statusdate=None,
        sterms=None,
        stratum=None,
        streak=None,
        subfamily=None,
        subjects=None,
        subspecies=None,
        technique=None,
        tempauthor=None,
        tempby=None,
        tempdate=None,
        temperatur=None,
        temploc=None,
        tempnotes=None,
        tempreason=None,
        tempuntil=None,
        texture=None,
        title=None,
        tlocfield1=None,
        tlocfield2=None,
        tlocfield3=None,
        tlocfield4=None,
        tlocfield5=None,
        tlocfield6=None,
        udf1=None,
        udf10=None,
        udf11=None,
        udf12=None,
        udf13=None,
        udf14=None,
        udf15=None,
        udf16=None,
        udf17=None,
        udf18=None,
        udf19=None,
        udf2=None,
        udf20=None,
        udf21=None,
        udf22=None,
        udf3=None,
        udf4=None,
        udf5=None,
        udf6=None,
        udf7=None,
        udf8=None,
        udf9=None,
        unit=None,
        updated=None,
        updatedby=None,
        used=None,
        valuedate=None,
        varieties=None,
        vexhtml=None,
        vexlabel1=None,
        vexlabel2=None,
        vexlabel3=None,
        vexlabel4=None,
        webinclude=None,
        weight=None,
        weightin=None,
        weightlb=None,
        width=None,
        widthft=None,
        widthin=None,
        xcord=None,
        ycord=None,
        zcord=None,
        zsorter=None,
        zsorterx=None,
    ):
        '''
        Copy this object, replace one or more fields, and return the copy.

        :type accessno: str or None
        :type accessory: str or None
        :type acqvalue: Decimal or None
        :type age: str or None
        :type appnotes: str or None
        :type appraisor: str or None
        :type assemzone: str or None
        :type bagno: str or None
        :type boxno: str or None
        :type caption: str or None
        :type cat: str or None
        :type catby: str or None
        :type catdate: datetime.datetime or None
        :type cattype: str or None
        :type chemcomp: str or None
        :type circum: Decimal or None
        :type circumft: Decimal or None
        :type circumin: Decimal or None
        :type classes: str or None
        :type colldate: datetime.datetime or None
        :type collection: str or None
        :type collector: str or None
        :type conddate: datetime.datetime or None
        :type condexam: str or None
        :type condition: str or None
        :type condnotes: str or None
        :type count: str or None
        :type creator: str or None
        :type creator2: str or None
        :type creator3: str or None
        :type credit: str or None
        :type crystal: str or None
        :type culture: str or None
        :type curvalmax: Decimal or None
        :type curvalue: Decimal or None
        :type dataset: str or None
        :type date: str or None
        :type datingmeth: str or None
        :type datum: str or None
        :type depth: Decimal or None
        :type depthft: Decimal or None
        :type depthin: Decimal or None
        :type descrip: str or None
        :type diameter: Decimal or None
        :type diameterft: Decimal or None
        :type diameterin: Decimal or None
        :type dimnotes: str or None
        :type dimtype: int or None
        :type dispvalue: str or None
        :type earlydate: int or None
        :type elements: str or None
        :type epoch: str or None
        :type era: str or None
        :type event: str or None
        :type ew: str or None
        :type excavadate: datetime.datetime or None
        :type excavateby: str or None
        :type exhibitid: str or None
        :type exhibitno: int or None
        :type exhlabel1: str or None
        :type exhlabel2: str or None
        :type exhlabel3: str or None
        :type exhlabel4: str or None
        :type exhstart: datetime.datetime or None
        :type family: str or None
        :type feature: str or None
        :type flagdate: datetime.datetime or None
        :type flagnotes: str or None
        :type flagreason: str or None
        :type formation: str or None
        :type fossils: str or None
        :type found: str or None
        :type fracture: str or None
        :type frame: str or None
        :type framesize: str or None
        :type genus: str or None
        :type gparent: str or None
        :type grainsize: str or None
        :type habitat: str or None
        :type hardness: str or None
        :type height: Decimal or None
        :type heightft: Decimal or None
        :type heightin: Decimal or None
        :type homeloc: str or None
        :type idby: str or None
        :type iddate: datetime.datetime or None
        :type imagefile: str or None
        :type imageno: int or None
        :type imagesize: str or None
        :type inscomp: str or None
        :type inscrlang: str or None
        :type inscrpos: str or None
        :type inscrtech: str or None
        :type inscrtext: str or None
        :type inscrtrans: str or None
        :type inscrtype: str or None
        :type insdate: datetime.datetime or None
        :type insphone: str or None
        :type inspremium: str or None
        :type insrep: str or None
        :type insvalue: Decimal or None
        :type invnby: str or None
        :type invndate: datetime.datetime or None
        :type kingdom: str or None
        :type latdeg: Decimal or None
        :type latedate: int or None
        :type legal: str or None
        :type length: Decimal or None
        :type lengthft: Decimal or None
        :type lengthin: Decimal or None
        :type level: str or None
        :type lithofacie: str or None
        :type loancond: str or None
        :type loandue: datetime.datetime or None
        :type loanid: str or None
        :type loaninno: str or None
        :type loanno: int or None
        :type loanrenew: datetime.datetime or None
        :type locfield1: str or None
        :type locfield2: str or None
        :type locfield3: str or None
        :type locfield4: str or None
        :type locfield5: str or None
        :type locfield6: str or None
        :type longdeg: Decimal or None
        :type luster: str or None
        :type made: str or None
        :type maintcycle: str or None
        :type maintdate: datetime.datetime or None
        :type maintnote: str or None
        :type material: str or None
        :type medium: str or None
        :type member: str or None
        :type mmark: str or None
        :type nhclass: str or None
        :type nhorder: str or None
        :type notes: str or None
        :type ns: str or None
        :type objectid: str or None
        :type objname: str or None
        :type objname2: str or None
        :type objname3: str or None
        :type objnames: str or None
        :type occurrence: str or None
        :type oldno: str or None
        :type origin: str or None
        :type othername: str or None
        :type otherno: str or None
        :type outdate: datetime.datetime or None
        :type owned: str or None
        :type parent: str or None
        :type people: str or None
        :type period: str or None
        :type phylum: str or None
        :type policyno: str or None
        :type ppid: str or None
        :type preparator: str or None
        :type prepdate: datetime.datetime or None
        :type preserve: str or None
        :type pressure: str or None
        :type provenance: str or None
        :type pubnotes: str or None
        :type qrurl: str or None
        :type recas: str or None
        :type recdate: str or None
        :type recfrom: str or None
        :type relation: str or None
        :type relnotes: str or None
        :type renewuntil: datetime.datetime or None
        :type repatby: str or None
        :type repatclaim: str or None
        :type repatdate: datetime.datetime or None
        :type repatdisp: str or None
        :type repathand: str or None
        :type repatnotes: str or None
        :type repatnotic: datetime.datetime or None
        :type repattype: str or None
        :type rockclass: str or None
        :type rockcolor: str or None
        :type rockorigin: str or None
        :type rocktype: str or None
        :type role: str or None
        :type role2: str or None
        :type role3: str or None
        :type school: str or None
        :type sex: str or None
        :type sgflag: str or None
        :type signedname: str or None
        :type signloc: str or None
        :type site: str or None
        :type siteno: str or None
        :type specgrav: str or None
        :type species: str or None
        :type sprocess: str or None
        :type stage: str or None
        :type status: str or None
        :type statusby: str or None
        :type statusdate: datetime.datetime or None
        :type sterms: str or None
        :type stratum: str or None
        :type streak: str or None
        :type subfamily: str or None
        :type subjects: str or None
        :type subspecies: str or None
        :type technique: str or None
        :type tempauthor: str or None
        :type tempby: str or None
        :type tempdate: datetime.datetime or None
        :type temperatur: str or None
        :type temploc: str or None
        :type tempnotes: str or None
        :type tempreason: str or None
        :type tempuntil: str or None
        :type texture: str or None
        :type title: str or None
        :type tlocfield1: str or None
        :type tlocfield2: str or None
        :type tlocfield3: str or None
        :type tlocfield4: str or None
        :type tlocfield5: str or None
        :type tlocfield6: str or None
        :type udf1: str or None
        :type udf10: str or None
        :type udf11: str or None
        :type udf12: str or None
        :type udf13: int or None
        :type udf14: Decimal or None
        :type udf15: Decimal or None
        :type udf16: Decimal or None
        :type udf17: Decimal or None
        :type udf18: datetime.datetime or None
        :type udf19: datetime.datetime or None
        :type udf2: str or None
        :type udf20: datetime.datetime or None
        :type udf21: str or None
        :type udf22: str or None
        :type udf3: str or None
        :type udf4: str or None
        :type udf5: str or None
        :type udf6: str or None
        :type udf7: str or None
        :type udf8: str or None
        :type udf9: str or None
        :type unit: str or None
        :type updated: datetime.datetime or None
        :type updatedby: str or None
        :type used: str or None
        :type valuedate: datetime.datetime or None
        :type varieties: str or None
        :type vexhtml: str or None
        :type vexlabel1: str or None
        :type vexlabel2: str or None
        :type vexlabel3: str or None
        :type vexlabel4: str or None
        :type webinclude: bool or None
        :type weight: Decimal or None
        :type weightin: Decimal or None
        :type weightlb: Decimal or None
        :type width: Decimal or None
        :type widthft: Decimal or None
        :type widthin: Decimal or None
        :type xcord: Decimal or None
        :type ycord: Decimal or None
        :type zcord: Decimal or None
        :type zsorter: str or None
        :type zsorterx: str or None
        :rtype: pastpy.models.object_record.ObjectRecord
        '''

        if accessno is None:
            accessno = self.accessno
        if accessory is None:
            accessory = self.accessory
        if acqvalue is None:
            acqvalue = self.acqvalue
        if age is None:
            age = self.age
        if appnotes is None:
            appnotes = self.appnotes
        if appraisor is None:
            appraisor = self.appraisor
        if assemzone is None:
            assemzone = self.assemzone
        if bagno is None:
            bagno = self.bagno
        if boxno is None:
            boxno = self.boxno
        if caption is None:
            caption = self.caption
        if cat is None:
            cat = self.cat
        if catby is None:
            catby = self.catby
        if catdate is None:
            catdate = self.catdate
        if cattype is None:
            cattype = self.cattype
        if chemcomp is None:
            chemcomp = self.chemcomp
        if circum is None:
            circum = self.circum
        if circumft is None:
            circumft = self.circumft
        if circumin is None:
            circumin = self.circumin
        if classes is None:
            classes = self.classes
        if colldate is None:
            colldate = self.colldate
        if collection is None:
            collection = self.collection
        if collector is None:
            collector = self.collector
        if conddate is None:
            conddate = self.conddate
        if condexam is None:
            condexam = self.condexam
        if condition is None:
            condition = self.condition
        if condnotes is None:
            condnotes = self.condnotes
        if count is None:
            count = self.count
        if creator is None:
            creator = self.creator
        if creator2 is None:
            creator2 = self.creator2
        if creator3 is None:
            creator3 = self.creator3
        if credit is None:
            credit = self.credit
        if crystal is None:
            crystal = self.crystal
        if culture is None:
            culture = self.culture
        if curvalmax is None:
            curvalmax = self.curvalmax
        if curvalue is None:
            curvalue = self.curvalue
        if dataset is None:
            dataset = self.dataset
        if date is None:
            date = self.date
        if datingmeth is None:
            datingmeth = self.datingmeth
        if datum is None:
            datum = self.datum
        if depth is None:
            depth = self.depth
        if depthft is None:
            depthft = self.depthft
        if depthin is None:
            depthin = self.depthin
        if descrip is None:
            descrip = self.descrip
        if diameter is None:
            diameter = self.diameter
        if diameterft is None:
            diameterft = self.diameterft
        if diameterin is None:
            diameterin = self.diameterin
        if dimnotes is None:
            dimnotes = self.dimnotes
        if dimtype is None:
            dimtype = self.dimtype
        if dispvalue is None:
            dispvalue = self.dispvalue
        if earlydate is None:
            earlydate = self.earlydate
        if elements is None:
            elements = self.elements
        if epoch is None:
            epoch = self.epoch
        if era is None:
            era = self.era
        if event is None:
            event = self.event
        if ew is None:
            ew = self.ew
        if excavadate is None:
            excavadate = self.excavadate
        if excavateby is None:
            excavateby = self.excavateby
        if exhibitid is None:
            exhibitid = self.exhibitid
        if exhibitno is None:
            exhibitno = self.exhibitno
        if exhlabel1 is None:
            exhlabel1 = self.exhlabel1
        if exhlabel2 is None:
            exhlabel2 = self.exhlabel2
        if exhlabel3 is None:
            exhlabel3 = self.exhlabel3
        if exhlabel4 is None:
            exhlabel4 = self.exhlabel4
        if exhstart is None:
            exhstart = self.exhstart
        if family is None:
            family = self.family
        if feature is None:
            feature = self.feature
        if flagdate is None:
            flagdate = self.flagdate
        if flagnotes is None:
            flagnotes = self.flagnotes
        if flagreason is None:
            flagreason = self.flagreason
        if formation is None:
            formation = self.formation
        if fossils is None:
            fossils = self.fossils
        if found is None:
            found = self.found
        if fracture is None:
            fracture = self.fracture
        if frame is None:
            frame = self.frame
        if framesize is None:
            framesize = self.framesize
        if genus is None:
            genus = self.genus
        if gparent is None:
            gparent = self.gparent
        if grainsize is None:
            grainsize = self.grainsize
        if habitat is None:
            habitat = self.habitat
        if hardness is None:
            hardness = self.hardness
        if height is None:
            height = self.height
        if heightft is None:
            heightft = self.heightft
        if heightin is None:
            heightin = self.heightin
        if homeloc is None:
            homeloc = self.homeloc
        if idby is None:
            idby = self.idby
        if iddate is None:
            iddate = self.iddate
        if imagefile is None:
            imagefile = self.imagefile
        if imageno is None:
            imageno = self.imageno
        if imagesize is None:
            imagesize = self.imagesize
        if inscomp is None:
            inscomp = self.inscomp
        if inscrlang is None:
            inscrlang = self.inscrlang
        if inscrpos is None:
            inscrpos = self.inscrpos
        if inscrtech is None:
            inscrtech = self.inscrtech
        if inscrtext is None:
            inscrtext = self.inscrtext
        if inscrtrans is None:
            inscrtrans = self.inscrtrans
        if inscrtype is None:
            inscrtype = self.inscrtype
        if insdate is None:
            insdate = self.insdate
        if insphone is None:
            insphone = self.insphone
        if inspremium is None:
            inspremium = self.inspremium
        if insrep is None:
            insrep = self.insrep
        if insvalue is None:
            insvalue = self.insvalue
        if invnby is None:
            invnby = self.invnby
        if invndate is None:
            invndate = self.invndate
        if kingdom is None:
            kingdom = self.kingdom
        if latdeg is None:
            latdeg = self.latdeg
        if latedate is None:
            latedate = self.latedate
        if legal is None:
            legal = self.legal
        if length is None:
            length = self.length
        if lengthft is None:
            lengthft = self.lengthft
        if lengthin is None:
            lengthin = self.lengthin
        if level is None:
            level = self.level
        if lithofacie is None:
            lithofacie = self.lithofacie
        if loancond is None:
            loancond = self.loancond
        if loandue is None:
            loandue = self.loandue
        if loanid is None:
            loanid = self.loanid
        if loaninno is None:
            loaninno = self.loaninno
        if loanno is None:
            loanno = self.loanno
        if loanrenew is None:
            loanrenew = self.loanrenew
        if locfield1 is None:
            locfield1 = self.locfield1
        if locfield2 is None:
            locfield2 = self.locfield2
        if locfield3 is None:
            locfield3 = self.locfield3
        if locfield4 is None:
            locfield4 = self.locfield4
        if locfield5 is None:
            locfield5 = self.locfield5
        if locfield6 is None:
            locfield6 = self.locfield6
        if longdeg is None:
            longdeg = self.longdeg
        if luster is None:
            luster = self.luster
        if made is None:
            made = self.made
        if maintcycle is None:
            maintcycle = self.maintcycle
        if maintdate is None:
            maintdate = self.maintdate
        if maintnote is None:
            maintnote = self.maintnote
        if material is None:
            material = self.material
        if medium is None:
            medium = self.medium
        if member is None:
            member = self.member
        if mmark is None:
            mmark = self.mmark
        if nhclass is None:
            nhclass = self.nhclass
        if nhorder is None:
            nhorder = self.nhorder
        if notes is None:
            notes = self.notes
        if ns is None:
            ns = self.ns
        if objectid is None:
            objectid = self.objectid
        if objname is None:
            objname = self.objname
        if objname2 is None:
            objname2 = self.objname2
        if objname3 is None:
            objname3 = self.objname3
        if objnames is None:
            objnames = self.objnames
        if occurrence is None:
            occurrence = self.occurrence
        if oldno is None:
            oldno = self.oldno
        if origin is None:
            origin = self.origin
        if othername is None:
            othername = self.othername
        if otherno is None:
            otherno = self.otherno
        if outdate is None:
            outdate = self.outdate
        if owned is None:
            owned = self.owned
        if parent is None:
            parent = self.parent
        if people is None:
            people = self.people
        if period is None:
            period = self.period
        if phylum is None:
            phylum = self.phylum
        if policyno is None:
            policyno = self.policyno
        if ppid is None:
            ppid = self.ppid
        if preparator is None:
            preparator = self.preparator
        if prepdate is None:
            prepdate = self.prepdate
        if preserve is None:
            preserve = self.preserve
        if pressure is None:
            pressure = self.pressure
        if provenance is None:
            provenance = self.provenance
        if pubnotes is None:
            pubnotes = self.pubnotes
        if qrurl is None:
            qrurl = self.qrurl
        if recas is None:
            recas = self.recas
        if recdate is None:
            recdate = self.recdate
        if recfrom is None:
            recfrom = self.recfrom
        if relation is None:
            relation = self.relation
        if relnotes is None:
            relnotes = self.relnotes
        if renewuntil is None:
            renewuntil = self.renewuntil
        if repatby is None:
            repatby = self.repatby
        if repatclaim is None:
            repatclaim = self.repatclaim
        if repatdate is None:
            repatdate = self.repatdate
        if repatdisp is None:
            repatdisp = self.repatdisp
        if repathand is None:
            repathand = self.repathand
        if repatnotes is None:
            repatnotes = self.repatnotes
        if repatnotic is None:
            repatnotic = self.repatnotic
        if repattype is None:
            repattype = self.repattype
        if rockclass is None:
            rockclass = self.rockclass
        if rockcolor is None:
            rockcolor = self.rockcolor
        if rockorigin is None:
            rockorigin = self.rockorigin
        if rocktype is None:
            rocktype = self.rocktype
        if role is None:
            role = self.role
        if role2 is None:
            role2 = self.role2
        if role3 is None:
            role3 = self.role3
        if school is None:
            school = self.school
        if sex is None:
            sex = self.sex
        if sgflag is None:
            sgflag = self.sgflag
        if signedname is None:
            signedname = self.signedname
        if signloc is None:
            signloc = self.signloc
        if site is None:
            site = self.site
        if siteno is None:
            siteno = self.siteno
        if specgrav is None:
            specgrav = self.specgrav
        if species is None:
            species = self.species
        if sprocess is None:
            sprocess = self.sprocess
        if stage is None:
            stage = self.stage
        if status is None:
            status = self.status
        if statusby is None:
            statusby = self.statusby
        if statusdate is None:
            statusdate = self.statusdate
        if sterms is None:
            sterms = self.sterms
        if stratum is None:
            stratum = self.stratum
        if streak is None:
            streak = self.streak
        if subfamily is None:
            subfamily = self.subfamily
        if subjects is None:
            subjects = self.subjects
        if subspecies is None:
            subspecies = self.subspecies
        if technique is None:
            technique = self.technique
        if tempauthor is None:
            tempauthor = self.tempauthor
        if tempby is None:
            tempby = self.tempby
        if tempdate is None:
            tempdate = self.tempdate
        if temperatur is None:
            temperatur = self.temperatur
        if temploc is None:
            temploc = self.temploc
        if tempnotes is None:
            tempnotes = self.tempnotes
        if tempreason is None:
            tempreason = self.tempreason
        if tempuntil is None:
            tempuntil = self.tempuntil
        if texture is None:
            texture = self.texture
        if title is None:
            title = self.title
        if tlocfield1 is None:
            tlocfield1 = self.tlocfield1
        if tlocfield2 is None:
            tlocfield2 = self.tlocfield2
        if tlocfield3 is None:
            tlocfield3 = self.tlocfield3
        if tlocfield4 is None:
            tlocfield4 = self.tlocfield4
        if tlocfield5 is None:
            tlocfield5 = self.tlocfield5
        if tlocfield6 is None:
            tlocfield6 = self.tlocfield6
        if udf1 is None:
            udf1 = self.udf1
        if udf10 is None:
            udf10 = self.udf10
        if udf11 is None:
            udf11 = self.udf11
        if udf12 is None:
            udf12 = self.udf12
        if udf13 is None:
            udf13 = self.udf13
        if udf14 is None:
            udf14 = self.udf14
        if udf15 is None:
            udf15 = self.udf15
        if udf16 is None:
            udf16 = self.udf16
        if udf17 is None:
            udf17 = self.udf17
        if udf18 is None:
            udf18 = self.udf18
        if udf19 is None:
            udf19 = self.udf19
        if udf2 is None:
            udf2 = self.udf2
        if udf20 is None:
            udf20 = self.udf20
        if udf21 is None:
            udf21 = self.udf21
        if udf22 is None:
            udf22 = self.udf22
        if udf3 is None:
            udf3 = self.udf3
        if udf4 is None:
            udf4 = self.udf4
        if udf5 is None:
            udf5 = self.udf5
        if udf6 is None:
            udf6 = self.udf6
        if udf7 is None:
            udf7 = self.udf7
        if udf8 is None:
            udf8 = self.udf8
        if udf9 is None:
            udf9 = self.udf9
        if unit is None:
            unit = self.unit
        if updated is None:
            updated = self.updated
        if updatedby is None:
            updatedby = self.updatedby
        if used is None:
            used = self.used
        if valuedate is None:
            valuedate = self.valuedate
        if varieties is None:
            varieties = self.varieties
        if vexhtml is None:
            vexhtml = self.vexhtml
        if vexlabel1 is None:
            vexlabel1 = self.vexlabel1
        if vexlabel2 is None:
            vexlabel2 = self.vexlabel2
        if vexlabel3 is None:
            vexlabel3 = self.vexlabel3
        if vexlabel4 is None:
            vexlabel4 = self.vexlabel4
        if webinclude is None:
            webinclude = self.webinclude
        if weight is None:
            weight = self.weight
        if weightin is None:
            weightin = self.weightin
        if weightlb is None:
            weightlb = self.weightlb
        if width is None:
            width = self.width
        if widthft is None:
            widthft = self.widthft
        if widthin is None:
            widthin = self.widthin
        if xcord is None:
            xcord = self.xcord
        if ycord is None:
            ycord = self.ycord
        if zcord is None:
            zcord = self.zcord
        if zsorter is None:
            zsorter = self.zsorter
        if zsorterx is None:
            zsorterx = self.zsorterx
        return self.__class__(accessno=accessno, accessory=accessory, acqvalue=acqvalue, age=age, appnotes=appnotes, appraisor=appraisor, assemzone=assemzone, bagno=bagno, boxno=boxno, caption=caption, cat=cat, catby=catby, catdate=catdate, cattype=cattype, chemcomp=chemcomp, circum=circum, circumft=circumft, circumin=circumin, classes=classes, colldate=colldate, collection=collection, collector=collector, conddate=conddate, condexam=condexam, condition=condition, condnotes=condnotes, count=count, creator=creator, creator2=creator2, creator3=creator3, credit=credit, crystal=crystal, culture=culture, curvalmax=curvalmax, curvalue=curvalue, dataset=dataset, date=date, datingmeth=datingmeth, datum=datum, depth=depth, depthft=depthft, depthin=depthin, descrip=descrip, diameter=diameter, diameterft=diameterft, diameterin=diameterin, dimnotes=dimnotes, dimtype=dimtype, dispvalue=dispvalue, earlydate=earlydate, elements=elements, epoch=epoch, era=era, event=event, ew=ew, excavadate=excavadate, excavateby=excavateby, exhibitid=exhibitid, exhibitno=exhibitno, exhlabel1=exhlabel1, exhlabel2=exhlabel2, exhlabel3=exhlabel3, exhlabel4=exhlabel4, exhstart=exhstart, family=family, feature=feature, flagdate=flagdate, flagnotes=flagnotes, flagreason=flagreason, formation=formation, fossils=fossils, found=found, fracture=fracture, frame=frame, framesize=framesize, genus=genus, gparent=gparent, grainsize=grainsize, habitat=habitat, hardness=hardness, height=height, heightft=heightft, heightin=heightin, homeloc=homeloc, idby=idby, iddate=iddate, imagefile=imagefile, imageno=imageno, imagesize=imagesize, inscomp=inscomp, inscrlang=inscrlang, inscrpos=inscrpos, inscrtech=inscrtech, inscrtext=inscrtext, inscrtrans=inscrtrans, inscrtype=inscrtype, insdate=insdate, insphone=insphone, inspremium=inspremium, insrep=insrep, insvalue=insvalue, invnby=invnby, invndate=invndate, kingdom=kingdom, latdeg=latdeg, latedate=latedate, legal=legal, length=length, lengthft=lengthft, lengthin=lengthin, level=level, lithofacie=lithofacie, loancond=loancond, loandue=loandue, loanid=loanid, loaninno=loaninno, loanno=loanno, loanrenew=loanrenew, locfield1=locfield1, locfield2=locfield2, locfield3=locfield3, locfield4=locfield4, locfield5=locfield5, locfield6=locfield6, longdeg=longdeg, luster=luster, made=made, maintcycle=maintcycle, maintdate=maintdate, maintnote=maintnote, material=material, medium=medium, member=member, mmark=mmark, nhclass=nhclass, nhorder=nhorder, notes=notes, ns=ns, objectid=objectid, objname=objname, objname2=objname2, objname3=objname3, objnames=objnames, occurrence=occurrence, oldno=oldno, origin=origin, othername=othername, otherno=otherno, outdate=outdate, owned=owned, parent=parent, people=people, period=period, phylum=phylum, policyno=policyno, ppid=ppid, preparator=preparator, prepdate=prepdate, preserve=preserve, pressure=pressure, provenance=provenance, pubnotes=pubnotes, qrurl=qrurl, recas=recas, recdate=recdate, recfrom=recfrom, relation=relation, relnotes=relnotes, renewuntil=renewuntil, repatby=repatby, repatclaim=repatclaim, repatdate=repatdate, repatdisp=repatdisp, repathand=repathand, repatnotes=repatnotes, repatnotic=repatnotic, repattype=repattype, rockclass=rockclass, rockcolor=rockcolor, rockorigin=rockorigin, rocktype=rocktype, role=role, role2=role2, role3=role3, school=school, sex=sex, sgflag=sgflag, signedname=signedname, signloc=signloc, site=site, siteno=siteno, specgrav=specgrav, species=species, sprocess=sprocess, stage=stage, status=status, statusby=statusby, statusdate=statusdate, sterms=sterms, stratum=stratum, streak=streak, subfamily=subfamily, subjects=subjects, subspecies=subspecies, technique=technique, tempauthor=tempauthor, tempby=tempby, tempdate=tempdate, temperatur=temperatur, temploc=temploc, tempnotes=tempnotes, tempreason=tempreason, tempuntil=tempuntil, texture=texture, title=title, tlocfield1=tlocfield1, tlocfield2=tlocfield2, tlocfield3=tlocfield3, tlocfield4=tlocfield4, tlocfield5=tlocfield5, tlocfield6=tlocfield6, udf1=udf1, udf10=udf10, udf11=udf11, udf12=udf12, udf13=udf13, udf14=udf14, udf15=udf15, udf16=udf16, udf17=udf17, udf18=udf18, udf19=udf19, udf2=udf2, udf20=udf20, udf21=udf21, udf22=udf22, udf3=udf3, udf4=udf4, udf5=udf5, udf6=udf6, udf7=udf7, udf8=udf8, udf9=udf9, unit=unit, updated=updated, updatedby=updatedby, used=used, valuedate=valuedate, varieties=varieties, vexhtml=vexhtml, vexlabel1=vexlabel1, vexlabel2=vexlabel2, vexlabel3=vexlabel3, vexlabel4=vexlabel4, webinclude=webinclude, weight=weight, weightin=weightin, weightlb=weightlb, width=width, widthft=widthft, widthin=widthin, xcord=xcord, ycord=ycord, zcord=zcord, zsorter=zsorter, zsorterx=zsorterx)

    @property
    def rockclass(self):
        '''
        :rtype: str
        '''

        return self.__rockclass

    @property
    def rockcolor(self):
        '''
        :rtype: str
        '''

        return self.__rockcolor

    @property
    def rockorigin(self):
        '''
        :rtype: str
        '''

        return self.__rockorigin

    @property
    def rocktype(self):
        '''
        :rtype: str
        '''

        return self.__rocktype

    @property
    def role(self):
        '''
        :rtype: str
        '''

        return self.__role

    @property
    def role2(self):
        '''
        :rtype: str
        '''

        return self.__role2

    @property
    def role3(self):
        '''
        :rtype: str
        '''

        return self.__role3

    @property
    def school(self):
        '''
        :rtype: str
        '''

        return self.__school

    @property
    def sex(self):
        '''
        :rtype: str
        '''

        return self.__sex

    @property
    def sgflag(self):
        '''
        :rtype: str
        '''

        return self.__sgflag

    @property
    def signedname(self):
        '''
        :rtype: str
        '''

        return self.__signedname

    @property
    def signloc(self):
        '''
        :rtype: str
        '''

        return self.__signloc

    @property
    def site(self):
        '''
        :rtype: str
        '''

        return self.__site

    @property
    def siteno(self):
        '''
        :rtype: str
        '''

        return self.__siteno

    @property
    def specgrav(self):
        '''
        :rtype: str
        '''

        return self.__specgrav

    @property
    def species(self):
        '''
        :rtype: str
        '''

        return self.__species

    @property
    def sprocess(self):
        '''
        :rtype: str
        '''

        return self.__sprocess

    @property
    def stage(self):
        '''
        :rtype: str
        '''

        return self.__stage

    @property
    def status(self):
        '''
        :rtype: str
        '''

        return self.__status

    @property
    def statusby(self):
        '''
        :rtype: str
        '''

        return self.__statusby

    @property
    def statusdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__statusdate

    @property
    def sterms(self):
        '''
        :rtype: str
        '''

        return self.__sterms

    @property
    def stratum(self):
        '''
        :rtype: str
        '''

        return self.__stratum

    @property
    def streak(self):
        '''
        :rtype: str
        '''

        return self.__streak

    @property
    def subfamily(self):
        '''
        :rtype: str
        '''

        return self.__subfamily

    @property
    def subjects(self):
        '''
        :rtype: str
        '''

        return self.__subjects

    @property
    def subspecies(self):
        '''
        :rtype: str
        '''

        return self.__subspecies

    @property
    def technique(self):
        '''
        :rtype: str
        '''

        return self.__technique

    @property
    def tempauthor(self):
        '''
        :rtype: str
        '''

        return self.__tempauthor

    @property
    def tempby(self):
        '''
        :rtype: str
        '''

        return self.__tempby

    @property
    def tempdate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__tempdate

    @property
    def temperatur(self):
        '''
        :rtype: str
        '''

        return self.__temperatur

    @property
    def temploc(self):
        '''
        :rtype: str
        '''

        return self.__temploc

    @property
    def tempnotes(self):
        '''
        :rtype: str
        '''

        return self.__tempnotes

    @property
    def tempreason(self):
        '''
        :rtype: str
        '''

        return self.__tempreason

    @property
    def tempuntil(self):
        '''
        :rtype: str
        '''

        return self.__tempuntil

    @property
    def texture(self):
        '''
        :rtype: str
        '''

        return self.__texture

    @property
    def title(self):
        '''
        :rtype: str
        '''

        return self.__title

    @property
    def tlocfield1(self):
        '''
        :rtype: str
        '''

        return self.__tlocfield1

    @property
    def tlocfield2(self):
        '''
        :rtype: str
        '''

        return self.__tlocfield2

    @property
    def tlocfield3(self):
        '''
        :rtype: str
        '''

        return self.__tlocfield3

    @property
    def tlocfield4(self):
        '''
        :rtype: str
        '''

        return self.__tlocfield4

    @property
    def tlocfield5(self):
        '''
        :rtype: str
        '''

        return self.__tlocfield5

    @property
    def tlocfield6(self):
        '''
        :rtype: str
        '''

        return self.__tlocfield6

    @property
    def udf1(self):
        '''
        :rtype: str
        '''

        return self.__udf1

    @property
    def udf10(self):
        '''
        :rtype: str
        '''

        return self.__udf10

    @property
    def udf11(self):
        '''
        :rtype: str
        '''

        return self.__udf11

    @property
    def udf12(self):
        '''
        :rtype: str
        '''

        return self.__udf12

    @property
    def udf13(self):
        '''
        :rtype: int
        '''

        return self.__udf13

    @property
    def udf14(self):
        '''
        :rtype: Decimal
        '''

        return self.__udf14

    @property
    def udf15(self):
        '''
        :rtype: Decimal
        '''

        return self.__udf15

    @property
    def udf16(self):
        '''
        :rtype: Decimal
        '''

        return self.__udf16

    @property
    def udf17(self):
        '''
        :rtype: Decimal
        '''

        return self.__udf17

    @property
    def udf18(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__udf18

    @property
    def udf19(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__udf19

    @property
    def udf2(self):
        '''
        :rtype: str
        '''

        return self.__udf2

    @property
    def udf20(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__udf20

    @property
    def udf21(self):
        '''
        :rtype: str
        '''

        return self.__udf21

    @property
    def udf22(self):
        '''
        :rtype: str
        '''

        return self.__udf22

    @property
    def udf3(self):
        '''
        :rtype: str
        '''

        return self.__udf3

    @property
    def udf4(self):
        '''
        :rtype: str
        '''

        return self.__udf4

    @property
    def udf5(self):
        '''
        :rtype: str
        '''

        return self.__udf5

    @property
    def udf6(self):
        '''
        :rtype: str
        '''

        return self.__udf6

    @property
    def udf7(self):
        '''
        :rtype: str
        '''

        return self.__udf7

    @property
    def udf8(self):
        '''
        :rtype: str
        '''

        return self.__udf8

    @property
    def udf9(self):
        '''
        :rtype: str
        '''

        return self.__udf9

    @property
    def unit(self):
        '''
        :rtype: str
        '''

        return self.__unit

    @property
    def updated(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__updated

    @property
    def updatedby(self):
        '''
        :rtype: str
        '''

        return self.__updatedby

    @property
    def used(self):
        '''
        :rtype: str
        '''

        return self.__used

    @property
    def valuedate(self):
        '''
        :rtype: datetime.datetime
        '''

        return self.__valuedate

    @property
    def varieties(self):
        '''
        :rtype: str
        '''

        return self.__varieties

    @property
    def vexhtml(self):
        '''
        :rtype: str
        '''

        return self.__vexhtml

    @property
    def vexlabel1(self):
        '''
        :rtype: str
        '''

        return self.__vexlabel1

    @property
    def vexlabel2(self):
        '''
        :rtype: str
        '''

        return self.__vexlabel2

    @property
    def vexlabel3(self):
        '''
        :rtype: str
        '''

        return self.__vexlabel3

    @property
    def vexlabel4(self):
        '''
        :rtype: str
        '''

        return self.__vexlabel4

    @property
    def webinclude(self):
        '''
        :rtype: bool
        '''

        return self.__webinclude

    @property
    def weight(self):
        '''
        :rtype: Decimal
        '''

        return self.__weight

    @property
    def weightin(self):
        '''
        :rtype: Decimal
        '''

        return self.__weightin

    @property
    def weightlb(self):
        '''
        :rtype: Decimal
        '''

        return self.__weightlb

    @property
    def width(self):
        '''
        :rtype: Decimal
        '''

        return self.__width

    @property
    def widthft(self):
        '''
        :rtype: Decimal
        '''

        return self.__widthft

    @property
    def widthin(self):
        '''
        :rtype: Decimal
        '''

        return self.__widthin

    def write(self, oprot):
        '''
        Write this object to the given output protocol and return self.

        :type oprot: thryft.protocol._output_protocol._OutputProtocol
        :rtype: pastpy.models.object_record.ObjectRecord
        '''

        oprot.write_struct_begin('ObjectRecord')

        if self.accessno is not None:
            oprot.write_field_begin(name='accessno', type=11, id=None)
            oprot.write_string(self.accessno)
            oprot.write_field_end()

        if self.accessory is not None:
            oprot.write_field_begin(name='accessory', type=11, id=None)
            oprot.write_string(self.accessory)
            oprot.write_field_end()

        if self.acqvalue is not None:
            oprot.write_field_begin(name='acqvalue', type=11, id=None)
            oprot.write_decimal(self.acqvalue)
            oprot.write_field_end()

        if self.age is not None:
            oprot.write_field_begin(name='age', type=11, id=None)
            oprot.write_string(self.age)
            oprot.write_field_end()

        if self.appnotes is not None:
            oprot.write_field_begin(name='appnotes', type=11, id=None)
            oprot.write_string(self.appnotes)
            oprot.write_field_end()

        if self.appraisor is not None:
            oprot.write_field_begin(name='appraisor', type=11, id=None)
            oprot.write_string(self.appraisor)
            oprot.write_field_end()

        if self.assemzone is not None:
            oprot.write_field_begin(name='assemzone', type=11, id=None)
            oprot.write_string(self.assemzone)
            oprot.write_field_end()

        if self.bagno is not None:
            oprot.write_field_begin(name='bagno', type=11, id=None)
            oprot.write_string(self.bagno)
            oprot.write_field_end()

        if self.boxno is not None:
            oprot.write_field_begin(name='boxno', type=11, id=None)
            oprot.write_string(self.boxno)
            oprot.write_field_end()

        if self.caption is not None:
            oprot.write_field_begin(name='caption', type=11, id=None)
            oprot.write_string(self.caption)
            oprot.write_field_end()

        if self.cat is not None:
            oprot.write_field_begin(name='cat', type=11, id=None)
            oprot.write_string(self.cat)
            oprot.write_field_end()

        if self.catby is not None:
            oprot.write_field_begin(name='catby', type=11, id=None)
            oprot.write_string(self.catby)
            oprot.write_field_end()

        if self.catdate is not None:
            oprot.write_field_begin(name='catdate', type=10, id=None)
            oprot.write_date_time(self.catdate)
            oprot.write_field_end()

        if self.cattype is not None:
            oprot.write_field_begin(name='cattype', type=11, id=None)
            oprot.write_string(self.cattype)
            oprot.write_field_end()

        if self.chemcomp is not None:
            oprot.write_field_begin(name='chemcomp', type=11, id=None)
            oprot.write_string(self.chemcomp)
            oprot.write_field_end()

        if self.circum is not None:
            oprot.write_field_begin(name='circum', type=11, id=None)
            oprot.write_decimal(self.circum)
            oprot.write_field_end()

        if self.circumft is not None:
            oprot.write_field_begin(name='circumft', type=11, id=None)
            oprot.write_decimal(self.circumft)
            oprot.write_field_end()

        if self.circumin is not None:
            oprot.write_field_begin(name='circumin', type=11, id=None)
            oprot.write_decimal(self.circumin)
            oprot.write_field_end()

        if self.classes is not None:
            oprot.write_field_begin(name='classes', type=11, id=None)
            oprot.write_string(self.classes)
            oprot.write_field_end()

        if self.colldate is not None:
            oprot.write_field_begin(name='colldate', type=10, id=None)
            oprot.write_date_time(self.colldate)
            oprot.write_field_end()

        if self.collection is not None:
            oprot.write_field_begin(name='collection', type=11, id=None)
            oprot.write_string(self.collection)
            oprot.write_field_end()

        if self.collector is not None:
            oprot.write_field_begin(name='collector', type=11, id=None)
            oprot.write_string(self.collector)
            oprot.write_field_end()

        if self.conddate is not None:
            oprot.write_field_begin(name='conddate', type=10, id=None)
            oprot.write_date_time(self.conddate)
            oprot.write_field_end()

        if self.condexam is not None:
            oprot.write_field_begin(name='condexam', type=11, id=None)
            oprot.write_string(self.condexam)
            oprot.write_field_end()

        if self.condition is not None:
            oprot.write_field_begin(name='condition', type=11, id=None)
            oprot.write_string(self.condition)
            oprot.write_field_end()

        if self.condnotes is not None:
            oprot.write_field_begin(name='condnotes', type=11, id=None)
            oprot.write_string(self.condnotes)
            oprot.write_field_end()

        if self.count is not None:
            oprot.write_field_begin(name='count', type=11, id=None)
            oprot.write_string(self.count)
            oprot.write_field_end()

        if self.creator is not None:
            oprot.write_field_begin(name='creator', type=11, id=None)
            oprot.write_string(self.creator)
            oprot.write_field_end()

        if self.creator2 is not None:
            oprot.write_field_begin(name='creator2', type=11, id=None)
            oprot.write_string(self.creator2)
            oprot.write_field_end()

        if self.creator3 is not None:
            oprot.write_field_begin(name='creator3', type=11, id=None)
            oprot.write_string(self.creator3)
            oprot.write_field_end()

        if self.credit is not None:
            oprot.write_field_begin(name='credit', type=11, id=None)
            oprot.write_string(self.credit)
            oprot.write_field_end()

        if self.crystal is not None:
            oprot.write_field_begin(name='crystal', type=11, id=None)
            oprot.write_string(self.crystal)
            oprot.write_field_end()

        if self.culture is not None:
            oprot.write_field_begin(name='culture', type=11, id=None)
            oprot.write_string(self.culture)
            oprot.write_field_end()

        if self.curvalmax is not None:
            oprot.write_field_begin(name='curvalmax', type=11, id=None)
            oprot.write_decimal(self.curvalmax)
            oprot.write_field_end()

        if self.curvalue is not None:
            oprot.write_field_begin(name='curvalue', type=11, id=None)
            oprot.write_decimal(self.curvalue)
            oprot.write_field_end()

        if self.dataset is not None:
            oprot.write_field_begin(name='dataset', type=11, id=None)
            oprot.write_string(self.dataset)
            oprot.write_field_end()

        if self.date is not None:
            oprot.write_field_begin(name='date', type=11, id=None)
            oprot.write_string(self.date)
            oprot.write_field_end()

        if self.datingmeth is not None:
            oprot.write_field_begin(name='datingmeth', type=11, id=None)
            oprot.write_string(self.datingmeth)
            oprot.write_field_end()

        if self.datum is not None:
            oprot.write_field_begin(name='datum', type=11, id=None)
            oprot.write_string(self.datum)
            oprot.write_field_end()

        if self.depth is not None:
            oprot.write_field_begin(name='depth', type=11, id=None)
            oprot.write_decimal(self.depth)
            oprot.write_field_end()

        if self.depthft is not None:
            oprot.write_field_begin(name='depthft', type=11, id=None)
            oprot.write_decimal(self.depthft)
            oprot.write_field_end()

        if self.depthin is not None:
            oprot.write_field_begin(name='depthin', type=11, id=None)
            oprot.write_decimal(self.depthin)
            oprot.write_field_end()

        if self.descrip is not None:
            oprot.write_field_begin(name='descrip', type=11, id=None)
            oprot.write_string(self.descrip)
            oprot.write_field_end()

        if self.diameter is not None:
            oprot.write_field_begin(name='diameter', type=11, id=None)
            oprot.write_decimal(self.diameter)
            oprot.write_field_end()

        if self.diameterft is not None:
            oprot.write_field_begin(name='diameterft', type=11, id=None)
            oprot.write_decimal(self.diameterft)
            oprot.write_field_end()

        if self.diameterin is not None:
            oprot.write_field_begin(name='diameterin', type=11, id=None)
            oprot.write_decimal(self.diameterin)
            oprot.write_field_end()

        if self.dimnotes is not None:
            oprot.write_field_begin(name='dimnotes', type=11, id=None)
            oprot.write_string(self.dimnotes)
            oprot.write_field_end()

        if self.dimtype is not None:
            oprot.write_field_begin(name='dimtype', type=8, id=None)
            oprot.write_i32(self.dimtype)
            oprot.write_field_end()

        if self.dispvalue is not None:
            oprot.write_field_begin(name='dispvalue', type=11, id=None)
            oprot.write_string(self.dispvalue)
            oprot.write_field_end()

        if self.earlydate is not None:
            oprot.write_field_begin(name='earlydate', type=8, id=None)
            oprot.write_i32(self.earlydate)
            oprot.write_field_end()

        if self.elements is not None:
            oprot.write_field_begin(name='elements', type=11, id=None)
            oprot.write_string(self.elements)
            oprot.write_field_end()

        if self.epoch is not None:
            oprot.write_field_begin(name='epoch', type=11, id=None)
            oprot.write_string(self.epoch)
            oprot.write_field_end()

        if self.era is not None:
            oprot.write_field_begin(name='era', type=11, id=None)
            oprot.write_string(self.era)
            oprot.write_field_end()

        if self.event is not None:
            oprot.write_field_begin(name='event', type=11, id=None)
            oprot.write_string(self.event)
            oprot.write_field_end()

        if self.ew is not None:
            oprot.write_field_begin(name='ew', type=11, id=None)
            oprot.write_string(self.ew)
            oprot.write_field_end()

        if self.excavadate is not None:
            oprot.write_field_begin(name='excavadate', type=10, id=None)
            oprot.write_date_time(self.excavadate)
            oprot.write_field_end()

        if self.excavateby is not None:
            oprot.write_field_begin(name='excavateby', type=11, id=None)
            oprot.write_string(self.excavateby)
            oprot.write_field_end()

        if self.exhibitid is not None:
            oprot.write_field_begin(name='exhibitid', type=11, id=None)
            oprot.write_string(self.exhibitid)
            oprot.write_field_end()

        if self.exhibitno is not None:
            oprot.write_field_begin(name='exhibitno', type=8, id=None)
            oprot.write_i32(self.exhibitno)
            oprot.write_field_end()

        if self.exhlabel1 is not None:
            oprot.write_field_begin(name='exhlabel1', type=11, id=None)
            oprot.write_string(self.exhlabel1)
            oprot.write_field_end()

        if self.exhlabel2 is not None:
            oprot.write_field_begin(name='exhlabel2', type=11, id=None)
            oprot.write_string(self.exhlabel2)
            oprot.write_field_end()

        if self.exhlabel3 is not None:
            oprot.write_field_begin(name='exhlabel3', type=11, id=None)
            oprot.write_string(self.exhlabel3)
            oprot.write_field_end()

        if self.exhlabel4 is not None:
            oprot.write_field_begin(name='exhlabel4', type=11, id=None)
            oprot.write_string(self.exhlabel4)
            oprot.write_field_end()

        if self.exhstart is not None:
            oprot.write_field_begin(name='exhstart', type=10, id=None)
            oprot.write_date_time(self.exhstart)
            oprot.write_field_end()

        if self.family is not None:
            oprot.write_field_begin(name='family', type=11, id=None)
            oprot.write_string(self.family)
            oprot.write_field_end()

        if self.feature is not None:
            oprot.write_field_begin(name='feature', type=11, id=None)
            oprot.write_string(self.feature)
            oprot.write_field_end()

        if self.flagdate is not None:
            oprot.write_field_begin(name='flagdate', type=10, id=None)
            oprot.write_date_time(self.flagdate)
            oprot.write_field_end()

        if self.flagnotes is not None:
            oprot.write_field_begin(name='flagnotes', type=11, id=None)
            oprot.write_string(self.flagnotes)
            oprot.write_field_end()

        if self.flagreason is not None:
            oprot.write_field_begin(name='flagreason', type=11, id=None)
            oprot.write_string(self.flagreason)
            oprot.write_field_end()

        if self.formation is not None:
            oprot.write_field_begin(name='formation', type=11, id=None)
            oprot.write_string(self.formation)
            oprot.write_field_end()

        if self.fossils is not None:
            oprot.write_field_begin(name='fossils', type=11, id=None)
            oprot.write_string(self.fossils)
            oprot.write_field_end()

        if self.found is not None:
            oprot.write_field_begin(name='found', type=11, id=None)
            oprot.write_string(self.found)
            oprot.write_field_end()

        if self.fracture is not None:
            oprot.write_field_begin(name='fracture', type=11, id=None)
            oprot.write_string(self.fracture)
            oprot.write_field_end()

        if self.frame is not None:
            oprot.write_field_begin(name='frame', type=11, id=None)
            oprot.write_string(self.frame)
            oprot.write_field_end()

        if self.framesize is not None:
            oprot.write_field_begin(name='framesize', type=11, id=None)
            oprot.write_string(self.framesize)
            oprot.write_field_end()

        if self.genus is not None:
            oprot.write_field_begin(name='genus', type=11, id=None)
            oprot.write_string(self.genus)
            oprot.write_field_end()

        if self.gparent is not None:
            oprot.write_field_begin(name='gparent', type=11, id=None)
            oprot.write_string(self.gparent)
            oprot.write_field_end()

        if self.grainsize is not None:
            oprot.write_field_begin(name='grainsize', type=11, id=None)
            oprot.write_string(self.grainsize)
            oprot.write_field_end()

        if self.habitat is not None:
            oprot.write_field_begin(name='habitat', type=11, id=None)
            oprot.write_string(self.habitat)
            oprot.write_field_end()

        if self.hardness is not None:
            oprot.write_field_begin(name='hardness', type=11, id=None)
            oprot.write_string(self.hardness)
            oprot.write_field_end()

        if self.height is not None:
            oprot.write_field_begin(name='height', type=11, id=None)
            oprot.write_decimal(self.height)
            oprot.write_field_end()

        if self.heightft is not None:
            oprot.write_field_begin(name='heightft', type=11, id=None)
            oprot.write_decimal(self.heightft)
            oprot.write_field_end()

        if self.heightin is not None:
            oprot.write_field_begin(name='heightin', type=11, id=None)
            oprot.write_decimal(self.heightin)
            oprot.write_field_end()

        if self.homeloc is not None:
            oprot.write_field_begin(name='homeloc', type=11, id=None)
            oprot.write_string(self.homeloc)
            oprot.write_field_end()

        if self.idby is not None:
            oprot.write_field_begin(name='idby', type=11, id=None)
            oprot.write_string(self.idby)
            oprot.write_field_end()

        if self.iddate is not None:
            oprot.write_field_begin(name='iddate', type=10, id=None)
            oprot.write_date_time(self.iddate)
            oprot.write_field_end()

        if self.imagefile is not None:
            oprot.write_field_begin(name='imagefile', type=11, id=None)
            oprot.write_string(self.imagefile)
            oprot.write_field_end()

        if self.imageno is not None:
            oprot.write_field_begin(name='imageno', type=8, id=None)
            oprot.write_i32(self.imageno)
            oprot.write_field_end()

        if self.imagesize is not None:
            oprot.write_field_begin(name='imagesize', type=11, id=None)
            oprot.write_string(self.imagesize)
            oprot.write_field_end()

        if self.inscomp is not None:
            oprot.write_field_begin(name='inscomp', type=11, id=None)
            oprot.write_string(self.inscomp)
            oprot.write_field_end()

        if self.inscrlang is not None:
            oprot.write_field_begin(name='inscrlang', type=11, id=None)
            oprot.write_string(self.inscrlang)
            oprot.write_field_end()

        if self.inscrpos is not None:
            oprot.write_field_begin(name='inscrpos', type=11, id=None)
            oprot.write_string(self.inscrpos)
            oprot.write_field_end()

        if self.inscrtech is not None:
            oprot.write_field_begin(name='inscrtech', type=11, id=None)
            oprot.write_string(self.inscrtech)
            oprot.write_field_end()

        if self.inscrtext is not None:
            oprot.write_field_begin(name='inscrtext', type=11, id=None)
            oprot.write_string(self.inscrtext)
            oprot.write_field_end()

        if self.inscrtrans is not None:
            oprot.write_field_begin(name='inscrtrans', type=11, id=None)
            oprot.write_string(self.inscrtrans)
            oprot.write_field_end()

        if self.inscrtype is not None:
            oprot.write_field_begin(name='inscrtype', type=11, id=None)
            oprot.write_string(self.inscrtype)
            oprot.write_field_end()

        if self.insdate is not None:
            oprot.write_field_begin(name='insdate', type=10, id=None)
            oprot.write_date_time(self.insdate)
            oprot.write_field_end()

        if self.insphone is not None:
            oprot.write_field_begin(name='insphone', type=11, id=None)
            oprot.write_string(self.insphone)
            oprot.write_field_end()

        if self.inspremium is not None:
            oprot.write_field_begin(name='inspremium', type=11, id=None)
            oprot.write_string(self.inspremium)
            oprot.write_field_end()

        if self.insrep is not None:
            oprot.write_field_begin(name='insrep', type=11, id=None)
            oprot.write_string(self.insrep)
            oprot.write_field_end()

        if self.insvalue is not None:
            oprot.write_field_begin(name='insvalue', type=11, id=None)
            oprot.write_decimal(self.insvalue)
            oprot.write_field_end()

        if self.invnby is not None:
            oprot.write_field_begin(name='invnby', type=11, id=None)
            oprot.write_string(self.invnby)
            oprot.write_field_end()

        if self.invndate is not None:
            oprot.write_field_begin(name='invndate', type=10, id=None)
            oprot.write_date_time(self.invndate)
            oprot.write_field_end()

        if self.kingdom is not None:
            oprot.write_field_begin(name='kingdom', type=11, id=None)
            oprot.write_string(self.kingdom)
            oprot.write_field_end()

        if self.latdeg is not None:
            oprot.write_field_begin(name='latdeg', type=11, id=None)
            oprot.write_decimal(self.latdeg)
            oprot.write_field_end()

        if self.latedate is not None:
            oprot.write_field_begin(name='latedate', type=8, id=None)
            oprot.write_i32(self.latedate)
            oprot.write_field_end()

        if self.legal is not None:
            oprot.write_field_begin(name='legal', type=11, id=None)
            oprot.write_string(self.legal)
            oprot.write_field_end()

        if self.length is not None:
            oprot.write_field_begin(name='length', type=11, id=None)
            oprot.write_decimal(self.length)
            oprot.write_field_end()

        if self.lengthft is not None:
            oprot.write_field_begin(name='lengthft', type=11, id=None)
            oprot.write_decimal(self.lengthft)
            oprot.write_field_end()

        if self.lengthin is not None:
            oprot.write_field_begin(name='lengthin', type=11, id=None)
            oprot.write_decimal(self.lengthin)
            oprot.write_field_end()

        if self.level is not None:
            oprot.write_field_begin(name='level', type=11, id=None)
            oprot.write_string(self.level)
            oprot.write_field_end()

        if self.lithofacie is not None:
            oprot.write_field_begin(name='lithofacie', type=11, id=None)
            oprot.write_string(self.lithofacie)
            oprot.write_field_end()

        if self.loancond is not None:
            oprot.write_field_begin(name='loancond', type=11, id=None)
            oprot.write_string(self.loancond)
            oprot.write_field_end()

        if self.loandue is not None:
            oprot.write_field_begin(name='loandue', type=10, id=None)
            oprot.write_date_time(self.loandue)
            oprot.write_field_end()

        if self.loanid is not None:
            oprot.write_field_begin(name='loanid', type=11, id=None)
            oprot.write_string(self.loanid)
            oprot.write_field_end()

        if self.loaninno is not None:
            oprot.write_field_begin(name='loaninno', type=11, id=None)
            oprot.write_string(self.loaninno)
            oprot.write_field_end()

        if self.loanno is not None:
            oprot.write_field_begin(name='loanno', type=8, id=None)
            oprot.write_i32(self.loanno)
            oprot.write_field_end()

        if self.loanrenew is not None:
            oprot.write_field_begin(name='loanrenew', type=10, id=None)
            oprot.write_date_time(self.loanrenew)
            oprot.write_field_end()

        if self.locfield1 is not None:
            oprot.write_field_begin(name='locfield1', type=11, id=None)
            oprot.write_string(self.locfield1)
            oprot.write_field_end()

        if self.locfield2 is not None:
            oprot.write_field_begin(name='locfield2', type=11, id=None)
            oprot.write_string(self.locfield2)
            oprot.write_field_end()

        if self.locfield3 is not None:
            oprot.write_field_begin(name='locfield3', type=11, id=None)
            oprot.write_string(self.locfield3)
            oprot.write_field_end()

        if self.locfield4 is not None:
            oprot.write_field_begin(name='locfield4', type=11, id=None)
            oprot.write_string(self.locfield4)
            oprot.write_field_end()

        if self.locfield5 is not None:
            oprot.write_field_begin(name='locfield5', type=11, id=None)
            oprot.write_string(self.locfield5)
            oprot.write_field_end()

        if self.locfield6 is not None:
            oprot.write_field_begin(name='locfield6', type=11, id=None)
            oprot.write_string(self.locfield6)
            oprot.write_field_end()

        if self.longdeg is not None:
            oprot.write_field_begin(name='longdeg', type=11, id=None)
            oprot.write_decimal(self.longdeg)
            oprot.write_field_end()

        if self.luster is not None:
            oprot.write_field_begin(name='luster', type=11, id=None)
            oprot.write_string(self.luster)
            oprot.write_field_end()

        if self.made is not None:
            oprot.write_field_begin(name='made', type=11, id=None)
            oprot.write_string(self.made)
            oprot.write_field_end()

        if self.maintcycle is not None:
            oprot.write_field_begin(name='maintcycle', type=11, id=None)
            oprot.write_string(self.maintcycle)
            oprot.write_field_end()

        if self.maintdate is not None:
            oprot.write_field_begin(name='maintdate', type=10, id=None)
            oprot.write_date_time(self.maintdate)
            oprot.write_field_end()

        if self.maintnote is not None:
            oprot.write_field_begin(name='maintnote', type=11, id=None)
            oprot.write_string(self.maintnote)
            oprot.write_field_end()

        if self.material is not None:
            oprot.write_field_begin(name='material', type=11, id=None)
            oprot.write_string(self.material)
            oprot.write_field_end()

        if self.medium is not None:
            oprot.write_field_begin(name='medium', type=11, id=None)
            oprot.write_string(self.medium)
            oprot.write_field_end()

        if self.member is not None:
            oprot.write_field_begin(name='member', type=11, id=None)
            oprot.write_string(self.member)
            oprot.write_field_end()

        if self.mmark is not None:
            oprot.write_field_begin(name='mmark', type=11, id=None)
            oprot.write_string(self.mmark)
            oprot.write_field_end()

        if self.nhclass is not None:
            oprot.write_field_begin(name='nhclass', type=11, id=None)
            oprot.write_string(self.nhclass)
            oprot.write_field_end()

        if self.nhorder is not None:
            oprot.write_field_begin(name='nhorder', type=11, id=None)
            oprot.write_string(self.nhorder)
            oprot.write_field_end()

        if self.notes is not None:
            oprot.write_field_begin(name='notes', type=11, id=None)
            oprot.write_string(self.notes)
            oprot.write_field_end()

        if self.ns is not None:
            oprot.write_field_begin(name='ns', type=11, id=None)
            oprot.write_string(self.ns)
            oprot.write_field_end()

        if self.objectid is not None:
            oprot.write_field_begin(name='objectid', type=11, id=None)
            oprot.write_string(self.objectid)
            oprot.write_field_end()

        if self.objname is not None:
            oprot.write_field_begin(name='objname', type=11, id=None)
            oprot.write_string(self.objname)
            oprot.write_field_end()

        if self.objname2 is not None:
            oprot.write_field_begin(name='objname2', type=11, id=None)
            oprot.write_string(self.objname2)
            oprot.write_field_end()

        if self.objname3 is not None:
            oprot.write_field_begin(name='objname3', type=11, id=None)
            oprot.write_string(self.objname3)
            oprot.write_field_end()

        if self.objnames is not None:
            oprot.write_field_begin(name='objnames', type=11, id=None)
            oprot.write_string(self.objnames)
            oprot.write_field_end()

        if self.occurrence is not None:
            oprot.write_field_begin(name='occurrence', type=11, id=None)
            oprot.write_string(self.occurrence)
            oprot.write_field_end()

        if self.oldno is not None:
            oprot.write_field_begin(name='oldno', type=11, id=None)
            oprot.write_string(self.oldno)
            oprot.write_field_end()

        if self.origin is not None:
            oprot.write_field_begin(name='origin', type=11, id=None)
            oprot.write_string(self.origin)
            oprot.write_field_end()

        if self.othername is not None:
            oprot.write_field_begin(name='othername', type=11, id=None)
            oprot.write_string(self.othername)
            oprot.write_field_end()

        if self.otherno is not None:
            oprot.write_field_begin(name='otherno', type=11, id=None)
            oprot.write_string(self.otherno)
            oprot.write_field_end()

        if self.outdate is not None:
            oprot.write_field_begin(name='outdate', type=10, id=None)
            oprot.write_date_time(self.outdate)
            oprot.write_field_end()

        if self.owned is not None:
            oprot.write_field_begin(name='owned', type=11, id=None)
            oprot.write_string(self.owned)
            oprot.write_field_end()

        if self.parent is not None:
            oprot.write_field_begin(name='parent', type=11, id=None)
            oprot.write_string(self.parent)
            oprot.write_field_end()

        if self.people is not None:
            oprot.write_field_begin(name='people', type=11, id=None)
            oprot.write_string(self.people)
            oprot.write_field_end()

        if self.period is not None:
            oprot.write_field_begin(name='period', type=11, id=None)
            oprot.write_string(self.period)
            oprot.write_field_end()

        if self.phylum is not None:
            oprot.write_field_begin(name='phylum', type=11, id=None)
            oprot.write_string(self.phylum)
            oprot.write_field_end()

        if self.policyno is not None:
            oprot.write_field_begin(name='policyno', type=11, id=None)
            oprot.write_string(self.policyno)
            oprot.write_field_end()

        if self.ppid is not None:
            oprot.write_field_begin(name='ppid', type=11, id=None)
            oprot.write_string(self.ppid)
            oprot.write_field_end()

        if self.preparator is not None:
            oprot.write_field_begin(name='preparator', type=11, id=None)
            oprot.write_string(self.preparator)
            oprot.write_field_end()

        if self.prepdate is not None:
            oprot.write_field_begin(name='prepdate', type=10, id=None)
            oprot.write_date_time(self.prepdate)
            oprot.write_field_end()

        if self.preserve is not None:
            oprot.write_field_begin(name='preserve', type=11, id=None)
            oprot.write_string(self.preserve)
            oprot.write_field_end()

        if self.pressure is not None:
            oprot.write_field_begin(name='pressure', type=11, id=None)
            oprot.write_string(self.pressure)
            oprot.write_field_end()

        if self.provenance is not None:
            oprot.write_field_begin(name='provenance', type=11, id=None)
            oprot.write_string(self.provenance)
            oprot.write_field_end()

        if self.pubnotes is not None:
            oprot.write_field_begin(name='pubnotes', type=11, id=None)
            oprot.write_string(self.pubnotes)
            oprot.write_field_end()

        if self.qrurl is not None:
            oprot.write_field_begin(name='qrurl', type=11, id=None)
            oprot.write_string(self.qrurl)
            oprot.write_field_end()

        if self.recas is not None:
            oprot.write_field_begin(name='recas', type=11, id=None)
            oprot.write_string(self.recas)
            oprot.write_field_end()

        if self.recdate is not None:
            oprot.write_field_begin(name='recdate', type=11, id=None)
            oprot.write_string(self.recdate)
            oprot.write_field_end()

        if self.recfrom is not None:
            oprot.write_field_begin(name='recfrom', type=11, id=None)
            oprot.write_string(self.recfrom)
            oprot.write_field_end()

        if self.relation is not None:
            oprot.write_field_begin(name='relation', type=11, id=None)
            oprot.write_string(self.relation)
            oprot.write_field_end()

        if self.relnotes is not None:
            oprot.write_field_begin(name='relnotes', type=11, id=None)
            oprot.write_string(self.relnotes)
            oprot.write_field_end()

        if self.renewuntil is not None:
            oprot.write_field_begin(name='renewuntil', type=10, id=None)
            oprot.write_date_time(self.renewuntil)
            oprot.write_field_end()

        if self.repatby is not None:
            oprot.write_field_begin(name='repatby', type=11, id=None)
            oprot.write_string(self.repatby)
            oprot.write_field_end()

        if self.repatclaim is not None:
            oprot.write_field_begin(name='repatclaim', type=11, id=None)
            oprot.write_string(self.repatclaim)
            oprot.write_field_end()

        if self.repatdate is not None:
            oprot.write_field_begin(name='repatdate', type=10, id=None)
            oprot.write_date_time(self.repatdate)
            oprot.write_field_end()

        if self.repatdisp is not None:
            oprot.write_field_begin(name='repatdisp', type=11, id=None)
            oprot.write_string(self.repatdisp)
            oprot.write_field_end()

        if self.repathand is not None:
            oprot.write_field_begin(name='repathand', type=11, id=None)
            oprot.write_string(self.repathand)
            oprot.write_field_end()

        if self.repatnotes is not None:
            oprot.write_field_begin(name='repatnotes', type=11, id=None)
            oprot.write_string(self.repatnotes)
            oprot.write_field_end()

        if self.repatnotic is not None:
            oprot.write_field_begin(name='repatnotic', type=10, id=None)
            oprot.write_date_time(self.repatnotic)
            oprot.write_field_end()

        if self.repattype is not None:
            oprot.write_field_begin(name='repattype', type=11, id=None)
            oprot.write_string(self.repattype)
            oprot.write_field_end()

        if self.rockclass is not None:
            oprot.write_field_begin(name='rockclass', type=11, id=None)
            oprot.write_string(self.rockclass)
            oprot.write_field_end()

        if self.rockcolor is not None:
            oprot.write_field_begin(name='rockcolor', type=11, id=None)
            oprot.write_string(self.rockcolor)
            oprot.write_field_end()

        if self.rockorigin is not None:
            oprot.write_field_begin(name='rockorigin', type=11, id=None)
            oprot.write_string(self.rockorigin)
            oprot.write_field_end()

        if self.rocktype is not None:
            oprot.write_field_begin(name='rocktype', type=11, id=None)
            oprot.write_string(self.rocktype)
            oprot.write_field_end()

        if self.role is not None:
            oprot.write_field_begin(name='role', type=11, id=None)
            oprot.write_string(self.role)
            oprot.write_field_end()

        if self.role2 is not None:
            oprot.write_field_begin(name='role2', type=11, id=None)
            oprot.write_string(self.role2)
            oprot.write_field_end()

        if self.role3 is not None:
            oprot.write_field_begin(name='role3', type=11, id=None)
            oprot.write_string(self.role3)
            oprot.write_field_end()

        if self.school is not None:
            oprot.write_field_begin(name='school', type=11, id=None)
            oprot.write_string(self.school)
            oprot.write_field_end()

        if self.sex is not None:
            oprot.write_field_begin(name='sex', type=11, id=None)
            oprot.write_string(self.sex)
            oprot.write_field_end()

        if self.sgflag is not None:
            oprot.write_field_begin(name='sgflag', type=11, id=None)
            oprot.write_string(self.sgflag)
            oprot.write_field_end()

        if self.signedname is not None:
            oprot.write_field_begin(name='signedname', type=11, id=None)
            oprot.write_string(self.signedname)
            oprot.write_field_end()

        if self.signloc is not None:
            oprot.write_field_begin(name='signloc', type=11, id=None)
            oprot.write_string(self.signloc)
            oprot.write_field_end()

        if self.site is not None:
            oprot.write_field_begin(name='site', type=11, id=None)
            oprot.write_string(self.site)
            oprot.write_field_end()

        if self.siteno is not None:
            oprot.write_field_begin(name='siteno', type=11, id=None)
            oprot.write_string(self.siteno)
            oprot.write_field_end()

        if self.specgrav is not None:
            oprot.write_field_begin(name='specgrav', type=11, id=None)
            oprot.write_string(self.specgrav)
            oprot.write_field_end()

        if self.species is not None:
            oprot.write_field_begin(name='species', type=11, id=None)
            oprot.write_string(self.species)
            oprot.write_field_end()

        if self.sprocess is not None:
            oprot.write_field_begin(name='sprocess', type=11, id=None)
            oprot.write_string(self.sprocess)
            oprot.write_field_end()

        if self.stage is not None:
            oprot.write_field_begin(name='stage', type=11, id=None)
            oprot.write_string(self.stage)
            oprot.write_field_end()

        if self.status is not None:
            oprot.write_field_begin(name='status', type=11, id=None)
            oprot.write_string(self.status)
            oprot.write_field_end()

        if self.statusby is not None:
            oprot.write_field_begin(name='statusby', type=11, id=None)
            oprot.write_string(self.statusby)
            oprot.write_field_end()

        if self.statusdate is not None:
            oprot.write_field_begin(name='statusdate', type=10, id=None)
            oprot.write_date_time(self.statusdate)
            oprot.write_field_end()

        if self.sterms is not None:
            oprot.write_field_begin(name='sterms', type=11, id=None)
            oprot.write_string(self.sterms)
            oprot.write_field_end()

        if self.stratum is not None:
            oprot.write_field_begin(name='stratum', type=11, id=None)
            oprot.write_string(self.stratum)
            oprot.write_field_end()

        if self.streak is not None:
            oprot.write_field_begin(name='streak', type=11, id=None)
            oprot.write_string(self.streak)
            oprot.write_field_end()

        if self.subfamily is not None:
            oprot.write_field_begin(name='subfamily', type=11, id=None)
            oprot.write_string(self.subfamily)
            oprot.write_field_end()

        if self.subjects is not None:
            oprot.write_field_begin(name='subjects', type=11, id=None)
            oprot.write_string(self.subjects)
            oprot.write_field_end()

        if self.subspecies is not None:
            oprot.write_field_begin(name='subspecies', type=11, id=None)
            oprot.write_string(self.subspecies)
            oprot.write_field_end()

        if self.technique is not None:
            oprot.write_field_begin(name='technique', type=11, id=None)
            oprot.write_string(self.technique)
            oprot.write_field_end()

        if self.tempauthor is not None:
            oprot.write_field_begin(name='tempauthor', type=11, id=None)
            oprot.write_string(self.tempauthor)
            oprot.write_field_end()

        if self.tempby is not None:
            oprot.write_field_begin(name='tempby', type=11, id=None)
            oprot.write_string(self.tempby)
            oprot.write_field_end()

        if self.tempdate is not None:
            oprot.write_field_begin(name='tempdate', type=10, id=None)
            oprot.write_date_time(self.tempdate)
            oprot.write_field_end()

        if self.temperatur is not None:
            oprot.write_field_begin(name='temperatur', type=11, id=None)
            oprot.write_string(self.temperatur)
            oprot.write_field_end()

        if self.temploc is not None:
            oprot.write_field_begin(name='temploc', type=11, id=None)
            oprot.write_string(self.temploc)
            oprot.write_field_end()

        if self.tempnotes is not None:
            oprot.write_field_begin(name='tempnotes', type=11, id=None)
            oprot.write_string(self.tempnotes)
            oprot.write_field_end()

        if self.tempreason is not None:
            oprot.write_field_begin(name='tempreason', type=11, id=None)
            oprot.write_string(self.tempreason)
            oprot.write_field_end()

        if self.tempuntil is not None:
            oprot.write_field_begin(name='tempuntil', type=11, id=None)
            oprot.write_string(self.tempuntil)
            oprot.write_field_end()

        if self.texture is not None:
            oprot.write_field_begin(name='texture', type=11, id=None)
            oprot.write_string(self.texture)
            oprot.write_field_end()

        if self.title is not None:
            oprot.write_field_begin(name='title', type=11, id=None)
            oprot.write_string(self.title)
            oprot.write_field_end()

        if self.tlocfield1 is not None:
            oprot.write_field_begin(name='tlocfield1', type=11, id=None)
            oprot.write_string(self.tlocfield1)
            oprot.write_field_end()

        if self.tlocfield2 is not None:
            oprot.write_field_begin(name='tlocfield2', type=11, id=None)
            oprot.write_string(self.tlocfield2)
            oprot.write_field_end()

        if self.tlocfield3 is not None:
            oprot.write_field_begin(name='tlocfield3', type=11, id=None)
            oprot.write_string(self.tlocfield3)
            oprot.write_field_end()

        if self.tlocfield4 is not None:
            oprot.write_field_begin(name='tlocfield4', type=11, id=None)
            oprot.write_string(self.tlocfield4)
            oprot.write_field_end()

        if self.tlocfield5 is not None:
            oprot.write_field_begin(name='tlocfield5', type=11, id=None)
            oprot.write_string(self.tlocfield5)
            oprot.write_field_end()

        if self.tlocfield6 is not None:
            oprot.write_field_begin(name='tlocfield6', type=11, id=None)
            oprot.write_string(self.tlocfield6)
            oprot.write_field_end()

        if self.udf1 is not None:
            oprot.write_field_begin(name='udf1', type=11, id=None)
            oprot.write_string(self.udf1)
            oprot.write_field_end()

        if self.udf10 is not None:
            oprot.write_field_begin(name='udf10', type=11, id=None)
            oprot.write_string(self.udf10)
            oprot.write_field_end()

        if self.udf11 is not None:
            oprot.write_field_begin(name='udf11', type=11, id=None)
            oprot.write_string(self.udf11)
            oprot.write_field_end()

        if self.udf12 is not None:
            oprot.write_field_begin(name='udf12', type=11, id=None)
            oprot.write_string(self.udf12)
            oprot.write_field_end()

        if self.udf13 is not None:
            oprot.write_field_begin(name='udf13', type=8, id=None)
            oprot.write_i32(self.udf13)
            oprot.write_field_end()

        if self.udf14 is not None:
            oprot.write_field_begin(name='udf14', type=11, id=None)
            oprot.write_decimal(self.udf14)
            oprot.write_field_end()

        if self.udf15 is not None:
            oprot.write_field_begin(name='udf15', type=11, id=None)
            oprot.write_decimal(self.udf15)
            oprot.write_field_end()

        if self.udf16 is not None:
            oprot.write_field_begin(name='udf16', type=11, id=None)
            oprot.write_decimal(self.udf16)
            oprot.write_field_end()

        if self.udf17 is not None:
            oprot.write_field_begin(name='udf17', type=11, id=None)
            oprot.write_decimal(self.udf17)
            oprot.write_field_end()

        if self.udf18 is not None:
            oprot.write_field_begin(name='udf18', type=10, id=None)
            oprot.write_date_time(self.udf18)
            oprot.write_field_end()

        if self.udf19 is not None:
            oprot.write_field_begin(name='udf19', type=10, id=None)
            oprot.write_date_time(self.udf19)
            oprot.write_field_end()

        if self.udf2 is not None:
            oprot.write_field_begin(name='udf2', type=11, id=None)
            oprot.write_string(self.udf2)
            oprot.write_field_end()

        if self.udf20 is not None:
            oprot.write_field_begin(name='udf20', type=10, id=None)
            oprot.write_date_time(self.udf20)
            oprot.write_field_end()

        if self.udf21 is not None:
            oprot.write_field_begin(name='udf21', type=11, id=None)
            oprot.write_string(self.udf21)
            oprot.write_field_end()

        if self.udf22 is not None:
            oprot.write_field_begin(name='udf22', type=11, id=None)
            oprot.write_string(self.udf22)
            oprot.write_field_end()

        if self.udf3 is not None:
            oprot.write_field_begin(name='udf3', type=11, id=None)
            oprot.write_string(self.udf3)
            oprot.write_field_end()

        if self.udf4 is not None:
            oprot.write_field_begin(name='udf4', type=11, id=None)
            oprot.write_string(self.udf4)
            oprot.write_field_end()

        if self.udf5 is not None:
            oprot.write_field_begin(name='udf5', type=11, id=None)
            oprot.write_string(self.udf5)
            oprot.write_field_end()

        if self.udf6 is not None:
            oprot.write_field_begin(name='udf6', type=11, id=None)
            oprot.write_string(self.udf6)
            oprot.write_field_end()

        if self.udf7 is not None:
            oprot.write_field_begin(name='udf7', type=11, id=None)
            oprot.write_string(self.udf7)
            oprot.write_field_end()

        if self.udf8 is not None:
            oprot.write_field_begin(name='udf8', type=11, id=None)
            oprot.write_string(self.udf8)
            oprot.write_field_end()

        if self.udf9 is not None:
            oprot.write_field_begin(name='udf9', type=11, id=None)
            oprot.write_string(self.udf9)
            oprot.write_field_end()

        if self.unit is not None:
            oprot.write_field_begin(name='unit', type=11, id=None)
            oprot.write_string(self.unit)
            oprot.write_field_end()

        if self.updated is not None:
            oprot.write_field_begin(name='updated', type=10, id=None)
            oprot.write_date_time(self.updated)
            oprot.write_field_end()

        if self.updatedby is not None:
            oprot.write_field_begin(name='updatedby', type=11, id=None)
            oprot.write_string(self.updatedby)
            oprot.write_field_end()

        if self.used is not None:
            oprot.write_field_begin(name='used', type=11, id=None)
            oprot.write_string(self.used)
            oprot.write_field_end()

        if self.valuedate is not None:
            oprot.write_field_begin(name='valuedate', type=10, id=None)
            oprot.write_date_time(self.valuedate)
            oprot.write_field_end()

        if self.varieties is not None:
            oprot.write_field_begin(name='varieties', type=11, id=None)
            oprot.write_string(self.varieties)
            oprot.write_field_end()

        if self.vexhtml is not None:
            oprot.write_field_begin(name='vexhtml', type=11, id=None)
            oprot.write_string(self.vexhtml)
            oprot.write_field_end()

        if self.vexlabel1 is not None:
            oprot.write_field_begin(name='vexlabel1', type=11, id=None)
            oprot.write_string(self.vexlabel1)
            oprot.write_field_end()

        if self.vexlabel2 is not None:
            oprot.write_field_begin(name='vexlabel2', type=11, id=None)
            oprot.write_string(self.vexlabel2)
            oprot.write_field_end()

        if self.vexlabel3 is not None:
            oprot.write_field_begin(name='vexlabel3', type=11, id=None)
            oprot.write_string(self.vexlabel3)
            oprot.write_field_end()

        if self.vexlabel4 is not None:
            oprot.write_field_begin(name='vexlabel4', type=11, id=None)
            oprot.write_string(self.vexlabel4)
            oprot.write_field_end()

        if self.webinclude is not None:
            oprot.write_field_begin(name='webinclude', type=2, id=None)
            oprot.write_bool(self.webinclude)
            oprot.write_field_end()

        if self.weight is not None:
            oprot.write_field_begin(name='weight', type=11, id=None)
            oprot.write_decimal(self.weight)
            oprot.write_field_end()

        if self.weightin is not None:
            oprot.write_field_begin(name='weightin', type=11, id=None)
            oprot.write_decimal(self.weightin)
            oprot.write_field_end()

        if self.weightlb is not None:
            oprot.write_field_begin(name='weightlb', type=11, id=None)
            oprot.write_decimal(self.weightlb)
            oprot.write_field_end()

        if self.width is not None:
            oprot.write_field_begin(name='width', type=11, id=None)
            oprot.write_decimal(self.width)
            oprot.write_field_end()

        if self.widthft is not None:
            oprot.write_field_begin(name='widthft', type=11, id=None)
            oprot.write_decimal(self.widthft)
            oprot.write_field_end()

        if self.widthin is not None:
            oprot.write_field_begin(name='widthin', type=11, id=None)
            oprot.write_decimal(self.widthin)
            oprot.write_field_end()

        if self.xcord is not None:
            oprot.write_field_begin(name='xcord', type=11, id=None)
            oprot.write_decimal(self.xcord)
            oprot.write_field_end()

        if self.ycord is not None:
            oprot.write_field_begin(name='ycord', type=11, id=None)
            oprot.write_decimal(self.ycord)
            oprot.write_field_end()

        if self.zcord is not None:
            oprot.write_field_begin(name='zcord', type=11, id=None)
            oprot.write_decimal(self.zcord)
            oprot.write_field_end()

        if self.zsorter is not None:
            oprot.write_field_begin(name='zsorter', type=11, id=None)
            oprot.write_string(self.zsorter)
            oprot.write_field_end()

        if self.zsorterx is not None:
            oprot.write_field_begin(name='zsorterx', type=11, id=None)
            oprot.write_string(self.zsorterx)
            oprot.write_field_end()

        oprot.write_field_stop()

        oprot.write_struct_end()

        return self

    @property
    def xcord(self):
        '''
        :rtype: Decimal
        '''

        return self.__xcord

    @property
    def ycord(self):
        '''
        :rtype: Decimal
        '''

        return self.__ycord

    @property
    def zcord(self):
        '''
        :rtype: Decimal
        '''

        return self.__zcord

    @property
    def zsorter(self):
        '''
        :rtype: str
        '''

        return self.__zsorter

    @property
    def zsorterx(self):
        '''
        :rtype: str
        '''

        return self.__zsorterx
