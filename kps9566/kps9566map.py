KPS9566ROW = list(range(0x81, 0xFF))
KPS9566COL = (list(range(0x41, 0x5A+1))+
    list(range(0x61, 0x7a+1))+
    list(range(0x81, 0xFF)))
KPS9566MAP=list('갃갅갆갋갌갍갎갏갘갂갻갽갾갿걁걂걃걄걅걆걇걉걊걎걏걐걑걒걓갺걌걳걵걶걻걼걽걾걿겂겇겈걲겫겭겮겱겲겳겴겵겶겷겺겾겿곀곂곃곣곥곦곩곫곭곮곲곷곸곹곻곢곴굑굓굕굖굗굙굚굛굜굝굞굟굠굢굥굦굧굨굩굪굫굒굤굯굱굲굷굸굹굺굾궃궄궅궆궇굮궀귝귟귡귢귣귥귦귧귨귩귪귫귭귮귯귲귳귴귵귶귷귞귰귻귽귾긂긃긄긅긆긊긎긏긐긑긒긓귺긌긳긵긶긹긻긼긽긾긿깂깈깋긲깄갟갡갢갣갥갦갧갨갩갪갫갮갲갳갴갵갶갷갞걕걗걙걚걛걝걞걟걠걡걢걣걤걥걦걧걩걪걫걬걭걮걯걖걨겏겑겒겓겕겖겗겘겙겚겛겞겢겣겤겥겦겧겎곅곇곉곊곋곍곎곏곐곑곒곓곔곖곙곚곛곜곝곞곟곆곘괷괹괺괻괽괾괿굀굁굂굃굆굊굋굌굍굎굏괶귃귅귆귇귉귊귋귌귍귎귏귒귕귖귗귘귙귚귛귂귔긕긗긘긙긚긛긜긝긞긟긠긡긢긣긤긥긦긧긩긪긫긬긭긮긯긖긨곿괁괂괅괇괈괉괊괋괎괒괓괔괕괖괗곾궋궍궎궏궑궒궓궔궕궖궗궙궚궛궞궟궠궡궢궣궊괛괝괞괟괡괢괣괤괥괦괧괨괪괫괮괯괰괱괲괳괚궧궨궩궪궫궬궭궮궯궰궱궲궳궴궵궶궹궺궻궼궽궾궿궦궸낝낞낣낤낥낦낧낪낰낲냓냕냖냗냙냚냛냜냝냞냟냢냣냦냧냨냩냪냫냒냤넍넎넏넑넔넕넖넗넚넞넟넠넡녃녅녆녇녉녊녋녌녍녎녏녒녖녗녙녚녛녂녻녽녾녿놁놃놄놅놆놇놊놎놏놐놑녺놌뇫뇭뇮뇯뇱뇲뇳뇴뇵뇶뇷뇺뇾뇿눀눁눂눃뇪뇼눇눉눊눍눎눏눐눑눒눓눖눚눛눜눝눟눆눘뉷뉹뉺뉻뉽뉾뉿늀늁늂늃늆늇늊늋늌늍늎늏뉶늈늓늕늖늗늛늜늝늞늟늢늧늨늩늫늒늤닋닍닎닏닑닓닔닕닖닗닚닞닟닠닡닣닊닜낷낹낺낻낽낾낿냀냁냂냃냆냊냋냌냍냎냏낶냭냯냰냱냲냳냴냵냶냷냸냹냺냻냼냽냾냿넁넂넃넄넅넆넇냮넀넧넩넪넫넭넮넯넰넱넲넳넶넺넻넼넽넾넿넦녝녟녡녢녣녤녥녦녧녨녩녪녫녬녭녮녯녱녲녳녴녵녶녷녞녰뇍뇏뇑뇒뇓뇕뇖뇗뇘뇙뇚뇛뇞뇡뇢뇣뇤뇥뇦뇧뇎뇠뉙뉛뉝뉞뉟뉡뉢뉣뉤뉥뉦뉧뉪뉫뉮뉯뉰뉱뉲뉳뉚뉬늭늯늱늲늳늵늶늷늸늹늺늻늽늾늿닂닃닄닅닆닇늮닀놕놗놙놚놛놝놞놟놠놡놢놣놤놥놦놩놪놫놬놭놮놯놖눡눣눤눥눦눧눩눪눫눬눭눮눯눰눱눲눵눶눷눸눹눺눻눢놱놳놴놵놶놷놸놹놺놻놼놽놾놿뇀뇁뇂뇃뇅뇆뇇뇈뇉뇊뇋놲뇄눽눿뉀뉁뉂뉃뉄뉅뉆뉇뉈뉉뉊뉋뉌뉍뉎뉏뉑뉒뉓뉔뉕뉖뉗눾뉐닧닩닪닰닱닶닼닽댝댟댠댡댢댣댤댥댦댧댨댩댪댫댬댭댮댯댱댲댳댴댵댶댷댞댰덗덙덚덝덠덡덢덣덦덪덬덭뎍뎏뎑뎒뎓뎕뎖뎗뎘뎙뎚뎛뎜뎝뎞뎟뎢뎣뎤뎥뎦뎧뎎돇돉돊돍돏돑돒돓돖돚돜돞돟돆돘됵됷됸됹됺됻됼됽됾됿둀둁둂둃둄둅둆둇둉둊둋둌둍둎둏됶둈둓둕둖둗둙둚둛둜둝둞둟둢둦둧둨둩둪둫둒둤듁듃듅듆듇듉듊듋듌듍듎듏듑듒듓듖듗듘듙듚듛듂듔듟듡듢듨듩듪듫듮듲듳듴듵듶듷듞듰딗딙딚딝딞딟딠딡딢딣딦딫딬딭딯딖댃댅댆댇댉댊댋댌댍댎댏댒댖댗댘댙댚댛댂댹댻댼댽댾댿덀덁덂덃덄덅덆덇덈덉덊덋덍덎덏덐덑덒덓댺덌덳덵덶덹덺덻덼덽덾덿뎂뎆뎇뎈뎉뎊뎋덲뎩뎫뎭뎮뎯뎰뎱뎲뎳뎴뎵뎶뎷뎸뎹뎺뎻뎽뎾뎿돀돁돂돃뎪뎼됙됛됝됞됟됡됢됣됤됥됦됧됪됮됯됰됱됲됳됚뒧뒩뒪뒫뒭뒮뒯뒰뒱뒲뒳뒶뒺뒻뒼뒽뒾뒿뒦뒸듹듻듽듾듿딁딂딃딄딅딆딇딈딊딋딎딏딐딑딒딓듺딌돡돣돥돦돧돩돪돫돬돭돮돯돰돱돲돳돵돶돷돸돹돺돻돢돴둭둯둱둲둳둵둶둷둸둹둺둻둽둾뒁뒂뒃뒄뒅뒆뒇둮돽돿됁됂됃됅됆됇됈됉됊됋됌됍됎됏됑됒됓됔됕됖됗돾뒉뒋뒌뒍뒎뒏뒐뒑뒒뒓뒔뒕뒖뒗뒘뒙뒚뒛뒞뒟뒠뒡뒢뒣뒊뒜띿랁랂랃랅랆랇랈랉랊랋랎랓랔랕띾랷랹랺랻랽랾랿럀럁럂럃럆럊럋럌럍럎럏랶럈럯럱럲럳럵럶럷럸럹럺럻럾렂렃렄렅럮렧렩렪렫렭렮렯렰렱렲렳렶렺렻렼렽렾렿렦롟롡롢롣롥롦롧롨롩롪롫롮롲롳롴롵롷롞롰룍룏룑룒룓룕룖룗룘룙룚룛룞룢룣룤룥룦룧룎룠룫룭룮룯룱룲룳룴룵룶룷룺룾룿뤀뤁뤂뤃룪룼륛륝륞륟륡륢륣륤륥륦륧륪륮륯륰륱륲륳륚륬륷륹륺륻륽륾륿릀릁릂릃릆릋릌릏륶릈릯릱릲릳릵릶릷릸릹릺릻릾맂맃맄맅맇릮맀랛랝랞랟랡랢랣랤랥랦랧랪랮랯랰랱랲랳랚럑럓럔럕럖럗럘럙럚럛럜럝럞럟럠럡럢럣럥럦럧럨럩럪럫럒럤렋렍렎렏렑렒렓렔렕렖렗렚렞렟렠렡렢렣렊롁롃롅롆롇롉롊롋롌롍롎롏롐롒롕롖롗롘롙롚롛롂롔뢱뢳뢵뢶뢷뢹뢺뢻뢼뢽뢾뢿룂룆룇룈룉룊룋뢲뤿륁륂륃륅륆륇륈륉륊륋륍륎륒륓륔륕륖륗뤾륐릑릓릕릖릗릙릚릛릜릝릞릟릡릢릣릥릦릧릨릩릪릫릒릤롹롻롽롾롿뢀뢁뢂뢃뢄뢅뢆뢇뢈뢊뢋뢎뢏뢐뢑뢒뢓롺뢌뤅뤇뤈뤉뤊뤋뤌뤍뤎뤏뤐뤑뤒뤓뤔뤕뤖뤗뤙뤚뤛뤜뤝뤞뤟뤆뢕뢗뢘뢙뢚뢛뢜뢝뢞뢟뢠뢡뢢뢣뢤뢥뢦뢧뢩뢪뢫뢬뢭뢮뢯뢖뤡뤣뤤뤥뤦뤧뤨뤩뤪뤫뤬뤭뤮뤯뤰뤱뤲뤳뤵뤶뤷뤸뤹뤺뤻뤢뤴맋맍맓맔맕맖맗맚맠맢맊맜먃먅먆먇먉먊먋먌먍먎먏먑먒먓먖먗먘먙먚먛먂먔먻먽먾먿멃멄멅멆멇멊멏멐멑멒먺멳멵멶멷멹멺멻멼멽멾멿몂몆몈몉몊몋멲몭몮몱몳몴몵몶몷몺몾몿뫀뫁뫂몪몼묙묛묝묞묟묡묢묣묤묥묦묧묨묪묭묮묯묰묱묲묳묚묬묷묹묺묿뭀뭁뭂뭃뭆뭊뭋뭌뭎뭈뮧뮩뮪뮫뮭뮮뮯뮰뮱뮲뮳뮵뮶뮺뮻뮼뮽뮾뮿뮦뮸믁믃믅믆믇믉믊믋믌믍믎믏믒믖믗믘믙믚믛믂믔믻믽믾밁밃밄밅밆밇밊밎밐밒밓믺맧맩맪맫맭맮맯맰맱맲맳맶맻맼맽맾맿맦먝먟먠먡먢먣먤먥먦먧먨먩먪먫먬먭먮먯먱먲먳먴먵먶먷먞먰멗멙멚멛멝멞멟멠멡멢멣멦멪멫멬멭멮멯멖몍몏몑몒몓몔몕몖몗몘몙몚몛몜몝몞몟몡몢몣몤몥몦몧몎몠뫽뫿묁묂묃묅묆묇묈묉묊묋묎묒묓묔묕묖묗뫾묐뮉뮋뮍뮎뮏뮑뮒뮓뮔뮕뮖뮗뮘뮙뮚뮛뮝뮞뮟뮠뮡뮢뮣뮊뮜믝믟믡믢믣믤믥믦믧믨믩믪믫믭믮믯믱믲믳믴믵믶믷믞믰뫅뫇뫉뫊뫋뫌뫍뫎뫏뫐뫑뫒뫓뫔뫕뫖뫗뫚뫛뫜뫝뫞뫟뫆뭑뭓뭕뭖뭗뭙뭚뭛뭜뭝뭞뭟뭢뭥뭦뭧뭨뭩뭪뭫뭒뫡뫣뫤뫥뫦뫧뫨뫩뫪뫫뫬뫭뫮뫯뫰뫱뫲뫳뫵뫶뫷뫸뫹뫺뫻뫢뫴뭭뭯뭰뭱뭲뭳뭴뭵뭶뭷뭸뭹뭺뭻뭼뭽뭾뭿뮁뮂뮃뮄뮅뮆뮇뭮뮀밙밚밠밡밢밣밦밪밫밬밮밯밨뱏뱑뱒뱓뱔뱕뱖뱗뱘뱙뱚뱛뱞뱟뱡뱢뱣뱤뱥뱦뱧뱎뱠벇벉벊벏벐벑벒벓벖벛벝벞벟벆벿볁볂볃볅볆볇볈볉볊볋볎볒볔볖볗벾볷볹볺볻볽볾볿봀봁봂봃봆봊봋봌봍봎봈뵥뵧뵩뵪뵫뵭뵮뵯뵰뵱뵲뵳뵴뵵뵶뵷뵹뵺뵻뵼뵽뵾뵿뵦뵸붃붅붆붋붌붍붎붏붒붖붗붘붛붂붔뷱뷳뷵뷶뷷뷹뷺뷻뷼뷽뷾뷿븂븆븇븈븉븊븋뷲븄븏븑븒븓븕븖븗븘븙븚븛븞븢븣븤븥븦븧븎븠빇빉빊빋빍빏빐빑빒빓빖빜빝빞빟빆빘밳밵밶밹밺밻밼밽밾밿뱂뱆뱇뱈뱊뱋밲뱩뱫뱬뱭뱮뱯뱰뱱뱲뱳뱴뱵뱶뱷뱸뱹뱺뱻뱽뱾뱿벀벁벂벃뱪뱼벣벥벦벩벪벫벬벭벮벯벲벶벷벸벹벺벻벢볙볛볝볞볟볠볡볢볣볤볥볦볧볨볩볪볫볭볮볯볰볱볲볳볚볬뵋뵍뵎뵏뵑뵒뵓뵔뵕뵖뵗뵚뵛뵝뵞뵟뵠뵡뵢뵣뵊뷗뷙뷚뷛뷝뷞뷟뷠뷡뷢뷣뷤뷥뷦뷧뷪뷫뷬뷭뷮뷯뷖뷨븩븫븭븮븯븱븲븳븴븵븶븷븸븹븺븻븾븿빀빁빂빃븪븼봑봓봕봖봗봘봙봚봛봜봝봞봟봠봢봥봦봧봨봩봪봫봒붝붟붠붡붢붣붥붦붧붨붩붪붫붬붭붮붱붲붳붵붶붷붞봭봯봱봲봳봴봵봶봷봸봹봺봻봼봽봾봿뵁뵂뵃뵄뵅뵆뵇봮붹붻붼붽붾붿뷀뷁뷂뷃뷄뷅뷆뷇뷈뷉뷊뷋뷍뷎뷏뷐뷑뷒뷓붺뷌삱삲삷삸삹삺삻삾샂샃샄샆샇삮샧샩샪샫샭샮샯샰샱샲샳샶샺샻샼샽샾샿샦샸섡섢섥섨섩섪섫섮섲섳섴섵섷셗셙셚셛셝셞셟셠셡셢셣셦셪셫셬셭셮셯셖솏솑솒솕솗솘솙솚솛솞솢솣솤솦솧솠쇿숁숂숃숅숆숇숈숉숊숋숎숒숓숔숕숖숗쇾숐숛숝숞숡숢숣숤숥숦숧숪숮숰숳숚숬슋슍슎슏슑슒슓슔슕슖슗슚슞슟슠슡슢슣슊슜슧슩슪슫슮슯슰슱슶슺슻슼슽슾슿슦슸싟싡싢싥싦싧싨싩싪싮싲싳싴싵싷싞싰샋샍샎샏샑샒샓샔샕샖샗샚샞샟샠샡샢샣샊섁섃섅섆섇섉섊섋섌섍섎섏섑섒섓섖섗섘섙섚섛섂섔섻섽섾섿셁셂셃셄셅셆셇셊셎셏셐셓섺셱셳셵셶셷셹셺셻셼셽셾셿솀솁솂솃솆솇솈솉솊솋셲솄쇣쇥쇦쇧쇩쇪쇫쇬쇭쇮쇯쇲쇶쇷쇸쇹쇺쇻쇢쉯쉱쉲쉳쉵쉶쉷쉸쉹쉺쉻쉾슂슃슄슅슆슇쉮슀싁싃싅싆싇싈싉싊싋싌싍싎싏싐싑싒싓싕싖싗싘싙싚싛싂싔솫솭솮솯솱솲솳솴솵솶솷솸솹솺솾솿쇀쇁쇂쇃솪솼숵숷숸숹숺숻숼숽숾숿쉀쉁쉂쉃쉄쉅쉆쉇쉉쉊쉋쉌쉍쉎쉏숶쇅쇇쇉쇊쇋쇍쇎쇏쇐쇑쇒쇓쇕쇖쇙쇚쇛쇜쇝쇞쇟쇆쉓쉕쉖쉗쉙쉚쉛쉜쉝쉞쉟쉢쉣쉦쉧쉨쉩쉪쉫쉒쉤잓잕잙잛잜잝잞잟잢잧잨잩잪잫잒쟋쟍쟏쟑쟒쟓쟔쟕쟖쟗쟚쟛쟞쟟쟠쟡쟢쟣쟊쟜젃젅젆젇젉젋젌젍젎젏젒젗젘젙젚젛젂젻젽젾젿졁졂졃졄졅졆졇졊졎졏졐졑졒졓젺졳졵졶졷졹졻졼졽졾졿좂좈좉좊졲좄죣죥죦죧죩죪죫죬죭죮죯죱죲죳죶죷죸죹죺죻죢죴죿줁줂줃줇줈줉줊줋줎줒줓줔줕줖줗죾줐쥭쥯쥱쥲쥳쥵쥶쥷쥸쥹쥺쥻쥽쥾쥿즂즃즄즅즆즇쥮즀즋즍즎즏즑즒즓즔즕즖즗즚즞즟즠즡즢즣즊즜짃짅짆짉짋짌짍짎짏짒짗짘짛짂짔잯잱잲잳잵잶잷잸잹잺잻잾쟂쟃쟄쟅쟆쟇잮쟥쟧쟩쟪쟫쟭쟮쟯쟰쟱쟲쟳쟴쟵쟶쟷쟹쟺쟻쟼쟽쟾쟿쟦쟸젟젡젢젣젥젦젧젨젩젪젫젮젲젳젴젵젷젞졕졗졙졚졛졝졞졟졠졡졢졣졤졥졦졧졩졪졫졬졭졮졯졖졨죅죇죉죊죋죍죎죏죐죑죒죓죖죚죛죜죝죞죟죆쥓쥕쥖쥙쥚쥛쥜쥝쥞쥟쥢쥥쥦쥧쥨쥩쥪쥫쥒쥤즥즧즨즩즪즫즬즭즮즯즰즱즲즳즴즵즶즷즹즺즻즼즽즾즿즦즸좏좑좒좓좕좖좗좘좙좚좛좜좞좢좣좤좥좦좧좎좠줙줛줜줝줞줟줠줡줢줣줤줥줦줧줨줩줪줫줭줮줯줰줱줲줳줚좩좫좬좭좮좯좰좱좲좳좴좵좶좷좸좹좺좻좾좿죀죁죂죃좪줵줷줹줺줻줽줾줿쥀쥁쥂쥃쥆쥇쥉쥊쥋쥌쥍쥎쥏줶찫찭찯찱찲찳찴찵찶찷찺찿챀챁챂챃찪챡챣챥챧챩챪챫챬챭챮챯챲챳챶챷챸챹챺챻챢챴첛첝첞첟첡첢첣첤첥첦첧첪첮첯첰첱첲첳첚쳓쳕쳖쳗쳙쳚쳛쳜쳝쳞쳟쳠쳡쳢쳣쳥쳦쳧쳨쳩쳪쳫쳒촋촍촎촏촑촒촓촔촕촖촗촚촞촟촠촡촢촣촊촜쵹쵻쵽쵾쵿춁춂춃춄춅춆춇춉춊춋춍춎춏춐춑춒춓쵺춌춗춙춚춝춞춟춠춡춢춣춦춪춫춬춭춮춯춖춨츅츇츉츊츋츍츎츏츐츑츒츓츕츖츗츚츛츜츝츞츟츆츘츣츥츦츧츩츪츫츬츭츮츯츲츶츷츸츹츺츻츢츴칛칝칞칢칣칤칥칦칧칪칮칯칰칱칲칳칚칬챇챉챊챋챍챎챏챐챑챒챓챖챚챛챜챝챞챟챆챽챿첀첁첂첃첄첅첆첇첈첉첊첋첌첍첎첏첑첒첓첔첕첖첗챾첐첷첹첺첻첽첾첿쳀쳁쳂쳃쳆쳊쳋쳌쳍쳎쳏첶쳭쳯쳱쳲쳳쳴쳵쳶쳷쳸쳹쳺쳻쳼쳽쳾쳿촂촃촄촅촆촇쳮촀쵝쵟쵡쵢쵣쵥쵦쵧쵨쵩쵪쵫쵮쵲쵳쵴쵵쵶쵷쵞쵰췩췫췭췮췯췱췲췳췴췵췶췷췺췾췿츀츁츂츃췪췼츽츿칀칁칂칃칄칅칆칇칈칉칊칋칌칍칎칏칑칒칓칔칕칖칗츾칐촧촩촪촫촭촮촯촰촱촲촳촴촵촶촷촺촻촼촽촾촿촦촸춱춳춴춵춶춷춸춹춺춻춼춽춾춿췀췁췂췅췆췇췈췉췊췋춲쵁쵃쵅쵆쵇쵈쵉쵊쵋쵌쵍쵎쵏쵐쵑쵒쵓쵕쵖쵗쵘쵙쵚쵛쵂쵔췍췏췑췒췓췔췕췖췗췘췙췚췛췜췝췞췟췡췢췣췤췥췦췧췎췠칷칹칺칻칽칾칿캀캁캂캃캆캊캋캌캍캏칶캯캱캲캳캴캵캶캷캸캹캺캻캾캿컂컃컄컅컆컇캮컀컧컩컪컭컮컯컰컱컲컳컶컺컻컼컿컦켝켟켡켢켣켥켦켧켨켩켪켫켮켲켳켴켵켶켷켞콗콙콚콛콝콞콟콠콡콢콣콦콪콫콬콭콮콯콖콨쿅쿇쿈쿉쿊쿋쿌쿍쿎쿏쿐쿑쿒쿓쿔쿕쿖쿗쿙쿚쿛쿜쿝쿞쿟쿆쿘쿣쿥쿦쿧쿩쿪쿫쿬쿭쿮쿯쿲쿶쿷쿸쿹쿺쿻쿢쿴큑큓큕큖큗큙큚큛큜큝큞큟큡큢큣큥큦큧큨큩큪큫큒큤큯큱큲큳큵큶큷큸큹큺큻큾큿킂킃킄킅킆킇큮킀킧킩킪킫킭킮킯킰킱킲킳킶킺킻킼킽킿킦킸캓캕캖캗캙캚캛캜캝캞캟캢캦캧캨캩캫캒컉컋컌컍컎컏컐컑컒컓컔컕컖컗컘컙컚컛컝컞컟컠컡컢컣컊컜켃켅켆켇켉켊켋켌켍켎켏켒켖켗켘켙켚켛켂켔켹켻켼켽켾켿콀콁콂콃콄콅콆콇콈콉콊콋콍콎콏콐콑콒콓켺콌쾩쾫쾬쾭쾮쾯쾱쾲쾳쾴쾵쾶쾷쾸쾹쾺쾻쾽쾾쾿쿀쿁쿂쿃쾪쾼퀷퀹퀺퀻퀽퀾퀿큀큁큂큃큆큊큋큌큍큎큏퀶큈킉킋킌킍킎킏킐킑킒킓킔킕킖킗킘킙킚킛킝킞킟킠킡킢킣킊킜콳콵콶콷콹콺콻콼콽콾콿쾁쾂쾃쾆쾇쾈쾉쾊쾋콲쾄쿽쿿퀁퀂퀃퀅퀆퀇퀈퀉퀊퀋퀌퀍퀎퀏퀒퀓퀔퀕퀖퀗쿾퀐쾍쾏쾑쾒쾓쾕쾖쾗쾘쾙쾚쾛쾜쾝쾞쾟쾢쾣쾤쾥쾦쾧쾎쾠퀛퀜퀝퀞퀟퀡퀢퀣퀤퀥퀦퀧퀨퀩퀪퀫퀮퀯퀰퀱퀲퀳퀚퀬탃탅탆탇탊탋탌탍탎탏탒탖탗탘탙탛탂탹탻탽탾탿턀턁턂턃턄턅턆턇턈턉턊턋턎턏턐턑턒턓탺턌턳턵턶턷턹턻턼턽턾턿텂텆텇텈텉텊텋턲텩텫텭텮텯텰텱텲텳텴텵텶텷텸텹텺텻텽텾텿톀톁톂톃텪톣톥톦톧톩톪톫톬톭톮톯톲톶톷톸톹톻톢톴툑툓툔툕툖툗툘툙툚툛툜툝툞툟툠툡툢툣툥툦툧툨툩툪툫툒툤툯툱툲툳툵툶툷툸툹툺툻툾퉂퉃퉄퉅퉆퉇툮퉀튝튟튡튢튣튥튦튧튨튩튪튫튭튮튯튲튳튴튵튶튷튞튰튻튽튾틁틃틄틅틆틇틊틎틏틐틑틒틓튺틌틳틵틶틷틹틺틻틼틽틾틿팂팆팇팈팉팊팋틲팄탟탡탢탣탥탦탧탨탩탪탫탮탲탳탴탵탷탞턕턗턘턙턚턛턜턝턞턟턠턡턢턣턤턥턦턧턩턪턫턬턭턮턯턖턨텏텑텒텓텕텖텗텘텙텚텛텞텢텣텤텥텧텎텠톅톇톉톊톋톌톍톎톏톐톑톒톓톔톕톖톗톙톚톛톜톝톞톟톆톘퇵퇷퇹퇺퇻퇼퇽퇾퇿툀툁툂툃툄툅툆툊툋툌툍툎툏퇶툈튃튅튆튇튉튊튋튌튍튎튏튒튓튖튗튘튙튚튛튂튔틕틗틙틚틛틝틞틟틠틡틢틣틦틧틩틪틫틬틭틮틯틖틨톽톿퇁퇂퇃퇄퇅퇆퇇퇈퇉퇊퇋퇌퇍퇎퇏퇑퇒퇓퇔퇕퇖퇗톾퇐퉉퉋퉌퉍퉎퉏퉐퉑퉒퉓퉔퉕퉖퉗퉘퉙퉚퉛퉝퉞퉟퉠퉡퉢퉣퉊퇙퇛퇜퇝퇞퇟퇠퇡퇢퇣퇤퇥퇦퇧퇨퇩퇪퇫퇭퇮퇯퇰퇱퇲퇳퇚퇬퉥퉧퉩퉪퉫퉬퉭퉮퉯퉰퉱퉲퉳퉴퉵퉶퉷퉹퉺퉻퉼퉽퉾퉿퉦팏팑팒팓팕팗팘팙팚팛팞팢팣팤팦팧퍇퍈퍉퍊퍋퍌퍍퍎퍏퍐퍑퍒퍓퍔퍕퍖퍗퍙퍚퍛퍜퍝퍞퍟퍆퍘퍿펁펂펃펅펆펇펈펉펊펋펎펒펓펔펕펖펗퍾펷펹펺펻펽펾펿폀폁폂폃폆폊폋폌폍폎폏펶폯폱폲폳폵폶폷폸폹폺폻폾퐂퐃퐄퐅퐆퐇폮퐀푝푟푡푢푣푥푦푧푨푩푪푫푬푮푱푲푳푴푵푶푷푞푰푻푽푾풁풃풄풅풆풇풊풎풏풐풑풒풓푺풌퓩퓫퓭퓮퓯퓱퓲퓳퓴퓵퓶퓷퓹퓺퓾퓿픀픁픂픃퓪퓼픅픇픉픊픋픍픎픏픐픑픒픓픖픚픛픜픝픞픟픆픘픿핁핂핃핅핆핇핈핉핊핋핎핒핓핔핕핖핗픾핐팫팭팮팯팱팲팳팴팵팶팷팺팾팿퍀퍁퍂퍃팪퍡퍣퍤퍥퍦퍧퍨퍩퍪퍫퍬퍭퍮퍯퍰퍱퍲퍳퍵퍶퍷퍸퍹퍺퍻퍢퍴펛펝펞펟펡펢펣펤펥펦펧펪펮펯펰펱펳펚펬폑폓폕폖폗폙폚폛폜폝폞폟폠폢폥폦폧폨폩폪폫폒폤푁푃푅푆푇푈푉푊푋푌푍푎푏푐푑푒푓푕푖푗푘푙푚푛푂푔퓍퓏퓑퓒퓓퓕퓖퓗퓘퓙퓚퓛퓝퓞퓡퓢퓣퓤퓥퓦퓧퓎퓠픡픣픥픦픧픨픩픪픫픬픭픮픯픰픱픲픳픵픶픷픸픹픺픻픢픴퐉퐋퐌퐍퐎퐏퐐퐑퐒퐓퐔퐕퐖퐗퐘퐙퐚퐛퐞퐟퐠퐡퐢퐣퐊퐜풕풗풘풙풚풛풜풝풞풟풠풡풢풣풤풥풦풧풪풫풬풭풮풯풖풨퐤퐥퐧퐨퐩퐪퐫퐬퐭퐮퐯퐰퐱퐲퐳퐴퐵퐶퐷퐹퐺퐻퐼퐽퐾퐿퐦퐸풰풱풳풴풵풶풷풸풹풺풻풼풽풾풿퓀퓁퓂퓃퓅퓆퓇퓈퓉퓊퓋풲퓄핛핝핞핟핡핢핣핤핦핧핪핮핯핰핱핲핳핚핬햑햓햔햕햖햗햘햙햚햛햜햝햞햟햠햡햢햣햦햧햨햩햪햫햒햤헋헍헎헏헑헓헔헖헚헞헟헠헡헢헣헊헜혃혅혆혇혉혊혋혌혍혎혏혒혖혗혘혙혚혛혂혻혽혾홁홂홃홄홆홇홊홎홏홐홒홓혺홌횩횫횭횮횯횱횲횳횴횵횶횷횸횺횽횾횿훀훁훂훃횪횼훇훉훊훋훍훎훏훐훒훓훖훚훛훜훝훞훟훆훘휷휹휺휻휽휾휿흀흁흂흃흅흆흊흋흌흍흎흏휶흈흓흕흚흛흜흞흟흢흦흧흨흪흫흒흤힋힍힎힏힑힒힓힔힕힖힗힚힞힟힠힡힢힣힊힜핷핹핺핻핽핾핿햀햁햂햃햆햊햋햌햍햎햏핶햭햯햰햱햲햳햴햵햶햷햸햹햺햻햼햽햾햿헁헂헃헄헅헆헇햮헀헧헩헪헫헭헮헯헰헱헲헳헶헺헻헼헽헾헿헦혝혟혡혢혣혥혦혧혨혩혪혫혬혮혯혱혲혳혴혵혶혷혞혰횏횑횒횓횕횖횗횘횙횚횛횜횞횢횣횤횥횦횧횎횠휛휝휞휟휡휢휣휤휥휦휧휪휮휯휰휱휲휳휚휬흭흯흱흲흳흵흶흷흸흹흺흻흾흿힂힃힄힅힆힇흮힀홗홙홚홛홝홞홟홠홡홢홣홦홪홫홬홭홮홯홖홨훣훥훦훧훩훪훫훬훭훮훯훱훲훳훶훷훸훹훺훻훢훴홳홵홶홷홸홹홺홻홼홽홾홿횀횁횂횆횇횈횉횊횋홲훿휁휂휃휅휆휇휈휉휊휋휌휍휎휏휒휓휔휕휖휗훾휐깏깑깒깕깗깘깙깚깛깞깢깣깤깦깧꺇꺉꺊꺋꺍꺎꺏꺐꺑꺒꺓꺔꺕꺖꺗꺙꺚꺛꺜꺝　、。，．·：；？！‥…～〃―‐＿￣／＼｜∥∕∖゛゜´｀¨＾ˇ˙︐︒︑⋮ⸯ‘’“”（）〔〕［］｛｝〈〉《》「」『』【】‚‛„‟︵︶︹︺﹇﹈︷︸︿﹀︽︾﹁﹂﹃﹄︻︼???????????꺞꺟꺆꺘꺿껁껂껃껅껆껇껈껉껊껋껎껒껓껔껕껖껗껵껷껹껺껻껽껾껿꼀꼁꼂꼃꼄꼅꼆꼉꼊꼋꼌꼎꼏껶꼯꼳꼵꼶꼷꼸꼹꼺꼻꼾꽄꽅꽆꽇꼮꽀꾝꾟꾠꾡꾢꾣꾤꾥꾦꾧꾨꾩꾪꾫꾬꾭꾮꾯꾱꾲꾳꾴꾵꾶＋－±×÷＝≠＜＞≦≧∞∴♂♀∠⊥⌒∂∇≡≒≈≪≫√∽∝∵∫∬∮∈∋⊆⊇⊂⊃∉∌⊈⊉⊄⊅∪∩∧∨￢⇒⇔∀∃∑＃＆＊＠§※☆★○●◎◇◆□■△▲▽▼▷◁▶◀∘∙❖⚐⚑♯♭♪†‡¶⊕⊖꾷꾞꾰꾻꾽꾾꿁꿂꿃꿄꿅꿆꿊꿏꿐꿑꿒꿓꾺꿌뀩뀫뀬뀭뀮뀯뀰뀱뀲뀳뀴뀵뀶뀷뀸뀹뀺뀻뀽뀾뀿끀끁끂끃뀪뀼끇끉끋끍끏끐끑끒끖끚끛끜끞끟끆끘끿낁낂낃낅낆낇낈낉낊낋낎낒낓낔낕낖낗끾낐깫???????????????０１２３４５６７８９???????ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ??????ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ????깭깮깯깱깲깳깴깵깶깷깺깾깿꺀꺁꺂꺃깪꺡꺣꺤꺥꺦꺧꺨꺩꺪꺫꺬꺭꺮꺯꺰꺱꺲꺳꺵꺶꺷꺸꺹꺺꺻꺢꺴껛껝껞껟껡껢껣껤껥껦껧껪껮껯껰껱껲껳껚꼑꼓꼔꼕꼖꼗꼘꼙꼚꼛꼜꼝꼞꼟꼠꼡꼢꼣꼥꼦ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅑㅓㅕㅗㅛㅜㅠㅡㅣㅐㅒㅔㅖㅚㅟㅢㅘㅝㅙㅞㄳㄵㄶㄺㄻㄼㄽㄾㄿㅀㅄㅿㆁㆆㆍᄼᄽᄾᄿᅎᅏᅐᅑᅔᅕ????????????????????꼧꼨꼩꼪꼫꼒꼤꾃꾅꾆꾇꾉꾊꾋꾌꾍꾎꾏꾒꾓꾖꾗꾘꾙꾚꾛꾂꾔뀍뀏뀑뀒뀓뀕뀖뀗뀘뀙뀚뀛뀞뀟뀢뀣뀤뀥뀦뀧뀎뀠끠끡끣끤끥끦끧끨끩끪끫끬끭끮끯끰끱끲끳끵끶끷끸끹끺끻끢끴꽋꽍꽎꽏꽑꽒АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ???????????????абвгдеёжзийклмнопрстуфхцчшщъыьэюя?????????????꽓꽔꽕꽖꽗꽘꽙꽚꽞꽟꽠꽡꽢꽣꽊꿕꿗꿙꿚꿛꿝꿞꿟꿠꿡꿢꿣꿤꿦꿪꿫꿬꿭꿮꿯꿖꽧꽩꽪꽫꽭꽮꽯꽰꽱꽲꽳꽴꽵꽶꽷꽺꽻꽼꽽꽾꽿꽦꽸꿳꿵꿶꿷꿹꿺꿻꿼꿽꿾꿿뀂뀃뀆뀇뀈뀉뀊뀋꿲딳딵딶딷딹ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ????????αβγδεζηθικλμνξοπρστυφχψω????????ⅠⅡⅢⅣⅤⅥⅦⅧⅨⅩ??????ⅰⅱⅲⅳⅴⅵⅶⅷⅸⅹ????딺딻딼딽딾땂땆땇땈땉땊땩땫땬땭땮땯땱땲땳땴땵땶땷땸땹땺땻땽땾땿떀떁떂떃땪땼떣떥떦떧떩떬떭떮떯떲떶떷떸떹떺떢뗙뗛뗜뗝뗞뗟뗠뗡뗢뗣뗤뗥뗦뗧뗨뗩뗪뗫뗭뗮뗯뗰뗱뗲뗳뗚똓똕똖똗똙①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳㉑㉒㉓㉔㉕㉖㉗㉘㉙㉚??㉠㉡㉢㉣㉤㉥㉦㉧㉨㉩㉪㉫㉬㉭??㉮㉯㉰㉱㉲㉳㉴㉵㉶㉷㉸㉹㉺㉻?⁰¹²³⁴⁵⁶⁷⁸⁹½⅓⅔¼¾?₀₁₂₃₄₅₆₇₈₉똚똛똜똝똞똟똢똦똧똨똩똪똫똒똤뚁뚃뚄뚅뚆뚇뚈뚉뚊뚋뚌뚍뚎뚏뚐뚑뚒뚓뚕뚖뚗뚘뚙뚚뚛뚂뚔뚟뚡뚢뚣뚥뚦뚧뚨뚩뚪뚮뚯뚲뚳뚴뚵뚶뚷뚞뚰뜍뜏뜐뜑뜒뜓뜔뜕뜖뜗뜘뜙뜚뜛뜜뜝뜞뜟뜡뜢뜣뜤°′″℃℉€￦＄￠￡￥％‰Å㏄㎡㎥㎝㎠㎤㎜㎟㎣㍷㍸㍹㎞㎢㎦㎙㎚㎛㎧㎨㎍㎎㎏㎴㎵㎶㎷㎸㎹㎀㎁㎂㎃㎄㎺㎻㎼㎽㎾㎿Ω㏀㏁㎐㎑㎒㎓㎔㏞㏟㎰㎱㎲㎳㎊㎋㎌㎩㎪㎫㎬ℓ㎕㎖㎗㎘㏿㎈㎉㎭㎮㎯㋌㏝㏈㋍㋎㏖㏋㏊뜥뜦뜧뜎뜠뜫뜭뜮뜱뜲뜳뜴뜵뜶뜷뜺뜾뜿띀띁띂띃뜪뜼띣띥띦띧띩띪띫띬띭띮띯띲띶띷띸띹띺띻띢띴땏땑땒땓땕땖땗땘땙땚땛땞땢땣땤땥땦땧땎떄떅떇떈떉떊떋떌떍떎떏떐떑떒떓떔떕떖떗떙떚─│┌┐┘└├┬┤┴┼━┃┏┓┛┗┣┳┫┻╋┠┯┨┷┿┝┰┥┸╂┒┑┚┙┖┕┎┍┞┟┡┢┦┧┩┪┭┮┱┲┵┶┹┺┽┾╀╁╃╄╅╆╇╈╉╊??????????????????????????떛떜떝떞떟떆떘떿뗁뗂뗃뗅뗆뗇뗈뗉뗊뗋뗎뗒뗓뗔뗕뗖뗗떾뗴뗵뗷뗸뗹뗺뗻뗼뗽뗾뗿똀똁똂똃똄똅똆똇똉똊똋똌똍똎똏뗶똈뙥뙧뙩뙪뙫뙬뙭뙮뙯뙰뙱뙲뙳뙴뙵뙶뙷뙹뙺뙻뙼뙽뙾뙿뙦뙸뛱뛳뛵뛶ぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをん???????????뛷뛹뛺뛻뛼뛽뛾뛿뜂뜃뜆뜇뜈뜉뜊뜋뛲뜄띇띉띊띋띍띎띏띐띑띒띓띖띗띚띛띜띝띞띟띆띘똭똯똱똲똳똵똶똷똸똹똺똻똼똽똾똿뙁뙂뙃뙄뙅뙆뙇똮뙀뚹뚻뚼뚽뚾뚿뛀뛁뛂뛃뛄뛅뛆뛇뛈뛉뛊뛋뛍뛎ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ????????뛏뛐뛑뛒뛓뚺뙋뙌뙍뙎뙏뙐뙑뙒뙓뙔뙕뙖뙗뙘뙙뙚뙛뙝뙞뙟뙠뙡뙢뙣뙊뙜뛕뛗뛘뛙뛚뛛뛜뛝뛞뛟뛠뛡뛢뛣뛤뛥뛦뛧뛩뛪뛫뛬뛭뛮뛯뛖뛨빣빥빦빧빩빫빬빭빮빯빲빶빷빸빹빺빢뺛뺝뺞뺟뺠뺡뺢뺣⍟☀☂☔☁❄⚡⚠№→←↑↓↗↖↘↙↔↕⇨⇦⇧⇩⬀⬁⬂⬃⬄⇳➡⬅⬆⬇⬈⬉⬊⬋⬌⬍♣♥♠♦〒?☏☎⏎☕㉼㉽㈝㈞㏇㋏㉐℡℻㍺®?????????????????????????????뺤뺥뺦뺧뺩뺪뺫뺭뺮뺯뺰뺱뺲뺳뺚뺬뻓뻕뻖뻙뻚뻛뻜뻝뻞뻟뻡뻢뻦뻧뻨뻩뻪뻫뻒뼋뼌뼍뼎뼏뼐뼑뼒뼓뼔뼕뼖뼗뼚뼞뼟뼠뼡뼢뼣뼊뽃뽅뽆뽇뽉뽊뽋뽌뽍뽎뽏뽒뽖뽗뽘뽙뽚뽛뽂뽔뾱뾳뾴뾵뾶뾷뾸뾹??????????????????????????????????????????????????????????????????????????????????????????????뾺뾻뾼뾽뾾뾿뿀뿁뿂뿃뿆뿇뿈뿉뿊뿋뾲뿄뿏뿑뿒뿓뿕뿖뿗뿘뿙뿚뿛뿞뿢뿣뿤뿥뿦뿧뿎뿠쀽쀿쁀쁁쁂쁃쁄쁅쁆쁇쁈쁉쁊쁋쁌쁍쁎쁏쁒쁓쁔쁕쁖쁗쀾쁐쁙쁛쁝쁞쁟쁡쁢쁣쁤쁥쁦쁧쁪쁫쁭쁮쁯쁰쁱쁲??????????????????????????????????????????????????????????????????????????????????????????????쁳쁚쁬삓삕삖삗삙삚삛삜삝삞삟삢삦삧삨삩삪삫삒삤빿뺁뺂뺃뺅뺆뺇뺈뺉뺊뺋뺎뺒뺓뺔뺕뺖뺗빾뺵뺷뺸뺹뺺뺻뺼뺽뺾뺿뻀뻁뻂뻃뻄뻅뻆뻇뻉뻊뻋뻌뻍뻎뻏뺶뻈뻯뻱뻲뻳뻵뻶뻷뻸뻹뻺뻻뻽뻾뻿뼂??????????????????????????????????????????????????????????????????????????????????????????????뼃뼄뼅뼆뼇뻮뼀뼤뼥뼧뼨뼩뼪뼫뼬뼭뼮뼯뼰뼱뼲뼳뼴뼵뼶뼷뼹뼺뼻뼼뼽뼾뼿뼦뼸뾕뾗뾘뾙뾚뾛뾜뾝뾞뾟뾠뾡뾢뾣뾤뾥뾦뾧뾩뾪뾫뾬뾭뾮뾯뾖뾨쀡쀣쀤쀥쀦쀧쀨쀩쀪쀫쀬쀭쀮쀯쀰쀱쀲쀳쀵쀶쀷쀸가각간갇갈갉갊감갑값갓강갖갗같갚갛갔갸갹갼걀걈걋걍거걱건걷걸걹걺검겁것겅겆겉겊겋겄겨격견겯결겸겹겻경곁겪겼고곡곤곧골곪곬곯곰곱곳공곶곺교굔굘굡굣구국군굳굴굵굶굻굼굽굿궁궂규균귤귬귱그극근귿쀹쀺쀻쀢쀴쁵쁷쁸쁹쁺쁻쁼쁽쁾쁿삀삁삂삃삄삅삆삇삉삊삋삌삍삎삏쁶삈뽝뽟뽠뽡뽢뽣뽤뽥뽦뽧뽨뽩뽪뽫뽬뽭뽮뽯뽱뽲뽳뽴뽵뽶뽷뽞뽰뿩뿫뿬뿭뿮뿯뿰뿱뿲뿳뿴뿵뿶뿷뿸뿹뿺뿻뿽뿾뿿쀀쀁쀂쀃글긁긇금급긋긍기긱긴긷길긺김깁깃깅깆깇깉깊개객갠갤갬갭갯갱갰걔걘걜게겍겐겔겜겝겟겡겠계곈곌곕곗괴괵괸괼굄굅굇굉굈귀귁귄귈귐귑귓긔과곽관괃괄괆괌괍괏광괐궈궉권궐궘궝궜괘괙괜괠괩괭괬궤궥궷나낙뿪뿼뽸뽹뽻뽼뽽뽾뽿뾀뾁뾂뾃뾄뾅뾆뾇뾈뾉뾊뾋뾍뾎뾏뾐뾑뾒뾓뽺뾌쀄쀅쀇쀈쀉쀊쀋쀌쀍쀎쀏쀐쀑쀒쀓쀔쀕쀖쀗쀙쀚쀛쀜쀝쀞쀟쀆쀘싽싾싿쌁쌂쌃쌄쌅쌆쌇쌊쌎쌏쌐쌑쌒싺쌱쌳쌵쌶쌷쌹쌺쌻쌼낛난낟날낡낢남납낫낭낮낯낱낳낚났냐냑냔냘냠냡냥너넉넋넌널넒넓넘넙넛넝넢넣넊넜녀녁년녈념녑녓녕녘녔노녹논놀놂놈놉놋농높놓뇨뇩뇬뇰뇸뇹뇻뇽누눅눈눋눌눔눕눗눙눞뉴뉵뉸뉼늄늅늉느늑는늘늙늚늠늡늣능쌽쌾쌿썀썁썂썃썆썇썈썉썊썋쌲썄썫썭썮썯썱썳썴썵썶썷썺썾썿쎀쎁쎂쎃쎡쎣쎤쎥쎦쎧쎨쎩쎪쎫쎬쎭쎮쎯쎰쎱쎲쎳쎵쎶쎷쎸쎹쎺쎻쎢쎴쏛쏝쏞쏡쏣쏤쏥쏦쏧쏪쏮쏯쏰쏱쏲쏳쏚쏬쑉쑋쑍쑎쑏쑑쑒늦늪니닉닌닐닒님닙닛닝닢내낵낸낼냄냅냇냉냈냬네넥넨넬넴넵넷넹넸녜녠뇌뇐뇔뇜뇝뇟뉘뉜뉠뉨뉩뉭늬늰늴늼닁놔놘놜놧놨눠눨눳눴놰눼다닥단닫달닭닮닯닲닳담답닷당닺닻닾닿닦닸댜더덕던덛덜덞덟덤덥덧덩덫쑓쑔쑕쑖쑗쑙쑚쑛쑞쑟쑠쑡쑢쑣쑊쑜쑧쑩쑪쑫쑭쑮쑯쑰쑱쑲쑳쑶쑷쑺쑻쑼쑽쑾쑿쑦쑸쓕쓗쓙쓚쓛쓜쓝쓞쓟쓠쓡쓢쓣쓤쓥쓦쓪쓫쓬쓭쓮쓯쓖쓨쓳쓵쓶쓷쓹쓻쓼쓽쓾씂씃씆씇씈씉씊씋쓲씄씫씭씮씱덮덯덖덨뎌뎐뎔뎡뎠도독돈돋돌돎돐돔돕돗동돛돝됴두둑둔둘둠둡둣둥듀듄듈듐듕드득든듣들듥듦듧듬듭듯등디딕딘딛딜딤딥딧딩딪딮딨대댁댄댈댐댑댓댕댔댸데덱덴덷델뎀뎁뎃뎅뎄뎨뎬되된될됨됩됫됭됬뒤뒥뒨뒬씲씳씴씵씶씷씺씾씿앀앁앂앃씪쌗쌙쌚쌛쌝쌞쌟쌠쌡쌢쌣쌦쌪쌫쌬쌭쌮쌯쌖썍썏썐썑썒썓썔썕썖썗썘썙썚썛썜썝썞썟썡썢썣썤썥썦썧썎썠쎇쎉쎊쎋쎍쎎쎏쎐쎑쎒쎓쎖쎗쎚쎛쎜쎝쎞쎟쎆쎘쎽쎿쏁뒴뒵뒷뒹듸듼딀딉딍돠돤돨둬둰둴둼둿뒀돼됀됄됐뒈뒝라락란랄람랍랏랑랒랖랗랐랴략랸랼럄럅럇량러럭런럴럼럽럿렁렆렇렀려력련렬렴렵렷령렸로록론롤롬롭롯롱롶료룐룔룜룝룟룡루룩룬룰룸룹룻룽류륙륜률륨륩쏂쏃쏄쏅쏆쏇쏈쏉쏊쏋쏌쏍쏎쏏쏑쏒쏓쏔쏕쏖쏗쎾쏐쐯쐱쐲쐳쐵쐶쐷쐸쐹쐺쐻쐾쐿쑁쑂쑃쑄쑅쑆쑇쐮쒹쒻쒽쒾쒿쓀쓁쓂쓃쓄쓅쓆쓇쓈쓉쓊쓋쓍쓎쓏쓐쓑쓒쓓쒺쓌씍씏씑씒씓씕씖씗씘씙씚씛씝씞륫륭르륵른를름릅릇릉릊릍릎리릭린릴림립릿링맆래랙랜랠램랩랫랭랬럐레렉렌렐렘렙렛렝렜례롄롈롑롓뢰뢴뢸룀룁룃룅룄뤼뤽륀륄륌륏륑릐릔릘릠롸롼뢉뢍뤄뤘뢔뢨뤠마막만많맏말맑맒맘맙맛망맞맟맡맣먀먁먄먈씟씡씢씣씤씥씦씧씎씠쏷쏹쏺쏻쏽쏾쏿쐀쐁쐂쐃쐄쐅쐆쐊쐋쐌쐍쐎쐏쏶쒁쒃쒄쒅쒆쒇쒈쒉쒊쒋쒌쒍쒎쒏쒐쒑쒒쒓쒕쒖쒗쒘쒙쒚쒛쒂쐓쐔쐕쐖쐗쐘쐙쐚쐛쐜쐝쐞쐟쐠쐡쐢쐣쐥쐦쐧쐨쐩쐪쐫쐒쒝쒟먐먕머먹먼멀멁멂멈멉멋멍멎멓멌며멱면멸몀몁몃명몇몄모목몫몬몯몰몲몸몹못몽뫃묘묜묠묩묫무묵문묻물묽묾뭄뭅뭇뭉뭍뭏묶뮤뮥뮨뮬뮴뮷뮹므믄믈믐믑믓믕미믹민믿밀밂밈밉밋밍및밑밌매맥맨맬맴맵맷맹맺맸먜쒡쒢쒣쒤쒥쒦쒧쒨쒩쒪쒫쒬쒮쒯쒱쒲쒳쒴쒵쒶쒷쒞쒰짟짡짣짥짦짨짩짪짫짮짲짳짴짵짶짷짞쨕쨗쨙쨚쨛쨜쨝쨞쨟쨠쨡쨢쨣쨥쨦쨧쨪쨫쨬쨭쨮쨯쨖쨨쩏쩑쩒쩓쩕쩖쩘쩙쩚쩛쩞쩢쩣쩤쩥쩦쩧쩎쪅쪇메멕멘멜멤멥멧멩멨몌몐뫼묀묄묌묍묏묑뮈뮌뮐믜믠믬뫄뫈뫙뫘뭐뭔뭘뭠뭡뭣뭤뫠뭬바박밗반받발밝밞밟밤밥밧방밭밖뱌뱍뱐뱜뱝버벅번벋벌벍벎범법벗벙벚벜벘벼벽변별볌볍볏병볓볕볐보복본볼봄봅봇봉봏볶뵤뵨쪈쪉쪊쪋쪌쪍쪎쪏쪐쪑쪒쪓쪔쪕쪖쪗쪙쪚쪛쪜쪝쪞쪟쪆쪿쫁쫂쫃쫅쫆쫇쫈쫉쫊쫋쫎쫔쫕쫖쪾쫐쬭쬯쬱쬲쬳쬴쬵쬶쬷쬸쬹쬺쬻쬽쬾쬿쭂쭃쭄쭅쭆쭇쬮쭀쭋쭍쭎쭏쭑쭒쭓쭔쭕쭖쭗쭚쭞쭟쭠쭡쭢쭣쭊뵬부북분붇불붉붊붐붑붓붕붙붚뷰뷴뷸븀븁븃븅브븍븐블븜븝븟븡비빅빈빌빎빔빕빗빙빚빛배백밴밷밸뱀뱁뱃뱅뱉뱄뱨베벡벤벧벨벰벱벳벵벴볘볜뵈뵉뵌뵐뵘뵙뵜뷔뷕뷘뷜뷩븨븬븰븽봐봔봡봣봤붜붤붯붴붰봬봰뵀붸쭜쮹쮻쮼쮽쮾쮿쯁쯂쯃쯄쯅쯆쯇쯈쯉쯊쯋쯍쯎쯏쯐쯑쯒쯓쮺쯌쯗쯙쯚쯛쯝쯞쯟쯠쯡쯢쯣쯥쯦쯫쯬쯭쯮쯯쯖쯨찏찑찒찓찕찖찗찘찙찚찛찞찣찤찥찎찠짻짽짾짿쨁쨂쨃쨄쨅쨆쨇쨊쨎쨏쨐쨑쨒쨓짺쨱사삭삯산삳살삵삶삼삽삿상샅샀샤샥샨샬샴샵샷샹서석섟선섣설섦섧섬섭섯성섶섞섰셔셕션셜셤셥셧셩셨소속손솓솔솖솜솝솟송솥솎쇼쇽숀숄숌숍숏숑수숙순숟술숨숩숫숭숯숱숲슈슉슌슐슘슙슛슝스슥슨슬슭슲슳슴쨳쨵쨶쨷쨸쨹쨺쨻쨼쨽쨾쨿쩀쩁쩂쩃쩅쩆쩇쩈쩉쩊쩋쨲쩄쩫쩭쩮쩯쩱쩲쩳쩴쩵쩶쩷쩺쩻쩾쩿쪀쪁쪂쪃쩪쩼쪡쪣쪤쪥쪦쪧쪨쪩쪪쪫쪬쪭쪮쪯쪰쪱쪲쪳쪵쪶쪷쪸쪹쪺쪻쪢쪴쬑쬓쬕쬖쬗쬙쬚쬛쬜쬝쬞습슷승시식신싣실싫심십싯싱싶새색샌샐샘샙샛생샜섀섄섈섐섕세섹센셀셈셉셋셍셑셒셌셰셴셸솅쇠쇡쇤쇨쇰쇱쇳쇵쇴쉬쉭쉰쉴쉼쉽쉿슁싀싄솨솩솬솰솻솽숴쉈쇄쇈쇌쇔쇗쇘쉐쉑쉔쉘쉠쉡쉥자작잔잖잗잘잚잠잡잣장쬟쬢쬣쬥쬦쬧쬨쬩쬪쬫쬒쮝쮟쮠쮡쮢쮣쮤쮥쮦쮧쮨쮩쮪쮫쮬쮭쮮쮯쮱쮲쮳쮴쮵쮶쮷쮞쮰쯱쯳쯵쯶쯷쯸쯹쯺쯻쯼쯽쯾쯿찀찁찂찃찅찆찇찈찉찊찋쯲찄쫛쫝쫞쫟쫡쫢쫣쫤쫥쫦쫧쫨쫩쫪쫫쫮쫯쫰쫱쫲잦잤쟈쟉쟌쟎쟐쟘쟙쟝저적전절젊점접젓정젖젔져젹젼졀졈졉졋졍졌조족존졸졺좀좁좃종좆좇좋죠죡죤죨죰죵주죽준줄줅줆줌줍줏중쥬쥰쥴쥼즁즈즉즌즐즘즙즛증지직진짇질짊짐집짓징짖짙짚재잭잰잴잼잽잿쟁쟀쟤쫳쫚쭥쭧쭨쭩쭪쭫쭬쭭쭮쭯쭰쭱쭲쭳쭴쭵쭶쭷쭺쭻쭼쭽쭾쭿쭦쫵쫷쫸쫹쫺쫻쫼쫽쫾쫿쬀쬁쬂쬃쬄쬅쬆쬇쬉쬊쬋쬌쬍쬎쬏쫶쮁쮃쮄쮅쮆쮇쮈쮉쮊쮋쮌쮍쮎쮏쮐쮑쮒쮓쮕쮖쮗쮘쮙쮚쮛쮂쮔앇앋앏앐쟨쟬제젝젠젤젬젭젯젱젶젰졔졘졜죄죈죌죔죕죗죙죘쥐쥑쥔쥗쥘쥠쥡쥣즤좌좍좐좔좝좟좡줘줬좨좽좼줴줸줼쥄쥅쥈차착찬찮찰참찹찻창찾찼챠챤챦챨챰챱챵처척천철첨첩첫청첬쳐쳑쳔쳘쳤초촉촌촐촘촙촛총쵸쵼춀춈앑앖앚앛앜앆앿얁얂얅얆얈얉얊얋얎얒얓얔얖앾얷얺얿엀엁엂엃엋엍얶엯엱엲엵엸엹엺엻옂옃옄옧옩옪옫옯옱옲옶옺옼옽옿옦옸욗욙욚욛욝욞욟욠욡욢욣욦욪욫욬욭욮욯욖욨욳욵욶욷욻욼욽욾추축춘춛출춤춥춧충츄츈츌츔츙츠측츤츨츰츱츳층치칙친칟칠칡침칩칫칭채책챈챌챔챕챗챙챘챼체첵첸첼쳄쳅쳇쳉쳈쳬쳰촁최쵠쵤쵬쵭쵯쵱취췬췰췸췹췻췽츼촤촥촨촬촹춰췃췄쵀쵄췌췐카칵칸칼캄캅캇캉캎캈캬캭캰욿웂웆웇웈웉웊웋욲웄윣윥윦윧윩윪윫윬윭윮윯윲윶윸윹윺윻윢윴윿읁읂읆읇읈읉읋읎윾읐읷읹읺읻읿잀잁잂잆잋잌잍잏읶앣앥앦앧앩앪앫앬앭앮앯앲앶앷앸앹앺앻앢얙얛얝얞얟얡얢얣얤얥얦캼캽컁커컥컨컫컬컴컵컷컹컽컾컸켜켠켤켬켭켯켱켰코콕콘콜콤콥콧콩쿄쿠쿡쿤쿨쿰쿱쿳쿵큐큔큘큠크큭큰클큼큽킁키킥킨킬킴킵킷킹킾캐캑캔캘캠캡캣캥캪캤컈케켁켄켈켐켑켓켕켸쾨쾰퀴퀵퀸퀼큄큅큇큉킈콰콱콴얧얨얪얫얭얮얯얰얱얲얳얚얬엓엕엖엗엙엚엛엜엝엞엟엢엦엧엨엩엪엫엒옉옋옍옎옏옑옒옓옔옕옖옗옚옞옟옠옡옢옣옊왻왽왾왿욁욂욃욄욅욆욇욊욎욏욐욑욒욓왺욌윇윉윊윋윍윎윏윐윑윒윓윖콸쾀쾅쿼퀀퀄퀑쾌쾐쾔쾡퀘퀙퀠퀭타탁탄탈탉탐탑탓탕탚탔탸탼턍터턱턴털턺텀텁텃텅텄텨텬텼토톡톤톨톰톱톳통톺툐투툭툰툴툼툽툿퉁튜튠튤튬튱트특튼튿틀틂틈틉틋틍티틱틴틸팀팁팃팅태택탠탤탬탭탯탱탶탰턔윚윛윜윝윞윟윆윘읙읛읝읞읟읡읢읣읤읥읦읧읩읪읭읮읯읰읱읲읳읚읬왃왅왆왉왊왋왌왍왎왏왒왖왗왘왙왚왛왂웏웑웒웓웕웖웗웘웙웚웛웞웢웣웤웥웦웧웎왟왡왢왣왤왥왦왧왨왩왪왫왭왮왲왳테텍텐텔템텝텟텡텦톄톈퇴퇸툇툉튀튁튄튈튐튑튕틔틘틜틤틥톼퇀퉈퉜퇘퉤퉨퉸파팍판팔팖팜팝팟팡팥팎팠퍄퍅퍼퍽펀펄펌펍펏펑펐펴펵편펼폄폅폇평폈포폭폰폴폼폽폿퐁표푠푤푭푯푸푹푼푿풀풂품풉풋풍퓨퓬퓰퓸왴왵왶왷왞왰웫웭웮웯웱웲웳웴웵웶웷웺웾웿윀윂윃웪웼???????????????????????????????????????????????????????????퓻퓽프픈플픔픕픗픙피픽핀필핌핍핏핑패팩팬팰팸팹팻팽팼퍠페펙펜펠펨펩펫펭펲폐폔폘폡폣푀푄퓌퓐퓔퓜퓟픠픤퐈퐝풔풩하학한할핥함합핫항햐향허헉헌헐헒헕헗험헙헛헝혀혁현혈혐협혓형혔호혹혼혿홀홅홈홉홋????????????????????????????????????????????????????????????????????????????????????홍홑효횬횰횹횻후훅훈훌훑훔훕훗훙휴휵휸휼흄흇흉흐흑흔흖흗흘흙흝흠흡흣흥흩히힉힌힐힘힙힛힝해핵핸핼햄햅햇행했햬헤헥헨헬헴헵헷헹헸혜혠혤혭회획횐횔횝횟횡휘휙휜휠휨휩휫휭희흰흴흼흽힁화확환활홤홥????????????????????????????????????????????????????????????????????????????????????홧황훠훡훤훨훰훵홰홱홴횃횅횄훼훽휀휄휑까깍깐깓깔깖깜깝깟깡깥깎깠꺄꺅꺈꺌꺼꺽껀껄껌껍껏껑꺾껐껴껸껼꼇꼍꼈꼬꼭꼰꼱꼲꼴꼼꼽꼿꽁꽂꽃꾜꾸꾹꾼꾿꿀꿇꿈꿉꿋꿍꿎뀨끄끅끈끊끌끎끓끔끕끗끙끝끼끽낀낄낌????????????????????????????????????????????????????????????????????????????????????낍낏낑깨깩깬깰깸깹깻깽깼꺠께껙껜껠껨껩껫껭껬꼐꾀꾁꾄꾈꾐꾑꾕뀌뀐뀔뀜뀝뀡꽈꽉꽌꽐꽛꽝꽜꿔꿘꿜꿥꿧꿩꿨꽤꽥꽨꽬꽹꿰꿱꿴꿸뀀뀁뀅뀄따딱딴딸딿땀땁땃땅땋딲땄땨땰떠떡떤떨떪떫떰떱떳떵떻떴뗘뗬또똑똔????????????????????????????????????????????????????????????????????????????????????똘똠똡똣똥뚀뚜뚝뚠뚤뚫뚬뚭뚱뜌뜨뜩뜬뜯뜰뜸뜹뜻뜽띠띡띤띨띰띱띳띵때땍땐땔땜땝땟땡땠떼떽뗀뗄뗌뗍뗏뗑뗐뙤뙨뛰뛴뛸뜀뜁뜅띄띅띈띌띔띕띙똬똰똴뚸뛌뙈뙉뛔빠빡빤빨빪빰빱빳빵빻빴뺘뺙뺜뺨뻐뻑뻔뻗뻘뻠????????????????????????????????????????????????????????????????????????????????????뻣뻥뻤뼈뼉뼘뼙뼛뼝뼜뽀뽁뽄뽈뽐뽑뽓뽕뾰뿅뿌뿍뿐뿔뿜뿝뿟뿡쀼쁑쁘쁜쁠쁨쁩삐삑삔삘삠삡삣삥빼빽뺀뺄뺌뺍뺏뺑뺐뺴뻬뻭뻰뻴뻼뼁뾔쀠쁴뽜뿨싸싹싻싼쌀쌈쌉쌋쌍쌓쌌쌰쌴쌸썅써썩썬썰썲썸썹썻썽썪썼쎠쏘쏙쏜丐个丱丶丿乢亅亙亟亠亳仂仆仞仭伜估佗佝佞佻佼侫俐俘俛俣俤俥俶俾倅倏倔倥倩偐偖偲傴僂働僮僵儂儔儕儖儚儻兔冂冉冏冓冖冢冫冰冱冲冴凅凛凧凩凪凭凵刋刔刧刳剄剏剞剳剴劬劭劵劼勠勦쏟쏠쏢쏨쏩쏫쏭쑈쑌쑐쑘쑝쑤쑥쑨쑬쑴쑵쑹쓔쓘쓧쓩쓰쓱쓴쓸쓺쓿씀씁씅씨씩씬씯씰씸씹씻씽씼쌔쌕쌘쌜쌤쌥쌧쌩쌨썌쎄쎅쎈쎌쎔쎕쎙쎼쏀쐬쐭쐰쐴쐼쐽쑀쒸쒼씌씐씔씜쏴쏵쏸쏼쐇쐉쐈쒀쒔쐐쐑쐤쒜쒠쒭짜짝짠짢짤勹匁匂匆匚匝匱匳匸卅卮卸卻厂厖厩厮厶叟叨叮叺吁吋听吭吮吽呀呆呎呟呰呶呷咄咋咢咥咼咾哂哇哘哢哦哩哽唏唔唳唸唹啀啌啗啜啝啻啾喃喋喞喟喨嗄嗷嗹嘖嘛嘸噂噌噎噛噤噪噬噸噺嚀嚇嚊嚏짧짬짭짯짱짰쨔쨘쨤쨩쩌쩍쩐쩔쩗쩜쩝쩟쩡쩠쪄쪘쪼쪽쫀쫄쫌쫍쫏쫑쫒쫓쫗쬬쬰쬼쭁쭈쭉쭌쭐쭘쭙쭛쭝쮸쯀쯔쯕쯘쯜쯤쯧쯩쯪찌찍찐찔찜찝찟찡찢찦찧째짹짼쨀쨈쨉쨋쨍쨌쨰쨴쩨쩩쩬쩰쩸쩹쩽쪠쬐쬔쬘쬠쬡쬤쮜쯰쯴嚔嚠嚶囀囁囂囃囈囎囮囿圉圜圦圷圸坩坿垉垤垪垰垳埆埒埓埔埖埣堋堙堝塀塒塙塰墫墸墹壗壜壥壼夂夊夐夘夥夬夸奩妁妛妝妣妲姥姶娉娵婀婪婬媼媽媾嫋嫐嫖嫗嫣嫺嫻嬬嬰嬲嬶嬾孅孛孥孳宀它쫘쫙쫜쫠쫭쫬쭤쭹쭸쫴쬈쮀아악안앉않알앍앎앒앓암압앗앙앝앞앟았야약얀얃얄얇얌얍얏양얕얗얐어억언얹얻얼얽얾엄업없엇엉엊엌엎엏었여역연엳열엶엷염엽엾엿영옅옆옇엮였오옥온올옭옮옰옳옴옵옷옹옻옾요욕宾寉寥寰尠尢屁屐屓屡屮屶岌岔岨岶岻岼峅峇峪峭峺崋崘崚崛崟崢嵎嵒嵳嵶嶂嶐嶬嶮嶷巉巓巵帚帷幃幎幔幗幵幺广庖廁廝廡廨廩廱廴廸廼廾弉弋弭弯弸彁彑彝彡彳徂很徭徼忝忤忱忸怎怐怕怙怛욘욜욤욥욧용우욱운울욹욺움웁웃웅유육윤율윰윱윳융윷으윽은읃을읅읊음읍읏응읒읓읔읕읖읗이익인일읽읾잃임입잇잉잊잎있애액앤앨앰앱앳앵앴얘얜얠얩에엑엔엘엠엡엣엥엤예옌옐옘옙옛옝옜외왹왼욀욈욉욋욍怦怩怫怺恆恊恚恟恫恷悁悃悄悋悒悗悵惆惓惘惣惴惷愀愃愬慍慥慯慱慳慴慵憖懆懌懍懣懾戔戛戝戞戲戳扎扛扞扠扣扨找抂抃抓抔抖抻拊拑拵拶挂挈挌挧挨捍捗捜捩捫捶掀掎掏掟掣掫掬掴掵掾揃위윅윈윌윔윕윗윙의읜읠읨읫와왁완왇왈왐왑왓왕왔워웍원월웜웝웟웡웠왜왝왠왬왯왱웨웩웬웰웸웹웻웽윁???????????????????????????????????????????????揉插揣揩搆搓搦搨搴搶摎摧摶撕撩擂擠擣擯擱擶擽攅攜攤攴攵敕敘敝旃旄旆旙旛昃昜昵晒晢晰暃暸暼曁曚曩朏朷朸朿杁杙杠杢杣杤杪杲杼枅枌枠枡枦枩枴枹柁柆柊柎柘柞柢柤柧柮栂栃栞栩栫栲伽佳假價加可呵哥嘉嫁家暇架枷柯歌珂痂稼苛茄街袈訶跏軻迦駕刻却各咯恪慤殼珏脚覺角閣侃刊墾奸姦干幹懇揀杆柬桿澗癎看磵稈竿簡肝艮艱諫間乫喝曷渴碣竭葛蝎褐鞨勘坎堪嵌感憾戡撼敢柑橄減甘疳監瞰紺邯鑑鑒栴框桍桝档桴桷桾梃梍梛梠梺梼棆棊棔棡棣棯椈椋椌椏椙椚椛椡椢椣椥椦椨椪椴椶椹楜楝楪楴楾榁榊榎榑榔榠榱榲榾榿槇槊槎槓槙槝槞槧槫槭槲槹樅樋樌樒樔樛樢樫樮樶橇橦橲橸橿檐檠檪檬檮龕匣岬甲胛鉀閘剛堈姜岡崗康强彊慷江畺疆糠絳綱羌腔舡薑襁講鋼降鱇倨去居巨拒据據渠擧炬祛距踞遽醵鉅鋸巪乾件健巾建愆楗腱虔蹇鍵騫乞傑杰桀儉劍劒檢瞼鈐黔劫怯迲擊格檄激膈覡隔堅牽犬甄絹繭肩見譴遣鵑抉檸櫁櫑櫞櫟櫨櫪櫺欅欟欷欸欹歃歉歔歙歹殀殍殕殤殪殫殳毟毯毳气氛氤汢汳沍沱沺泅泙泝泱洒洟洫洳浤涸淌淒淕淤淦淬渕渝渮湎溂溏溘溲溷溽滕滬滷漉漓漾潦潯潴潸澀澂澆澡澪濆濔濘濛濮濺瀦決潔結缺訣兼慊箝謙鉗鎌京俓倞傾儆勁勍卿坰境庚徑慶憬擎敬景暻更梗涇炅烱璟璥瓊痙硬磬竟競絅經耕耿脛莖警輕逕鏡頃頸驚鯨古叩告呱固姑孤尻庫拷攷故敲暠枯槁沽痼皐睾稿羔考股膏苦苽菰藁蠱袴詁誥賈辜錮雇顧瀰瀲灯炮焜煕煢熈熕熨燗燠燬燵燹爍爨爿牋牴牾犂犇犒犖犹狃狆狒狛狠狢狷猗猯猴獎獏玻珈珱珸琲瑣瑰瑳瓧瓩瓰瓱瓲瓸甃甅甌甍甎甓甜甼畉畋畚畤畩畭畷疔疚疣痃痊痞痳痾痿瘁瘉瘋瘰瘴癆癈癘高鼓哭斛曲梏穀谷鵠困坤崑昆梱棍滾琨袞鯤汨骨供公共功孔工恐恭拱控攻珙空蚣貢鞏交僑咬喬嬌嶠巧攪敎校橋狡皎矯絞翹膠蕎蛟較轎郊餃驕鮫丘久九仇俱具勾區口句咎嘔坵垢寇嶇廐懼拘救晷枸柩構歐毆毬求溝灸狗玖癜癢癧癨癪癶皀皋皖皚皰皴皸皹盍盥盪盻眇眛眤眥眦睇睚睥睨瞎瞠瞶瞹瞽矇矍矚矧矼砌砠硲硴碆碓碕碯碵碾磆磑磔磚磴磽礇礑礒礙礦祓祕祟祢禀禊禰禺秡秣秬稘穃窖窶窿竃竈竍竏竓竕竚竡竢竦球瞿矩究絿耉臼舅舊苟衢謳購軀逑邱鉤銶駒驅鳩鷗龜國局菊鞠鞫麴君窘群裙軍郡堀屈掘窟宮弓穹窮芎躬叫圭奎揆槻珪硅畦窺竅糾葵規赳逵閨勻均畇筠菌鈞橘克剋劇戟棘極隙僅劤勤懃斤根槿瑾筋芹菫覲謹近饉今妗擒昑竰笂笄笆笈笊笘笥笨笳筅筈筥筧筰筱筴箆箍箒箘箙箜箟篋篌篏篝篥篦篳篶篷簀簍簑簓簔簗簟簣簷簸籀籏籐籔籘籟籥籵籾粁粂粍粐粡粢粤粨粫粭粽糀糂糅糒糘糜糢糯糲糴糶糺紕紜紲紿絋絎絏絖絛檎琴禁禽芩衾衿襟金錦伋及急扱汲級給亘兢矜肯企伎其冀嗜器圻基埼夔奇妓寄岐崎己幾忌技旗旣朞期杞棋棄機欺氣汽沂淇玘琦琪璂璣畸畿碁磯祁祇祈祺箕紀綺羈耆耭肌記譏豈起錡錤飢饑騎騏驥麒喫緊佶吉拮桔介价個絣絽綉綛綟綣綫綮綯綰緕緜緤緲縅縋縒縢縲縵縹縺縻繖繙繚繝繦繧繻繽繿纃纈纐纔罅罍罎网罘罟罠罧罨罩羂羃羆羇羝羣羯羶翦翳翻耄耋耒耙耜耡耨聒聢聶聹肓肘肚肬肭胖胙胝胯胼腆腓腟腮腴膂凱塏愷愾慨改槪漑疥皆盖箇芥蓋鎧開喀客坑粳羹偈揭係啓堺契季屆憩悸戒桂械棨溪界癸磎稽系繫繼計誡谿階鷄乖傀塊壞怪愧拐槐蒯魁宏紘肱轟歸貴鬼寡戈果瓜科菓誇課跨過鍋顆廓槨藿郭串冠官寬慣棺款灌琯瓘管罐菅膃膓膕膤膩膰膸臉臑臙臚臠舁舂舐舘舮舳舸艘艚艝艟艢艨艪艫艷芫苅苓苙苜苣苫苳苴苹苺苻茆茖茘茜茣荅荐荵荼莅莇莓莚莟莠莨莵菎菘菟菠菷菻萇萋萓萠萢萪萵萼葆葎葩葭葮葷葹蒂蒄蒟蒹蓁蓊觀貫關館刮恝括适侊光匡壙廣曠洸炚狂珖筐胱鑛倦券勸卷圈拳捲權淃眷厥獗蕨蹶闕卦掛罫几机櫃潰詭軌饋儺娜懦拏拿那諾暖煖難捏捺涅南娚枏楠湳男納衲囊女年秊念恬捻寧寗獰努奴弩怒瑙駑濃膿農尿鬧嫩訥杻紐能尼蓐蓖蓙蓿蔀蔆蔕蔟蔦蕀蕈蕊蕋蕕蕗蕘蕚蕷蕾薀薈薊薐薗薙薤薹藐藹藾蘋蘢蘰虍虻蚋蚪蚫蚯蚰蚶蛄蛆蛉蛞蛩蛬蛯蛸蛹蛻蜆蜉蜊蜍蜑蜒蜥蜩蜴蜷蜻蜿蝋蝌蝓蝙蝠蝣蝪蝮螫螯螻螽蟀蟆蟇蟋蟐蟒蟶蟷蠍泥匿溺乃內奈柰耐惱腦多茶丹亶但單團壇彖斷旦檀段湍短端簞緞蛋袒鄲鍛撻澾橽獺疸達啖坍憺擔曇淡湛潭澹痰聃膽蕁覃談譚錟沓畓答踏遝唐堂塘幢戇撞棠當糖螳黨德悳倒兜刀到圖堵塗導屠島嶋度徒悼挑掉搗桃棹櫂淘蠎蠑蠕蠖蠡蠧蠹衂衄衞衵衽袙袢袤袮袰袱袵袷袿裃裄裘裲裹裼裾褂褄褊褌褝褞褫襃襌襖襞襠襦襭襯襴襷襾覈覗覘覦覬覯覿觚觜觝訐詆詈詑詒詫詬詼誂誄誑誚諚諞諠諢諤諳謇謦譛譟譫讌讎讙谺豎渡滔濤燾盜睹禱稻萄覩賭跳蹈逃途道都鍍陶韜毒瀆牘犢獨督禿篤纛讀墩惇敦旽暾沌焞燉獤豚頓乭堗突仝冬凍動同憧東桐棟洞潼疼瞳童胴董銅斗杜枓痘竇荳豆逗頭屯臀芚遁遯鈍得嶝橙燈登等藤謄鄧騰代垈坮大對岱帶待豐豢豬豸豼貅貉貍貎貔貘貮貲賺贋贏贐贔贛赧赱趁跂跖跚跟跪跫跼跿踈踉踝踟蹌蹐蹕蹣蹲蹼躄躅躋躑躓躔躙躡躱躾軅軈軛軼輊轂轆轌轗轜轡轣轤辟辮辷辻込辿迄迢迥迴迸迺逎逖逧逶遉遏遒遖遘戴擡玳臺袋貸隊黛喇懶癩羅蘿螺裸邏樂洛烙珞絡落酪駱亂卵欄欒瀾爛蘭鸞剌辣嵐擥攬欖濫籃纜藍襤覽拉臘蠟鑞娘廊朗浪狼琅瑯螂郞掠略亮倆兩凉梁樑粮粱糧良諒輛量侶儷勵厲呂廬慮戾旅櫚濾礪藜蠣閭驢驪麗黎力曆歷遨遶郛郢郤鄰酖酘酣酥酲酳醂醐醢醪醺釁釛釟釡釦釶釼釿鈔鈕鈩鈷鉈鉋鉐鉚鉾銚銛鋩鋲鋺錆錏錙錣錵錺錻鍄鍖鍜鍠鍬鎗鎹鏈鏐鏖鏗鏘鏝鏥鏨鐃鐇鐐鐓鐔鐙鐚鐡鐶鐺鑁鑓鑠鑢鑪鑰鑵鑷鑼鑾钁閂閊瀝礫靂憐戀攣漣煉璉練聯蓮輦連鍊冽列劣洌烈裂廉斂殮濂簾獵令伶囹岺嶺怜玲笭羚翎聆逞鈴零靈領齡勞撈擄櫓潞瀘爐盧老蘆虜路輅露魯鷺鹵碌祿綠菉錄鹿麓論壟弄朧瀧瓏籠聾了僚寮廖料燎療瞭聊蓼遼龍壘婁屢樓淚漏閖閠閧閹閾闃闌闍闥阨阯陏陦陬陲隈隗隰隲隴隶隹隼雫霄霈霍霏霤霪霸霾靆靉靠靤靦靨靫靹靼鞁鞄鞅鞆鞐鞘鞜鞣鞦鞳鞴韃韭韮韲頏頡頤頷顋顏顰顱顳顴颪颶飩飫餒餔餝餡餤餬餮餽餾饂饐饕馗馘瘻累縷蔞褸鏤陋劉旒柳榴流溜瀏琉瑠留瘤硫謬類六戮陸侖倫崙淪綸輪律慄栗隆勒肋轢凜凌楞稜綾菱陵俚利厘吏唎履悧李梨浬犁狸理璃痢籬罹羸莉裏裡里釐離鯉吝潾燐璘藺躪隣鱗麟林淋琳臨霖砬立笠粒來崍徠萊冷例澧馼駘駛駮駲駸駻騅騨騾驂驤驫骭骰骼髀髏髑髞髟髢髣髦髫髭髱髴髷髻鬆鬘鬟鬢鬣鬥鬨鬩鬮鬯鬲鬻魍魎魑魘魴鮃鮒鮓鮖鮗鮠鮨鮪鮭鮴鮹鯀鯆鯊鯏鯑鯒鯔鯛鯡鯢鯣鯰鯱鯲鯵鰄鰆鰈鰉鰊鰌鰓鰔鰛鰡鰤禮醴儡瀨牢磊賂賚賴雷摩瑪痲碼磨馬魔麻寞幕漠膜莫邈万卍娩巒彎慢挽晩曼滿漫灣瞞萬蔓蠻謾輓饅鰻唜抹末沫茉襪靺亡妄忘忙望網罔芒茫莽輞邙冪覓免冕勉棉沔眄眠綿緬面麵滅蔑冥名命明暝椧溟皿瞑茗蓂螟酩銘鳴侮鰭鰮鰯鰰鰹鰺鰾鱆鱈鱒鱚鱧鱶鱸鳰鴃鴆鴇鴈鴒鴕鴟鴣鴪鴫鴾鴿鵁鵄鵆鵈鵐鵙鵜鵞鵤鵯鵺鶇鶉鶚鶤鶫鶲鶸鶺鶻鷁鷂鷆鷏鷓鷙鷦鷭鷯鷽鸛鹸麁麈麋麌麑麕麩麪麭麸麼麿黌黏黐黝黠黥黯黶黷黹黻黼黽冒募姆帽慕摸摹暮某模母毛牟牡瑁眸矛耗芼茅謀謨貌木沐牧目睦穆鶩歿沒夢朦蒙卯墓妙廟描昴杳渺猫畝竗苗錨務巫憮懋戊拇撫无楙武毋無珷繆舞茂蕪誣貿霧鵡墨默們刎吻問文汶紊紋聞蚊門雯勿物味媚尾嵋彌微未梶楣鼕鼬鼾齏齔齠齣齦齲齶龠???????????????膑卐?????????????????????????????????????????????????????渼湄眉米美薇謎迷靡黴岷悶愍憫敏旻旼民泯玟珉緡閔密蜜謐埋妹媒寐昧枚梅每沕煤罵買賣邁魅脈貊陌驀麥孟氓猛盟盲萌袂剝博拍搏撲朴樸泊珀璞箔粕縛膊舶薄迫雹駁伴半反叛拌搬攀斑槃泮潘班畔瘢盤盼磐磻礬絆般蟠????????????????????????????????????????????????????????????????????????????????????返頒飯勃拔撥渤潑發跋醱鉢髮魃倣傍坊妨尨幇彷房放方旁昉枋榜滂磅紡肪膀舫芳蒡蚌訪謗邦防龐幡樊煩燔番繁蕃藩飜伐筏罰閥凡帆梵氾汎泛犯範范法琺僻劈壁擘檗璧癖碧蘗闢霹卞弁徧變辨辯邊別瞥鱉鼈丙倂兵屛幷昞????????????????????????????????????????????????????????????????????????????????????昺柄棅炳甁病秉竝輧餠騈保報堡寶普步湺潽珤甫菩補褓譜輔伏僕匐卜宓復服洑福腹茯蔔複覆輹馥鰒本乶丰俸奉封峯峰捧棒烽熢琫縫蓬蜂逢鋒鳳付俯傅剖副否咐埠夫婦孚孵富府扶敷斧浮溥父符簿缶腐腑膚艀芙莩訃負賦????????????????????????????????????????????????????????????????????????????????????賻赴趺部釜阜附駙鳧北分吩噴墳奔奮忿憤扮昐汾焚盆粉糞紛芬賁雰不佛弗彿拂崩朋棚硼繃鵬丕備匕匪卑妃婢庇悲憊扉批斐枇榧比毖毗毘沸泌琵痺砒碑秕秘粃緋翡肥脾臂菲蜚裨誹譬費鄙非飛鼻嚬嬪彬斌檳殯浜濱瀕牝玭◑⊘✉☛☞✌✍✏✎✐✓✔⊡⎔⊙??????????????⚓☼◉?????????✪✯✬✫✮✭✰✩???貧賓贇頻氷憑聘馮騁倍俳培徘拜排杯湃焙盃背胚裴裵褙賠輩配陪伯佰帛柏栢白百魄乍事些仕伺似使俟史司唆嗣四士奢娑寫寺射巳師徙思捨斜斯柶査梭死沙泗渣瀉獅砂社祀祠私篩紗絲肆舍莎蓑蛇裟詞詐謝賜赦辭邪飼駟麝削朔傘刪山散汕珊産疝算蒜酸霰乷撒殺煞薩三杉森滲芟蔘衫揷澁霎鈒鍤颯上傷像償商喪嘗孀尙峠常床庠廂想桑橡湘爽牀狀相祥箱翔裳觴詳象賞霜墅壻嶼序庶徐恕抒捿敍暑曙書栖棲犀瑞筮絮緖署胥舒薯西誓逝鋤黍鼠???????????????????????????????????????????????????????????夕奭席惜昔晳析汐淅潟石碩蓆釋錫仙僊先善嬋宣扇敾旋渲煽琁瑄璇璿癬禪線繕羨腺膳船蘚蟬詵跣選銑鐥饍鮮卨屑楔泄洩渫舌薛褻設說雪齧剡暹殲纖蟾贍閃陝攝涉燮城姓宬性惺成星晟猩珹盛省筬聖聲腥誠醒召嘯塑宵小???????????????????????????????????????少巢所掃搔昭梳沼消溯瀟炤燒甦疏疎瘙笑篠簫素紹蔬蕭蘇訴逍遡邵銷韶騷俗屬束涑粟續謖贖速孫巽損蓀遜飡率宋悚松淞訟誦送頌修受售嗽囚垂壽嫂守岫峀帥愁戍手授搜收數樹殊水洙漱燧狩獸琇璲瘦睡秀穗竪粹綏綬繡➔➘➙➚➛➜➝➟➠➢➣➤➥➦➧➨➩➪➫➬➭➮➯➱➲➳➴➵➶➷➸➹➺➻➾➼➽??????????????⟷⇌⥫⥬⇐⟹????????????????羞脩茱蒐蓚藪袖誰讐輸遂邃酬銖銹隋隧隨雖需須首髓鬚叔塾夙孰宿淑潚熟琡璹肅菽巡徇循恂旬栒楯橓殉洵淳珣盾瞬筍純脣舜荀蓴蕣詢諄醇錞順馴戌術述鉥崇崧嵩瑟膝蝨濕拾習褶襲丞乘僧勝升承昇繩蠅陞侍匙嘶始媤尸ᵃᵇᶜᵈᵉᶠᵍᵏᵐⁿᵒᵖᵗᵘᵛₐₑᵢⱼₒᵣᵤᵥₓ????????????????????屎屍市弑恃施是時杮柴猜矢示翅蒔蓍視試詩諡豕豺埴寔式息拭植殖湜熄篒識軾食飾蝕伸侁信呻娠宸愼新晨燼申神紳腎臣莘薪藎蜃訊身辛迅失室實悉審尋心愖沁深瀋甚芯諶什十僿璽賽嗇塞穡索色牲生甥笙世勢歲洗稅笹ᵅᵝᵞᵟᵋᶿᶹᵠᵡ??ᵦᵧᵨᵩᵪ??⁺⁻???????????₊₋???????????細貰衰釗刷灑碎鎖仔刺咨姉姿子字孜恣慈滋炙煮玆瓷疵磁紫者自茨蔗藉諮資赭雌作勺嚼斫昨灼炸爵綽芍酌雀鵲孱棧殘潺盞岑暫潛箴簪蠶雜丈仗匠場墻壯奬將帳庄張掌暲杖樟檣欌漿牆獐璋章粧腸臟臧莊葬蔣薔藏裝贓醬㉛㉜㉝㉞㉟㊱㊲㊳㊴㊵㊶㊷㊸㊹㊺㊻㊼㊽㊾㊿????????????????????????長障佇低儲咀姐底抵杵楮樗沮渚狙猪疽箸紵苧菹著藷詛貯躇這邸雎齟勣吊嫡寂摘敵滴狄的磧積笛籍績翟荻謫賊赤跡蹟迪迹適鏑佃佺傳全典前剪塡塼奠專展廛悛戰栓殿氈澱煎琠田甸畑癲筌箋箭篆纏詮輾轉鈿銓錢鐫電顚????????????????????????︰????????????????????????????顫餞切截折浙癤竊節絶占岾店拈漸点粘霑鮎點接摺椄蝶丁井亭停偵呈姃定幀庭廷征情挺政整旌晶晸柾楨檉正汀淀淨渟湞瀞炡玎珽町睛碇禎程穽精綎艇訂諪貞鄭酊釘鉦鋌錠霆靖靜頂鼎俎兆凋助嘲弔彫措操早晁曺曹朝條∅⊗〓?♧♡♤♢◯⦾??????????????????????????????????K₩₤¥??????????????????棗槽漕潮照燥爪璪眺祖祚租稠窕粗糟組繰肇藻蚤詔調趙躁造遭釣阻雕鳥族簇足鏃存尊卒拙猝倧宗從悰慫棕淙琮種終綜縱腫踪踵蹤鍾鐘主住侏做姝胄呪周奏宙州廚晝朱柱株注洲湊澍炷珠疇籌紂紬綢舟蛛註誅走躊輳週酎ヽヾゝゞ々〆〇ー????????????????ㅥㅭㅱㅲㅳㅴㅵㅶㅷㅸㅹㅺㅻㅽㅾㆀㆄㆅㆇㆈㆉㆊㆋㆌᆞㆎ????????????????????????????????酒鑄駐竹粥俊儁准埈寯峻晙樽浚準濬焌㻐畯竣蠢逡遵雋駿茁中仲衆重卽櫛楫汁葺增憎拯曾烝甑症繒蒸證贈之只咫地址志持指摯支旨智枝枳止池沚漬痣知砥祉祗紙肢脂至芝芷蜘誌贄趾遲直稙稷織職唇嗔塵振搢晉晋桭榛????????????????????????????????????????????????????????????????????????????????????殄津溱珍瑨璡畛疹盡眞瞋秦縉縝臻蔯袗診賑軫辰進鎭陣陳震侄叱姪嫉帙桎瓆疾秩窒膣蛭質跌迭朕執潗緝輯鏶集徵懲澄再哉在宰才材栽梓渽滓災縡裁財載齋齎爭箏諍錚制劑啼堤帝弟悌提梯濟祭第臍薺製諸蹄醍除際霽題齊罪佐坐左座挫且借叉嗟嵯差次此磋箚蹉車遮釵捉搾着窄錯鑿齪撰澯燦璨瓚竄簒纂粲纘讚贊鑽餐饌刹察擦札紮僭參塹嶄慘慙懺斬站讒譖讖倉倡創唱娼廠彰愴敞昌昶暢槍滄漲猖瘡窓脹艙菖蒼凄妻悽處倜剔尺慽戚拓擲斥滌瘠脊蹠陟隻仟千喘天川擅泉淺玔穿舛薦賤踐遷釧闡阡韆凸哲喆徹撤澈綴輟轍鐵僉尖沾添甛瞻簽籤詹諂堞妾帖捷牒疊睫諜貼輒廳晴淸聽菁請靑鯖初剿哨憔抄招梢椒楚樵炒焦硝礁礎秒稍肖艸苕草蕉貂超酢醋醮促嗾囑燭矗蜀觸寸忖村邨叢塚寵悤憁摠總聰蔥銃墜抽推椎楸樞湫皺秋芻萩諏趨追鄒酋醜錐錘鎚雛騶鰍丑畜祝竺筑築縮蓄蹙蹴軸逐春椿瑃出朮黜充忠沖蟲衝衷仄側厠惻測闖層侈値嗤峙幟恥梔治淄熾痔痴癡稚穉緇緻置致蚩輜雉馳齒則勅飭親七柒漆侵寢斟枕沈浸琛砧針鍼蟄秤稱債埰寀寨彩採砦綵菜蔡采冊柵策責体剃替涕滯締諦逮遞體催崔最取吹嘴娶就炊翠聚脆膵臭趣醉驟鷲撮悴贅萃快他侘咤唾墮妥惰打拖朶楕橢舵陀駝倬卓啄坼托擢晫柝濁濯琢琸託鐸呑嘆坦彈憚歎灘炭綻誕奪脫探眈耽貪塔搭榻宕帑湯蕩攄兎吐土討慟桶痛筒筩統通偸套妬投透鬪慝特兌台太怠態殆汰泰笞胎苔跆邰颱馱宅擇澤撑堆槌腿褪退頹坡婆巴把播擺杷波派爬琶破罷芭跛陂頗判坂板版瓣販辦鈑阪八叭捌愎便偏扁片篇編翩遍鞭騙貶坪平枰萍評佈包匍匏咆哺圃布怖抛抱捕暴曝泡浦疱砲胞脯苞葡蒲袍褒逋鋪飽鮑幅瀑爆輻俵剽彪慓杓標漂瓢票表豹飄飇驃品稟楓諷豊風彼披疲皮被避匹弼必珌畢疋筆苾馝乏逼佩唄悖敗沛浿牌狽稗貝覇彭澎烹膨吠嬖幣廢弊斃肺蔽閉陛下何厦夏廈昰河瑕荷蝦賀遐霞鰕壑學瘧虐謔鶴寒恨悍旱汗漢澣瀚罕翰閒閑限韓割轄函含咸啣喊晗檻涵緘艦銜陷鹹合哈盒蛤閤闔亢伉姮嫦巷恒抗杭桁沆港缸肛航項享向嚮珦鄕響餉饗香噓墟虛許憲櫶獻軒歇險驗奕爀赫革俔峴弦懸晛泫炫玹現玄眩睍絃絢縣舷衒賢鉉顯孑穴血頁嫌俠協夾峽挾浹狹脅脇莢鋏陜頰亨兄刑型形泂滎瀅灐炯熒珩荊螢衡逈邢鎣馨乎互呼壕壺好岵弧戶扈昊晧毫浩淏湖滸澔濠濩灝狐琥瑚瓠皓祜糊縞胡芦葫蒿虎號蝴護豪鎬頀顥惑或酷婚昏混渾琿魂忽惚笏哄弘汞泓洪烘紅虹訌鴻哮嚆孝效斅曉梟涍淆爻肴酵驍侯候厚后吼喉嗅帿後朽煦珝逅鬍勛勳塤壎焄暈熏燻薰訓薨休携烋虧恤譎鷸兇凶匈洶胸黑昕欣炘痕吃屹紇訖欠欽歆吸恰洽翕興詰亥偕咳垓奚孩害懈楷海瀣蟹解該諧邂駭骸劾核倖幸杏荇行兮彗惠慧暳蕙蹊醯鞋匯回廻徊恢悔懷晦會檜淮澮灰獪繪膾茴蛔誨賄劃獲宖橫彙徽揮暉煇諱輝麾僖凞喜噫囍姬嬉希憙憘戱晞曦熙熹熺犧禧稀羲化和嬅樺火畵禍禾花華話譁貨靴擴攫確碻穫丸喚奐宦幻患換桓歡晥渙煥環紈還驩鰥活滑猾豁闊凰幌徨恍惶愰慌晃晄榥況湟滉潢煌璜皇篁簧荒蝗遑鐄隍黃喧暄煊萱卉喙毁雙氏亞俄兒啞娥峨我牙芽莪蛾衙訝阿雅餓鴉鵝堊岳嶽幄惡愕握渥鄂鍔顎鰐齷安岸按晏案眼雁鞍顔鮟斡謁軋閼唵岩巖庵暗癌菴闇壓押狎鴨仰央怏昻殃秧鴦也倻冶夜惹揶椰爺耶野弱約若葯蒻藥躍佯壤孃恙揚攘敭暘楊樣洋瀁煬痒瘍禳穰羊襄讓釀陽養圄御於漁瘀禦語馭魚齬億憶抑檍臆偃堰彦焉言諺孼櫱俺儼嚴奄掩淹嶪業予余如歟汝璵礖與艅茹輿轝餘亦域役易疫繹譯逆驛嚥堧姸娟宴延捐挻撚椽沇沿涎涓淵演烟然煙燕燃硏硯筵緣縯衍軟鉛鳶悅熱閱厭染炎焰琰稔艶苒閻髥鹽曄燁葉塋嶸影映暎楹榮永泳渶潁濚瀛瀯煐營瑛瑩瓔盈穎纓英詠迎鍈霙五伍俉傲午吾吳嗚塢墺奧娛寤悟懊敖旿晤梧汚澳烏熬獒筽蜈誤鰲鼇屋沃獄玉鈺溫瑥瘟穩縕蘊兀壅擁瓮甕癰翁邕雍饔僥凹堯夭妖姚嶢拗搖撓擾曜橈燿瑤窈窯繇繞耀腰蟯要謠遙邀饒慾欲浴縟褥辱俑傭冗勇埇墉容庸慂榕涌湧溶熔瑢用甬聳茸蓉踊鎔鏞于佑偶優又友右宇寓尤愚憂旴牛玗瑀盂祐禑禹紆羽芋藕虞迂遇郵釪隅雨雩勖彧旭昱栯煜稶郁頊云橒殞澐熉耘芸蕓運隕雲韻蔚鬱熊雄乳侑儒兪唯喩孺宥幼幽庾悠惟愈愉揄攸有柔柚楡楢油洧游濡猶猷瑜由癒維臾萸裕誘諛諭踰蹂遊逾遺酉釉鍮堉毓肉育允奫尹潤玧胤鈗閏聿戎瀜絨融垠恩慇殷誾銀隱乙吟淫蔭陰音飮揖泣邑凝應膺鷹二以伊夷姨已弛彛怡爾珥異痍移而耳肄苡荑貳貽邇飴餌瀷益翊翌翼謚人仁刃印咽因姻寅引忍湮絪茵蚓認靭靷一佚佾壹日溢逸鎰馹任壬妊姙恁荏賃入卄仍剩孕芿刈厓哀埃崖愛曖涯碍縊艾隘靄厄扼掖液腋額櫻罌鶯鸚円乂倪叡曳汭濊猊睿穢芮藝蘂裔詣譽豫銳隷霓預喂外嵬巍歪猥畏位偉僞危圍委威尉慰暐渭爲瑋緯胃萎葦蔿蝟衛褘謂違韋魏依倚儀宜意懿擬椅毅疑矣義艤薏蟻衣誼議醫娃渦瓦窩窪臥蛙蝸訛婉完宛梡椀浣玩琓琬碗緩翫脘腕莞豌阮頑曰往旺枉汪王元原員圓園垣媛嫄寃怨愿援沅洹湲源爰猿瑗苑菀袁轅遠院願鴛月越鉞倭矮???????????????????????????????????????????????'.replace('〒?','〒'))
KPS9566ALTERNATIVES = {
    '\u02BC': '︐',
    '\uF000': '˙',
    '\uF001': '︐',
    '\uF002': '︒',
    '\uF003': '︑',
    '\uF004': 'ⸯ',
    '\uF005': '',
    '\uF006': '',
    '\uF007': '‚',
    '\uF008': '‛',
    '\uF009': '„',
    '\uF00A': '‟',
    '\uF00B': '﹇',
    '\uF00C': '﹈',
    '\uF00D': '',
    '\uF00E': '',
    '\uF00F': '',
    '\uF010': '',
    '\uF011': '⚐',
    '\uF012': '⚑',
    '\uF013': '',
    '\uF014': '',
    '\uF015': '',
    '\uF016': '',
    '\uF017': '',
    '\uF018': '',
    '\uF019': '½',
    '\uF01A': '⅓',
    '\uF01B': '⅔',
    '\uF01C': '¼',
    '\uF01D': '¾',
    '\uF01E': '㍷',
    '\uF01F': '㍸',
    '\uF020': '㍹',
    '\uF021': '㏞',
    '\uF022': '㏟',
    '\uF023': '㏿',
    '\uF024': '㋌',
    '\uF025': '㋍',
    '\uF026': '㋎',
    '\uF027': '',
    '\uF028': '',
    '\uF029': '☔',
    '\uF02A': '⚡',
    '\uF02B': '⚠',
    '\uF02C': '⬀',
    '\uF02D': '⬁',
    '\uF02E': '⬂',
    '\uF02F': '⬃',
    '\uF030': '⬄',
    '\uF031': '➡',
    '\uF032': '⬅',
    '\uF033': '⬆',
    '\uF034': '⬇',
    '\uF035': '⬈',
    '\uF036': '⬉',
    '\uF037': '⬊',
    '\uF038': '⬋',
    '\uF039': '⬌',
    '\uF03A': '⬍',
    '\uF03C': '',
    '\uF03D': '',
    '\uF03E': '☕',
    '\uF03F': '㉼',
    '\uF040': '㉽',
    '\uF041': '㈝',
    '\uF042': '㈞',
    '\uF043': '㋏',
    '\uF044': '㉐',
    '\uF045': '℻',
    '\uF046': '㍺',
    '\uF100': '˙',
    '\uF101': '︐',
    '\uF102': '︒',
    '\uF103': '︑',
    '\uF104': 'ⸯ',
    '\uF105': '',
    '\uF106': '',
    '\uF107': '‚',
    '\uF108': '‛',
    '\uF109': '„',
    '\uF10A': '‟',
    '\uF10B': '﹇',
    '\uF10C': '﹈',
    '\uF10D': '',
    '\uF10E': '',
    '\uF10F': '',
    '\uF110': '',
    '\uF111': '⚐',
    '\uF112': '⚑',
    '\uF113': '',
    '\uF114': '',
    '\uF115': '',
    '\uF116': '',
    '\uF117': '',
    '\uF118': '',
    '\uF119': '½',
    '\uF11A': '⅓',
    '\uF11B': '⅔',
    '\uF11C': '¼',
    '\uF11D': '¾',
    '\uF11E': '㍷',
    '\uF11F': '㍸',
    '\uF120': '',
    '\uF121': '',
    '\uF122': '',
    '\uF123': '㏿',
    '\uF124': '㋌',
    '\uF125': '㋍',
    '\uF126': '㋎',
    '\uF127': '',
    '\uF128': '',
    '\uF129': '☔',
    '\uF12A': '⚡',
    '\uF12B': '⚠',
    '\uF12C': '⬀',
    '\uF12D': '⬁',
    '\uF12E': '⬂',
    '\uF12F': '⬃',
    '\uF130': '⬄',
    '\uF131': '➡',
    '\uF132': '⬅',
    '\uF133': '⬆',
    '\uF134': '⬇',
    '\uF135': '⬈',
    '\uF136': '⬉',
    '\uF137': '⬊',
    '\uF138': '⬋',
    '\uF139': '⬌',
    '\uF13A': '⬍',
    '\uF13B': '',
    '\uF13C': '',
    '\uF13D': '',
    '\uF13E': '☕',
    '\uF13F': '㉼',
    '\uF140': '㉽',
    '\uF141': '㈝',
    '\uF142': '㈞',
    '\uF143': '㋏',
    '\uF144': '㉐',
    '\uF145': '℻',
    '\uF146': '㍺',
}