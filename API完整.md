# VU插件帮助文档

> 从 1.chm 转换而来

> 共 538 个页面

---

## 

免责声明
关于[无忧AI综合插件]使用的免责声明
欢迎使用[无忧AI综合插件]（以下简称“本插件”）。本插件由[无忧开发组]（以下简称“我们”）开发并提供。在您使用本插件之前，请仔细阅读以下免责声明。使用本插件即表示您已阅读、理解并同意接受以下条款和条件。
1.合法与合规使用：
	您承诺仅将本插件用于合法、合规的用途。我们明确禁止任何形式的非法活动，包括但不限于制作、使用或传播游戏脚本、作弊软件、自动化工具等，以规避游戏的安全机制或获取不正当利益。
2.个人责任与风险：
	您对本插件的使用承担全部责任。我们不对您使用本插件所产生的任何后果负责，包括但不限于因违反法律法规而导致的法律责任。
3.脚本与自动化：
	我们明确声明，本插件并非为制作游戏脚本或自动化工具而设计。任何使用本插件进行此类活动的行为均属用户个人行为，与我们无关。我们强烈建议您遵守游戏开发商的使用协议和法律法规，避免任何形式的作弊行为。
4.数据安全与隐私：
	虽然本插件具有内存读写功能，但您应自行负责保护数据安全，避免数据泄露或滥用。我们不对因您使用本插件而导致的任何数据安全或隐私泄露问题负责。
5.免责与限制：
	在任何情况下，我们均不对因使用本插件而产生的直接、间接、特殊或后果性损害负责，包括但不限于数据丢失、游戏账号封禁、法律纠纷等。我们保留在必要时采取法律措施的权利。
6.法律适用与争议解决：
	本免责声明受中国法律管辖。因本免责声明引起的或与本免责声明有关的任何争议，应提交至人民法院/公安部门进行解决。
7.修订与更新：
	我们保留随时修订和更新本免责声明的权利。任何修订和更新将在发布后即时生效。请定期检查本免责声明以获取最新信息。
8.终止使用：
	如您违反本免责声明的任何条款，我们有权立即终止您对本插件的使用权，并保留采取进一步法律行动的权利。
请在使用本插件前仔细阅读并理解以上免责声明。如您不同意以上条款，请立即停止使用本插件。
开发者信息：
无忧开发组
电子邮箱: voouer@qq.com
联系QQ: 7891634

---

## 

本插件设计初衷为解决计算机自动化任务,目前通过本插件可以轻松实现模拟人工进行操作,以执行电脑上一切行为,包括模拟人工刷视频、购物、绘图、写文案、编辑视频、玩游戏(非挂机脚本)、场景探索、家居监视等.

 

在本插件开发之初,我们借鉴了许多同类型优秀插件的功能,并且予以完善和优化,以实现更好的使用体验.

 

在此特别鸣谢 天使、dm、乐玩、图灵、figma、yolo、opencv、paddleocr等诸多优秀插件或模块的开发者,正因为有你或者你们开发出各种功能的视觉识别插件,才让我们拥有底气去实现这个通用计算机控制模块的插件.

 

对,我们称本插件为通用计算机控制模块,意味着您使用这一款插件,便可以完成绝大多数计算机任务.

 

目前阶段,本插件功能已经完全覆盖天使、dm、乐玩等插件基本所有功能.

Ocr识别 : 字库完全兼容dm插件字库,并且进行了性能优化,在相同图片上的识别和找字速度比之提升了5-20倍!

找图找色 : 使用与dm相同的四角同色图作为透明图,兼容所有图色功能,并且在对方插件的基础上进行了性能优化和准确度提升,同图片同窗口找一万次的情况下,速度提升大概3-5倍,CPU性能降低10-30％,准确率提升5％左右.另外增加super找图接口,可以对缩放和色差严重的图片也能实现精准查找.

内存汇编 : 接口: 1:1还原dm接口,支持CE和OD语法,并在对标插件的基础上,优化读写速度和容错处理,加入无痕写入,汇编语法兼容性提升.

后台键鼠 : 驱动级后台键盘鼠标,无需注入任何dll到目标窗口,即可实现键鼠模拟,拒绝侵害他人软件权益.

护盾功能 : 阻止非法读取调用本插件进程数据信息,拒绝我们的程序成为被侵害目标,本插件所有护盾也没有对其他程序进行侵害的功能,实际上也并不需要.

 

 

 

相对比前面提到的各种插件,本插件另新增了诸多强大功能,供君使用.
1. 加入了远程调用系统,支持软件与目标电脑隔离运行,也就是软件没有存在于其他电脑,但是也可以像在本地一样运行,对远程电脑进行图色查找,内存读写,键鼠操作!
2. 加入了AI人工智能模块,支持高精度图色识别,对象检测,图像处理和匹配.
3. 加入了json接口,支持任意编程语言解析和构建json数据.
4. 加入了智能导航算法,支持路径规划和A*寻路.
5. 加入了图像编辑功能,支持将彩色图转灰度图或者进行二值化,支持任意图片操作,含旋转,缩放,裁剪,抠图,调色等诸多功能.
6. 加入了进程隔离,类似于沙盘系统,可以让目标进程运行在一片虚拟环境中,避免其非法获取我们计算机中的数据(也可实现程序多开).
7. 其他算法接口,例如多边形计算,最近边/线/点计算等.
8. 加入了智能聊天系统,可以本地部署模型或者使用在线API接口,对接llm大模型实现类似chatgpt聊天系统,支持文件识别和本地函数调用(智能体必备).
9. 加入了音频处理,支持对任意音频的读入与写出,支持编辑裁剪音频,可以使用系统的音频设备进行录音和播放.
10. 加入了智能语音系统,支持将音频语音内容转为文本,也支持将文本生成为音频,支持多种音色生成与自定义音色的克隆音色.
11. 加入了跨机绘制功能,支持dx窗口绘制任意图形,支持远程调用:在我的电脑上调用绘制命令后在你的屏幕上显示我想要绘制的画面.

...

...

功能持续完善中.

---

## 

无忧AI综合插件(vu.dll)采用C/C++编写,性能强劲,功能强大,并导出为标准导出函数,适用于所有编程语言.

本插件主要功能如下(持续更新中):
1. 机器视觉部分,含后台窗口截图、文本识别、图片识别、像素查找、物体检测、实例分割、姿态识别 等多种高级视觉功能.
2. 键盘鼠标部分,支持前台和后台窗口的键盘鼠标操作,可以模拟实现真实人类对计算机键鼠的所有操作功能.
3. 内存读写部分,支持对本插件调用进程以及其他进程的内存读取和修改,支持特征码定位内存地址和对进程数据查找,支持无痕写入.(注:请遵守法律,勿侵犯他人软件)
4. 汇编和hook,本插件支持直接使用汇编语法转换为可执行指令在指定进程中运行.同时也可以对指定进程安装hook实现数据监视.(注:请遵守法律,勿侵犯他人软件)
5. 护盾系统,主要针对操作系统以及调用者进程/窗口执行保护,避免他人肆意侵害您的软件作品.
6. 窗口和进程,支持对任意窗口和进程的信息获取和操作,包括但不限于创建进程/窗口,窗口位置的获取和设置,窗口状态的获取和设置,进程模块的枚举和检测,进程句柄的查询和操作等等功能.
7. 远程调用,本插件的绝大多数功能如图色识别、键鼠操作、内存、汇编、hook、窗口/进程操作等,都可以远程进行调用,可以轻松实现对局域网或互联网远程计算机操作,让您编写的软件无需运行在目标电脑上,便可以像是在本地运行一样实现各种功能,由此可以极大概率避免他人对您软件的侵犯.(隔离运行)
8. AI赋能,支持多种人工智能,目前实现的有A*寻路,图像拼接,特征匹配,轮廓查找,物体检测,姿态识别,场景分割等,旨在利用本插件打造可以在电脑上完成所有任务的超强智能体.
9. 图像编辑,支持对图像进行任意操作,包括且不限于缩放、裁剪、拼接、模糊、锐化、色调、抠图等多种功能,利用本插件可以轻松打造一款类似于photoshop的图像编辑软件.
10. 音频处理,支持对音频的读入和写出,以及其他功能,包括重采样、格式转换、录音、播放等.
11. 智能聊天,可以使用本地部署或者在线api接口实现对接llm大模型,实现类似于chatgpt的智能聊天,支持文件传入与本地函数调用.
12. 智能语音,支持将音频语音转为文本内容,文本转音频语音,支持多种音色的语音合成同时也支持自定义音色的语音克隆.
13. 跨机绘制,支持本机或远程电脑绘制,创建dx窗口绘制任意内容,支持文本绘制、线条绘制、框体和图片绘制等,支持在我的电脑上调用绘制命令后在你的屏幕上显示我想要绘制的画面.
...
...
其他功能尚在实现和完善中...
倘若您有好的功能需求或建议,请不吝赐教,我们会尽最大努力去实现咱们的灵感和想法!
无忧开发组联系方式:QQ7891634电子邮箱voouer@qq.com

---

## 

函数简介:

将文件内容传递给模型,使其能够获知除了文字信息外的其他数据.支持本地文件和网络文件.

基础的chat类聊天大模型仅具有文本聊天的功能,无法获取图片、音频、视频、文档等其他格式的数据,使用本函数可以将这些数据传递给模型.

注意:仅支持在线大模型传递文件,而且传递文件给模型需要明确该模型是否具有处理当前文件的能力,假如你将视频文件传给了仅具有文字聊天能力的模型,那么不会起任何作用.

可以从你选择的接口平台了解目标模型都支持什么类型的文件输入.

函数原型:

int LlmAddFile(type, url)

参数定义:

type 整数型:文件类型,取值如下:

1:图片文件,本地文件格式必须为jpg,网络文件格式不受限制

2:音频文件,本地文件格式必须为mp3,网络文件格式不受限制

3:视频文件,本地文件格式必须为mp4,网络文件格式不受限制

4:其他格式的文件,目前仅支持网络文件,需要先将文件上传到网络上然后再使用此文件所在url.

url 字符串:本地文件路径或文件在网络上的url.例如:"./img/苹果.jpg" "https://www.123.com/abc.wav"

注意:当type 为0且url为空文本时,或者url= "清空"时,将会清除当前需要传递的所有文件.

返回值:

整数型:

0:失败

1:成功

如果返回0，可以调用GetLastError()来查看具体失败错误码,帮助分析问题.

示例:

    // 传递在线文件,文件格式不受限制

    vu.LlmAddFile(1, "https://www.123.com/abc.png");

 

    // 传递本地文件,文件格式必须为jpg、mp3、mp4其中一种

vu.LlmAddFile(2, "c://test.mp3");

 

 

使用完整示例:

    vusoft vu;

    vu.Create();//或者使用CreateRemote()创建远程调用对象

    

    ret = vu.LlmInit(model_url, api_key);

    std::cout << "[LLM] 加载结果:" << ret << std::endl;

 

    // 传递在线文件,文件格式不受限制

vu.LlmAddFile(1, "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg");

 

    while (true)

    {

        std::cout << "提问: ";

        std::string str_message;

        std::cin >> str_message;// 输入问题,假如为:"这张图片中都有啥???"

 

        if (str_message == "/exit")

            break;

        

        // 使用qwen-vl-plus模型,此模型支持图像理解,会看图片

        model_name = "qwen-vl-plus";

        ret = vu.LlmRun(str_message.data(), model_name, true);

        if (ret <= 0)

        {

            std::cout << "[LLM] 推理错误:" << vu.GetLastError() << std::endl;

            continue;

        }

 

        // 假设以下代码在其他线程运行,用来实时获取流式推理结果

        // ----------------------线程开始---------------------

        std::cout << "应答: " << std::endl;

        std::string str_assistant;

        bool is_end = false;

        while (is_end == false)

        {

            str_assistant = vu.LlmGetResponse(is_end);

            std::cout << str_assistant << std::endl;

        }

        // ----------------------线程结束---------------------

        

        // 添加模型回复的内容,使模型具有记忆

        ret = vu.LlmAddMessage(2, str_assistant.data());

 

}
 

输出结果如下

 

[LLM] 加载结果:1

[LLM] 设置模型:1

提问: 这张图片中都有啥???

应答:

这张图片展示了一位女士和一只狗在沙滩上互动的场景。具体细节如下：

 

1. **人物**：

   - 一位女士坐在沙滩上，穿着格子衬衫和黑色裤子。

   - 她面带微笑，似乎在与狗互动。

 

2. **动物**：

   - 一只狗坐在女士旁边，看起来是一只金毛猎犬。

   - 狗戴着彩色的项圈，显得非常可爱。

   - 狗伸出前爪，似乎是在与女士握手或玩耍。

 

3. **环境**：

   - 场景发生在沙滩上，背景是大海和天空。

   - 太阳的位置表明这是日落时分，光线柔和，给整个画面增添了一种温暖的氛围。

   - 沙滩上有脚印，显示出这里有人来人往。

 

4. **活动**：

   - 女士和狗之间似乎正在进行愉快的互动，可能是在玩耍或者训练。

 

总体来说，这是一幅温馨和谐的画面，展示了人与宠物之间的美好时光。

---

## 

函数简介:

添加指定内容给大模型,使其具有更强的能力和记忆.

其实LLM模型并没有记忆能力,它每次推理都是基于当前提供的输入进行的,像一个健忘的老人一样,每次问它问题都是重新回答.

以聊天模型为例子:

如果想让它像是正常人一样具有记忆,清楚之前都聊过什么,就需要将它每次的输出都添加进来,这样它就能够在之前聊天内容的基础上进行推理,像是具有记忆了一样.

 

函数原型:

int LlmAddMessage(mode, msg)

参数定义:

mode 整数型:添加的内容模式,取值如下:

0:模型的设定,指明模型的功用或者角色,一般全局设置一次即可.

1:用户的输入,本模式仅作为保留,默认不用设置,因为本插件底层已经对用户输入进行了特殊处理.

2:模型的回复,它的主要作用是提供对话上下文和历史记录,从而让模型能够进行连贯的多轮对话.

msg 字符串:传递给模型的文本内容,自然语言描述,例如:"你好!","你喜欢人工智能吗?"

注意:当mode为0且msg为空文本时,或者msg = "清空"时,将会清除大模型的所有设定和记忆.

返回值:

整数型:

0:失败

1:成功

如果返回0，可以调用GetLastError()来查看具体失败错误码,帮助分析问题.

示例:

以下代码是在聊天对话基础上进行了角色扮演和增加了记忆功能

    vusoft vu;

    vu.Create();//或者使用CreateRemote()创建远程调用对象

    

    ret = vu.LlmInit(model_url, api_key);

    std::cout << "[LLM] 加载结果:" << ret << std::endl;

 

    // 设置模型基础功能

    msg = R"(你是一个热爱角色扮演的家伙.

现在你扮演的角色是一名中国古代给人看病的医生,熟练掌握中医技术.

我现在是你的病人,需要向你求助.)";

    

    ret = vu.LlmAddMessage(0, msg);// mode为0,一般全局设置一次即可

    std::cout << "[LLM] 设置模型:" << ret << std::endl;

 

    while (true)

    {

        std::cout << "提问: ";

        std::string str_message;

        std::cin >> str_message;// 输入问题,假如为:"吃什么药可以长生不死???"

 

        if (str_message == "/exit")

            break;

        

        // 使用qwen-plus模型

        model_name = "qwen-plus";

        ret = vu.LlmRun(str_message.data(), model_name, true);

        if (ret <= 0)

        {

            std::cout << "[LLM] 推理错误:" << vu.GetLastError() << std::endl;

            continue;

        }

 

        // 假设以下代码在其他线程运行,用来实时获取流式推理结果

        // ----------------------线程开始---------------------

        std::cout << "应答: " << std::endl;

        std::string str_assistant;

        bool is_end = false;

        while (is_end == false)

        {

            str_assistant = vu.LlmGetResponse(is_end);

            std::cout << str_assistant << std::endl;

        }

        // ----------------------线程结束---------------------

        

        // 添加模型回复的内容,使模型具有记忆

        ret = vu.LlmAddMessage(2, str_assistant.data());

 

    }

 

    //清空大模型所有设定和记忆

    vu.LlmAddMessage(0, "");

vu.LlmAddMessage(0, "清空");

//上面两种方式实现的效果是一样的,只需要一种方式调用即可.

---

## 

函数简介:

增加大模型function call构建函数的参数.

LLM模型只能推理,无法调用函数,如果想让它对接你的函数接口,例如调用操作键盘鼠标的函数,则需要构建function call,告诉它你都提供了哪些函数给它,这些函数都有什么用途,参数都是什么.

这样大模型在推理时,如果需要靠提交的函数来完成任务,则会返回函数的调用信息,如此这般,程序就能依赖大模型的推理结果实现调用指定函数了.

本函数是构建函数参数所用,比如你有一个函数:

int mouse_move(int x,int y)

这个函数有两个参数x和y,那么你就首先需要按顺序通过LlmAddParameter()构建参数x和y之后,再通过LlmAddToolCall()来完成构建整个函数.

函数原型:

int LlmAddParameter(name, type, description, is_force_use)

参数定义:

name 字符串:要构建的参数的名字,例如"x"或者"y".

type 整数型:要构建的参数的类型,取值如下:

1:字符串类型,例如"我是文本"

2:数值类型,包括小数和整数,例如:3.1415

3:整数类型,不允许有小数部分,例如:-100

4:布尔类型,例如:true, false

5:对象类型,例如:{ "name": "帅哥", "age": 18 }

6:数组类型,例如:[1, 2, 3]或["a", "b"]

7:空值类型,表示空

description 字符串:参数的描述信息,使用自然语言实现,例如:"窗口的x坐标"

is_force_use 整数型:是否强制填写本参数,0=默认不填写,1=必须填写.大模型会根据这个来决定当前构建的参数是否需要填写.

返回值:

整数型:

返回的是当前成功构建的参数的个数.

当调用LlmAddToolCall()实现整个函数的构建后,所有缓存的参数构建将会清空.

示例:

    // 假如我有一个查询天气的函数

    // int get_current_weather(location,time) 

    // 需要如下方式构建这个function call

 

    // 构建一个function call,让大模型可以实现函数调用.

    

    // 1.先构建get_current_weather()的两个参数

    vu.LlmAddParameter("location", 1, "城市或县区，比如北京市、杭州市、余杭区等。", true);

    vu.LlmAddParameter("time", 1, "查询的时间，格式为YYYY-MM-DD或相对时间（如今天、明天、三天后）", false);//is_force_use为false,默认不填写事件

 

    // 2.构建toolcall实现完整的函数构建

    ret = vu.LlmAddToolCall("get_current_weather", "当你想查询指定城市的天气时非常有用。");

    std::cout << "[LLM] 构建get_current_weather函数结果:" << ret << std::endl;

---

## 

函数简介:

给大模型添加一个function call函数,让大模型懂得去调用自定义的函数做某些事情.

LLM模型只能推理,无法调用函数,如果想让它对接你的函数接口,例如调用操作键盘鼠标的函数,则需要构建function call,告诉它你都提供了哪些函数给它,这些函数都有什么用途,参数都是什么.

这样大模型在推理时,如果需要靠提交的函数来完成任务,则会返回函数的调用信息,如此这般,程序就能依赖大模型的推理结果实现调用指定函数了.

本函数是构建供模型调用的自定义函数所用,比如你有一个函数:

int mouse_move(int x,int y)

这个函数有两个参数x和y,那么你就首先需要按顺序通过LlmAddParameter()构建参数x和y之后,再通过LlmAddToolCall()来完成构建整个函数.

函数原型:

int LlmAddToolCall(name, description)

参数定义:

name 字符串:函数的名字,例如:"mouse_move".

description 字符串:当前要构建的函数的描述信息,告诉大模型在何等情况下使用这个要构建出来的函数.例如:"当你想要移动鼠标的时候,本函数非常有用".

返回值:

整数型:

0:失败

1:成功

如果返回0，可以调用GetLastError()来查看具体失败错误码,帮助分析问题.

示例:

下面是一个简单的使用function call框架示例,给大模型赋能函数调用功能(AI智能体).

 

    vusoft vu;

    vu.Create();//或者使用CreateRemote()创建远程调用对象

    

    ret = vu.LlmInit(model_url, api_key);

    std::cout << "[LLM] 加载结果:" << ret << std::endl;

 

    // 假如我有一个查询天气的函数

    // int get_current_weather(string location,string time) 

    // 需要如下方式构建这个function call

 

    // 构建一个function call,让大模型可以实现函数调用.

    

    // 1.先构建get_current_weather()的两个参数

    vu.LlmAddParameter("location", 1, "城市或县区，比如北京市、杭州市、余杭区等。", true);

    vu.LlmAddParameter("time", 1, "查询的时间，格式为YYYY-MM-DD或相对时间（如今天、明天、三天后）", false);//is_force_use为false,默认不填写时间

 

    // 2.构建toolcall实现完整的函数构建

    ret = vu.LlmAddToolCall("get_current_weather", "当你想查询指定城市的天气时非常有用。");

    std::cout << "[LLM] 构建get_current_weather函数结果:" << ret << std::endl;

 

    // 可以增加多个function call

    vu.LlmAddParameter("name", 1, "歌曲的名字,比如 青花瓷 伤心太平洋 等。", true);

    vu.LlmAddParameter("singer", 1, "歌手,比如 周杰伦 刘德华 等", true);

    vu.LlmAddToolCall("play_music", "当想打开音乐播放器放歌时非常有用。");

 

    while (true)

    {

        std::cout << "提问: ";

        std::string str_message;

        std::cin >> str_message;// 输入问题,假如为:"我要听周杰伦的青花瓷,帮我进行播放!!!"

 

        if (str_message == "/exit")

            break;

 

        // 增加让大模型调用自定义函数的功能

        while (true)

        {

            // 使用qwen-plus模型

            model_name = "qwen-plus";

            ret = vu.LlmRun(str_message.data(), model_name, true);

            if (ret <= 0)

            {

                std::cout << "[LLM] 推理错误:" << vu.GetLastError() << std::endl;

                continue;

            }

 

            // 当需要调用函数时,要将消息内容清空,避免重复传递.

            if (ret == 2)

                str_message = "";

 

            // 假设以下代码在其他线程运行,用来实时获取流式推理结果

            // ----------------------线程开始---------------------

            std::cout << "应答: " << std::endl;

            std::string str_assistant;

            bool is_end = false;

            while (is_end == false)

            {

                str_assistant = vu.LlmGetResponse(is_end);

                std::cout << str_assistant << std::endl;

            }

            // ----------------------线程结束---------------------

 

 

            // 添加模型回复的内容,使模型具有记忆

            if (ret != 2)

            {

                // 只有在不调用函数的时候才添加回复

                ret = vu.LlmAddMessage(2, str_assistant.data());

                break;// 则跳出本层循环,重新开启对话

            }

            

            // 需要调用函数,模型返回的调用请求可能有多条,可能请求调用多个函数,所以我们用循环

            bool isToolCall = true;

            while (isToolCall)

            {

                // 查询是否有需要调用的函数

                int count = 0;

                res = vu.LlmGetToolCall(count);// 每次调用LlmGetToolCall()都会返回一条函数请求

                if (strlen(res) <= 0 || count <= 0)

                    isToolCall = false;

                

                // 没有请求,跳出本层循环

                if(!isToolCall)

                    break;

 

                // 解析大模型的函数调用JSON请求

                LONG64 pJson = vu.JsonReadInPut(res);

                LONG64 pID = vu.JsonReadGetValObjByKey(pJson, "id");

                LONG64 pName = vu.JsonReadGetValObjByKey(pJson, "name");

                LONG64 pArgs = vu.JsonReadGetValObjByKey(pJson, "args");

                std::string strID = vu.JsonReadGetStr(pID);

                std::string strName = vu.JsonReadGetStr(pName);

                std::string strContent = "";

                std::string args;

 

                {

                    // 进行参数解析

                    LONG num = vu.JsonReadGetObjSize(pArgs);

                    for (size_t i = 0; i < num; i++)

                    {

                        LONG64 pKey = vu.JsonReadGetKeyObj(pArgs, i);

                        std::string strKey = vu.JsonReadGetStr(pKey);

                        LONG64 pVal = vu.JsonReadGetValObjByIndex(pArgs, i);

                        LONG nType = vu.JsonReadGetObjType(pVal);

                        std::cout << "strKey:" << strKey << std::endl;

                        switch (nType)

                        {

                        case 1:

                            args += "(" + strKey + ":" + vu.JsonReadGetStr(pVal) + ")";

                            std::cout << "string:" << vu.JsonReadGetStr(pVal) << std::endl;

                            break;

                        case 2:

                            args += "(" + strKey + ":" + std::to_string(vu.JsonReadGetNum(pVal)) + ")";

                            std::cout << "number:" << vu.JsonReadGetNum(pVal) << std::endl;

                            break;

                        }

                    }

                }

                

                // 调用查询天气的函数

                if (strName == "get_current_weather")

                {

                    // 这里模拟我们调用了get_current_weather()

                    get_current_weather(args);

                    strContent = "今天是雨天";

                }

 

                // 调用播放音乐的函数

                if (strName == "play_music")

                {

                    // 这里模拟我们调用了get_current_weather()

                    play_music(args);

                    strContent = "播放成功,请安静聆听美妙的音乐吧°";

                }

 

                // 将调用函数的结果提交给大模型

                vu.LlmAddToolResult(strID.data(), strContent.data());

                std::cout << "调用自定义函数-> id:" << strID << " 函数名字:" << strName << " 参数:" << args << std::endl;

                std::cout << "执行结果:" << strContent << std::endl;

            }

 

        }

}

 

上述代码实现了一个简单的AI智能体,并且提供了两个自定义的函数给大模型.

因为篇幅原因,并没有对上述框架的代码做过多优化,其实应该将解析函数请求和调用函数部分封装成子程序,避免代码杂乱.

另外我们提供了一份易语言关于构建AI智能体的示例demo.

感兴趣的同学可以在插件下载目录中找到.

 
 

运行后控制台输出如下内容:

 

[LLM] 加载结果:1

[LLM] 构建get_current_weather函数结果:1

提问: 我要听周杰伦的晴天

应答:

<think>

 

好的，用户说他要听周杰伦的晴天。首先，我需要确认他想听的是原版还是演唱会版本。根据知识库里的信息，周杰伦的《晴天》有几个不同的版本，包括原版和多个Live版本，比如2004无与伦比演唱会的现场版，还有地表最强世界巡回演唱会的版本。不过，用户没有特别指定版本，所以通常默认会推荐原版或者最受欢迎的版本。

 

接下来，我需要检查可用的工具。用户提供的工具中有play_music函数，需要歌曲名和歌手名作为参数。这里用户已经明确给出了歌手是周杰伦，歌曲是晴天，所以参数都满足。需要调用play_music函数来播放这首歌。

 

另外，知识库中提到《晴天》的歌词和不同版本的演唱会上的表演信息，可能用户如果感兴趣的话，可以后续提供更多信息，比如歌词或者演唱会的时间点。不过当前用户的需求只是播放歌曲，所以先执行播放即可。

 

需要确认是否有版权问题或者其他限制，但根据提供的工具，假设play_music函数已经处理了这些，直接调用即可。因此，正确的做法是调用play_music函数，参数为name: "晴天"，singer: "周杰伦"。

strKey:name

string:晴天

strKey:singer

string:周杰伦

调用自定义函数-> id:call_2162583193eb492c83a387 函数名字:play_music 参数:(name:晴天)(singer:周杰伦)

执行结果:播放成功,请安静聆听美妙的音乐吧°

应答:

<think>

 

好的，用户让我播放周杰伦的《晴天》，我已经调用了play_music函数，返回结果是播放成功。现在需要给出一个自然的中文回复，确认歌曲开始播放，并且保持友好和简洁。

 

首先，用户的需求明确，就是想听这首歌，所以直接确认播放成功即可。不需要额外信息，但可以加点情感词，比如“美妙的音乐”来增强体验。同时，保持口语化，避免机械感，所以用“请安静聆听”这样的表达。另外，用户可能希望立即开始听歌，所以回复要简短，不打扰他们享受音乐。

 

检查是否有需要补充的信息，比如歌词或演唱会信息，但根据之前的对话，用户只是要播放歌曲，所以不需要多余内容。确保回复符合工具调用的结果，即播放成功，然后结束。最后用一个合适的符号，比如°，让回复看起来更自然。

 

 

</think>

 

播放成功，请安静聆听美妙的音乐吧°

---

## 

函数简介:

当大模型请求使用function call调用函数时,将调用结果告诉给它.

函数原型:

int LlmAddToolResult(id, content)

参数定义:

id 字符串:大模型请求调用函数时生成的函数id,通过解析LlmGetToolCall()可以获得这个参数.

content 字符串:id对应的function call函数调用结果,用自然语言进行描述,例如:"调用失败了,需要重新更换参数."或者"调用获得天气的函数结果是:北京市今天多云,三十八摄氏度".

返回值:

整数型:

返回已经通知过调用结果的请求的数量,该数量将会在下次调用LlmRun()函数时归零.

示例:

                // 获取需要调用的函数

                res = vu.LlmGetToolCall(count);// 每次调用LlmGetToolCall()都会返回一条函数请求

                // 解析大模型的函数调用JSON请求

                /*此处省略解析res的步骤......*/

 

                strID = /*从res中解析出的函数id*/;

                strName = /*从res中解析出的函数名称*/;

                args = “从res中解析出要传递的参数”;

 

                // 调用查询天气的函数

                if (strName == "get_current_weather")

                {

                    // 这里模拟我们调用了get_current_weather()

                    get_current_weather(args);

                    strContent = "今天是雨天";

                }

                // 将调用函数的结果提交给大模型

                vu.LlmAddToolResult(strID, strContent);

                std::cout << "调用自定义函数-> id:" << strID << " 函数名字:" << strName << " 参数:" << args << std::endl;

                std::cout << "执行结果:" << strContent << std::endl;

---

## 

函数简介:

获取大模型的推理结果,支持以流式的方式获取.

何为流式获取?因为大模型输出的结果往往很大,多为长文本或音视频等内容,如果一次性获取完整结果,需要推理很长时间,为了缓解等待时长,所以可以一边推理一边输出,像水流一样源源不断.因此流式输出每次只能获取到结果的一部分,直到推理结束.

注意:函数LlmRun()为阻塞执行方式,推理结束后才会返回,所以想实时获取流式结果,需要在调用LlmRun()后用其他线程去循环LlmGetResponse()拉取结果.

函数原型:

string LlmGetResponse(is_end)

参数定义:

is_end 变参指针:返回是否推理结束,0=未结束,1=结束.

返回值:

字符串:

推理的结果内容

示例:

    vusoft vu;

    vu.Create();//或者使用CreateRemote()创建远程调用对象

    

    ret = vu.LlmInit(model_url, api_key);

    std::cout << "[LLM] 加载结果:" << ret << std::endl;

 

    while (true)

    {

        std::cout << "提问: ";

        std::string str_message;

        std::cin >> str_message;

 

        if (str_message == "/exit")

            break;

        

        // 使用qwen-plus模型

        model_name = "qwen-plus";

        ret = vu.LlmRun(str_message.data(), model_name, true);

        if (ret <= 0)

        {

            std::cout << "[LLM] 推理错误:" << vu.GetLastError() << std::endl;

            continue;

        }

 

        // 假设以下代码在其他线程运行,用来实时获取流式推理结果

        // ----------------------线程开始---------------------

        std::cout << "应答: " << std::endl;

        bool is_end = false;

        while (is_end == false)

        {

            std::string str_assistant = vu.LlmGetResponse(is_end);

            std::cout << str_assistant << std::endl;

        }

        // ----------------------线程结束---------------------

        

    }

---

## 

函数简介:

从大模型推理结果获取调用函数的请求.

当我们构建了自定义函数function call提交给大模型后,如果大模型觉得用户的提问需要调用这些函数,则会生成调用函数的请求,通过此函数可以获取到大模型想调用的函数.

注意:某些情况下大模型需要调用多个函数共同来完成任务,所以本插件会将所有function call的请求都缓存下来,每次调用LlmGetToolCall()时都会从缓存中按顺序读取一条请求.

函数原型:

string LlmGetToolCall(count)

参数定义:

count 变参指针:返回当前模型请求调用的函数数量.

返回值:

字符串:

以JSON字符串格式存储的调用请求,完整存放了模型想要调用的函数名字和所需传递的参数.需要使用JsonReadXXXXXXXX系列函数对其解析.

具体使用方法请参阅.

解析后会获得以下字符串数据:

id:请求函数的id(字符串).

name:请求函数的名字(字符串).

args:请求函数的参数,它也是一个JSON对象,需要二次解析获取所有参数.

具体如何使用本插件解析JSON字符串,请参阅相关API手册.

注意:关于JSON解析,本插件可以达到万字解析不足1微秒(us)的速度,应是全世界最顶尖的解析速度了.

同时由于JSON数据往往是以字符串格式存放,虽然也可以用文本操作的手段来提取内容,但如果数据中的结构体十分复杂,文本提取将会变得困难无比.

所以推荐使用本插件来解析JSON数据,关于AI的模型推理结果,大多数都会以JSON来传输,故此,十分重要!

示例:

 

 

                // 查询是否有需要调用的函数

                int count = 0;

                res = vu.LlmGetToolCall(count);// 每次调用LlmGetToolCall()都会返回一条函数请求

 

 

                // 解析大模型的函数调用JSON请求

                LONG64 pJson = vu.JsonReadInPut(res);

                LONG64 pID = vu.JsonReadGetValObjByKey(pJson, "id");

                LONG64 pName = vu.JsonReadGetValObjByKey(pJson, "name");

                LONG64 pArgs = vu.JsonReadGetValObjByKey(pJson, "args");

                std::string strID = vu.JsonReadGetStr(pID);

                std::string strName = vu.JsonReadGetStr(pName);

                std::string args;

 

                {

                    // 进行参数解析

                    LONG num = vu.JsonReadGetObjSize(pArgs);

                    for (size_t i = 0; i < num; i++)

                    {

                        LONG64 pKey = vu.JsonReadGetKeyObj(pArgs, i);

                        std::string strKey = vu.JsonReadGetStr(pKey);

                        LONG64 pVal = vu.JsonReadGetValObjByIndex(pArgs, i);

                        LONG nType = vu.JsonReadGetObjType(pVal);

                        std::cout << "strKey:" << strKey << std::endl;

                        switch (nType)

                        {

                        case 1:

                            args += "(" + strKey + ":" + vu.JsonReadGetStr(pVal) + ")";

                            std::cout << "string:" << vu.JsonReadGetStr(pVal) << std::endl;

                            break;

                        case 2:

                            args += "(" + strKey + ":" + std::to_string(vu.JsonReadGetNum(pVal)) + ")";

                            std::cout << "number:" << vu.JsonReadGetNum(pVal) << std::endl;

                            break;

                        }

                    }

                }

---

## 

函数简介:

初始化加载大模型,支持离线和在线两种部署方式.

离线大模型仅具备基础的聊天推理功能,且较吃机器配置,建议使用在线部署方式.

函数原型:

int LlmInit(model_url,api_key)

参数定义:

model_url 字符串:离线大模型目录的存放路径,或者在线API接口url

api_key 字符串:在线API接口的秘钥,一般在提供大模型在线接口的平台注册后可以获取.本参数仅对接在线模型需要填写,离线模型填空即可.

返回值:

整数型:

0:失败

1:成功

示例:

vusoft vu;

vu.Create();//或者使用CreateRemote()创建远程调用对象

    

ret = vu.LlmInit(model_url, api_key);

std::cout << "[LLM] 加载结果:" << ret << std::endl;

 

 

 

 

 

/*---------------------------------------------------------------------------------------

* 参数model_url可以是离线大模型目录,也可以是在线模型API接口URL地址,具体取决于您的使用意愿.

* ---------------------------------------------------------------------------------------*/

 

// 部署离线本地llm大模型(使用Qwen3-0.6B模型),API秘钥填写空字符串

model_url = "./_model/chat/Qwen3-0.6B/";

api_key = "";

ret = vu.LlmInit(model_url, api_key);

 

// 部署在线云端llm大模型(当前示例使用阿里百炼平台的API接口,您也可以选择其他平台,只要其支持OpenApi规范即可)

model_url="https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions";

api_key = "在阿里百炼平台注册账号后,获取到的专属你的API秘钥";

ret = vu.LlmInit(model_url, api_key);

 

 

/*============================================================================

* 问:如何选择在线接口平台?

* -----------------------------------------------------------------------

* 答:目前国内外的大模型基本都提供了API接口,很多都支持OpenApi规范,

* 所以选择平台时仅需从大模型的先进程度、费用、性能、延迟等各方面综合考量.

* 有些平台提供新人免费额度或者每日免费用量,而且使用评率不高的话完全可以做

* 到白嫖.

* -----------------------------------------------------------------------

* 

* -----------------------------------------------------------------------

* 问:有哪些支持的平台可供选择?

* -----------------------------------------------------------------------

* 答:推荐以下性价比较高的平台.

*-----------------------------------------------------------------------

* 智谱AI---------------部分支持OpenApi--------

* 官网:https://www.bigmodel.cn/invite?icode=OZLnjtadA1AXRtciCpGtu0jPr3uHog9F4g5tjuOUqno%3D

* --------------------------------------------

* 阿里云百炼-----------完全支持OpenApi--------

* 官网:https://bailian.console.aliyun.com/?spm=5176.29597918.J_zK-KF2dfzE2iOekxSO0K-.1.33987b08mlSOX2&tab=model#/model-market

* --------------------------------------------

* 无问芯穹-------------完全支持OpenApi--------

* 官网:https://docs.infini-ai.com/gen-studio/models/playground.html

* --------------------------------------------

* 另外还有Deepseek、月之暗面、腾讯混元、百度智能云千帆等,以后有更好的平台我们也会更新推荐出来.

*============================================================================*/

---

## 

函数简介:

重置llm大模型,仅支持本地离线部署的模型.

函数原型:

int LlmReset()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

如果返回0，可以调用GetLastError()来查看具体失败错误码,帮助分析问题.

示例:

    vusoft vu;

    vu.Create();//或者使用CreateRemote()创建远程调用对象

    

    // 部署离线本地llm大模型(使用Qwen3-0.6B模型),API秘钥填写空字符串

    model_url = "./_model/chat/Qwen3-0.6B/";

    api_key = "";

    ret = vu.LlmInit(model_url, api_key);

    std::cout << "[LLM] 加载结果:" << ret << std::endl;

 

    ret = vu.LlmReset();

    std::cout << "[LLM] 重置结果:" << ret << std::endl;

---

## 

函数简介:

让llm大模型执行推理,以文本形式告诉大模型用户想要干什么.

推理成功后,需要调用LlmGetResponse获取结果.

函数原型:

int LlmRun(message,model,is_think)

参数定义:

message 字符串:传递给llm模型的想法,以常规文本的形式传递,例如:"你是谁?你会干什么?帮我写一个打地鼠的C++游戏源码!"

model 字符串:llm模型名字,每次调用本函数可以使用不同的模型.

is_think 整数型:是否深度思考模式,取值:0=不思考,1=深度思考.

返回值:

整数型:

0:失败

1:成功

2:需要调用交代给大模型的自定义函数才能继续(关于function call).

如果返回0，可以调用GetLastError来查看具体失败错误码,帮助分析问题.

示例:

    vusoft vu;

    vu.Create();//或者使用CreateRemote()创建远程调用对象

    

    ret = vu.LlmInit(model_url, api_key);

    std::cout << "[LLM] 加载结果:" << ret << std::endl;

 

    while (true)

    {

        std::cout << "提问: ";

        std::string str_message;

        std::cin >> str_message;

 

        if (str_message == "/exit")

            break;

        

        // 使用qwen-plus模型,可随时换其他模型,例如:"deepseek-r1"

        model_name = "qwen-plus";

        ret = vu.LlmRun(str_message.data(), model_name, true);

        if (ret <= 0)

        {

            std::cout << "[LLM] 推理错误:" << vu.GetLastError() << std::endl;

            continue;

        }

        std::cout << "应答: " << std::endl;

        bool is_end = false;

        std::string str_assistant = vu.LlmGetResponse(is_end);

        std::cout << str_assistant << std::endl;

}

 

 

上述代码便是一个完整的LLM聊天模型的基础框架,此时用户只需要在提问时输入自己想法,便可以获得模型推理后返回的结果.

这就是一个简略版的文本聊天机器人.

---

## 

LLM功能介绍

 

LLM是英文Large Language Model 的缩写，中文意思是“大语言模型”，也就是大模型。

当前AI最热门的研究项目均离不开LLM技术支持。

ChatGPT、文心一言、豆包、通义千问等都是LLM的应用。

它不仅可以实现聊天、知识问答、创作和绘画，还能具备强大的思考和记忆能力，能够帮我们完成许多任务，例如：写代码、打游戏、唱歌等。

 

本插件深度耦合LLM技术方案，提供了本地和线上部署大模型的方案，助力您对接最新的人工智能。

 

当前LLM功能支持对接线上OpenAPI规范的大模型接口，可以轻松切换不同的大模型，同时为将来迭代更新做更兼容的支持。

 

使用本插件，您可以轻松的自己构建一个本地或者云端服务器上的AI智能体，不光可以当做ChatGPT一样进行文字聊天，还可以开发类似于小智AI的机器人，也可以实现让大模型帮你操作电脑，购买外卖、火车票、查询新闻、播放音乐、语音聊天、视频聊天，还能让它帮你操作键盘鼠标进行打游戏，搞一个机器人吗喽帮你干活也挺有意思哈。

 

当前集成功能如下:

1.离线llm模型部署,最低4G显存的N卡便可以流畅推理.

2.对接在线OpenAPI规范的llm模型接口,白嫖的接口也可以使用.

3.支持运行时模型切换(仅支持在线API接口方式对接),可以顺畅的上一秒还在使用文本聊天大模型,下一秒就切换成了视频生成大模型.

4.支持流式响应获取,无延迟获取大模型的响应结果,告别提问一句得等半天.

5.支持文件上传给大模型,例如文档/图片/音视频.

6.支持function call工具调用,让大模型可以调用你编写的函数,例如:鼠标移动、键盘操作、播放音乐、查询网页等.(工具函数需要自己编写,提供给大模型告知用法和参数类型)

7.上述功能已经基本涵盖了当前大模型应用的所有主流用法,基于这些功能已经足可开发市面上你见过或没见过的所有AI应用了.

8.不过我们还是会孜孜不倦的继续开发新的功能,以提供更好的使用方式.

 

 

有关本插件LLM部分功能的详细用法,请阅览相关部分的API文档.

 

另外我们提供了用易语言编写的语音聊天机器人的demo,新接触本功能的同学可以在插件下载目录中寻找.

感谢您的支持!!!

---

## 

函数简介:

在指定范围内检测并识别字符串内容,不需要制作字库.

函数原型:

string AiOcrDetectObjects(x1,y1,x2,y2)

参数定义:

x1 整数型:区域的左上X坐标

y1 整数型:区域的左上Y坐标

x2 整数型:区域的右下X坐标

y2 整数型:区域的右下Y坐标

返回值:

字符串:
返回的是所有识别到的字符串,以json(字符串)格式返回,失败返回空字符串.

格式如下:

 {

 "范围": [[50, 29], [289, 32], [289, 64], [50, 62]],

 "内容": "纯臻营养护发素",

 "置信度": 0.99576914310455322,

 "分类置信度": null,

 "分类标签": -1,

 "单字": "纯[[50,29],[84,29],[84,62],[50,62]]臻[[84,29],[118,30],[118,63],[84,62]]营[[118,30],[152,30],[152,63],[118,63]]养[[152,30],[187,31],[187,63],[152,63]]护[[187,31],[221,31],[221,63],[187,63]]发[[221,31],[255,32],[255,64],[221,63]]素[[255,32],[289,32],[289,64],[255,64]]"

 }

 

示例:

    vu.SetPath("D:\\AI\\模型\\");

    vu.AiOcrSetModel(0, "det.onnx", "rec.onnx", "rec.txt");

    vu.AiOcrUseModel(0);

    res = vu.AiOcrDetectObjects(0, 0, 200, 200);

std::cout << "识别结果:" << res << std::endl;

 

注意:返回值是一个标准的json对象数据,可以通过字符串查找分割等方式进行解析也可以借用插件的json解析功能提取数据.

具体示例可以参考OCR示例的demo源码,你也可以封装成自己的解析函数.

---

## 

函数简介:

从文件加载指定的模型,此模型应为OCR模型,用来进行字符串识别.

函数原型:

LONG AiOcrSetModel(index, det_model,rec_model,rec_dict)

参数定义:

index 整数型: 模型的序号.  从0开始

det_model 字符串:det模型的路径,这个是用来检测字符串位置的模型.

rec_model 字符串:rec模型的路径,这个是用来检测字符串内容的模型.

rec_dict 字符串:文字识别的字典文件.

注意:所有文件路径都不可以包含中文字串,所以需要将这些资源提前放在用英文起名的目录中!

返回值:

整数型:
1  表示成功
0  失败

示例:

    

	// 模型所在的路径不可包含中文字串

	vu.SetPath("D:\\AI\\model\\");

	vu.AiOcrSetModel(0, "det.onnx", "rec.onnx", "rec.txt");

---

## 

函数简介:

切换当前使用的模型序号.用于AiOcrDetectObjects等接口.

函数原型:

LONG AiOcrUseModel(index)

参数定义:

index 整数型: 模型的序号.

返回值:

整数型:
1  表示成功
0  失败

示例:

    vu.AiOcrUseModel(0);

---

## 

函数简介:

在指定范围内检测并识别表单内容,不需要制作字库.

函数原型:

string AiTableDetectObjects(x1,y1,x2,y2)

参数定义:

x1 整数型:区域的左上X坐标

y1 整数型:区域的左上Y坐标

x2 整数型:区域的右下X坐标

y2 整数型:区域的右下Y坐标

返回值:

字符串:
返回的是所有识别到的字符串,以json(字符串)格式返回,失败返回空字符串.

示例:

    vu.SetPath("D:\\AI\\模型\\");

    vu.AiTableSetModel(0, "det.onnx", "rec.onnx", "rec.txt","table.onnx","table.txt","layout.onnx","layout.txt");

    vu.AiTableUseModel(0);

 

    vu.AiTableDetectObjects(0, 0, 200, 200);

std::cout << "识别结果:" << res << std::endl;

 

注意:返回值是一个标准的json对象数据,可以通过字符串查找分割等方式进行解析也可以借用插件的json解析功能提取数据.

具体示例可以参考OCR示例的demo源码,你也可以封装成自己的解析函数.

---

## 

函数简介:

从文件加载指定的模型,此模型应为表单识别模型,用来进行表单字符串识别.

函数原型:

LONG AiTableSetModel(index,det_model,rec_model,rec_dict,table_model, table_dict,layout_model,layout_dict)

参数定义:

index 整数型: 模型的序号.  从0开始

det_model 字符串:det模型的路径,这个是用来检测字符串位置的模型.

rec_model 字符串:rec模型的路径,这个是用来检测字符串内容的模型.

rec_dict 字符串:文字识别的字典文件.

table_model 字符串:表格模型的路径,表格识别模型专门用于检测和识别图像中的表格结构。它能够识别表格的行、列和单元格，从而提取表格数据。

table_dict 字符串:表格识别的字典文件.

layout_model 字符串:用于指定版面分析模型的路径。版面分析模型用于识别文档的整体结构，包括文本块、标题、段落、图片等元素的位置和关系。这对于复杂文档的自动化处理非常重要，因为它能够帮助理解文档的布局和内容组织。

layout_dict 字符串:版面分析任务的字典文件.

返回值:

整数型:
1  表示成功
0  失败

示例:

    vu.SetPath("D:\\AI\\模型\\");

    vu.AiTableSetModel(0, "det.onnx", "rec.onnx", "rec.txt","table.onnx","table.txt","layout.onnx","layout.txt");

---

## 

函数简介:

切换当前使用的模型序号.用于AiTableDetectObjects等接口.

函数原型:

LONG AiTableUseModel(index)

参数定义:

index 整数型: 模型的序号.

返回值:

整数型:
1  表示成功
0  失败

示例:

    vu.AiTableUseModel(0);

---

## 

函数简介:

在指定范围内检测对象,支持多种yolo检测模型,包括物体检测,实例分割,姿态识别,定向边界等完整yolov11版本的所有功能.

函数原型:

string AiYoloDetectObjects(x1, y1, x2, y2,prob,iou)

参数定义:

x1 整数型:区域的左上X坐标

y1 整数型:区域的左上Y坐标

x2 整数型:区域的右下X坐标

y2 整数型:区域的右下Y坐标

prob双精度浮点型: 置信度,也可以认为是相似度. 超过这个prob的对象才会被检测

iou 双精度浮点型: 用于对多个检测框进行合并.  越大越不容易合并(很多框重叠). 越小越容易合并(可能会把正常的框也给合并). 所以这个值一般建议0.4-0.6之间. 
               可以在Yolo综合工具里进行测试.

返回值:

字符串:
返回的是所有检测到的对象,以json(字符串)格式返回,根据不同模型返回的数据也不相同,可以通过解析json来获取检测到的所有对象.失败返回空字符串.

示例:

    vu.AiYoloUseModel(0);

    res = vu.AiYoloDetectObjects(0, 0, 2000, 2000, 0.5, 0.45);

std::cout << "检测结果:" << res << std::endl;

 

注意:因为每一种模型返回的数据分布都不相同,所以需要自定义解析功能.

例如姿态识别模型解析出来的结果类似以下数据:

 {

 "范围": [668, 391, 809, 875],

 "任务": "pose",

 "名称": " 'person'",

 "置信度": 0.88229143619537354,

 "旋转角度": 0,

 "坐标数组": [[794, 432], [796, 422], [792, 421], [800, 428], [801, 426], [803, 486], [804, 479], [780, 567], [779, 561], [756, 564], [758, 550], [794, 636], [796, 632], [761, 729], [770, 728], [723, 839], [729, 838]]

 }

这是一个标准的json对象数据,可以通过字符串查找分割等方式进行解析,获取对象范围,置信度,各个肢体所在位置等.

也可以借用插件的json解析功能提取数据.

具体示例可以参考YOLO示例的demo源码,你也可以封装成自己的解析函数.

---

## 

函数简介:

从文件加载指定的模型

函数原型:

long AiYoloSetModel(index,file)

参数定义:

index 整数型: 模型的序号.  从0开始

file字符串: 模型文件名. 比如"xxxx.onnx",文件路径必须为全英文,不可以有中文字串.

返回值:

整数型:
1  表示成功
0  失败

示例:

	// 模型所在的路径不可包含中文字串

	vu.SetPath("c:\\model\\");

	vu.AiYoloSetModel(0, "det.onnx");	//物体检测

	vu.AiYoloSetModel(1, "seg.onnx");	//实例分割

	vu.AiYoloSetModel(2, "pose.onnx");	//姿态识别

	vu.AiYoloSetModel(3, "obb.onnx");	//定向边界

---

## 

函数简介:

从内存加载指定的模型.

函数原型:

long AiYoloSetModelMemory(index,data,size)

参数定义:

index 整数型: 模型的序号.  从0开始

data 长整数型: 模型的内存地址

size 整数型: 模型的大小

返回值:

返回值

示例:

    vu.SetPath("D:\\AI\\模型\\");

    data = vu.ReadFileData("物体检测.onnx",len);

    vu.AiYoloSetModelMemory(0, data, len);

---

## 

函数简介:

切换当前使用的模型序号.用于AiYoloDetectXX等系列接口.

函数原型:

long AiYoloUseModel(index)

参数定义:

index 整数型: 模型的序号.

返回值:

整数型:
1  表示成功
0  失败

示例:

    vu.AiYoloUseModel(0);

---

## 

yolo是一种基于人工智能用于计算机视觉任务的对象检测系统,处理速度快，能够实现实时目标检测，适合应用于自动驾驶、视频监控等领域.

它能够以极快的速度在一张图片上检测出物体的类别,位置,以及多种物品之间进行轮廓分割等.

 

使用步骤:

1.数据集的采集.
一般需要采集目标物体的多张图片,可以使用相机拍摄,也可以使用截图,总之将目标物体的图片存放收集起来,做成数据集相册.可以同时收集多种类别的目标,图片越多越好,至少得一百张才能达到初步效果.

2.数据标注
使用专用的数据集标注工具对数据图片进行标注,推荐使用本插件配套的LabelVision标注工具进行标注,工具的用法可以参考教程.
 

3.训练模型
用足够的标注好的数据对模型进行训练.同样也有配套的训练工具YOLO训练测试工具帮您快速训练出优秀的高性能模型.
 

4.模型部署
模型训练好之后,就可以使用插件的yolo功能进行部署,通过调用AiYoloSetModel(),AiYoloDetectObjects()等函数,可以轻松实现对图片中对象的多种检测.
    vu.SetPath("D:\\AI\\模型\\");
    data = vu.ReadFileData("物体检测.onnx",len);
    vu.AiYoloSetModelMemory(0, data, len);
 
    vu.AiYoloUseModel(0);
    res = vu.AiYoloDetectObjects(0, 0, 2000, 2000, 0.5, 0.45);
    std::cout << "检测结果:" << res << std::endl;

注:
如果想提高检测效率，两个途径
1. 使用更小更快的预训练模型. 比如yolov8n
2. 运行的机器CPU核心数越多,效率越高. 因为检测函数内部是多线程执行的.

如果想提高检测精度,两个途径
1. 使用更大但是更慢的预训练模型. 比如yolov8x
2. 对于每个类尽可能多的提供训练图片. 尽可能多的提供各种复杂背景下的训练图片. 尽可能对每个类在各种复杂背景下都提供训练图片. 训练的轮次可以稍微多一些.

如果发现自己训练后的模型,会越训练越差,说明是你训练的过头了(过拟合),减少轮次,重新训练.

 

当前yolo接口和各种工具支持yolo全系列版本(常用的是yolov3-11).

---

## 

简介:

唤醒词与关键字检测使用的是相同的技术手段,仅仅是使用场景不同.

唤醒词:程序一直处于低功耗的休眠状态,直到语音识别到指定的唤醒词,才开始进入工作状态.

关键字:程序在工作时检查语音中是否存在指定的词汇,一般用来屏蔽违禁词.

使用方式:

首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndAsr()对目标音频数据进行检测.

SndAsr()将会返回检测到的内容,若在同一段音频中同时存在多个唤醒词/关键字,则返回的内容将会使用"&"进行分隔,若未检测到唤醒词/关键字,则返回空字符串.

 

在使用SndSetModel()设置参数时:

参数model_path:必须为关键字检测模型的目录路径,该模型可以在插件下载目录找到.模型路径必须为全英文路径,不可以带中文或中文标点.

参数words:需要为具有固定格式内容的txt文件,或者原始字符串.其格式为: 汉语音节 + " @"(空格+@) + 关键字/唤醒词. 其中汉语音节必须包含声母+韵母+声调,声母与韵母之间用空格隔开.

 

在使用SndAsr()设置参数时:

参数buf:必须为音频数据指针(浮点型数据).

参数num_samples:必须为音频数据中浮点数的个数.

参数sample_rate:必须为音频的采样率,最佳采样率为16000,其他采样率或许无法实现效果.

 

提供给SndAsr()的音频数据必须为单通道音频,可以使用AudioReadFile()读取音频文件获取数据,也可以使用AudioRecordStart()+AudioRecordReadStream()获取音频设备的音频流数据.

 

示例:

        vusoft vu;

        vu.Create();// 或者使用CreateRemote()创建远程调用对象

 

        // 使用唤醒词/关键字模型

        int mode = 1;

        string model_path = "D:/Code/_model/snd/kws";

        string words = "D:/Code/_model/snd/kws/keywords.txt";

 

        // words也可以是指定的唤醒词/关键字内容

        words = R"(x iǎo ài t óng x ué @小爱同学

n ǐ h ǎo w èn w èn @你好问问

t uì ch ū x ì t ǒng @退出系统)";

 

 

        std::cout << "开始初始化模型,请耐心等待..." << std::endl;

        vu.SndSetModel(0, mode, model_path, words);

 

        std::cout << "启动麦克风输入..." << std::endl;

        int sample_rate = 16000;

        vu.AudioRecordStart(sample_rate, -1);

 

        std::cout << "现在,你可以对着麦克风说话,试试效果了!" << std::endl;

        while (true)

        {

            Sleep(1000);

            LONG64 buf = 0, count = 0;

            vu.AudioRecordReadStream(buf, count);

            if (buf && count)

            {

                std::string  res = vu.SndAsr(0, (LONG64)buf, count, sample_rate, true);

                if (res.length() > 0)

                    std::cout << "识别到:" << res << std::endl;

                if (res == "退出系统")

                    break;

            }

 

        }

        vu.AudioRecordStop();

        std::cout << "当前已退出" << std::endl;

        system("pause");

 

运行上述代码后控制台打印内容如下:

 
开始初始化模型,请耐心等待...
启动麦克风输入...
现在,你可以对着麦克风说话,试试效果了!
识别到:你好问问
识别到:小爱同学
识别到:小爱同学&你好问问
识别到:退出系统
当前已退出
请按任意键继续. . .

---

## 

简介:
需要联网的快速语音合成,如果您的机器配置过低,无法实时生成音频,推荐使用此方案.
此语音生成模型可以做到实时语音生成,也就是说从语音开始到结束,生成的速度是快于播放速度的.
支持多国语言与三百余种音色.
支持男声与女声.
支持流式生成.
使用方式:
首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndTts()对目标文本转为音频数据.
SndTts()将会实现将文本转语音,并且返回生成的音频的采样率.
可以在SndTts()执行期间另起一条线程,并且调用SndGetStream()来获取音频流数据.
 
在使用SndSetModel()设置参数时:
参数model_path:参数无效,需要为空字符串.
参数words:参数无效,需要为空字符串. 
 
在使用SndTts()设置参数时:
参数spk_id:必须为说话人字符串,例如:"zh-CN-XiaoxiaoNeural",其它值可以通过此查询.
参数is_prompt_speech:参数无效.
 
在使用SndGetStream()设置参数时:
参数samples:必须为用来接收音频数据指针的变量.
参数num_samples:必须为用来接收音频数据中浮点数个数的变量.
示例:

        vusoft vu;

        vu.Create();// 或者使用CreateRemote()创建远程调用对象

 

        int mode = 8;

 

        std::cout << "开始初始化模型,请耐心等待..." << std::endl;

        vu.SndSetModel(0, mode, "", "");

 

 

        string text = "实在难以相信,我现在说的话竟然是AI生成出来的!";

        int sample_rate = 0;

 

        std::cout << "生成语音中..." << std::endl;

        ULONGLONG start_time = GetTickCount64();

        sample_rate = vu.SndTts(0, text, "zh-CN-XiaoxiaoNeural", 1.0, true);

        std::cout << "耗时:" << GetTickCount64() - start_time << "ms" << std::endl;

 

 

        // 下面所有代码,可以运行在另外一条线程中,以获取实时生成的音频流数据

 

        // 发起播放音频

        vu.AudioPlayStart(1, sample_rate, -1);

        // 获取音频流数据

        while (true)

        {

            LONG64 samples = 0, num_sample = 0;

            std::string res = vu.SndGetStream(0, samples, num_sample);

            std::cout << "获取音频流数据结果:" << res << std::endl;

 

            // 将音频流数据写入扬声器进行播放

            vu.AudioPlayWriteStream(1, sample_rate, samples, num_sample);

 

            if (res == "running")

                continue;

            break;

        }

 

        /*等待播放结束,或者达成什么条件后,调用AudioPlayStop()结束播放*/

        while (vu.AudioGetStreamSize(1) != 0)

        {

            Sleep(1);

        }

 

        vu.AudioPlayStop();

 

        system("pause");

---

## 

简介:
说话人列表,仅供在线语音合成使用,由SndTts()参数spk_id指定下述列表中的说话人.
说话人:

中文:

zh-CN-XiaoxiaoNeural

zh-CN-XiaoyiNeural

zh-CN-YunjianNeural

zh-CN-YunxiNeural

zh-CN-YunxiaNeural

zh-CN-YunyangNeural

zh-CN-liaoning-XiaobeiNeural

zh-CN-shaanxi-XiaoniNeural

zh-HK-HiuGaaiNeural

zh-HK-HiuMaanNeural

zh-HK-WanLungNeural

zh-TW-HsiaoChenNeural

zh-TW-YunJheNeural

zh-TW-HsiaoYuNeural

 

英文:
en-AU-NatashaNeural
en-AU-WilliamNeural
en-CA-ClaraNeural
en-CA-LiamNeural
en-HK-YanNeural
en-HK-SamNeural
en-IN-NeerjaExpressiveNeural
en-IN-NeerjaNeural
en-IN-PrabhatNeural
en-IE-ConnorNeural
en-IE-EmilyNeural
en-KE-AsiliaNeural
en-KE-ChilembaNeural
en-NZ-MitchellNeural
en-NZ-MollyNeural
en-NG-AbeoNeural
en-NG-EzinneNeural
en-PH-JamesNeural
en-PH-RosaNeural
en-US-AvaNeural
en-US-AndrewNeural
en-US-EmmaNeural
en-US-BrianNeural
en-SG-LunaNeural
en-SG-WayneNeural
en-ZA-LeahNeural
en-ZA-LukeNeural
en-TZ-ElimuNeural
en-TZ-ImaniNeural
en-GB-LibbyNeural
en-GB-MaisieNeural
en-GB-RyanNeural
en-GB-SoniaNeural
en-GB-ThomasNeural
en-US-AnaNeural
en-US-AndrewMultilingualNeural
en-US-AriaNeural
en-US-AvaMultilingualNeural
en-US-BrianMultilingualNeural
en-US-ChristopherNeural
en-US-EmmaMultilingualNeural
en-US-EricNeural
en-US-GuyNeural
en-US-JennyNeural
en-US-MichelleNeural
en-US-RogerNeural
en-US-SteffanNeural

 

其他语种:

af-ZA-AdriNeural

af-ZA-WillemNeural

sq-AL-AnilaNeural

sq-AL-IlirNeural

am-ET-AmehaNeural

am-ET-MekdesNeural

ar-DZ-AminaNeural

ar-DZ-IsmaelNeural

ar-BH-AliNeural

ar-BH-LailaNeural

ar-EG-SalmaNeural

ar-EG-ShakirNeural

ar-IQ-BasselNeural

ar-IQ-RanaNeural

ar-JO-SanaNeural

ar-JO-TaimNeural

ar-KW-FahedNeural

ar-KW-NouraNeural

ar-LB-LaylaNeural

ar-LB-RamiNeural

ar-LY-ImanNeural

ar-LY-OmarNeural

ar-MA-JamalNeural

ar-MA-MounaNeural

ar-OM-AbdullahNeural

ar-OM-AyshaNeural

ar-QA-AmalNeural

ar-QA-MoazNeural

ar-SA-HamedNeural

ar-SA-ZariyahNeural

ar-SY-AmanyNeural

ar-SY-LaithNeural

ar-TN-HediNeural

ar-TN-ReemNeural

ar-AE-FatimaNeural

ar-AE-HamdanNeural

ar-YE-MaryamNeural

ar-YE-SalehNeural

az-AZ-BabekNeural

az-AZ-BanuNeural

bn-BD-NabanitaNeural

bn-BD-PradeepNeural

bn-IN-BashkarNeural

bn-IN-TanishaaNeural

bs-BA-VesnaNeural

bs-BA-GoranNeural

bg-BG-BorislavNeural

bg-BG-KalinaNeural

my-MM-NilarNeural

my-MM-ThihaNeural

ca-ES-EnricNeural

ca-ES-JoanaNeural

hr-HR-GabrijelaNeural

hr-HR-SreckoNeural

cs-CZ-AntoninNeural

cs-CZ-VlastaNeural

da-DK-ChristelNeural

da-DK-JeppeNeural

nl-BE-ArnaudNeural

nl-BE-DenaNeural

nl-NL-ColetteNeural

nl-NL-FennaNeural

nl-NL-MaartenNeural

et-EE-AnuNeural

et-EE-KertNeural

fil-PH-AngeloNeural

fil-PH-BlessicaNeural

fi-FI-HarriNeural

fi-FI-NooraNeural

fr-BE-CharlineNeural

fr-BE-GerardNeural

fr-CA-ThierryNeural

fr-CA-AntoineNeural

fr-CA-JeanNeural

fr-CA-SylvieNeural

fr-FR-VivienneMultilingualNeural

fr-FR-RemyMultilingualNeural

fr-FR-DeniseNeural

fr-FR-EloiseNeural

fr-FR-HenriNeural

fr-CH-ArianeNeural

fr-CH-FabriceNeural

gl-ES-RoiNeural

gl-ES-SabelaNeural

ka-GE-EkaNeural

ka-GE-GiorgiNeural

de-AT-IngridNeural

de-AT-JonasNeural

de-DE-SeraphinaMultilingualNeural

de-DE-FlorianMultilingualNeural

de-DE-AmalaNeural

de-DE-ConradNeural

de-DE-KatjaNeural

de-DE-KillianNeural

de-CH-JanNeural

de-CH-LeniNeural

el-GR-AthinaNeural

el-GR-NestorasNeural

gu-IN-DhwaniNeural

gu-IN-NiranjanNeural

he-IL-AvriNeural

he-IL-HilaNeural

hi-IN-MadhurNeural

hi-IN-SwaraNeural

hu-HU-NoemiNeural

hu-HU-TamasNeural

is-IS-GudrunNeural

is-IS-GunnarNeural

id-ID-ArdiNeural

id-ID-GadisNeural

iu-Latn-CA-SiqiniqNeural

iu-Latn-CA-TaqqiqNeural

iu-Cans-CA-SiqiniqNeural

iu-Cans-CA-TaqqiqNeural

ga-IE-ColmNeural

ga-IE-OrlaNeural

it-IT-GiuseppeMultilingualNeural

it-IT-DiegoNeural

it-IT-ElsaNeural

it-IT-IsabellaNeural

ja-JP-KeitaNeural

ja-JP-NanamiNeural

jv-ID-DimasNeural

jv-ID-SitiNeural

kn-IN-GaganNeural

kn-IN-SapnaNeural

kk-KZ-AigulNeural

kk-KZ-DauletNeural

km-KH-PisethNeural

km-KH-SreymomNeural

ko-KR-HyunsuMultilingualNeural

ko-KR-InJoonNeural

ko-KR-SunHiNeural

lo-LA-ChanthavongNeural

lo-LA-KeomanyNeural

lv-LV-EveritaNeural

lv-LV-NilsNeural

lt-LT-LeonasNeural

lt-LT-OnaNeural

mk-MK-AleksandarNeural

mk-MK-MarijaNeural

ms-MY-OsmanNeural

ms-MY-YasminNeural

ml-IN-MidhunNeural

ml-IN-SobhanaNeural

mt-MT-GraceNeural

mt-MT-JosephNeural

mr-IN-AarohiNeural

mr-IN-ManoharNeural

mn-MN-BataaNeural

mn-MN-YesuiNeural

ne-NP-HemkalaNeural

ne-NP-SagarNeural

nb-NO-FinnNeural

nb-NO-PernilleNeural

ps-AF-GulNawazNeural

ps-AF-LatifaNeural

fa-IR-DilaraNeural

fa-IR-FaridNeural

pl-PL-MarekNeural

pl-PL-ZofiaNeural

pt-BR-ThalitaMultilingualNeural

pt-BR-AntonioNeural

pt-BR-FranciscaNeural

pt-PT-DuarteNeural

pt-PT-RaquelNeural

ro-RO-AlinaNeural

ro-RO-EmilNeural

ru-RU-DmitryNeural

ru-RU-SvetlanaNeural

sr-RS-NicholasNeural

sr-RS-SophieNeural

si-LK-SameeraNeural

si-LK-ThiliniNeural

sk-SK-LukasNeural

sk-SK-ViktoriaNeural

sl-SI-PetraNeural

sl-SI-RokNeural

so-SO-MuuseNeural

so-SO-UbaxNeural

es-AR-ElenaNeural

es-AR-TomasNeural

es-BO-MarceloNeural

es-BO-SofiaNeural

es-CL-CatalinaNeural

es-CL-LorenzoNeural

es-CO-GonzaloNeural

es-CO-SalomeNeural

es-ES-XimenaNeural

es-CR-JuanNeural

es-CR-MariaNeural

es-CU-BelkysNeural

es-CU-ManuelNeural

es-DO-EmilioNeural

es-DO-RamonaNeural

es-EC-AndreaNeural

es-EC-LuisNeural

es-SV-LorenaNeural

es-SV-RodrigoNeural

es-GQ-JavierNeural

es-GQ-TeresaNeural

es-GT-AndresNeural

es-GT-MartaNeural

es-HN-CarlosNeural

es-HN-KarlaNeural

es-MX-DaliaNeural

es-MX-JorgeNeural

es-NI-FedericoNeural

es-NI-YolandaNeural

es-PA-MargaritaNeural

es-PA-RobertoNeural

es-PY-MarioNeural

es-PY-TaniaNeural

es-PE-AlexNeural

es-PE-CamilaNeural

es-PR-KarinaNeural

es-PR-VictorNeural

es-ES-AlvaroNeural

es-ES-ElviraNeural

es-US-AlonsoNeural

es-US-PalomaNeural

es-UY-MateoNeural

es-UY-ValentinaNeural

es-VE-PaolaNeural

es-VE-SebastianNeural

su-ID-JajangNeural

su-ID-TutiNeural

sw-KE-RafikiNeural

sw-KE-ZuriNeural

sw-TZ-DaudiNeural

sw-TZ-RehemaNeural

sv-SE-MattiasNeural

sv-SE-SofieNeural

ta-IN-PallaviNeural

ta-IN-ValluvarNeural

ta-MY-KaniNeural

ta-MY-SuryaNeural

ta-SG-AnbuNeural

ta-SG-VenbaNeural

ta-LK-KumarNeural

ta-LK-SaranyaNeural

te-IN-MohanNeural

te-IN-ShrutiNeural

th-TH-NiwatNeural

th-TH-PremwadeeNeural

tr-TR-EmelNeural

tr-TR-AhmetNeural

uk-UA-OstapNeural

uk-UA-PolinaNeural

ur-IN-GulNeural

ur-IN-SalmanNeural

ur-PK-AsadNeural

ur-PK-UzmaNeural

uz-UZ-MadinaNeural

uz-UZ-SardorNeural

vi-VN-HoaiMyNeural

vi-VN-NamMinhNeural

cy-GB-AledNeural

cy-GB-NiaNeural

zu-ZA-ThandoNeural

zu-ZA-ThembaNeural

---

## 

简介:
将音频文件中的人声与背景声进行分离,例如将歌曲的歌手声音与背景音乐分离.
使用方式:
首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndSep()对目标音频文件进行分离处理.
SndSep()将会实现人声与背景声分离,并返回是否成功.
 
在使用SndSetModel()设置参数时:
参数model_path:必须为声源分离模型的目录路径,该模型可以在插件下载目录找到.模型路径必须为全英文路径,不可以带中文或中文标点.
参数words:参数无效,需要为空字符串. 
示例:

        vusoft vu;

        vu.Create();//或者使用CreateRemote()创建远程调用对象

 

        int mode = 6;

        string model_path = "D:/Code/_model/snd/sep";

 

        std::cout << "开始初始化模型,请耐心等待..." << std::endl;

        vu.SndSetModel(0, mode, model_path, "");

 

        // 支持使用插件路径或者相对路径

        vu.SetPath("c:/voice_sep/");

 

        string input_wave = "sample.wav";

        string output_vocals_wave = "output_vocals.wav";

        string output_residual_wave = "output_residual.wav";

 

        std::cout << "执行声源分离..." << std::endl;

        ULONGLONG start_time = GetTickCount64();

        int ret = vu.SndSep(0, input_wave, output_vocals_wave, output_residual_wave);

        std::cout << "耗时:" << GetTickCount64() - start_time << "ms" << std::endl;

 

        system("pause");

---

## 

简介:
给大段的无标点状态的文本添加标点符号,使其更容易阅读.
支持各种常用标点.
使用方式:
首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndAsr()对目标字符串进行处理.
SndAsr()将会添加过标点符号的新字符串.
 
在使用SndSetModel()设置参数时:
参数model_path:必须为添加标点模型的目录路径,该模型可以在插件下载目录找到.模型路径必须为全英文路径,不可以带中文或中文标点.
参数words:参数无效,需要为空字符串.
 
在使用SndAsr()设置参数时:
参数buf:必须为需要添加标点符号的字符串地址.
参数num_samples:无效,填0即可.
参数sample_rate:无效,填0即可.
参数isFinished:无效,填0即可. 
示例:

        vusoft vu;

        vu.Create();// 或者使用CreateRemote()创建远程调用对象

 

        int mode = 4;

        string model_path = "D:/Code/_model/snd/punct";

        vu.SndSetModel(0, mode, model_path, "");

 

        std::string str = "我说的这些话都是没有加过标点符号的我也很好奇加上标点符号后会变成什么样子你要不要告诉我标点符号该怎么添加不然看这段话能把人给累嘎了";

        std::cout << "原始文本:" << std::endl << str << std::endl;

 

        ULONGLONG start_time = GetTickCount64();

 

        string res = vu.SndAsr(0, (LONG64)str.data(), 0, 0, 0);

 

        std::cout << "耗时:" << GetTickCount64() - start_time << "ms" << std::endl;

 

        std::cout << "处理结果:" << res << std::endl;

 
        system("pause");   
运行上述代码后控制台打印内容如下:
 
原始文本:
我说的这些话都是没有加过标点符号的我也很好奇加上标点符号后会变成什么样子你要不要告诉我标点符号该怎么添加不然看这段话能把人给累嘎了
耗时:18ms
处理结果:我说的这些话都是没有加过标点符号的，我也很好奇，加上标点符号后会变成什么样子。你要不要告诉我标点符号该怎么添加 ，不然看这段话能把人给累嘎了。
请按任意键继续. . .

---

## 

简介:
无需联网的语音合成,仅需少量功耗,就能在极短的时间内将文字转换成语音.
此语音生成模型可以做到实时语音生成,也就是说从语音开始到结束,生成的速度是快于播放速度的.
支持中英文生成语音与百余种音色.
支持男声与女声.
支持流式生成.
使用方式:
首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndTts()对目标文本转为音频数据.
SndTts()将会实现将文本转语音,并且返回生成的音频的采样率.
可以在SndTts()执行期间另起一条线程,并且调用SndGetStream()来获取音频流数据.
 
在使用SndSetModel()设置参数时:
参数model_path:必须为离线语音合成模型的目录路径,该模型可以在插件下载目录找到.模型路径必须为全英文路径,不可以带中文或中文标点.
参数words:参数无效,需要为空字符串. 
 
在使用SndTts()设置参数时:
参数spk_id:必须为说话人ID(音色ID)字符串,其值为"0"到"102".
参数is_prompt_speech:参数无效.
 
在使用SndGetStream()设置参数时:
参数samples:必须为用来接收音频数据指针的变量.
参数num_samples:必须为用来接收音频数据中浮点数个数的变量.
示例:

        vusoft vu;

        vu.Create();//或者使用CreateRemote()创建远程调用对象

 

        int mode = 7;

        string model_path = "D:/Code/_model/snd/tts";

 

        std::cout << "开始初始化模型,请耐心等待..." << std::endl;

        vu.SndSetModel(0, mode, model_path, "");

 

        string text = "实在难以相信,我现在说的话竟然是AI生成出来的!";

        int sample_rate = 0;

 

        std::cout << "生成语音中..." << std::endl;

        ULONGLONG start_time = GetTickCount64();

        sample_rate = vu.SndTts(0, text, "102", 1.0, true);

        std::cout << "耗时:" << GetTickCount64() - start_time << "ms" << std::endl;

 

 

        // 下面所有代码,可以运行在另外一条线程中,以获取实时生成的音频流数据

 

        // 发起播放音频

        vu.AudioPlayStart(1, sample_rate, -1);

 

        // 获取音频流数据

        while (true)

        {

            LONG64 samples = 0, num_sample = 0;

            std::string res = vu.SndGetStream(0, samples, num_sample);

            std::cout << "获取音频流数据结果:" << res << std::endl;

 

            // 将音频流数据写入扬声器进行播放

            vu.AudioPlayWriteStream(1, sample_rate, samples, num_sample);

 

            if (res == "running")

                continue;

            break;

        }

       

 

        /*等待播放结束,或者达成什么条件后,调用AudioPlayStop()结束播放*/

        while (vu.AudioGetStreamSize(1) != 0)

        {

            Sleep(1);

        }

 

        vu.AudioPlayStop();

 

        system("pause");

---

## 

简介:

语音活动检测,专门用来检测当前语音数据中是否包含人声(是否有人说话).

本模型运行时一直处于低功耗模式,当检测到人声时可以去执行其他任务,例如语音转文本等.

使用方式:

首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndAsr()对目标音频数据进行检测.

SndAsr()将会返回是否检测到人声,如果存在人声,则返回"yes",否则返回"no".

 

在使用SndSetModel()设置参数时:

参数model_path:必须为语音活动检测模型的目录路径,该模型可以在插件下载目录找到.模型路径必须为全英文路径,不可以带中文或中文标点.

参数words:需要为字符串类型的音频采样率,推荐使用16000的采样率的音频,即填写"16000",其他采样率或许会无法兼容模型.

 

在使用SndAsr()设置参数时:

参数buf:必须为音频数据指针(浮点型数据).

参数num_samples:必须为音频数据中浮点数的个数.

参数sample_rate:必须为音频的采样率,最佳采样率为16000.

 

提供给SndAsr()的音频数据必须为单通道音频,可以使用AudioReadFile()读取音频文件获取数据,也可以使用AudioRecordStart()+AudioRecordReadStream()获取音频设备的音频流数据.

 

示例:

    vusoft vu;

    vu.Create();// 或者使用CreateRemote()创建远程调用对象

    int sample_rate = 16000;

    

    int mode = 2;

    string model_path = "D:/Code/_model/snd/vad";

    std::string str_asmple_rate = std::to_string(sample_rate);

 

    std::cout << "开始初始化模型,请耐心等待..." << std::endl;

    vu.SndSetModel(0, mode, model_path,  str_asmple_rate.c_str());

 

    std::cout << "启动麦克风输入..." << std::endl;

    vu.AudioRecordStart(sample_rate, -1);

 

    std::cout << "现在,你可以对着麦克风说话,试试效果了!" << std::endl;

    std::string str_last;

    while (true)

    {

        LONG64 buf = 0, count = 0;

        vu.AudioRecordReadStream(buf, count);

        if (buf && count)

        {

            string res = vu.SndAsr(0,(LONG64)buf, count, sample_rate, true);

            if (str_last != res)

            {

                str_last = res;

                std::cout << "是否说话:" << res << std::endl;

            }   

        }

        Sleep(500);

    }

 

    vu.AudioRecordStop();

    std::cout << "当前已退出" << std::endl;

    system("pause"); 

运行上述代码后控制台打印内容如下:

 

        开始初始化模型,请耐心等待...

        启动麦克风输入...

        现在,你可以对着麦克风说话,试试效果了!

        是否说话:no

        是否说话:yes

        是否说话:no

        是否说话:yes

---

## 

简介:
语音识别检测,用来将人声话语转为文本字符串,识别语音说话内容.
本模型当前识别效率属于世界顶级梯队之一,可以实现无GPU环境识别一分钟语音仅需1-10秒(Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz).
实时性极强,适合影视/直播实时字幕、会议记录等场景.
使用方式:
首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndAsr()对目标音频数据进行检测.
SndAsr()将会返回识别的结果,几乎可以做到0延迟获取语音内容.
 
在使用SndSetModel()设置参数时:
参数model_path:必须为语音识别模型的目录路径,该模型可以在插件下载目录找到.模型路径必须为全英文路径,不可以带中文或中文标点.
参数words:需要为热词修正的txt文件(必须绝对路径),或者想要使用的热词.热词格式为:词组+空格+":"+权重值.
例如:"李白儿 :80.0" (模型默认的词组权重值为2.0,最大值为65535.0,提升权重值有利于模型学习到新词汇.)
 
在使用SndAsr()设置参数时:
参数buf:必须为音频数据指针(浮点型数据).
参数num_samples:必须为音频数据中浮点数的个数.
参数sample_rate:必须为音频的采样率,最佳采样率为16000.
参数isFinished:必须为音频中人声是否结束,如果结束需要设置为1,否则为0.
 
提供给SndAsr()的音频数据必须为单通道音频,可以使用AudioReadFile()读取音频文件获取数据,也可以使用AudioRecordStart()+AudioRecordReadStream()获取音频设备的音频流数据.
 
示例:
下述示例使用语音检测模型来识别人声是否结束,辅助语音识别模型进行识别语音内容.

        vusoft vu;

        vu.Create();// 或者使用CreateRemote()创建远程调用对象

 

        // 定义采样率

        int sample_rate = 16000;

        std::string str_asmple_rate = std::to_string(sample_rate);

 

        // 使用语音检测模型进行辅助

        int mode_vad = 2;

        string path_vad = "D:/Code/_model/snd/vad";

 

        std::cout << "开始初始化语音检测模型,请耐心等待..." << std::endl;

        int ret = vu.SndSetModel(0, mode_vad, path_vad, str_asmple_rate.c_str());

        if (ret != 1)

            std::cout << "错误:" << vu.SndGetError(0) << std::endl;

 

 

        // 加载语音识别模型

        int mode_rec = 3;

        string path_rec = "D:/Code/_model/snd/rec";

        string hotwords = "李白儿 :80.0";// 热词修正

 

        std::cout << "开始初始化语音识别模型,请耐心等待..." << std::endl;

        ret = vu.SndSetModel(1, mode_rec, path_rec, hotwords);

        if (ret != 1)

            std::cout << "错误:" << vu.SndGetError(0) << std::endl;

 

        // 使用麦克风输入语音

        std::cout << "启动麦克风输入..." << std::endl;

        vu.AudioRecordStart(sample_rate, -1);

 

        std::cout << "现在,你可以对着麦克风说话,试试效果了!" << std::endl;

 

        std::string str_last_rec;

        std::string str_last_vad;

        while (true)

        {

            // 获取麦克风音频

            LONG64 buf = 0, count = 0;

            vu.AudioRecordReadStream(buf, count);

            if (buf && count)

            {

                // 是否说完话

                bool is_end = 0;

 

                // 先进行语音活动检测,是否人声

                string res = vu.SndAsr(0, (LONG64)buf, count, sample_rate, false);

                if (str_last_vad != res)

                {

                    str_last_vad = res;

                    if (str_last_vad == "no")// 说明已经说完话了

                        is_end = 1;

                }

 

                // 只有当人声存在或者当前已经说完话时,才进行语音识别

                if (is_end || str_last_vad == "yes")

                {

                    // 使用语音识别模型将语音转文字

                    res = vu.SndAsr(1, (LONG64)buf, count, sample_rate, is_end);

                    if (str_last_rec != res)

                    {

                        str_last_rec = res;

                        std::cout << "说话内容:" << res << std::endl;

                    }

                }

            }

            Sleep(1000);

        }

        vu.AudioRecordStop();

        std::cout << "当前已退出" << std::endl;
        system("pause");    
运行上述代码后控制台打印内容如下:
 
开始初始化语音检测模型,请耐心等待...
开始初始化语音识别模型,请耐心等待...
启动麦克风输入...
现在,你可以对着麦克风说话,试试效果了!
说话内容:大家好
说话内容:大家好今天
说话内容:大家好今天是礼拜二
说话内容:大家好今天是礼拜二同时也是李白儿
说话内容:大家好今天是礼拜二同时也是李白儿的生日
说话内容:大家好今天是礼拜二同时也是李白儿的生日我送了她一
说话内容:大家好今天是礼拜二同时也是李白儿的生日我送了她一份语音
说话内容:大家好今天是礼拜二同时也是李白儿的生日我送了她一份语音识别
说话内容:大家好今天是礼拜二同时也是李白儿的生日我送了她一份语音识别模型
说话内容:大家好今天是礼拜二同时也是李白儿的生日我送了她一份语音识别模型他高兴的又
说话内容:大家好今天是礼拜二同时也是李白儿的生日我送了她一份语音识别模型他高兴的又吟了一首诗

---

## 

简介:
将目标语音的背景噪声最大化去除,在保留清晰人声的同时,可以有效去除背景噪声,使人声更加容易分辨和识别.
使用方式:
首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndAsr()对目标音频数据进行处理.最后再调用SndGetStream()获取降噪后的音频. 
 
在使用SndSetModel()设置参数时:
参数model_path:必须为语音降噪模型的目录路径,该模型可以在插件下载目录找到.模型路径必须为全英文路径,不可以带中文或中文标点.
参数words:参数无效,需要为空字符串.
 
在使用SndAsr()设置参数时:
参数buf:必须为音频数据指针(浮点型数据).
参数num_samples:必须为音频数据中浮点数的个数.
参数sample_rate:必须为音频的采样率,最佳采样率为16000.
 
在使用SndGetStream()设置参数时:
参数samples:必须为用来接收音频数据指针的变量.
参数num_samples:必须为用来接收音频数据中浮点数个数的变量.
 
示例:

        vusoft vu;

        vu.Create();// 或者使用CreateRemote()创建远程调用对象

 

        string path_voice = "c:/denoise/test.wav";

        int channels = 0;

        int sample_rate = 0;

        LONG64 buf = 0, count = 0;

 

        std::cout << "读取音频..." << std::endl;

        vu.AudioReadFile((LONG64)path_voice, channels, sample_rate, buf, count);

 

        string res = "";

 

        int mode = 5;

        string model_path = "D:/Code/_model/snd/denoise";

 

        std::cout << "开始初始化模型,请耐心等待..." << std::endl;

        vu.SndSetModel(0, mode, model_path, "");

 

        std::cout << "对音频进行降噪..." << std::endl;

        vu.SndAsr(0, (LONG64)buf, count, sample_rate, false);

 

        LONG64 buf_new = 0, count_new = 0;

        std::cout << "获取处理后音频" << std::endl;

        vu.SndGetStream(0, buf_new, count_new);

 

        string path_denoise = "c:/denoise/test_denoise.wav";

        std::cout << "新的音频写出" << std::endl;

        vu.AudioWriteFile(path_denoise, channels, sample_rate, buf_new, count_new);

 

 

        system("pause");

---

## 

简介:
将一段语音或者文字用指定的音色进行生成,可以使用任何人的音色.
支持零样本语音克隆.
支持实时音色克隆.
支持音色替换.
注意:使用音色克隆相关功能,请务必遵守国家法律法规,严禁使用本功能进行诈骗、伪造身份、散布虚假信息、诽谤他人、实施骚扰或任何其他违法犯罪活动。您必须确保已获得声音主人的充分授权。您需对使用本功能产生的一切后果独立承担法律责任。
使用方式:
因为音色克隆模型较大,无法支持32位程序加载,所以需要安装64位的服务端程序进行调用.
 
使用步骤:
1.在官网后台下载VoiceClone.exe这个服务端软件.
2.登录软件,并点击软件下方的启动服务端,并等待API服务端开启成功.
3.按下面的调用方式,实现编程对接.
 
编程对接:
首先调用SndSetModel(),并设置对应的参数,等待模型初始化成功之后,调用SndTts()将目标文本/音频转为使用指定提示音色的音频.
SndTts()将会实现音色克隆或替换,并且返回生成的音频的采样率.
可以在SndTts()执行期间另起一条线程,并且调用SndGetStream()来获取音频流数据.
 
在使用SndSetModel()设置参数时:
参数model_path:必须为服务端软件所在设备的IP和端口,例如:"http://127.0.0.1:8888".
参数words:必须包含提示音频文件、提示音频说话内容、需要设定的说话人id(自己指定任意字串,以便后续随时切换说话人音色),格式为:音频文件+"&&"+音频内容+"&&"+说话人id. 
 
在使用SndTts()设置参数时:
参数text:若为一段音频文件的路径(绝对路径),则会执行将此音频的音色替换为提示音频的音色.否则将会使用本参数的文本进行音色克隆生成.
参数spk_id:必须为使用SndSetModel()时设置的说话人id.
参数is_prompt_speech:参数表示是否强制倾向提示音频的音色,若值为1则强制倾向提示音频的音色,届时生成的音色更加接近提示音频,但是可能无法更好的适应语境.
 
在使用SndGetStream()设置参数时:
参数samples:必须为用来接收音频数据指针的变量.
参数num_samples:必须为用来接收音频数据中浮点数个数的变量.
示例:

        // 使用音色克隆的文本转语音或者音色替换音频,均需要开启服务端,方法就是打开VoiceClone.exe这个服务端软件,点击启动服务端即可

        // 服务端的下载地址可在官网后台获取

 

        vusoft vu;

        vu.Create();// 或者使用CreateRemote()创建远程调用对象

 

 

        std::string server = "http://127.0.0.1:8888";

        std::string prompt_path = "./test.wav";

        std::string prompt_text = "希望你以后能够做的比我还好呦。";

        std::string spk_id = "spk_1";

        std::string words = prompt_path + "&&" + prompt_text + "&&" + spk_id;

 

        int mode = 9;

 

        std::cout << "开始初始化模型,请耐心等待..." << std::endl;

        vu.SndSetModel(0, mode, server.c_str(), words.c_str());

 

 

        string text = "实在难以相信,我现在说的话竟然是AI生成出来的!";

        //text = "./sound.wav";//如果输入的内容为音频文件路径,则将会执行音色替换,否则为音色克隆的声音合成

        int sample_rate = 0;

 

        ULONGLONG start_time = GetTickCount64();

        sample_rate = vu.SndTts(0, text, spk_id.data(), 1.0, true);

        std::cout << "耗时:" << GetTickCount64() - start_time << "ms" << std::endl;

 

        // 下面所有代码,可以运行在另外一条线程中,以获取实时生成的音频流数据

 

        // 发起播放音频

        vu.AudioPlayStart(1, sample_rate, -1);

        // 获取音频流数据

        while (true)

        {

            LONG64 samples = 0, num_sample = 0;

            std::string res = vu.SndGetStream(0, samples, num_sample);

            std::cout << "获取音频流数据结果:" << res << std::endl;

 

            // 将音频流数据写入扬声器进行播放

            vu.AudioPlayWriteStream(1, sample_rate, samples, num_sample);

 

            if (res == "running")

                continue;

            break;

        }

 

        /*等待播放结束,或者达成什么条件后,调用AudioPlayStop()结束播放*/

        while (vu.AudioGetStreamSize(1) != 0)

        {

            Sleep(1);

        }

 

        vu.AudioPlayStop();

 

        system("pause");

---

## 

函数简介:

执行语音识别相关任务,目前支持的模式如下:

唤醒词/关键字检测

人声活动检测

语音转文本

文本标点符号添加

语音降噪

根据调用SndSetModel()时使用的模型执行相关任务.

函数原型:

string SndAsr(index, buf, num_samples, sample_rate, isFinished)

参数定义:
index 整数型:模型的序号,从0开始.
 
buf 长整数型:传输的数据,取值如下:
文本字符串地址:当SndSetModel()的mode参数为4(文本标点符合添加)时,需要传递添加标点符号的文本字符串地址.
音频数据地址:当SndSetModel()的mode参数为非4的值时,均需要传递音频数据,数据为浮点型,可以通过AudioReadFile()或者AudioRecordReadStream()获取.
 
num_samples 长整数型:音频数据的浮点数个数,当SndSetModel()的mode参数为4(文本标点符合添加)时,本参数无效.
 
sample_rate 整数型:音频的采样率,推荐使用16000采样率的音频,否则可能导致模型不兼容.当SndSetModel()的mode参数为4(文本标点符合添加)时,本参数无效.
 
isFinished 整数型:音频中的语音说话是否结束,仅限当SndSetModel()的mode参数为3(语音转文本)时,本参数才有用,其他情况本参数无效.

返回值:

字符串:

具体的返回值取决于当前使用的模型,模型基于SndSetModel()的mode参数进行选择,如下所示:

mode = 1 : 返回识别到的唤醒词/关键字,多个结果之间用"&"分隔.

mode = 2 : 返回"yes"表示识别到人声,否则为"no".

mode = 3 : 返回识别到的语音文本内容.

mode = 4 : 返回添加过标点符号的文本内容.

mode = 5 : 返回"ok"表示降噪成功 ,否则为"fail".

示例:

根据使用的模型,使用方法均有所不同,模型基于SndSetModel()的mode参数进行选择,如下所示:

mode = 1 : 唤醒词与关键字检测.

mode = 2 : 语音活动检测.

mode = 3 : 语音识别功能.

mode = 4 : 文本添加标点符号.

mode = 5 : 语音降噪功能.

---

## 

函数简介:
获取指定序号的语音模型的错误信息.前提是已经使用SndSetModel()加载完毕模型.

 

函数原型:

string SndGetError(index)

参数定义:

index 整数型:模型的序号,从0开始.

返回值:

字符串:

返回当前序号的语音模型错误信息,若没有错误信息,则返回空字符串.

示例:

    string err0 = vu.SndGetError(0);

    string err1 = vu.SndGetError(1);

    string err2 = vu.SndGetError(2);

---

## 

函数简介:

获取音频模型任务执行时生成的音频流数据.目前支持的模式如下:

语音降噪

离线语音生成

在线语音生成

音色克隆或替换
其他模式的音频任务将会获取不到数据.

函数原型:

string SndGetStream(index, samples, num_samples)

参数定义:

index 整数型:模型的序号,从0开始.

 
samples 变参指针:返回当前模型中音频流数据所在的内存指针,可以从这里读取缓冲的音频数据.因为数据是以浮点数存储,所以这里的指针可以当做浮点数类型指针(C/C++中的float *)
 
num_samples 变参指针:返回音频数据流中浮点数的个数,可以通过它计算出读取到的音频数据的总大小,计算方式num_samples × 4 .

 

返回值:

字符串:

"ok":当前阶段的音频流数据已经全部读取完毕.

"running":当前阶段的音频流数据还有剩余.

"fail":读取音频流失败,或者不存在

示例:

            LONG64 samples = 0, num_sample = 0;

            std::string res = vu.SndGetStream(0, samples, num_sample);

            std::cout << "获取音频流数据结果:" << res << std::endl;

 

其他示例请参考:

语音降噪

离线语音生成

在线语音生成

音色克隆或替换

---

## 

函数简介:

执行声源分离相关任务,将一段音频的人声与背景声分离,常用于音乐分离歌手声音与伴奏.
根据调用SndSetModel()时使用的模型执行相关任务.

函数原型:

int SndSep(index, input_wave, output_vocals_wave, output_residual_wave)

参数定义:

index 整数型:模型的序号,从0开始.

 

input_wave 字符串:需要被分离人声与背景声的音频文件路径.注意:仅支持.wav格式的音频文件.

 

output_vocals_wave 字符串:指定用来写出人声音频的路径.分离成功后会新建此文件并写入分离后的人声音频.注意:仅支持.wav为后缀文件路径.

 

output_residual_wave 字符串:指定用来写入剩余声音的路径.分离成功后会新建此文件并写入分离后的剩余音频.注意:仅支持.wav为后缀文件路径.

返回值:

整数型:

0:失败

1:成功
如果返回0，可以调用GetLastError()来查看具体失败错误码,帮助分析问题.

示例:
必须在调用SndSetModel()的时候mode参数为6(声源分离).
 
详细示例见:声源分离功能

---

## 

函数简介:

设置当前对象加载声音处理模型.

函数原型:

int SndSetModel(index, model_path, mode, words, info)

参数定义:

index 整数型:模型的序号,从0开始.

 

mode 整数型:要使用的音频模型模式,取值如下:

1:唤醒词/关键字检测.

2:语音活动检测(当前音频是否有人说话).

3:语音识别(语音转文本).

4:文本添加标点符号(将无标点的大段文本添加标点符号).

5:语音降噪(提升人声清晰度).

6:声源分离(背景音乐与人声进行分离).

7:离线语音合成(文本转语音,合成速度与系统硬件配置有关).
8:在线语音合成(文本转语音,合成速度与网速有关).
9:音色克隆(例如将一段文本用你自己的声音生成语音).

 

model_path 字符串:使用mode所指定的模型的路径(必须使用绝对路径).特殊情况:

mode = 8 : 当使用的模型为在线语音合成时,本参数无效,可填空字符串.

mode = 9 : 当使用的是音色克隆模型时,本参数需要为您自己架设的服务器地址和端口.

 

words 字符串:传给模型的附加信息,根据参数mode的选择的模型,传递针对所选模型的信息,具体方式如下所示:

mode = 1 : 需要给唤醒词/关键字检测模型传递要设置的唤醒词/关键字,可以是txt文件路径,也可以是字符串类型的唤醒词/关键字.具体用法请参考唤醒词或关键字检测.

mode = 2 : 需要给语音活动检测模型传递要设置的采样率,必须是字符串类型的数值表达,例如:"16000".具体用法请参考语音活动检测.

mode = 3 : 需要给语音识别模型传递的热词修正词语,可以是txt文件路径,也可以使字符串类型的热词.具体用法请参考语音识别热词修正部分.

mode = 9 : 需要给音色克隆模型传递的说话人数据,模型在克隆音色时会与此参数的设定进行关联,之后在执行音色克隆任务时便可使用指定的音色进行生成.具体用法请参考音色克隆.

mode = 其他 : 本参数不生效.

返回值:

整数型:

0:失败

1:成功
如果返回0，可以调用GetLastError()来查看具体失败错误码,帮助分析问题.

示例:

示例1:

唤醒词与关键字检测

 

示例2:

语音活动检测

 

示例3:

语音识别功能

 

示例4:

文本添加标段符号

 

示例5:

语音降噪功能

 

示例6:

声源分离功能

 

示例7:

离线语音合成

 

示例8:

在线语音合成

 

示例9:

音色克隆与替换

---

## 

函数简介:

执行语音生成相关的任务.目前支持的模式如下:

离线语音生成

在线语音生成

音色克隆或替换
根据调用SndSetModel()时使用的模型执行相关任务.

函数原型:

int SndTts(index, text, spk_id, speed, is_prompt_speech)

参数定义:

index 整数型:模型的序号,从0开始.

 

text 字符串:需要生成的内容.取值如下:
音频文件地址:仅限SndSetModel()的mode参数为9(音色克隆)时,且需要将指定目标的音频说话声音替换为预设的提示音频音色时,才需要填写音频文件的地址.
生成音频的文本:其他情况均需要填写需要生成音频的文本.
 

spk_id 字符串:想要使用的音色的说话人id,具体id的值由SndSetModel()时传递的words参数所包含,详细情况请阅览音色克隆.

 

speed 小数型:要生成的音频的语音速度,取值范围0-10,值越大,语速越快.

 
is_prompt_speech 整数型:是否否强制倾向提示音频的音色,若值为1则强制倾向提示音频的音色,届时生成的音色更加接近提示音频,但是可能无法更好的适应语境.仅限SndSetModel()时mode为9(音色克隆)时有用,其他模式本参数均无效.

 

返回值:

整数型:

成功返回生成的音频的采样率,失败返回0.

示例:
根据使用的模型,使用方法均有所不同,模型基于SndSetModel()的mode参数进行选择,如下所示:
mode = 7 : 离线语音合成.
mode = 8 : 在线语音合成.
mode = 9 : 音色克隆功能.

---



---

## 



---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标.

此接口使用Ai模块来实现,比传统的FindPic的效果更好. 不需要训练

函数原型:

long AiFindPic(x1, y1, x2, y2, pic_name, sim, dir,intX, intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

整数型:
返回找到的图片的序号,从0开始索引.如果没找到返回-1

示例:

    ret = vu.AiFindPic(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",  0.9, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标.

此接口使用Ai模块来实现,比传统的FindPicE的效果更好.不需要训练

函数原型:

string AiFindPicE(x1, y1, x2, y2, pic_name, sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index,x,y", 比如"3,100,200"

示例:

    res = vu.AiFindPicE(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",  0.9, 0);

    if (strstr(res, ","))

        std::cout << "找到图片:" << res << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标.

此接口使用Ai模块来实现,比传统的FindPicEx的效果更好.不需要训练

函数原型:

string AiFindPicEx(x1, y1, x2, y2, pic_name, sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)

比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的图片是图像序号为0的图片,坐标是(100,20),第二个是序号为2的图片,坐标(30,40)

示例:

    char * sss = (char*)vu.AiFindPicEx(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp", 0.9, 0);

    //sss结果为id1,x1,y1|id2,x2,y2|....idn,xn,yn

    //id为图片在图片列表中的索引，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",")== NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char * ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            long id = v.StrToNum(v.StrSplitGet(0), 10);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << id << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标. 此函数同AiFindPicEx.只是返回值不同.

此接口使用Ai模块来实现,比传统的FindPicExS的效果更好.不需要训练

函数原型:

string AiFindPicExS(x1, y1, x2, y2, pic_name,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回的是所有找到的坐标格式如下:"file,x,y| file,x,y..| file,x,y" (图片左上角的坐标)

比如"1.bmp,100,20|2.bmp,30,40" 表示找到了两个,第一个,对应的图片是1.bmp,坐标是(100,20),第二个是2.bmp,坐标(30,40)

示例:

    char* sss = (char*)vu.AiFindPicExS(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",0.9, 0);

    //sss结果为file1,x1,y1|file2,x2,y2|....filen,xn,yn

    //file为图片名字，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",") == NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char* ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            const char* f = v.StrSplitGet(0);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << f << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.

此接口使用Ai模块来实现,比传统的FindPicMem的效果更好.不需要训练

函数原型:

long AiFindPicMem(x1, y1, x2, y2, pic_info,sim, dir,intX, intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

整数型:
返回找到的图片的序号,从0开始索引.如果没找到返回-1

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

    ret = vu.AiFindPicMem(0, 0, 2000, 2000, pic_info, 0.9, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.

此接口使用Ai模块来实现,比传统的FindPicMemE的效果更好.不需要训练

函数原型:

string AiFindPicMemE(x1, y1, x2, y2, pic_info, sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index,x,y", 比如"3,100,200"

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

    res = vu.AiFindPicMemE(0,0,2000,2000, pic_info,0.9,0);

    if (strstr(res, ","))

        std::cout << "找到图片:" << res << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标. 这个函数要求图片是数据地址.

此接口使用Ai模块来实现,比传统的FindPicMemEx的效果更好.不需要训练

函数原型:

string AiFindPicMemEx(x1, y1, x2, y2, pic_info,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)

比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的图片是图像序号为0的图片,坐标是(100,20),第二个是序号为2的图片,坐标(30,40)

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

 

    char* sss = (char*)vu.AiFindPicMemEx(0, 0, 2000, 2000, pic_info,1.0, 0);

    //sss结果为id1,x1,y1|id2,x2,y2|....idn,xn,yn

    //id为图片在图片列表中的索引，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",") == NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char* ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            long id = v.StrToNum(v.StrSplitGet(0), 10);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << id << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 此函数同FindPic.只是返回值不同.

此接口使用Ai模块来实现,比传统的FindPicS的效果更好. 不需要训练

函数原型:

string AiFindPicS(x1, y1, x2, y2, pic_name, sim, dir,intX, intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

字符串:
返回找到的图片的文件名. 没找到返回长度为0的字符串.

示例:

    res = vu.AiFindPicS(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",  0.9, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标.

此接口使用Ai模块来实现,比传统的FindPic的效果更好. 不需要训练

与AiFindPic不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

LONG AiFindPicSuper(x1,y1,x2,y2,pic_name,sim,detMode,isBin,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下

0:标准模式,兼顾准确率和速度

1:高精度模式,但是速度会慢

2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

整数型:
返回找到的图片的序号,从0开始索引.如果没找到返回-1

示例:

    ret = vu.AiFindPicSuper(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",0.9, 0,0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标.

此接口使用Ai模块来实现,比传统的FindPicE的效果更好.不需要训练

与AiFindPicE不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

string AiFindPicSuperE(x1, y1, x2, y2, pic_name, sim,detMode,isBin)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下

0:标准模式,兼顾准确率和速度

1:高精度模式,但是速度会慢

2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图

返回值:

字符串:
返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index,x,y", 比如"3,100,200"

示例:

    res = vu.AiFindPicSuperE(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",0.9, 0,0);

    if (strstr(res, ","))

        std::cout << "找到图片:" << res << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标.

此接口使用Ai模块来实现,比传统的FindPicEx的效果更好.不需要训练

与AiFindPicEx不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

string AiFindPicSuperEx(x1, y1, x2, y2, pic_name, sim,detMode,isBin)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下

0:标准模式,兼顾准确率和速度

1:高精度模式,但是速度会慢

2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图

返回值:
字符串:
返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)

比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的图片是图像序号为0的图片,坐标是(100,20),第二个是序号为2的图片,坐标(30,40)

示例:

    sss = vu.AiFindPicSuperEx(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",0.9, 0,0);

    //sss结果为id1,x1,y1|id2,x2,y2|....idn,xn,yn

    //id为图片在图片列表中的索引，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",")== NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char * ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            long id = v.StrToNum(v.StrSplitGet(0), 10);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << id << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标. 此函数同AiFindPicEx.只是返回值不同.

此接口使用Ai模块来实现,比传统的FindPicExS的效果更好.不需要训练

与AiFindPicExS不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

string AiFindPicSuperExS(x1, y1, x2, y2, pic_name, sim,detMode,isBin)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下

0:标准模式,兼顾准确率和速度

1:高精度模式,但是速度会慢

2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图

返回值:
字符串:
返回的是所有找到的坐标格式如下:"file,x,y| file,x,y..| file,x,y" (图片左上角的坐标)

比如"1.bmp,100,20|2.bmp,30,40" 表示找到了两个,第一个,对应的图片是1.bmp,坐标是(100,20),第二个是2.bmp,坐标(30,40)

 

示例:

    sss = vu.AiFindPicSuperExS(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",0.9, 0,0);

    //sss结果为file1,x1,y1|file2,x2,y2|....filen,xn,yn

    //file为图片名字，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",") == NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char* ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            const char* f = v.StrSplitGet(0);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << f << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.

此接口使用Ai模块来实现,比传统的FindPicMem的效果更好. 不需要训练

与AiFindPicMem不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

LONG AiFindPicSuperMem(x1,y1,x2,y2,pic_info,sim,detMode,isBin,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下

0:标准模式,兼顾准确率和速度

1:高精度模式,但是速度会慢

2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

整数型:
返回找到的图片的序号,从0开始索引.如果没找到返回-1

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

    ret = vu.AiFindPicSuperMem(0, 0, 2000, 2000, pic_info, 0.9, 0,0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.

此接口使用Ai模块来实现,比传统的FindPicMemE的效果更好. 不需要训练

与AiFindPicMemE不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

string AiFindPicSuperMemE(x1,y1,x2,y2,pic_info,sim,detMode,isBin)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下

0:标准模式,兼顾准确率和速度

1:高精度模式,但是速度会慢

2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图

返回值:

字符串:
返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index,x,y", 比如"3,100,200"

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

    ret = vu.AiFindPicSuperMemE(0, 0, 2000, 2000, pic_info, 0.9, 0,0);

    if (strstr(res, ","))

        std::cout << "找到图片:" << res << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标.

此接口使用Ai模块来实现,比传统的FindPicMemE的效果更好. 不需要训练

与AiFindPicMemE不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

string AiFindPicSuperMemEx(x1,y1,x2,y2,pic_info,sim,detMode,isBin)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下

0:标准模式,兼顾准确率和速度

1:高精度模式,但是速度会慢

2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图

返回值:

字符串:
返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)

比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的图片是图像序号为0的图片,坐标是(100,20),第二个是序号为2的图片,坐标(30,40)

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

    sss = vu.AiFindPicSuperMemEx(0, 0, 2000, 2000, pic_info, 0.9, 0,0);

    //sss结果为id1,x1,y1|id2,x2,y2|....idn,xn,yn

    //id为图片在图片列表中的索引，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",")== NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char * ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            long id = v.StrToNum(v.StrSplitGet(0), 10);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << id << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 此函数同FindPic.只是返回值不同.

此接口使用Ai模块来实现,比传统的FindPicS的效果更好. 不需要训练

与AiFindPicS不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果.

函数原型:

string AiFindPicSuperS(x1, y1, x2, y2, pic_name, sim, detMode,isBin,intX,intY

)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
sim 双精度浮点型:相似度,取值范围0.1-1.0

detMode 整数型:匹配模式,取值如下
0:标准模式,兼顾准确率和速度
1:高精度模式,但是速度会慢
2:高速度模式,但是精度会差

isBin 整数型:是否二值化图像,取值如下(二值化后图像会变色灰度图,有些图片光线明暗变换剧烈,比如一会白天一会夜晚,此时使用二值化图像会更准确)

0:不进行二值化找图

1:将图像二值化后再找图
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

字符串:
返回找到的图片的文件名. 没找到返回长度为0的字符串.

示例:

    res = vu.AiFindPicSuperS(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp",0.9, 0,0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

Json解析,获取json对象数组对象的成员对象.

函数原型:

LONG64 JsonReadGetArrayObj(obj,index)

参数定义:

obj 长整数型:Json数组对象指针.

index 整数型:Json数组对象中成员对象的索引

返回值:

长整数型:

失败返回0,成功返回JSON数组对象中的成员对象指针.

示例:

    str = "{\

                \"phones\" : [\

                    \"212 555-1234\",\

                    \"646 555-5678\"\

                ]\

            }";

    obj = vu.JsonReadInPut(str);

    arr = vu.JsonReadGetValObjByKey(obj, "phones");

    num = vu.JsonReadGetArraySize(arr);

    std::cout << "数组成员数:" << num << std::endl;

 

    val = vu.JsonReadGetArrayObj(arr, 0);

    res = vu.JsonReadGetStr(val);

    std::cout << "成员内容:" << res << std::endl;

---

## 

函数简介:

Json解析,获取json对象数组对象的成员个数.

函数原型:

LONG JsonReadGetArraySize(obj)

参数定义:

obj 长整数型:Json对象指针.

返回值:

整数型:

返回json数组对象的成员个数.

示例:

    str = "{\

                \"phones\" : [\

                    \"212 555-1234\",\

                    \"646 555-5678\"\

                ]\

            }";

    obj = vu.JsonReadInPut(str);

    arr = vu.JsonReadGetValObjByKey(obj, "phones");

    num = vu.JsonReadGetArraySize(arr);

    std::cout << "数组成员数:" << num << std::endl;

---

## 

函数简介:

Json解析,通过索引获取键名对象(指针)

函数原型:

LONG64 JsonReadGetKeyObj(obj, index)

参数定义:

obj 长整数型:Json对象指针.

index 整数型:要取键名的对象索引.

返回值:

长整数型:

失败返回0,成功返回键名对象指针.

示例:

    key = vu.JsonReadGetKeyObj(obj, 0);

    std::cout << "val:" << key<< std::endl;

---

## 

函数简介:

Json解析,获取json对象(键值对象)的数值内容.

函数原型:

DOUBLE JsonReadGetNum(obj)

参数定义:

obj 长整数型:Json对象指针.

返回值:

双精度浮点型:

返回键值对象中存储的数值,以双精度浮点型返回,若需要其他类型的数值可以进行强制转换(例如转为整数型).

示例:

    val = vu.JsonReadGetValObjByKey(val, "age");

    ret = vu.JsonReadGetNum(val);

    intVal = (int)ret;

---

## 

函数简介:

Json解析,获取对象尺寸.

函数原型:

LONG JsonReadGetObjSize(obj)

参数定义:

obj 长整数型:要获取尺寸的对象指针.

返回值:

整数型:

失败返回0,成功返回对象的长度(或者键值对子对象的个数).

示例:

    val = vu.JsonReadGetValObjByKey(obj, "user");

    ret = vu.JsonReadGetObjSize(val);

    std::cout << "size:" << ret << std::endl;

---

## 

函数简介:

Json解析,获取对象类型.

函数原型:

LONG JsonReadGetObjType(obj)

参数定义:

obj 长整数型:要获取类型的对象指针.

返回值:

整数型:

返回对象的类型,取值如下

0:未知类型/错误

1:字符串类型

2:数值类型

3:数组类型

4:对象的类型是一个Json对象

示例:

    val = vu.JsonReadGetValObjByKey(obj, "user");

    ret = vu.JsonReadGetObjType(val);

    std::cout << "type:" << ret << std::endl;

---

## 

函数简介:

Json解析,获取json对象(键值对象)的字符串内容.

函数原型:

string JsonReadGetStr(obj)

参数定义:

obj 长整数型:Json对象指针.

返回值:

字符串:

返回键值对象中存储的字符串内容.

示例:

    val = vu.JsonReadGetValObjByKey(val, "name");

    res = vu.JsonReadGetStr(val);

---

## 

函数简介:

Json解析,通过索引获取键值对象(指针)

函数原型:

LONG64 JsonReadGetValObjByIndex(obj,index)

参数定义:

obj 长整数型:Json对象指针.

index 整数型:要取键值的对象索引.

返回值:

长整数型:

失败返回0,成功返回键值对象指针.

示例:

    val = vu.JsonReadGetValObjByIndex(obj, 0);

    val = vu.JsonReadGetValObjByIndex(val, 1);

    std::cout << "val:" << val << std::endl;

---

## 

函数简介:

Json解析,通过键名获取键值对象(指针)

函数原型:

LONG64 JsonReadGetValObjByKey(obj,key)

参数定义:

obj 长整数型:Json对象指针.

key 字符串:要取键值的对象键名.

返回值:

长整数型:

失败返回0,成功返回键值对象指针.

示例:

    val = vu.JsonReadGetValObjByKey(obj, "user");

    val = vu.JsonReadGetValObjByKey(val, "name");

    std::cout << "val:" << val << std::endl;

---

## 

函数简介:

Json解析,读入json对象字符串内容.

函数原型:

LONG64 JsonReadInPut(str)

参数定义:

str 字符串:json数据字符串,一般为以下格式

{ "user": 
{ 
"name": "VU",
 	"age": 18 
}

}

返回值:

长整数型:

失败返回0,成功返回一个解析json的根对象指针.

示例:

    str = "{ \"user\": { \"name\": \"VU\", \"age\": 18 }";

    obj = vu.JsonReadInPut(str);

---

## 

函数简介:

Json构建,对Json构建的对象写入JSON数组对象键值数据.

函数原型:

LONG JsonWriteAddArray(pJson,key,arr)

参数定义:

pJson 长整数型:Json对象指针.

key 字符串:要写入对象的键名.

arr 长整数型:要写入对象的数组对象指针.

返回值:

整数型:

0:失败

1:成功

示例:

    obj = vu.JsonWriteCreateObj();

    arr = vu.JsonWriteCreateArray(obj);

    vu.JsonWriteArrayAddStr(arr, "文本");

    vu.JsonWriteArrayAddNum(arr, 123);

    vu.JsonWriteAddArray(obj, "array", arr);

---

## 

函数简介:

Json构建,对Json构建的对象写入数值类型的键值数据.

函数原型:

LONG JsonWriteAddNum(pJson,key,val)

参数定义:

pJson 长整数型:Json对象指针.

key 字符串:要写入对象的键名.

val 双精度浮点型:要写入对象的数值内容.

返回值:

整数型:

0:失败

1:成功

示例:

    obj = vu.JsonWriteCreateObj();

    ret = vu.JsonWriteAddNum(obj, "age", 18);

---

## 

函数简介:

Json构建,对Json构建的对象写入JSON对象(将json对象作为数据写入对象中).

函数原型:

LONG JsonWriteAddObj(pJson,key,obj)

参数定义:

pJson 长整数型:Json对象指针.

key 字符串:要写入对象的键名.

obj长整数型:要写入对象的Json对象指针.

返回值:

整数型:

0:失败

1:成功

示例:

    obj = vu.JsonWriteCreateObj();

 

    obj_son = vu.JsonWriteCreateObj();

    vu.JsonWriteAddStr(obj_son, "name", "VU");

 

    vu.JsonWriteAddObj(obj, "obj", obj_son);

---

## 

函数简介:

Json构建,对Json构建的对象写入文本类型键值数据.

函数原型:

LONG JsonWriteAddStr(pJson,key,val)

参数定义:

pJson 长整数型:Json对象指针.

key 字符串:要写入对象的键名.

val 字符串:要写入对象的文本类型键值.

返回值:

整数型:

0:失败

1:成功

示例:

    obj = vu.JsonWriteCreateObj();

    ret = vu.JsonWriteAddStr(obj, "name", "VU");

---

## 

函数简介:

Json构建,对Json构建的数组对象新增JSON数组类型数据.

函数原型:

LONG JsonWriteArrayAddArray(arr,val_arr)

参数定义:

arr 长整数型:Json数组对象指针.

val_arr 长整数型:要写入数组对象的JSON数组内容.

返回值:

返回值

示例:

obj = vu.JsonWriteCreateObj();

 

//创建一个数组对象用来存放数组数据

    arr = vu.JsonWriteCreateArray(obj);

    //再次新建一个子数组对象

    arr_son = vu.JsonWriteCreateArray(obj);

    vu.JsonWriteArrayAddNum(arr_son, 11);

    vu.JsonWriteArrayAddNum(arr_son, 22);

    vu.JsonWriteArrayAddNum(arr_son, 33);

 

    vu.JsonWriteArrayAddArray(arr, arr_son)

---

## 

函数简介:

Json构建,对Json构建的数组对象新增数值类型数据.

函数原型:

LONG JsonWriteArrayAddNum(arr,val)

参数定义:

arr 长整数型:Json数组对象指针.

val 双精度浮点型:要写入数组对象的数值类型内容.

返回值:

整数型:

0:失败

1:成功

示例:

    obj = vu.JsonWriteCreateObj();

    arr = vu.JsonWriteCreateArray(obj);

 

    vu.JsonWriteArrayAddNum(arr, 0.1);

    vu.JsonWriteArrayAddNum(arr, 1.0);

    vu.JsonWriteArrayAddNum(arr, 1234);

---

## 

函数简介:

Json构建,对Json构建的数组对象新增JSON对象类型数据.

函数原型:

LONG JsonWriteArrayAddObj(arr,obj)

参数定义:

arr 长整数型:Json数组对象指针.

obj 长整数型:要写入数组对象的JSON对象内容.

返回值:

整数型:

0:失败

1:成功

示例:

    //创建json对象

    obj = vu.JsonWriteCreateObj();

    //创建json数组

    arr = vu.JsonWriteCreateArray(obj);

    //创建json子对象

    obj_son = vu.JsonWriteCreateObj();

    //给子对象添加键值对

    vu.JsonWriteAddStr(obj_son, "name", "VU");

    //将子对象添加到数组中

    vu.JsonWriteArrayAddObj(arr, obj_son);

---

## 

函数简介:

Json构建,对Json构建的数组对象新增文本类型数据.

函数原型:

LONG JsonWriteArrayAddStr(arr,val)

参数定义:

arr 长整数型:Json数组对象指针.

val 字符串:要写入数组对象的文本类型内容.

返回值:

整数型:

0:失败

1:成功

示例:

    obj = vu.JsonWriteCreateObj();

    arr = vu.JsonWriteCreateArray(obj);

 

    vu.JsonWriteArrayAddStr(arr, "文本1");

    vu.JsonWriteArrayAddStr(arr, "文本2");

    vu.JsonWriteArrayAddStr(arr, "文本3");

---

## 

函数简介:

Json构建,清除Json构建的缓冲区,并释放Json对象.

函数原型:

LONG JsonWriteClear()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

    ret = vu.JsonWriteClear();

---

## 

函数简介:

Json构建,创建一个Json数组对象,用来写入数组数据.

函数原型:

LONG64 JsonWriteCreateArray(pJson)

参数定义:

pJson 长整数型:Json对象指针.

返回值:

长整数型:

失败返回0,成功返回一个新建的Json数组对象指针.

示例:

    obj = vu.JsonWriteCreateObj();

    arr = vu.JsonWriteCreateArray(obj);

---

## 

函数简介:

Json构建,创建一个Json对象,用来写入数据.

函数原型:

LONG64 JsonWriteCreateObj()

参数定义:

无

返回值:

长整数型:

失败返回0,成功返回一个新建的Json对象指针.

示例:

    obj = vu.JsonWriteCreateObj();

---

## 

函数简介:

Json构建,从Json构建的对象中删除指定键名的成员数据.

函数原型:

LONG JsonWriteDeleteKey(pJson,key)

参数定义:

pJson 长整数型:Json数组对象指针.

key 字符串:要删除的json成员的键名.

返回值:

整数型:

0:失败

1:成功

示例:

    //创建json对象

    obj = vu.JsonWriteCreateObj();

    //给对象添加键值对

    vu.JsonWriteAddStr(obj, "name", "VU");

    //将键值对从对象中删除

    vu.JsonWriteDeleteKey(obj, "name");

---

## 

函数简介:

Json构建,将构建好的JSON对象数据生成为字符串类型的JSON数据.

函数原型:

string JsonWriteOutPut(pJson)

参数定义:

pJson 长整数型:Json对象指针.

返回值:

字符串:

返回构建好的json对象数据内容,以字符串形式表示.

格式：

{ "user": 

{ 
"name": "VU",
 "age": 18 

}

}

示例:

    ret = vu.JsonWriteClear();

    obj = vu.JsonWriteCreateObj();

    ret = vu.JsonWriteAddStr(obj, "name", "VU");

    res = vu.JsonWriteOutPut(obj);

    std::cout << "json:" << res << std::endl;

---

## 

函数简介:

将指定长度的数据转为二进制文本字符串

函数原型:

string BytesToData(pBuf,len)

参数定义:

pBuf 长整数型:存放数据的内存地址,仅限本程序或者插件内部的内存地址

len 整数型:数据的长度

返回值:

字符串:

返回转换后的二进制数据,以字符串形式描述，比如"12 34 56 78 90 ab cd"

示例:

    res = vu.BytesToData(pBuf, len);

---

## 

函数简介:

取消无痕写入(抹除无痕并恢复原始数据)

函数原型:

LONG64 DataAddrCancelNoTrace(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

返回值:

整数型:

0:失败

1:成功

示例:

    ret = vu.DataAddrCancelNoTrace(hwnd, 0x7788666);

---

## 

函数简介:

取消无痕写入(抹除无痕并恢复原始数据)

函数原型:

LONG64 DataCancelNoTrace(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

返回值:

整数型:

0:失败

1:成功

示例:

    ret = vu.DataCancelNoTrace(hwnd,"4DA678")

;

---

## 

函数简介:

将二进制数据转为字节集数据,并返回指向转换后的数据指针.

注意:此函数会将转换后的数据存放在插件内存,在下次调用本函数时会释放内存,如果需要长久使用,请将数据拷贝到自己申请的内存中.

函数原型:

LONG64 DataToBytes(data,len)

参数定义:

data 字符串:二进制数据，以字符串形式描述，比如"12 34 56 78 90 ab cd"

len 变参指针:返回转换后数据的长度

返回值:

长整数型:

返回指向转换后的字节集数据的指针

示例:

    ret = vu.DataToBytes("12 34 56 78 90 ab cd", len);

    std::cout << "数据存放指针:" << ret << std::endl;

    std::cout << "数据长度:" << len << std::endl;

---

## 

函数简介:

双精度浮点型数据转二进制数据

函数原型:

string DoubleToData(value)

参数定义:

value 双精度浮点型:需要被转换的数据

返回值:

字符串:

返回转换后的二进制数据,以字符串形式描述，比如"AA BB CC DD EE FF 12 34"

示例:

    res = vu.DoubleToData(123.456);

---

## 

函数简介:

搜索指定的二进制数据,默认步长是1.默认开启多线程,默认搜索全部内存军类型.如果要定制搜索,请用FindDataEx

函数原型:

string FindData(hwnd, addr_range, data)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

data 字符串: 要搜索的二进制数据 以字符串的形式描述比如"00 01 23 45 67 86 ab ce f1"等. 
             这里也可以支持模糊查找,用??来代替单个字节. 比如"00 01 ?? ?? 67 86 ?? ce f1"等. 
             注意,这里不支持半个字节,比如3?这种不行.

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindData(hwnd, "00000000-FFFFFFFF", "00 01 23 45 67 86 ab ce f1");

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的二进制数据.

函数原型:

string FindDataEx(hwnd, addr_range, data,step,multi_thread,mode)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

data 字符串: 要搜索的二进制数据 以字符串的形式描述比如"00 01 23 45 67 86 ab ce f1"等
             这里也可以支持模糊查找,用??来代替单个字节. 比如"00 01 ?? ?? 67 86 ?? ce f1"等.
             注意,这里不支持半个字节,比如3?这种不行.

step 整数型: 搜索步长.

multi_thread整数型:表示是否开启多线程查找.  0不开启，1开启.
                   开启多线程查找速度较快，但会耗费较多CPU资源. 不开启速度较慢，但节省CPU.

mode 整数型: 1 表示开启快速扫描(略过只读内存)  0表示所有内存类型全部扫描.

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindDataEx(hwnd, "00000000-FFFFFFFF", "00 01 23 45 67 86 ab ce f1", 4, 1, 0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的双精度浮点数,默认步长是1.如果要定制步长，请用FindDoubleEx

函数原型:

string FindDouble(hwnd, addr_range, double_value_min, double_value_max)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

double_value_min 双精度浮点型: 搜索的双精度数值最小值

double_value_max 双精度浮点型: 搜索的双精度数值最大值 
最终搜索的数值大与等于double_value_min,并且小于等于double_value_max

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindDouble(hwnd, "00000000-FFFFFFFF", 0.5, 1.0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的双精度浮点数.

函数原型:

string FindDoubleEx(hwnd, addr_range, double_value_min, double_value_max,step,multi_thread,mode)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

double_value_min 双精度浮点型: 搜索的双精度数值最小值

double_value_max 双精度浮点型: 搜索的双精度数值最大值 

最终搜索的数值大与等于double_value_min,并且小于等于double_value_max

step 整数型: 搜索步长.

multi_thread整数型:表示是否开启多线程查找.  0不开启，1开启.
                   开启多线程查找速度较快，但会耗费较多CPU资源. 不开启速度较慢，但节省CPU.

mode 整数型: 1 表示开启快速扫描(略过只读内存)  0表示所有内存类型全部扫描.

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindDoubleEx(hwnd, "00000000-FFFFFFFF", 0.5, 1.0, 8, 1, 0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的单精度浮点数,默认步长是1.如果要定制步长，请用FindFloatEx

函数原型:

string FindFloat(hwnd, addr_range, float_value_min, float_value_max)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

float_value_min 单精度浮点型: 搜索的单精度数值最小值

float_value_max 单精度浮点型: 搜索的单精度数值最大值 
最终搜索的数值大与等于float_value_min,并且小于等于float_value_max

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindFloat(hwnd, "00000000-FFFFFFFF", 0.5, 1.0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的单精度浮点数. 

函数原型:

string FindFloatEx(hwnd, addr_range, float_value_min, float_value_max,step,multi_thread,mode)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

float_value_min 单精度浮点型: 搜索的单精度数值最小值

float_value_max 单精度浮点型: 搜索的单精度数值最大值 
最终搜索的数值大与等于float_value_min,并且小于等于float_value_max

step 整数型: 搜索步长.

multi_thread整数型:表示是否开启多线程查找.  0不开启，1开启.
                   开启多线程查找速度较快，但会耗费较多CPU资源. 不开启速度较慢，但节省CPU.

mode 整数型: 1 表示开启快速扫描(略过只读内存)  0表示所有内存类型全部扫描.

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindFloatEx(hwnd, "00000000-FFFFFFFF", 0.5, 1.0, 4, 1, 0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的整数,默认步长是1.如果要定制步长，请用FindIntEx

函数原型:

string FindInt(hwnd, addr_range, int_value_min, int_value_max,type)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

int_value_min 长整数型: 搜索的整数数值最小值

int_value_max 长整数型: 搜索的整数数值最大值 
最终搜索的数值大与等于int_value_min,并且小于等于int_value_max

type 整数型: 搜索的整数类型,取值如下

      0 : 32位

      1 : 16 位

      2 : 8位

      3 : 64位

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindInt(hwnd, "00000000-FFFFFFFF", 300, 300, 0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的整数.

函数原型:

string FindIntEx(hwnd, addr_range, int_value_min, int_value_max,type,step,multi_thread,mode)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

int_value_min 长整数型: 搜索的整数数值最小值

int_value_max 长整数型: 搜索的整数数值最大值 
最终搜索的数值大与等于int_value_min,并且小于等于int_value_max

type 整数型: 搜索的整数类型,取值如下

      0 : 32位

      1 : 16 位

      2 : 8位

      3 : 64位

step 整数型: 搜索步长.

multi_thread整数型:表示是否开启多线程查找.  0不开启，1开启.
                   开启多线程查找速度较快，但会耗费较多CPU资源. 不开启速度较慢，但节省CPU.

mode 整数型: 1 表示开启快速扫描(略过只读内存)  0表示所有内存类型全部扫描.

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindIntEx(hwnd, "00000000-FFFFFFFF", 300, 300, 0, 2, 1, 0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的字符串,默认步长是1.如果要定制步长，请用FindStringEx

函数原型:

string FindString(hwnd, addr_range, string_value,type)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

string_value 字符串: 搜索的字符串

type 整数型: 搜索的字符串类型,取值如下

      0 : Ascii字符串

      1 : Unicode字符串

      2 : UTF8字符串

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindString(hwnd, "00000000-FFFFFFFF", "哈哈哈哈", 0);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

搜索指定的字符串.

函数原型:

string FindStringEx(hwnd, addr_range, string_value,type,step,multi_thread,mode)

参数定义:

hwnd 整数型: 指定搜索的窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr_range 字符串: 指定搜索的地址集合，字符串类型，这个地方可以是上次FindXXX的返回地址集合,可以进行二次搜索.(类似CE的再次扫描)

             如果要进行地址范围搜索，那么这个值为的形如如下(类似于CE的新搜索)

				"00400000-7FFFFFFF" "80000000-BFFFFFFF" "00000000-FFFFFFFF" 等.

string_value 字符串: 搜索的字符串

type 整数型: 搜索的字符串类型,取值如下

      0 : Ascii字符串

      1 : Unicode字符串

      2 : UTF8字符串

step 整数型: 搜索步长.

multi_thread整数型:表示是否开启多线程查找.  0不开启，1开启.
                   开启多线程查找速度较快，但会耗费较多CPU资源. 不开启速度较慢，但节省CPU.

mode 整数型: 1 表示开启快速扫描(略过只读内存)  0表示所有内存类型全部扫描.

返回值:

字符串:
返回搜索到的地址集合，地址格式如下:

"addr1|addr2|addr3…|addrn"

比如"400050|423435|453430"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

    res = vu.FindStringEx(hwnd, "00000000-FFFFFFFF", "哈哈哈哈", 0, 2, 1, 1);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "找到的地址:" << res << std::endl;

    }

---

## 

函数简介:

浮点型数据转二进制数据

函数原型:

string FloatToData(value)

参数定义:

value 单精度浮点型:需要被转换的数据

返回值:

字符串:

返回转换后的二进制数据,以字符串形式描述，比如"AA BB CC DD EE FF 12 34"

示例:

    res = vu.FloatToData(123.456);

---

## 

函数简介:

根据指定的窗口句柄，来获取对应窗口句柄进程下的指定模块的基址

函数原型:

LONGLONG GetModuleBaseAddr(hwnd,module)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

module 字符串: 模块名

返回值:

长整数型:
模块的基址

示例:

    base_addr = vu.GetModuleBaseAddr(hWnd, "gdi32.dll");

    std::cout << "模块基址:" << base_addr << std::endl;

---

## 

函数简介:

根据指定的窗口句柄，来获取对应窗口句柄进程下的指定模块的大小

函数原型:

long GetModuleSize(hwnd,module)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

module 字符串: 模块名

返回值:

整数型:
模块的大小

示例:

    module_size = vu.GetModuleSize(hWnd, "gdi32.dll");

    std::cout << "模块大小:" << module_size << std::endl;

---

## 

函数简介:

根据指定的目标模块地址,获取目标窗口(进程)内的导出函数地址.

函数原型:

LONGLONG GetRemoteApiAddress(hwnd,base_addr,fun_name)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

base_addr 长整数型: 目标模块地址,比如user32.dll的地址,可以通过GetModuleBaseAddr来获取.

fun_addr字符串: 需要获取的导出函数名.  比如"SetWindowTextA".

返回值:

长整数型:
获取的地址. 如果失败返回0

示例:

    //此例子用来在目标进程内执行SetWindowTextA来更改窗口标题.

    hwnd = vu.GetMousePointWindow();

    user32_base = vu.GetModuleBaseAddr(hwnd, "user32.dll");

    SetWindowTextA_addr = vu.GetRemoteApiAddress(hwnd, user32_base, "SetWindowTextA");

 

    addr = vu.VirtualAllocEx(hwnd, 0, 50, 0);

    vu.WriteStringAddr( hwnd, addr, 0, "哈哈");

 

 

    char asm_ins[300] = { 0 };

 

    isX64 = vu.ProcessIsX64(hwnd);

    // 64位和32位的汇编代码不同

    if (isX64 != 1)

    {

        vu.AsmClear();

        sprintf(asm_ins, "mov eax,%s", vu.StrNumConvert(addr, 16));

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "push eax");

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "mov eax,%s", vu.StrNumConvert(hwnd, 16));

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "push eax");

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "call %s", vu.StrNumConvert(SetWindowTextA_addr, 16));

        vu.AsmAdd(asm_ins);

 

    }

    else

    {

        vu.AsmClear();

        sprintf(asm_ins, "mov rdx,%s", vu.StrNumConvert(hwnd, 16));

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "mov rcx,%s", vu.StrNumConvert(addr, 16));

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "mov rax,%s", vu.StrNumConvert(SetWindowTextA_addr, 16));

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "sub rsp,28");

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "call rax");

        vu.AsmAdd(asm_ins);

        sprintf(asm_ins, "add rsp,28");

        vu.AsmAdd(asm_ins);

    }

 

    vu.AsmCall(hWnd, 1);

    vu.VirtualFreeEx(hwnd, addr);

---

## 

函数简介:

创建一个钩子(HOOK),使得目标程序在执行到钩子位置时会跳转到目标地址执行代码.

注意:调用此函数仅仅是生成一个HOOK代码,功能并未生效!!!

若想使HOOK生效,还需要调用HookStartAddr或者HookStart才可以.

原因是有些HOOK代码需要执行原始代码,正常情况下HOOK后原始的代码将不会再被执行,所以需要首先创建一个HOOK代码,并将原始代码写入到HOOK代码中,这样在执行HOOK时,才会执行原始代码.

函数原型:

LONG64 HookCreate(hwnd,addrFrom,addrTo)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addrFrom 字符串:目标代码地址,可以是任意代码段位置,可以是函数头,中,尾部,当程序执行到此位置时,会跳转到addrTo传递的地址处.

addrTo 字符串:目的代码地址,可以是程序本身的代码段位置,也可以是我们申请的代码段位置(必须确保此处内存空间为可执行内存.)

返回值:

长整数型:

失败返回0,成功返回一个新的代码段地址,此地址是原始的addrFrom 代码段地址拷贝,因为我们HOOK启动之后,程序是无法在执行原始代码了,如果需要执行原始代码,只能调用此处的返回值(原始代码的拷贝地址)了.

示例:

    original = vu.HookCreate(hwnd, "0x12345678", "0x87654321");

    vu.HookStart(hwnd, "0x12345678", 0);

 

    //也可以和汇编混用

    vu.AsmClear();

    vu.AsmAdd("mov eax,1");

    vu.AsmAdd("push 0123456");

    vu.AsmAdd("call 0343434");

ret = vu.AsmMemAlloc(hWnd, addr, size);

 

    original = vu.HookCreate(hwnd, "0x12345678", vu.StrNumConvert(addr, 16));

    vu.HookStart(hwnd, "0x12345678", 0);

 

 

    //注意如果HOOK未停止时不可以释放汇编写入的内存,否则程序会崩溃

    //所以需要先停止HOOK再释放汇编内存

    vu.HookStop(hwnd, "0x12345678");

    ret = vu.AsmMemFree(hWnd, addr);

 

 

    //或者可以在HOOK中调用原始函数

    addr = vu.VirtualAllocEx(hwnd, 0, 200, 0);

    original = vu.HookCreate(hwnd, "0x12345678", vu.StrNumConvert(addr, 16));

    vu.AsmClear();

    vu.AsmAdd("mov eax,1");

    vu.AsmAdd("push 0123456");

    std::string call = "call ";

    call += vu.StrNumConvert(original, 16);

    vu.AsmAdd(call.c_str());//组成类似于 "call original"的字符串

    data = vu.Assemble(0, 0);

    //将汇编代码写入我们申请的内存中

    vu.WriteDataAddr(hwnd, addr, data);

    //启动hook

    vu.HookStart(hwnd, "0x12345678", 0);

---

## 

函数简介:

创建一个钩子(HOOK),使得目标程序在执行到钩子位置时会跳转到目标地址执行代码.

注意:调用此函数仅仅是生成一个HOOK代码,功能并未生效!!!

若想使HOOK生效,还需要调用HookStartAddr或者HookStart才可以.

原因是有些HOOK代码需要执行原始代码,正常情况下HOOK后原始的代码将不会再被执行,所以需要首先创建一个HOOK代码,并将原始代码写入到HOOK代码中,这样在执行HOOK时,才会执行原始代码.

函数原型:

LONG64 HookCreateAddr(hwnd,addrFrom,addrTo)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addrFrom 长整数型:目标代码地址,可以是任意代码段位置,可以是函数头,中,尾部,当程序执行到此位置时,会跳转到addrTo传递的地址处.

addrTo 长整数型:目的代码地址,可以是程序本身的代码段位置,也可以是我们申请的代码段位置(必须确保此处内存空间为可执行内存.)

返回值:

长整数型:

失败返回0,成功返回一个新的代码段地址,此地址是原始的addrFrom 代码段地址拷贝,因为我们HOOK启动之后,程序是无法在执行原始代码了,如果需要执行原始代码,只能调用此处的返回值(原始代码的拷贝地址)了.

示例:

    original = vu.HookCreateAddr(hwnd, 0x12345678, 0x87654321);

    vu.HookStartAddr(hwnd, 0x12345678, 0);

 

    //也可以和汇编混用

    vu.AsmClear();

    vu.AsmAdd("mov eax,1");

    vu.AsmAdd("push 0123456");

    vu.AsmAdd("call 0343434");

    ret = vu.AsmMemAlloc(hWnd, addr, size);

    original = vu.HookCreateAddr(hwnd, 0x12345678, addr);

    vu.HookStartAddr(hwnd, 0x12345678, 0);

    

//注意如果HOOK未停止时不可以释放汇编写入的内存,否则程序会崩溃

    //所以需要先停止HOOK再释放汇编内存

    vu.HookStopAddr(hwnd, 0x12345678);

    ret = vu.AsmMemFree(hWnd, addr);

 

 

    //或者可以在HOOK中调用原始函数

    addr = vu.VirtualAllocEx(hwnd, 0, 200, 0);

    original = vu.HookCreateAddr(hwnd, 0x12345678, addr);

    vu.AsmClear();

    vu.AsmAdd("mov eax,1");

    vu.AsmAdd("push 0123456");

    std::string call = "call ";

    call += vu.StrNumConvert(original, 16);

    vu.AsmAdd(call.c_str());//组成类似于 "call original"的字符串

    data = vu.Assemble(0, 0);

    //将汇编代码写入我们申请的内存中

    vu.WriteDataAddr(hwnd, addr, data);

    //启动hook

    vu.HookStartAddr(hwnd, 0x12345678, 0);

---

## 

函数简介:

启动创建的钩子(HOOK)功能,调用本函数前必须先使用HookCreateAddr或HookCreate进行创建,否则不会生效.

函数原型:

LONG64 HookStart(hwnd, addrFrom,isNoTrace)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addrFrom 字符串:目标代码地址,必须和创建时填写的参数保持一致,否则将会失败.

isNoTrace 整数型:是否无痕hook.如果使用无痕功能需要支持vt,无痕hook之后原始代码只有在执行时才会发生改变,读取时保持不变,可以完美过CRC检测(需要在BindWindowEx()时,public参数具有public.memory.drv属性).

取值:

0:不使用无痕HOOK

1:使用无痕HOOK

返回值:

长整数型:

0:失败

1:成功

示例:

    original = vu.HookCreate(hwnd, "0x12345678", "0x87654321");

    vu.HookStart(hwnd, "0x12345678", 0);

---

## 

函数简介:

启动创建的钩子(HOOK)功能,调用本函数前必须先使用HookCreateAddr或HookCreate进行创建,否则不会生效.

函数原型:

LONG64 HookStartAddr(hwnd, addrFrom,isNoTrace)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addrFrom 长整数型:目标代码地址,必须和创建时填写的参数保持一致,否则将会失败.

isNoTrace 整数型:是否无痕hook.如果使用无痕功能需要支持vt,无痕hook之后原始代码只有在执行时才会发生改变,读取时保持不变,可以完美过CRC检测(需要在BindWindowEx()时,public参数具有public.memory.drv属性).

取值:

0:不使用无痕HOOK

1:使用无痕HOOK

返回值:

长整数型:

0:失败

1:成功

示例:

    original = vu.HookCreateAddr(hwnd, 0x12345678, 0x87654321);

    vu.HookStartAddr(hwnd, 0x12345678, 0);

---

## 

函数简介:

停止指定地址的HOOK执行.

函数原型:

LONG64 HookStop(hwnd,addrFrom)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addrFrom 字符串:目标代码地址,必须和创建时填写的参数保持一致,否则将会失败.

返回值:

长整数型:

0:失败

1:成功

示例:

    original = vu.HookCreate(hwnd, "0x12345678", "0x87654321");

    vu.HookStart(hwnd, "0x12345678", 0);

//需要停止时才调用

    vu.HookStop(hwnd, "0x12345678");

---

## 

函数简介:

停止指定地址的HOOK执行.

函数原型:

LONG64 HookStopAddr(hwnd,addrFrom)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addrFrom 长整数型:目标代码地址,必须和创建时填写的参数保持一致,否则将会失败.

返回值:

长整数型:

0:失败

1:成功

示例:

    original = vu.HookCreateAddr(hwnd, 0x12345678, 0x87654321);

vu.HookStartAddr(hwnd, 0x12345678, 0);

//需要停止时才调用

    vu.HookStopAddr(hwnd, 0x12345678);

---

## 

函数简介:

在目标程序中注入可执行程序或dll

函数原型:

LONG64 InjectFile(hwnd,file)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

file 字符串:文件路径

返回值:

长整数型:

0:失败

1:成功

示例:

    ret = vu.InjectFile(hwnd, "c:\\test.dll");

    std::cout << "注入结果:" << res << std::endl;

---

## 

函数简介:

在目标程序中注入可执行程序或dll

函数原型:

LONG64 InjectFileData(hwnd,file_data,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

file_data 长整数型:可执行文件exe或者dll的存放内存地址

len 长整数型:可执行文件的数据大小

返回值:

长整数型:

0:失败

1:成功

示例:

    data = vu.ReadFileData("c:\\test.dll", size);

    ret = vu.InjectFileData(hwnd, data, size);

    std::cout << "注入结果:" << res << std::endl;

---

## 

函数简介:

整数型数据转二进制数据

函数原型:

string IntToData(value)

参数定义:

value 整数型:需要被转换的数据

返回值:

字符串:

返回转换后的二进制数据,以字符串形式描述，比如"AA BB CC DD EE FF 12 34"

示例:

    res = vu.IntToData(123456);

---

## 

函数简介:

读取指定地址的二进制数据

函数原型:

string ReadData(hwnd,addr,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

len 整数型: 二进制数据的长度

返回值:

字符串:
读取到的数值,以16进制表示的字符串 每个字节以空格相隔 比如"12 34 56 78 ab cd ef"

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadData(hwnd,"4DA678",10)

---

## 

函数简介:

读取指定地址的二进制数据

函数原型:

string ReadDataAddr(hwnd,addr,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

len 整数型: 二进制数据的长度

返回值:

字符串:
读取到的数值,以16进制表示的字符串 每个字节以空格相隔 比如"12 34 56 78 ab cd ef"
如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadDataAddr(hwnd,123456,10)

---

## 

函数简介:

读取指定地址的二进制数据,只不过返回的是内存地址,而不是字符串.适合高级用户

函数原型:

long ReadDataAddrToBin(hwnd,addr,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

len 整数型: 二进制数据的长度

返回值:

整数型:
读取到的数据指针. 返回0表示读取失败.

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadDataAddrToBin(hwnd,12341234 ,10);

 

注:调用此接口获取的数据指针保存在当前对象中,到下次调用此接口时,内部就会释放.
哪怕是转成字节集,这个地址也还是在此字节集中使用. 如果您要此地址一直有效，那么您需要自己拷贝字节集到自己的字节集中.

---

## 

函数简介:

读取指定地址的二进制数据,只不过返回的是内存地址,而不是字符串.

函数原型:

long ReadDataToBin(hwnd,addr,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

len 整数型: 二进制数据的长度

返回值:

整数型:
读取到的数据指针. 返回0表示读取失败.

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadDataToBin(hwnd,"4DA678",10)

---

## 

函数简介:

读取指定地址的双精度浮点数

函数原型:

double ReadDouble(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

返回值:

双精度浮点型:
读取到的数值 

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadDouble(hwnd,"4DA678")

---

## 

函数简介:

读取指定地址的双精度浮点数

函数原型:

double ReadDoubleAddr(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

返回值:

双精度浮点型:
读取到的数值 

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadDoubleAddr(hwnd,123456)

---

## 

函数简介:

读取指定地址的单精度浮点数

函数原型:

float ReadFloat(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

返回值:

单精度浮点型:
读取到的数值 

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadFloat(hwnd,"4DA678")

---

## 

函数简介:

读取指定地址的单精度浮点数

函数原型:

float ReadFloatAddr(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 长整数型: 地址

返回值:

单精度浮点型:
读取到的数值

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadFloatAddr(hwnd,123456)

---

## 

函数简介:

读取指定地址的整数数值，类型可以是8位，16位  32位 或者64位

函数原型:

LONGLONG ReadInt(hwnd,addr,type)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

type 整数型: 整数类型,取值如下

      0 : 32位有符号

      1 : 16 位有符号

      2 : 8位有符号

      3 : 64位

      4 : 32位无符号

      5 : 16位无符号

      6 : 8位无符号

返回值:

长整数型:
读取到的数值

如果要想知道函数是否执行成功，请查看GetLastError函数. 

示例:

value = vu.ReadInt(hwnd,"4DA678",0)

---

## 

函数简介:

读取指定地址的整数数值，类型可以是8位，16位 32位 或者64位

函数原型:

LONGLONG ReadIntAddr(hwnd,addr,type)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

type 整数型: 整数类型,取值如下

      0 : 32位

      1 : 16 位

      2 : 8位

	   3 : 64位

      4 : 32位无符号

      5 : 16位无符号

      6 : 8位无符号

返回值:

长整数型:
读取到的数值

如果要想知道函数是否执行成功，请查看GetLastError函数. 

示例:

value = vu.ReadIntAddr(hwnd,123456 ,0)

---

## 

函数简介:

读取指定地址的字符串，可以是GBK字符串或者是Unicode字符串.(必须事先知道内存区的字符串编码方式)

函数原型:

string ReadString(hwnd,addr,type,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

type 整数型: 字符串类型,取值如下

      0 : GBK字符串

	   1 : Unicode字符串

      2 : UTF8字符串

len 整数型: 需要读取的字节数目.如果为0，则自动判定字符串长度.

返回值:

字符串:
读取到的字符串

如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

value = vu.ReadString(hwnd,"4DA678",0,0)

---

## 

函数简介:

读取指定地址的字符串，可以是GBK字符串或者是Unicode字符串.(必须事先知道内存区的字符串编码方式)

函数原型:

string ReadStringAddr(hwnd,addr,type,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

type 整数型: 字符串类型,取值如下

      0 : GBK字符串

	   1 : Unicode字符串

      2 : UTF8字符串

len 整数型: 需要读取的字节数目.如果为0，则自动判定字符串长度.

返回值:

字符串:
读取到的字符串

如果要想知道函数是否执行成功，请查看GetLastError函数. 

示例:

value = vu.ReadStringAddr(hwnd,123456 ,0,0)

---

## 

函数简介:

设置是否把所有内存接口函数中的窗口句柄当作进程ID,以支持直接以进程ID来使用内存接口

函数原型:

long SetMemoryHwndAsProcessId(en)

参数定义:

en 整数型: 取值如下
	         0 : 关闭  1 : 开启

返回值:

整数型:
0 : 失败
1 : 成功

示例:

vu.SetMemoryHwndAsProcessId(1)

注: 默认是当作窗口句柄

---

## 

函数简介:

字符串数据转二进制数据

函数原型:

string StringToData(value)

参数定义:

value 字符串:需要被转换的数据

返回值:

字符串:

返回转换后的二进制数据,以字符串形式描述，比如"AA BB CC DD EE FF 12 34"

示例:

    res = vu.StringToData("我是字符串");

---

## 

函数简介:

在指定的窗口所在进程分配一段内存

函数原型:

LONGLONG VirtualAllocEx(hwnd,addr,size,type)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 长整数型: 预期的分配地址。 如果是0表示自动分配，否则就尝试在此地址上分配内存.

size 整数型: 需要分配的内存大小.

type 整数型: 需要分配的内存类型，取值如下:
             0 : 可读可写可执行
             1 : 可读可执行，不可写
             2 : 可读可写,不可执行

返回值:

长整数型:
分配的内存地址，如果是0表示分配失败

示例:

    addr = vu.VirtualAllocEx(hwnd, 0, 50, 0);

    vu.WriteString(hwnd, vu.StrNumConvert(SetWindowTextA_addr, 16), 0, "哈哈");

    vu.VirtualFreeEx(hwnd, addr);

注:用此函数分配的内存，必须用VirtualFreeEx来释放,以免目标进程内存泄漏.

---

## 

函数简介:

释放用VirtualAllocEx分配的内存

函数原型:

long VirtualFreeEx(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: VirtualAllocEx返回的地址

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    addr = vu.VirtualAllocEx(hwnd, 0, 50, 0);

    vu.WriteString(hwnd, vu.StrNumConvert(SetWindowTextA_addr, 16), 0, "哈哈");

vu.VirtualFreeEx(hwnd, addr);

注:用此函数分配的内存，必须用VirtualFreeEx来释放,以免目标进程内存泄漏.

---

## 

函数简介:

修改指定的窗口所在进程的地址的读写属性,修改为可读可写可执行.

函数原型:

long VirtualProtectEx(hwnd,addr,size,type,new_protect)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 长整数型: 需要修改的地址

size 整数型: 需要修改的地址大小.

type 整数型: 修改的地址读写属性类型，取值如下:
             0 : 可读可写可执行,此时new_protect参数无效
             1 : 修改为new_protect指定的读写属性
new_protect整数型: 指定的读写属性

返回值:

整数型:
0 : 失败
1 : 修改之前的读写属性

示例:

    old_protect = vu.VirtualProtectEx(hwnd, 0x400000, 5, 0, 0);

    if (old_protect != 0)

    {

        vu.AsmClear();

        vu.AsmAdd("lea eax,[400000]");

        vu.AsmAdd("mov dword ptr[eax],0");

        vu.AsmCall(hWnd, 1);

        vu.VirtualProtectEx(hwnd, 0x400000, 5, 1, old_protect);

    }

---

## 

函数简介:

获取指定窗口，指定地址的内存属性.

函数原型:

string VirtualQueryEx(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 长整数型: 需要查询的地址

返回值:

字符串:
查询的结果以字符串形式.  内容是"BaseAddress,AllocationBase,AllocationProtect,RegionSize,State,Protect,Type"
数值都是10进制表达.

示例:

    res = vu.VirtualQueryEx(hwnd, 0x400000);

    //解析结果

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    if (ret >= 7)

    {

        BaseAddress = vs.StrToNum(vs.StrSplitGet(0), 10);

        AllocationBase = vs.StrToNum(vs.StrSplitGet(1), 10);

        AllocationProtect = vs.StrToNum(vs.StrSplitGet(2), 10);

        RegionSize = vs.StrToNum(vs.StrSplitGet(3), 10);

        State = vs.StrToNum(vs.StrSplitGet(4), 10);

        Protect = vs.StrToNum(vs.StrSplitGet(5), 10);

        Type = vs.StrToNum(vs.StrSplitGet(6), 10);

    }

---

## 

函数简介:

对指定地址写入二进制数据

函数原型:

long WriteData(hwnd,addr,data)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

data 字符串: 二进制数据，以字符串形式描述，比如"12 34 56 78 90 ab cd"

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteData(hwnd,"4DA678","12 34 56 78 90 ab cd")

---

## 

函数简介:

对指定地址写入二进制数据

函数原型:

long WriteDataAddr(hwnd,addr,data)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

data 字符串: 二进制数据，以字符串形式描述，比如"12 34 56 78 90 ab cd"

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDataAddr(hwnd,123456 ,"12 34 56 78 90 ab cd")

---

## 

函数简介:

对指定地址写入二进制数据,只不过直接从数据指针获取数据写入,不通过字符串

函数原型:

long WriteDataAddrFromBin(hwnd,addr,data,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

data 整数型: 数据指针
len  整数型: 数据长度

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDataAddrFromBin(hwnd,2934793257239,1231234,10)

---

## 

函数简介:

无痕写入

对指定地址写入二进制数据,只不过直接从数据指针获取数据写入,不通过字符串

注意:无痕写入针对的是执行内存,当程序执行到此内存地址的代码时,则会执行无痕写入的代码数据,而非原本的代码,正常情况下读取内存时不会发生变换,仅限执行!!!可以完美过CRC检测,使用本功能需要支持VT.

 

需要在BindWindowEx()时,public参数具有public.memory.drv属性,并且成功加载驱动,否则无痕无效.

函数原型:

long WriteDataAddrFromBinNoTrace(hwnd,addr,data,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

data 整数型: 数据指针
len  整数型: 数据长度

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDataAddrFromBinNoTrace(hwnd,2934793257239,1231234,10)

---

## 

函数简介:

无痕写入

对指定地址写入二进制数据

注意:无痕写入针对的是执行内存,当程序执行到此内存地址的代码时,则会执行无痕写入的代码数据,而非原本的代码,正常情况下读取内存时不会发生变换,仅限执行!!!可以完美过CRC检测,使用本功能需要支持VT.

 

需要在BindWindowEx()时,public参数具有public.memory.drv属性,并且成功加载驱动,否则无痕无效.

函数原型:

long WriteDataAddrNoTrace(hwnd,addr,data)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

data 字符串: 二进制数据，以字符串形式描述，比如"12 34 56 78 90 ab cd"

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDataAddrNoTrace(hwnd,123456 ,"12 34 56 78 90 ab cd")

---

## 

函数简介:

对指定地址写入二进制数据,只不过直接从数据指针获取数据写入,不通过字符串

函数原型:

long WriteDataFromBin(hwnd,addr,data,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

data 整数型: 数据指针
len  整数型: 数据长度

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDataFromBin(hwnd,"4DA678",1231234,10)

---

## 

函数简介:

无痕写入

对指定地址写入二进制数据,只不过直接从数据指针获取数据写入,不通过字符串

注意:无痕写入针对的是执行内存,当程序执行到此内存地址的代码时,则会执行无痕写入的代码数据,而非原本的代码,正常情况下读取内存时不会发生变换,仅限执行!!!可以完美过CRC检测,使用本功能需要支持VT.

 

需要在BindWindowEx()时,public参数具有public.memory.drv属性,并且成功加载驱动,否则无痕无效.

函数原型:

long WriteDataFromBinNoTrace(hwnd,addr,data,len)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

data 整数型: 数据指针
len  整数型: 数据长度

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDataFromBinNoTrace(hwnd,"4DA678",1231234,10)

---

## 

函数简介:

无痕写入

对指定地址写入二进制数据

注意:无痕写入针对的是执行内存,当程序执行到此内存地址的代码时,则会执行无痕写入的代码数据,而非原本的代码,正常情况下读取内存时不会发生变换,仅限执行!!!可以完美过CRC检测,使用本功能需要支持VT.

 

需要在BindWindowEx()时,public参数具有public.memory.drv属性,并且成功加载驱动,否则无痕无效.

函数原型:

long WriteDataNoTrace(hwnd,addr,data)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

data 字符串: 二进制数据，以字符串形式描述，比如"12 34 56 78 90 ab cd"

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDataNoTrace(hwnd,"4DA678","12 34 56 78 90 ab cd")

---

## 

函数简介:

对指定地址写入双精度浮点数

函数原型:

long WriteDouble(hwnd,addr,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

v 双精度浮点型: 双精度浮点数

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDouble(hwnd,"4DA678",2.34)

---

## 

函数简介:

对指定地址写入双精度浮点数

函数原型:

long WriteDoubleAddr(hwnd,addr,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

v 双精度浮点型: 双精度浮点数

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteDoubleAddr(hwnd,123456 ,2.34)

---

## 

函数简介:

对指定地址写入单精度浮点数

函数原型:

long WriteFloat(hwnd,addr,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

v 单精度浮点型: 单精度浮点数

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteFloat(hwnd,"4DA678",2.34)

---

## 

函数简介:

对指定地址写入单精度浮点数

函数原型:

long WriteFloatAddr(hwnd,addr,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

v 单精度浮点型: 单精度浮点数

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteFloatAddr(hwnd,123456 ,2.34)

---

## 

函数简介:

对指定地址写入整数数值，类型可以是8位，16位 32位 或者64位

函数原型:

long WriteInt(hwnd,addr,type,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

type 整数型: 整数类型,取值如下

      0 : 32位

      1 : 16 位

      2 : 8位

      3 : 64位

v 长整数型: 整形数值

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteInt(hwnd,"4DA678",0,100)

---

## 

函数简介:

对指定地址写入整数数值，类型可以是8位，16位 32位 或者64位

函数原型:

long WriteIntAddr(hwnd,addr,type,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

type 整数型: 整数类型,取值如下

      0 : 32位

      1 : 16 位

      2 : 8位

      3 : 64位

v 长整数型: 整形数值

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.WriteIntAddr(hwnd,123456,0,100)

---

## 

函数简介:

对指定地址写入字符串，可以是Ascii字符串或者是Unicode字符串

函数原型:

long WriteString(hwnd,addr,type,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr 字符串: 用字符串来描述地址，类似于CE的地址描述，数值必须是16进制,里面可以用[ ] + -这些符号来描述一个地址。+表示地址加，-表示地址减
       模块名必须用<>符号来圈起来

		例如:

"4DA678" 最简单的方式，用绝对数值来表示地址

"<360SE.exe>+DA678" 相对简单的方式，只是这里用模块名来决定模块基址，后面的是偏移

"[4DA678]+3A" 用绝对数值加偏移，相当于一级指针

"[<360SE.exe>+DA678]+3A" 用模块定基址的方式，也是一级指针

"[[[<360SE.exe>+DA678]+3A]+5B]+8" 这个是一个三级指针

总之熟悉CE的人 应该对这个地址描述都很熟悉,我就不多举例了

type 整数型: 字符串类型,取值如下

      0 : Ascii字符串

	   1 : Unicode字符串

      2 : UTF8字符串

v 字符串: 字符串

返回值:

整数型:
0: 失败

1: 成功

示例:

ret = vu.WriteString(hwnd,"4DA678",0,"我是来测试的")

---

## 

函数简介:

对指定地址写入字符串，可以是Ascii字符串或者是Unicode字符串

函数原型:

long WriteStringAddr(hwnd,addr,type,v)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

addr长整数型: 地址

type 整数型: 字符串类型,取值如下

      0 : Ascii字符串

	   1 : Unicode字符串

      2 : UTF8字符串

v 字符串: 字符串

返回值:

整数型:
0: 失败

1: 成功

示例:

ret = vu.WriteStringAddr(hwnd,123456 ,0,"我是来测试的")

---

## 

函数简介:

绑定指定的窗口,并指定这个窗口的屏幕颜色获取方式,鼠标仿真模式,键盘仿真模式.

函数原型:

LONG BindWindowEx(hwnd,display,mouse,keypad,public,mode)

参数定义:

hwnd 整数型: 指定的窗口句柄
display 字符串: 屏幕颜色获取方式 取值有以下几种

"normal" : 正常模式,平常我们用的前台截屏模式

"gdi" : gdi模式,用于窗口采用GDI方式刷新时. 

"dx" : dx模式,此模式兼容性较强.
mouse 字符串: 鼠标仿真模式 取值有以下几种

"normal" : 正常模式,平常我们用的前台鼠标模式

"windows": Windows模式,采取模拟windows消息方式 ,可以支持有多个子窗口的窗口后台

dx模式,取值可以是以下任意组合. 组合采用"|"符号进行连接.

1. "dx.state"  此模式表示锁定鼠标输入状态.

2. "dx.raw" 有些窗口需要这个才可以正常操作鼠标. 

3. "dx.input"  此模式表示锁定鼠标输入接口.

4. "dx.position"  此模式表示锁定鼠标位置.

5. "dx.focus" 此模式表示锁定鼠标输入焦点.
keypad 字符串: 键盘仿真模式 取值有以下几种

"normal" : 正常模式,平常我们用的前台键盘模式

"windows": Windows模式,采取模拟windows消息方式 同按键的后台插件.

dx模式,取值可以是以下任意组合. 组合采用"|"符号进行连接.

1. "dx.state"  此模式表示锁定键盘输入状态.
2. "dx.raw" 有些窗口需要这个才可以正常操作键盘. 

3. "dx.input"  此模式表示锁定键盘输入接口.

public 字符串: 公共属性 dx模式共有 

1."public.hide.dll" 此模式将会隐藏目标进程的vu插件，避免被检测...

2."public.memory.drv" 本对象的所有内存相关操作将会以内核方式执行.将会加载驱动. 

mode 整数型: 模式。取值有以下几种

0:强烈推荐使用此模式，后台效果是最好的.

1:使用驱动级后台键盘和鼠标.

2:同模式1,将会强制使用VT模式的后台键盘鼠标,仅限intel处理器的用户.

 

返回值:

整数型:
0: 失败
1: 成功

2:伪绑定成功.

(当后台键鼠中有"dx.raw"这个属性,但是目标窗口却不支持时,将会自动匹配最合适的绑定方案,此时绑定成功后便是伪绑定,可能与原本设置的绑定参数不相同.)

如果返回0，可以调用GetLastError来查看具体失败错误码,帮助分析问题.

示例:

ret=vu.BindWindowEx(hwnd, "normal", "normal", "normal", "", 0);

ret=vu.BindWindowEx(hwnd, "normal", "dx", "windows", "", 0);

ret=vu.BindWindowEx(hwnd, "dx", "dx", "dx", "", 0);

ret=vu.BindWindowEx(hwnd,"dx","dx.state|dx.raw|dx.input|dx.position|dx.focus","dx.state|dx.raw|dx.input","public.hide.dll",0);

 

// 下面方式将会使用完全形态的驱动级后台键鼠以及内存操作

ret=vu.BindWindowEx(hwnd,"dx","dx.state|dx.raw|dx.input|dx.position|dx.focus","dx.state|dx.raw|dx.input","public.memory.drv",1);

注意:

绑定之后,所有的坐标都相对于窗口的客户区坐标(不包含窗口边框)
另外,绑定窗口后,如果脚本任务结束,必须加以下代码,以保证所有资源正常释放(解除绑定)

ret = vu.UnBindWindow()

另外 绑定dx会比较耗时间,请不要频繁调用此函数.

还有一点特别要注意的是,有些窗口绑定之后必须加一定的延时,否则后台也无效.一般1秒到2秒的延时就足够.

---

## 

函数简介:

获取当前对象已经绑定的窗口句柄. 无绑定返回0

函数原型:

LONG GetBindWindow()

参数定义:

无

返回值:

整数型: 窗口句柄 

示例:

bind_hwnd = vu.GetBindWindow();

---

## 

函数简介:

判定指定窗口是否已经被后台绑定. (前台无法判定) 

函数原型:

long IsBind(hwnd)

参数定义:

hwnd 整数型: 窗口句柄

返回值:

整数型:

0: 没绑定,或者窗口不存在.

1: 已经绑定.

示例:

dm_ret = vu.IsBind(hwnd)

---

## 

函数简介:

禁止外部输入到指定窗口

函数原型:

long LockInput(lock)

参数定义:

lock 整数型: 0关闭锁定
       1 开启锁定(键盘鼠标都锁定)
       2 只锁定鼠标
       3 只锁定键盘

返回值:

整数型:
0: 失败
1: 成功

示例:

// 绑定为后台

ret = vu.BindWindowEx(hwnd, "dx", "dx", "dx", "", 0);

vu.LockInput(1);

//这里做需要锁定输入做的事情

vu.LockInput(0);

 

注意:此接口只针对dx键鼠. 普通键鼠无效. 
有时候，绑定为dx 鼠标模式时(或者没有锁定鼠标位置或状态时)，在脚本处理过程中，在某个时候需要临时锁定外部输入，以免外部干扰，那么这个函数就非常有用.
比如某个信息，需要鼠标移动到某个位置才可以获取，但这时，如果外部干扰，那么很可能就会获取失败，所以，这时候就很有必要锁定外部输入. 
当然，锁定完以后，记得要解除锁定，否则外部永远都无法输入了，除非解除了窗口绑定.

---

## 

函数简介:

在不解绑的情况下,切换绑定窗口.(可以是任意进程窗口) 

函数原型:

long SwitchBindWindow(hwnd)

参数定义:

hwnd 整数型: 需要切换过去的窗口句柄

返回值:

整形数:
0: 失败
1: 成功

示例:

// 绑定为后台

ret = vu.BindWindowEx(hwnd, "dx", "dx", "dx", "", 0);

// 切换

hwnd = 1234;

ret = vu.SwitchBindWindow(hwnd);

注:此函数一般用在绑定以后，窗口句柄改变了的情况。如果必须不解绑，那么此函数就很有用了。

---

## 

函数简介:

解除绑定窗口,并释放系统资源.一般在退出时调用

函数原型:

LONG UnBindWindow()

参数定义:

无

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.BindWindowEx(hwnd, "normal", "normal", "normal", "", 0);

    /* 执行其他命令,例如找图,找色,鼠标移动等

    * ....

    * 执行结束*/

    ret = vu.UnBindWindow();

---

## 

函数简介:

创建插件对象,只有调用过本命令后才能正常使用插件,否则所有命令均会无效.

注意:本命令创建的是本地对象,仅限本机运行,若要使用远程对象,请调用CreateRemote()命令.

函数原型:

LONG64  Create()

参数定义:

无

返回值:

长整数型:

返回插件对象的内存指针,若创建失败则返回0.

示例:

    obj = vu.Create();

    if (obj > 0)

        std::cout << "创建对象 = " << obj << std::endl;

    else

        std::cout << "创建对象失败" << std::endl;

---

## 

函数简介:

连接终端电脑并创建一个远程对象,所创建的对象可以直接调用终端电脑上的插件命令,使用方法与本机运行等同.

注意:本命令创建的是远程对象,若要使用本机对象,请使用Create()

函数原型:

LONG64  CreateRemote(ip, port)

参数定义:

ip 字符串:要连接的目标终端电脑IP地址

port 整数型:终端电脑启动时的端口号

返回值:

长整数型:

远程对象的内存指针,如果创建失败则返回0

示例:

    obj = vu.CreateRemote("192.168.0.100", 5555);

    if (obj > 0)

        std::cout << "创建远程对象 = " << obj << std::endl;

    else

        std::cout << "创建远程对象失败" << std::endl;

 

注意:在创建远程对象时,请确保终端电脑已经通过调用TerminalStart()启动,否则将无法在本机创建远程对象.

---

## 

函数简介:

对数据内容进行加密/解密

函数原型:

LONG64 Crypt(mode,key,data,in_out_Len)

参数定义:

mode 整数型:加解密模式,取值如下:

0:对data数据进行加密

1:对data数据进行解密

key 字符串:加解密使用的秘钥文本,加密key和解密key必须相同,否则无法解密

data 长整数型:加密或者解密数据的数据内存指针

in_out_Len 变参指针:传入的是data数据的长度,执行完毕后会从此参数返回加解密后新数据的长度,若执行失败返回0

返回值:

长整数型:

返回加密后或者解密后数据所在的内存指针,若执行失败则返回0

注意:无论是加密还是解密后,返回值指向的内存地址均为临时存放数据的内存,在下次调用本函数的时候会被释放,所以当获取到返回值时请及时拷贝此指针的数据.

示例:

// 构建需要加密的数据,可以是字符串或者读取到的文件内容等字节集数据,例如图片

std::string strCrpyt = "我是测试数据";

LONG64 pStr = (LONG64)strCrpyt.data();

LONG nRet = strCrpyt.size();

	

// 进行加密操作

LONG64 nRet64 = vu.Crypt(0, "key123", pStr, nRet);

// 申请内存并拷贝加密结果

char* bufEncrypt = (char*)malloc(nRet);

memcpy(bufEncrypt, (char*)nRet64, nRet);

std::cout << "加密长度:" << nRet << std::endl;

std::cout << "加密结果:" << bufEncrypt << std::endl;

	

// 进行解密操作

nRet64 = vu.Crypt(1, "key123", nRet64, nRet);

// 申请内存并拷贝解密结果

char* bufDecrypt = (char*)malloc(nRet);

memcpy(bufDecrypt, (char*)nRet64, nRet);

std::cout << "解密长度:" << nRet << std::endl;

std::cout << "解密结果:" << bufDecrypt << std::endl;

 

说明:此加解密安全性极高,倘若您的程序中有使用txt文件、图片、onnx模型文件等需要外部调用的资源,而且不想让其他人轻易获取这些文件,则可以使用本函数将其加密后再写出到硬盘,调用时仅需读取后再解密,即可正常使用.

本插件大多数需要调用外部资源的接口均支持对文件原始数据字节集进行传参与使用.

故此无需担心资源外泄.

---

## 

函数简介:

销毁并释放本对象,调用后本对象的所有插件命令将会失效.

注意:无论是本地对象还是远程对象,调用本命令后都会被执行销毁.

函数原型:

LONG64 Delete()

参数定义:

无

返回值:

长整数型:

0:失败

1:成功

示例:

//或者调用CreateRemote()创建远程对象

obj = vu.Create();

if (obj > 0)
std::cout << "创建对象 = " << obj << std::endl;

else
std::cout << "创建对象失败" << std::endl;

/*

* 执行其他命令,例如找图,找色,鼠标移动等

* ....

* 执行结束

*/

 

//销毁对象

vu.Delete();

---

## 

函数简介:

返回当前对象的ID值，这个值对于每个对象是唯一存在的。可以用来判定两个对象是否一致.

函数原型:

LONG GetID()

参数定义:

无

返回值:

整数型:
当前对象的ID值.

示例:

    ret = vu.GetID();

    std::cout << "对象ID:"<< ret << std::endl;

---

## 

函数简介:

获取插件命令的最后错误

函数原型:

string GetLastError()

参数定义:

无

返回值:

字符串:

没有错误则为空字符串

否则返回错误发生原因(字符串表达)

示例:

    res = vu.GetLastError();

    std::cout << "GetLastError = " << res << std::endl;

---

## 

函数简介:

获取全局路径.(可用于调试)

函数原型:

string GetPath()

参数定义:

无

返回值:

字符串:
以字符串的形式返回当前设置的全局路径

示例:

    res = vu.GetPath();

    std::cout << "GetPath = "<< res << std::endl;

---

## 

函数简介:

调用此函数来注册，从而使用插件的高级功能.推荐使用此函数.

函数原型:

LONG Reg(reg_code,ver_info)

参数定义:

reg_code 字符串: 注册码. (从插件后台获取)

ver_info 字符串: 版本附加信息. 可以在后台详细信息查看. 可以任意填写. 可留空. 长度不能超过32. 并且只能包含数字和字母以及小数点. 这个版本信息不是插件版本.

返回值:

整数型:

1 : 成功
0 : 注册失败,参数填写错误
-1 : 非法注册,或将面临封禁
-101 : 参数reg_code错误

-102 : 参数ver_info错误
-103 : 当前机器系统环境异常(无法获取机器码).
-201 : 未知错误
如果注册失败,可以使用GetLastError()查阅错误详细信息.

示例:

    ret = vu.Reg("123456", "");

    if (ret != 1)

        std::cout << "注册失败,只能使用免费功能" << std::endl;

---

## 

函数简介:

在调用Reg()之前可以调用本函数更改服务器Url地址.(ip地址列表在VIP群中发布)

函数原型:

string RegUrl(server_url)

参数定义:

server_url 字符串: 服务器Url地址

返回值:

字符串:

返回新的服务器Url地址

示例:

    res = vu.RegUrl("http://12.34.56.78:88");

    if (res != “”)

        std::cout << "服务器url:"<< res << std::endl;

---

## 

函数简介:

设定图色的获取方式，默认是显示器或者后台窗口(具体参考BindWindowEx)

函数原型:

LONG SetDisplayInput(mode)

参数定义:

mode 字符串: 图色输入模式取值有以下几种

1."screen" 这个是默认的模式，表示使用显示器或者后台窗口

2."pic:file" 指定输入模式为指定的图片,如果使用了这个模式，则所有和图色相关的函数均视为对此图片进行处理.
比如文字识别查找图片 颜色 等等一切图色函数.

3."mem:addr,size" 指定输入模式为指定的图片,此图片在内存当中. addr为图像内存地址,size为图像内存大小.
如果使用了这个模式，则所有和图色相关的函数,均视为对此图片进行处理.
比如文字识别 查找图片 颜色 等等一切图色函数.

返回值:

整数型:
0: 失败

1: 成功

示例:

// 设定为默认的模式

ret = vu.SetDisplayInput("screen");

 

// 设定为图片模式 图片采用相对路径模式 相对于SetPath的路径

ret = vu.SetDisplayInput("pic:test.bmp");

 

// 设为图片模式 图片采用绝对路径模式

ret = vu.SetDisplayInput("pic:d:\test\test.bmp");

 

// 设置为图片模式,图片从内存中获取

ret = vu.SetDisplayInput("mem:1230434,884");

---

## 

函数简介:

设置全局路径,设置了此路径后,所有接口调用中,相关的文件都相对于此路径. 比如图片,字库等.

函数原型:

LONG SetPath(path)

参数定义:

path 字符串: 路径,可以是相对路径,也可以是绝对路径

返回值:

整数型:
0: 失败
1: 成功

示例:

    // 以下代码把全局路径设置到了c盘根目录

    ret = vu.SetPath("c:\\");

 

    // 如下是把全局路径设置到了相对于当前exe所在的路径

    ret = vu.SetPath(".\\MyData");

    // 以上，如果exe在c:\test\a.exe 那么，就相当于把路径设置到了c:\test\MyData

---

## 

函数简介:

创建一个终端,用来接收远程电脑发送的指令,让插件可以直接在远程终端电脑运行,而无需将程序拷贝到目标终端设备.

需要在远程终端安装插件,并且调用一次本函数.

函数原型:

long  TerminalStart(port)

参数定义:

port 整数型:终端(本地)的端口号,取值范围1024-65535

返回值:

整数型:

返回创建的终端对象,可用来释放终端.(一般调用本函数后无需释放,除非你确实需要.)

示例:

pObj = vu.TerminalStart(5555);

if (pObj > 0)
std::cout << "终端对象 = " << pObj << std::endl;

这是终端电脑上需要调用的命令,只要执行过本命令后就不用再做任何处理了.

之后在另外一台电脑上直接使用CreateRemote()命令连接终端,就可以在它上面调用本插件几乎所有命令了.(算法类和图像编辑除外)

操作方式与常规方式一样,只不过所有找图、找字、内存等操作并不是对控制端电脑进行,而是对使用TerminalStart()创建终端的电脑进行了.

以下是图示:

---

## 

函数简介:

停止终端,将会结束终端的运行,控制端电脑无法使用此命令,需要在终端调用.(一般情况下启动终端后无需调用本命令,控制端电脑销毁远程对象时会自动注销终端的对象,除非终端电脑的使用者想主动断开控制端的联系)

函数原型:

LONG64  TerminalStop(pTerminal)

参数定义:

pTerminal 整数型:通过TerminalStart()命令创建的终端对象返回值

返回值:

长整数型:

0:失败

1:成功

示例:

    pObj = vu.TerminalStart(5555);

    if (pObj > 0)

        std::cout << "终端对象 = " << pObj << std::endl;

 

    ret = vu.TerminalStop(pObj);

    if (ret > 0)

        std::cout << "停止终端 = " << ret << std::endl;

---

## 

函数简介:

返回当前插件版本号

函数原型:

string Ver()

参数定义:

无

返回值:

字符串:

当前插件的版本描述字符串

示例:

    res = vu.Ver();

    std::cout << "Ver = " << res << std::endl;

---

## 

函数简介:

A星寻路,寻找路径,并返回第一个最近可抵达的坐标位置.

函数原型:

LONG AStartFindWay(beginX, beginY, endX, endY,intX,intY)

参数定义:

beginX 整数型:寻路开始的x坐标

beginY 整数型:寻路开始的y坐标

endX 整数型:目标x坐标

endY 整数型:目标y坐标

intX 变参指针:返回最近的x坐标

intY 变参指针:返回最近的y坐标

返回值:

整数型:
0:失败
1:成功

示例:

    vu.AStartFindWay(12, 34, 99, 81, intX, intY);

    std::cout << "可通行最近坐标:" << intX << "," << intY << std::endl;

---

## 

函数简介:

A星寻路,加载地图数据,地图数据必须为黑白图,黑色表示不可通行(障碍),白色表示可以通行(道路).

函数原型:

LONG AStartLoadMapData(pData,isInvert)

参数定义:

pData 长整数型:地图数据文件的内存地址

isInvert 整数型:是否反色,表示将黑色转白色,白色转黑色,加入你的地图数据白色是障碍,黑色是道路时,可以通过设置此值来转换.

0:不进行反色转换.

1:反色转换

返回值:

整数型:
0:失败
1:成功

示例:

    data = vu.ReadFileData("c:\\长安城.bmp", len);

    ret = vu.AStartLoadMapData(data, 0);

---

## 

函数简介:

A星寻路,加载地图文件,地图文件必须为黑白24位图,黑色表示不可通行(障碍),白色表示可以通行(道路).

函数原型:

LONG AStartLoadMapFile(file,isInvert)

参数定义:

file字符串:地图位图文件的路径

isInvert 整数型:是否反色,表示将黑色转白色,白色转黑色,加入你的地图数据白色是障碍,黑色是道路时,可以通过设置此值来转换.

0:不进行反色转换.

1:反色转换

返回值:

整数型:
0:失败
1:成功

示例:

    ret = vu.AStartLoadMapFile("c:\\长安城.bmp", 0);

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret = vu.AStartLoadMapFile("长安城.bmp", 0);

---

## 

函数简介:

A星寻路,获取路径最优的下个坐标位置.

函数原型:

LONG AStartNextWay(currentX,currentY,intX,intY,dir)

参数定义:

currentX 整数型:当前所处的x坐标

currentY 整数型:当前所处的y坐标

intX 变参指针:返回最近的x坐标

intY 变参指针:返回最近的y坐标

dir变参指针:返回最近xy坐标相对于当前xy坐标的方向.

方向为以最小坐标在图片左上角为规则,取值如下,

0:左

1:右

2:上

3:下

4:左上

5:右上

6:右下

7:左下

注意:如果你的坐标规则不是左上角为最小坐标,那么需要自行转换,例如当dir返回值为0时表示右,为1表示左等.

返回值:

整数型:
0:失败
1:成功

示例:

    下面给出的示例是一个完整的A星导航使用方法.

 

    vu.SetPath("c:\\game\\");

    //加载A星24位地图的位图文件.

    ret = vu.AStartLoadMapFile("长安城.bmp", 0);

 

    //设置方向和代价

    ret = vu.AStartSet(1, 10, 14, 1);

 

    //设置起始点坐标和终点坐标

    vu.AStartFindWay(12, 34, 99, 81, intX, intY);

    std::cout << "可通行最近坐标:" << intX << "," << intY << std::endl;

 

    while (true)

    {

        //获取当前xy坐标

        cX = 取当前X();//您自定义的函数,用来取当前所在位置x

        cY = 取当前Y();//您自定义的函数,用来取当前所在位置y

 

        vu.AStartNextWay(cX, cY, intX, intY, dir);

        std::cout << "下个坐标:" << intX << "," << intY << std::endl;

        std::cout << "方向:" << dir << std::endl;

 

        //前往坐标位置

        前往坐标位置(intX, intY,dir);//您自定义的函数,用来前往坐标位置

 

        //判断是否到达终点

        if (intX == 99 && intY == 81)

        {

            break;

        }

    }

---

## 

函数简介:

A星寻路,设置导航方向和导航代价

函数原型:

LONG AStartSet(dir,beeline,diagonal,isCenter)

参数定义:

dir 整数型:是否8个方向导航,默认为上下左右4个方向,如果需要同时获取(左上)(左下)(右上)(右下),这个参数就很有用了.

0:4个方向

1:8个方向

beeline 整数型:直走代价,左-右,上-下 4个方向直线导航的代价,代价越大,则越不容易直走.取值范围为1-100,默认为10.

diagonal 整数型:斜走代价,(左上)-(右下),(右上)-(左下) 4个方向斜线导航的代价,代价越大则越不容易斜走.取值范围为1-100,默认为14.

isCenter 整数型:是否尽量靠着可通行路径的中间导航.某些地图边缘会有许多零碎障碍,如果默认的导航容易在拐角处卡住导致无法寻路,所以使用此参数可以规避在路径边缘位置行走.

0:不靠道路中心行走.

1:按照道路中心行走.

返回值:

整数型:
0:失败
1:成功

示例:

    ret = vu.AStartSet(1, 10, 14, 1);

---

## 

A星寻路的原理是从相邻坐标进行迭代计算是否可以通行,并优先搜索最优可能产生最佳路径的坐标.
通常用来实现机器人导航,车辆导航,游戏NPC寻路等功能.
 
下面我们以游戏NPC寻路为例,用来实现A星地图制作,其他用途的导航方法类似.
本文所介绍的所有素材均来源于网络,并不存在针对任何游戏的行为.
 
1.首先准备一张游戏地图.

例如:

 
2.将地图制作成黑白色的路径坐标图.黑色代表障碍物,白色代表可通行区域(使用综合工具,或者PS等绘图软件均可).

制作完成结果:

 
制作的黑白图越精细,寻路的效率和准确度越高.本例仅仅大致做了一张实例图,并非完美精细寻路图.
3.地图缩放或者坐标倍率转换.
因为我们制作的地图的坐标系未必和游戏中坐标系相同,例如我们做的这张图大小为1063 x 564个像素.但是游戏是2126,1128为最大xy坐标,而且游戏的0,0坐标在地图的左下角.
我们计算后得到游戏最大坐标正好是我们制作的黑白图的两倍,所以我们可以对这张图进行两倍缩放并保存为.bmp位图.
也可以在寻路的时候,将坐标进行2倍结果计算.例如我们通过插件的A星寻路功能得到最近坐标是100,200,那么就需要在这个结果上x2,来匹配游戏坐标,最终正确结果应该为200,400.
当然以上方式可能并不能适用于所有情况,我在这里 仅提供一个大致方法,针对不同应用场景,所需要的方法也不尽相同.
如果游戏坐标0,0位置在地图左下角,那么还需要计算正确的坐标,如上述我们得到了最终结果是200,400,其实这个结果还需要进行转换,方法是游戏的最大坐标减去我们得到的坐标.所以应该是:2126-200,1128-400.
4.最终应用.
通过以上步骤,我们便可以实现在游戏中应用A星寻路进行导航了.如果您的项目需要实现的是机器人导航或者车辆导航,使用方法与上述大致相同,只是地图会更大,寻路会变慢许多.

---

## 

函数简介:

对指定的数据地址和长度，组合成新的参数. FindPicMem FindPicMemE 以及FindPicMemEx专用

函数原型:

string AppendPicAddr(pic_info,addr,size)

参数定义:

pic_info 字符串: 老的地址描述串

addr 整数型: 数据地址

size 整数型: 数据长度

返回值:

字符串:
新的地址描述串

示例:

pic_info = ""

pic_info = vu.AppendPicAddr(pic_info,12034,643)

pic_info = vu.AppendPicAddr(pic_info,328435,8935)

pic_info = vu.AppendPicAddr(pic_info,809234,789)

---

## 

函数简介:

抓取指定区域(x1, y1, x2, y2)的图像,保存为file(24位位图)

函数原型:

long Capture(x1, y1, x2, y2, file)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
file 字符串:保存的文件名,保存的地方一般为SetPath中设置的目录

     当然这里也可以指定全路径名.

返回值:

整数型:
0:失败
1:成功

示例:

    ret = vu.Capture(0, 0, 2000, 2000, "screen.bmp");

---

## 

函数简介:

抓取指定区域(x1, y1, x2, y2)的动画，保存为gif格式

函数原型:

long CaptureGif(x1, y1, x2, y2, file,delay,time)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
file 字符串:保存的文件名,保存的地方一般为SetPath中设置的目录

     当然这里也可以指定全路径名.
delay 整数型: 动画间隔，单位毫秒。如果为0，表示只截取静态图片
time 整数型: 总共截取多久的动画，单位毫秒。

返回值:

整数型:
0:失败
1:成功

示例:

	// 截取动画

	ret = vu.CaptureGif(0, 0, 2000, 2000, "screen.gif", 100, 3000);

 

	// 截取静态

	ret = vu.CaptureGif(0, 0, 2000, 2000, "screen.gif", 0, 0);

---

## 

函数简介:

抓取指定区域(x1, y1, x2, y2)的图像,保存为file(JPG压缩格式)

函数原型:

long CaptureJpg(x1, y1, x2, y2, file)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
file 字符串:保存的文件名,保存的地方一般为SetPath中设置的目录

     当然这里也可以指定全路径名.

返回值:

整数型:
0:失败
1:成功

示例:

    ret = vu.CaptureJpg(0, 0, 2000, 2000, "screen.jpg");

---

## 

函数简介:

同Capture函数，只是保存的格式为PNG.

函数原型:

long CapturePng(x1, y1, x2, y2, file)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
file 字符串:保存的文件名,保存的地方一般为SetPath中设置的目录

     当然这里也可以指定全路径名.

返回值:

整数型:
0:失败
1:成功

示例:

    ret = vu.CapturePng(0, 0, 2000, 2000, "screen.png");

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标.

函数原型:

long FindPic(x1, y1, x2, y2, pic_name, delta_color,sim, dir,intX, intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
delta_color 字符串:颜色色偏比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示). 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

整数型:
返回找到的图片的序号,从0开始索引.如果没找到返回-1

示例:

    ret = vu.FindPic(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp", "000000", 0.9, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

在大的图片中找小的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标.

函数原型:

string FindPicByPic(source_pic,target_pic,delta_color,sim, dir)

参数定义:

source_pic 字符串:源图片(大图),仅支持一张图片,将在此图中寻找target_pic指定的图片

target_pic 字符串:目标图(小图),可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"

delta_color 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"

sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回的是所有找到的坐标格式如下:"file,x,y| file,x,y..| file,x,y" (图片左上角的坐标)

比如"1.bmp,100,20|2.bmp,30,40" 表示找到了两个,第一个,对应的图片是1.bmp,坐标是(100,20),第二个是2.bmp,坐标(30,40)

示例:

    char* sss = (char*)vu.FindPicByPic("screen.bmp", "1.bmp|2.bmp|3.bmp", "000000", 0.9, 0);

    //sss结果为file1,x1,y1|file2,x2,y2|....filen,xn,yn

    //file为图片名字，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",") == NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char* ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            const char* f = v.StrSplitGet(0);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << f << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标.

函数原型:

string FindPicE(x1, y1, x2, y2, pic_name, delta_color,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
delta_color 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index,x,y", 比如"3,100,200"

示例:

    res = vu.FindPicE(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp", "000000", 0.9, 0);

    if (strstr(res, ","))

        std::cout << "找到图片:" << res << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标.

函数原型:

string FindPicEx(x1, y1, x2, y2, pic_name, delta_color,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
delta_color 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)

比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的图片是图像序号为0的图片,坐标是(100,20),第二个是序号为2的图片,坐标(30,40)

示例:

    char * sss = (char*)vu.FindPicEx(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp", "000000", 0.9, 0);

    //sss结果为id1,x1,y1|id2,x2,y2|....idn,xn,yn

    //id为图片在图片列表中的索引，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",")== NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char * ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            long id = v.StrToNum(v.StrSplitGet(0), 10);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << id << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标. 此函数同FindPicEx.只是返回值不同.

函数原型:

string FindPicExS(x1, y1, x2, y2, pic_name, delta_color,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
delta_color 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回的是所有找到的坐标格式如下:"file,x,y| file,x,y..| file,x,y" (图片左上角的坐标)

比如"1.bmp,100,20|2.bmp,30,40" 表示找到了两个,第一个,对应的图片是1.bmp,坐标是(100,20),第二个是2.bmp,坐标(30,40)

示例:

    char* sss = (char*)vu.FindPicExS(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp", "000000", 0.9, 0);

    //sss结果为file1,x1,y1|file2,x2,y2|....filen,xn,yn

    //file为图片名字，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",") == NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char* ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            const char* f = v.StrSplitGet(0);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << f << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.

函数原型:

long FindPicMem(x1, y1, x2, y2, pic_info, delta_color,sim, dir,intX, intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
delta_color 字符串:颜色色偏比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

整数型:
返回找到的图片的序号,从0开始索引.如果没找到返回-1

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

    ret = vu.FindPicMem(0, 0, 2000, 2000, pic_info, "000000", 0.9, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 这个函数要求图片是数据地址.

函数原型:

string FindPicMemE(x1, y1, x2, y2, pic_info, delta_color,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
delta_color 字符串:颜色色偏比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回找到的图片序号(从0开始索引)以及X和Y坐标 形式如"index,x,y", 比如"3,100,200"

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

    res = vu.FindPicMemE(0,0,2000,2000, pic_info,"000000",0.9,0);

    if (strstr(res, ","))

        std::cout << "找到图片:" << res << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,并且返回所有找到的图像的坐标. 这个函数要求图片是数据地址.

函数原型:

string FindPicMemEx(x1, y1, x2, y2, pic_info, delta_color,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_info 字符串: 图片数据地址集合. 格式为"地址1,长度1|地址2,长度2.....|地址n,长度n". 可以用AppendPicAddr来组合. 
          地址表示24位位图资源在内存中的首地址，用十进制的数值表示
          长度表示位图资源在内存中的长度，用十进制数值表示.
delta_color 字符串:颜色色偏比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回的是所有找到的坐标格式如下:"id,x,y|id,x,y..|id,x,y" (图片左上角的坐标)

比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的图片是图像序号为0的图片,坐标是(100,20),第二个是序号为2的图片,坐标(30,40)

示例:

    pic_info = "";

    pic_info = vu.AppendPicAddr(pic_info, 12034, 643);

    pic_info = vu.AppendPicAddr(pic_info, 328435, 8935);

    pic_info = vu.AppendPicAddr(pic_info, 809234, 789);

 

    char* sss = (char*)vu.FindPicMemEx(0, 0, 2000, 2000, pic_info, "020202", 1.0, 0);

    //sss结果为id1,x1,y1|id2,x2,y2|....idn,xn,yn

    //id为图片在图片列表中的索引，x,y为图片在屏幕中的坐标

    if (strstr(sss, ",") == NULL)

        std::cout << "未找到图片" << std::endl;

    else

    {

        vusoft vs;

        long len = vs.StrSplitInit(sss, "|");

        for (long i = 0; i < len; i++)

        {

            const char* ss = vs.StrSplitGet(i);

            vusoft v;

            long n = v.StrSplitInit(ss, ",");

            if (n != 3)

                continue;

            long id = v.StrToNum(v.StrSplitGet(0), 10);

            long x = v.StrToNum(v.StrSplitGet(1), 10);

            long y = v.StrToNum(v.StrSplitGet(2), 10);

            std::cout << "找到图片:" << id << "," << x << "," << y << std::endl;

        }

    }

---

## 

函数简介:

查找指定区域内的图片,位图必须是24位色格式,支持透明色,当图像上下左右4个顶点的颜色一样时,则这个颜色将作为透明色处理.

这个函数可以查找多个图片,只返回第一个找到的X Y坐标. 此函数同FindPic.只是返回值不同.

函数原型:

string FindPicS(x1, y1, x2, y2, pic_name, delta_color,sim, dir,intX, intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片名,可以是多个图片,比如"test.bmp|test2.bmp|test3.bmp"
delta_color 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回图片左上角的X坐标
intY 变参指针:返回图片左上角的Y坐标

返回值:

字符串:
返回找到的图片的文件名. 没找到返回长度为0的字符串.

示例:

    res = vu.FindPicS(0, 0, 2000, 2000, "1.bmp|2.bmp|3.bmp", "000000", 0.9, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到图片所在位置:" << intX << "," << intY << std::endl;

    else

        std::cout << "未找到图片" << std::endl;

---

## 

函数简介:

获取指定图片的尺寸

函数原型:

string GetPicSize(pic_name,w,h)

参数定义:

pic_name 字符串: 文件名 比如"1.bmp"

w 变参指针:返回图片宽度

h 变参指针:返回图片高度

返回值:

字符串:
形式如 "w,h" 比如"30,20"

示例:

    ret = vu.SetPath("c:\test");

    res = vu.GetPicSize("1.bmp", w, h);

    std::cout << "图片宽度:" << w << std::endl;

    std::cout << "图片高度:" << h << std::endl;

---

## 

函数简介:

获取指定区域的图像,用二进制数据的方式返回,方便二次开发.

函数原型:

long GetScreenData(x1,y1,x2,y2)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标

返回值:

整数型:
返回的是指定区域的二进制颜色数据地址,每个颜色是4个字节,表示方式为(00RRGGBB)

示例:

无示例,开发者都懂的。

注意,调用完此接口后，返回的数据指针在当前vu对象销毁时，或者再次调用GetScreenData时，会自动释放.

---

## 

函数简介:

获取指定区域的图像,用24位位图的数据格式返回,方便二次开发.（或者可以配合SetDisplayInput的mem模式）

函数原型:

long GetScreenDataBmp(x1,y1,x2,y2,data,size)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
data 变参指针:返回图片的数据指针
size 变参指针:返回图片的数据长度

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    vu.GetScreenDataBmp(0, 0, 100, 200, data, size);

    if (data && size)

        std::cout << "获取到图片数据" << std::endl;

 

注意:每次调用本接口都会对图片数据指针进行销毁并重新分配,所以若想永久保留图片数据,请及时拷贝data数据,避免下次调用本接口而被释放.

---

## 

函数简介:

判断指定的区域，在指定的时间内(秒),图像数据是否一直不变.(卡屏). (或者绑定的窗口不存在也返回1)

函数原型:

long IsDisplayDead(x1,y1,x2,y2,t)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
t  整数型:需要等待的时间,单位是秒 

返回值:

整数型:
0 : 没有卡屏，图像数据在变化.
1 : 卡屏. 图像数据在指定的时间内一直没有变化. 或者绑定的窗口不见了.

示例:

ret = vu.IsDisplayDead(0, 0, 100, 200, 10);

std::cout << "是否卡屏:" << ret << std::endl;

注:此函数的原理是不停的截取指定区域的图像，然后比较，如果改变就立刻返回0,否则等待直到指定的时间到达.

---

## 

函数简介:

根据通配符获取文件集合. 方便用于FindPic和FindPicEx

函数原型:

string MatchPicName(pic_name)

参数定义:

pic_name 字符串: 文件名比如"1.bmp|2.bmp|3.bmp" 等,可以使用通配符,比如

          "*.bmp" 这个对应了所有的bmp文件

          "a?c*.bmp" 这个代表了所有第一个字母是a 第三个字母是c 第二个字母任意的所有bmp文件

          "abc???.bmp|1.bmp|aa??.bmp" 可以这样任意组合.

返回值:

字符串:
返回的是通配符对应的文件集合，每个图片以|分割

示例:

ret = vu.SetPath("c:\test")

all_pic = "abc*.bmp"

pic_name = vu.MatchPicName(all_pic)

 

// 比如c:\test目录下有abc001.bmp abc002.bmp abc003.bmp

// 那么pic_name 的值为abc001.bmp|abc002.bmp|abc003.bmp

---

## 

函数简介:

给指定的字库中添加一条字库信息.

函数原型:

long AddDict(index,dict_info)

参数定义:

index 整数型:字库的序号,支持任意正整数型,例如0或65535
dict_info 字符串:字库描述串，具体参考综合工具中的字符定义

返回值:

整数型:
0:失败
1:成功

示例:

    ret = vu.AddDict(0, "081101BF8020089FD10A21443F85038$记$0.0$11");

注意: 此函数尽量在小字库中使用，大字库中使用AddDict速度比较慢

另，此函数是向指定的字库所在的内存中添加,而不是往文件中添加. 添加以后立刻就可以用于文字识别。无须再SetDict

如果要保存添加进去的字库信息，需要调用SaveDict

---

## 

函数简介:

清空指定的字库.

函数原型:

long ClearDict(index)

参数定义:

index 整数型:字库的序号

返回值:

整数型:
0:失败
1:成功

示例:

vu.ClearDict(0);

注意: 此函数尽量在小字库中使用，大字库中使用ClearDict速度比较慢

另外，此函数支持清空内存中的字库，而不是字库文件本身.

---

## 

函数简介:

删除指定字库中指定条目的字库信息.

此函数仅将内存中的字库条目删除,并不影响字库文件的内容.

函数原型:

LONG DelDict(LONG index, LONG font_index)

参数定义:

index 整数型: 字库序号

font_index 整数型: 字库条目序号(从0开始计数,数值不得超过指定字库的字库上限,具体参考GetDictCount)

返回值:

整数型:

0:失败

1:成功

示例:

        // 删除0号字库第10个条目

        vu.DelDict(0, 10);

---

## 

函数简介:

根据指定的范围,以及指定的颜色描述，提取点阵信息，类似于综合工具里的多个点阵提取.

函数原型:

string FetchDots(x1, y1, x2, y2, color_format, rowGap, colGap)

参数定义:

x1 整数型:左上角X坐标

y1 整数型:左上角Y坐标

x2 整数型:右下角X坐标

y2 整数型:右下角Y坐标

color 字符串: 颜色格式串.注意，RGB和HSV,以及灰度格式都支持.

rowGap 整数型:行间距,超过此间距则视为另起一行的文字.

colGap 整数型:列间距,超过此间距则视为另起一列的文字.

返回值:

字符串:

识别到的多个点阵的信息,每一块点阵信息用回车换行符"\r\n"分隔,不同于FetchWord()函数会直接返回标准的字库点阵信息,本函数返回的信息中使用坐标位置代替字库文本,用来进行未知文本的识别.

示例:

        res = vu.FetchDots(0, 0, 800, 600, "ffffff-000000", 1, 1);

---

## 

函数简介:

根据指定的范围,以及指定的颜色描述，提取点阵信息，类似于综合工具里的单独提取.

函数原型:

string FetchWord(x1, y1, x2, y2, color_format, word)

参数定义:

x1 整数型:左上角X坐标

y1 整数型:左上角Y坐标

x2 整数型:右下角X坐标

y2 整数型:右下角Y坐标

color 字符串: 颜色格式串.注意，RGB和HSV,以及灰度格式都支持.

word 字符串: 待定义的文字,不能为空，且不能为关键符号"$"

返回值:

字符串:

识别到的点阵信息，可用于AddDict

如果失败，返回空

示例:

		// RGB颜色点阵信息

		res = vu.FetchWord(200, 200, 250, 250, "abcdef-101010|ffffff-101010", "张三");

		if(strlen(res) > 0)

			vu.AddDict(0, res);

 

		// RGB颜色为背景色提取点阵信息

		res = vu.FetchWord(200, 200, 250, 250, "b@abcdef-101010|ffffff-101010", "张三");

		if (strlen(res) > 0)

			vu.AddDict(0, res);

 

		// HSV颜色为背景色提取点阵信息

		res = vu.FetchWord(200, 200, 250, 250, "b@0.100.100-0.0.0|100.0.0-0.0.0", "张三");

		if (strlen(res) > 0)

			vu.AddDict(0, res);

 

		// 灰度值为背景色提取点阵信息

		res = vu.FetchWord(200, 200, 250, 250, "b@#0-0|#42-0", "张三");

		if (strlen(res) > 0)

			vu.AddDict(0, res);

---

## 

函数简介:

在屏幕范围(x1,y1,x2,y2)内,查找string(可以是任意个字符串的组合),并返回符合color_format的坐标位置,相似度sim同Ocr接口描述.

(多色,差色查找类似于Ocr接口,不再重述)

函数原型:

long FindStr(x1,y1,x2,y2,string,color_format,sim,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串,可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例 .注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
intX 变参指针:返回X坐标没找到返回-1
intY 变参指针:返回Y坐标没找到返回-1

返回值:

整数型:
返回字符串的索引 没找到返回-1, 比如"长安|洛阳",若找到长安，则返回0,若找到洛阳则返回1

示例:

    ret = vu.FindStr(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到字符:" << intX << "," << intY << std::endl;

注: 此函数的原理是先Ocr识别，然后再查找。所以速度比FindStrFast要慢，尤其是在字库
很大，或者模糊度不为1.0时。

一般字库字符数量小于100左右，模糊度为1.0时，用FindStr要快一些,否则用FindStrFast.

---

## 

函数简介:

在屏幕范围(x1,y1,x2,y2)内,查找string(可以是任意个字符串的组合),并返回符合color_format的坐标位置,相似度sim同Ocr接口描述.

(多色,差色查找类似于Ocr接口,不再重述)

函数原型:

string FindStrE(x1,y1,x2,y2,string,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回字符串序号以及X和Y坐标,形式如"id,x,y", 比如"0,100,200",没找到时，id和X以及Y均为-1，"-1,-1,-1"

示例:

    res = vu.FindStrE(0, 0, 2000, 2000, "长安", "9f2e3f-000000", 1.0);

    vusoft vs;

    long len = vs.StrSplitInit(res, ",");

    if (len == 3)

    {

        const char* str = vs.StrSplitGet(0);

        long x = vs.StrToNum(vs.StrSplitGet(1), 10);

        long y = vs.StrToNum(vs.StrSplitGet(2), 10);

        std::cout << "找到: id = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 此函数的原理是先Ocr识别，然后再查找。所以速度比FindStrFastE要慢，尤其是在字库很大，或者模糊度不为1.0时。

一般字库字符数量小于100左右，模糊度为1.0时，用FindStrE要快一些,否则用FindStrFastE.

---

## 

函数简介:

在屏幕范围(x1,y1,x2,y2)内,查找string(可以是任意字符串的组合),并返回符合color_format的所有坐标位置,相似度sim同Ocr接口描述.

(多色,差色查找类似于Ocr接口,不再重述)

函数原型:

string FindStrEx(x1,y1,x2,y2,string,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回所有找到的坐标集合,格式如下:
"id,x0,y0|id,x1,y1|......|id,xn,yn"
比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的是序号为0的字符串,坐标是(100,20),第二个是序号为2的字符串,坐标(30,40)

示例:

    res = vu.FindStrEx(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0);

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        const char* str = v.StrSplitGet(0);

        long x = v.StrToNum(v.StrSplitGet(1), 10);

        long y = v.StrToNum(v.StrSplitGet(2), 10);

        std::cout << "找到: id = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 此函数的原理是先Ocr识别，然后再查找。所以速度比FindStrExFast要慢，尤其是在字库
很大，或者模糊度不为1.0时。

一般字库字符数量小于100左右，模糊度为1.0时，用FindStrEx要快一些,否则用FindStrFastEx.

---

## 

函数简介:

在屏幕范围(x1,y1,x2,y2)内,查找string(可以是任意字符串的组合),并返回符合color_format的所有坐标位置,相似度sim同Ocr接口描述.

(多色,差色查找类似于Ocr接口,不再重述). 此函数同FindStrEx,只是返回值不同.

函数原型:

string FindStrExS(x1,y1,x2,y2,string,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回所有找到的坐标集合,格式如下:
"str,x0,y0| str,x1,y1|......| str,xn,yn"
比如"长安,100,20|大雁塔,30,40" 表示找到了两个,第一个是长安 ,坐标是(100,20),第二个是大雁塔,坐标(30,40)

示例:

    res = vu.FindStrExS(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0);

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        const char* str = v.StrSplitGet(0);

        long x = v.StrToNum(v.StrSplitGet(1), 10);

        long y = v.StrToNum(v.StrSplitGet(2), 10);

        std::cout << "找到: 字串 = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 此函数的原理是先Ocr识别，然后再查找。所以速度比FindStrExFastS要慢，尤其是在字库
很大，或者模糊度不为1.0时。

一般字库字符数量小于100左右，模糊度为1.0时，用FindStrExS要快一些,否则用FindStrFastExS.

---

## 

函数简介:

同FindStr。

函数原型:

long FindStrFast(x1,y1,x2,y2,string,color_format,sim,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串,可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
intX 变参指针:返回X坐标 没找到返回-1
intY 变参指针:返回Y坐标 没找到返回-1

返回值:

整数型:
返回字符串的索引 没找到返回-1, 比如"长安|洛阳",若找到长安，则返回0

示例:

    ret = vu.FindStrFast(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到字符:" << intX << "," << intY << std::endl;

注: 此函数比FindStr要快很多，尤其是在字库很大时，或者模糊识别时，效果非常明显。
推荐使用此函数。
另外由于此函数是只识别待查找的字符，所以可能会有如下情况出现问题。

比如 字库中有"张和三" 一共3个字符数据，然后待识别区域里是"张和三",如果用FindStr查找"张三"肯定是找不到的，

但是用FindStrFast却可以找到，因为"和"这个字符没有列入查找计划中所以，在使用此函数时，也要特别注意这一点。

---

## 

函数简介:

同FindStrE

函数原型:

string FindStrFastE(x1,y1,x2,y2,string,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回字符串序号以及X和Y坐标,形式如"id,x,y", 比如"0,100,200",没找到时，id和X以及Y均为-1，"-1,-1,-1"

示例:

    res = vu.FindStrFastE(0, 0, 2000, 2000, "长安", "9f2e3f-000000", 1.0);

    vusoft vs;

    long len = vs.StrSplitInit(res, ",");

    if (len == 3)

    {

        const char* str = vs.StrSplitGet(0);

        long x = vs.StrToNum(vs.StrSplitGet(1), 10);

        long y = vs.StrToNum(vs.StrSplitGet(2), 10);

        std::cout << "找到: id = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 此函数比FindStrE要快很多，尤其是在字库很大时，或者模糊识别时，效果非常明显。
推荐使用此函数。

另外由于此函数是只识别待查找的字符，所以可能会有如下情况出现问题。

比如 字库中有"张和三" 一共3个字符数据，然后待识别区域里是"张和三",如果用FindStrE查找
"张三"肯定是找不到的，但是用FindStrFastE却可以找到，因为"和"这个字符没有列入查找计划中
所以，在使用此函数时，也要特别注意这一点。

---

## 

函数简介:

同FindStrEx

函数原型:

string FindStrFastEx(x1,y1,x2,y2,string,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回所有找到的坐标集合,格式如下:
"id,x0,y0|id,x1,y1|......|id,xn,yn"
比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的是序号为0的字符串,坐标是(100,20),第二个是序号为2的字符串,坐标(30,40)

示例:

    res = vu.FindStrFastEx(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0);

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        const char* str = v.StrSplitGet(0);

        long x = v.StrToNum(v.StrSplitGet(1), 10);

        long y = v.StrToNum(v.StrSplitGet(2), 10);

        std::cout << "找到: id = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 此函数比FindStrEx要快很多，尤其是在字库很大时，或者模糊识别时，效果非常明显。
推荐使用此函数。

另外由于此函数是只识别待查找的字符，所以可能会有如下情况出现问题。

比如 字库中有"张和三" 一共3个字符数据，然后待识别区域里是"张和三",如果用FindStrEx查找
"张三"肯定是找不到的，但是用FindStrFastEx却可以找到，因为"和"这个字符没有列入查找计划中
所以，在使用此函数时，也要特别注意这一点。

---

## 

函数简介:

同FindStrExS.

函数原型:

string FindStrFastExS(x1,y1,x2,y2,string,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例 .注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回所有找到的坐标集合,格式如下:
"str,x0,y0| str,x1,y1|......| str,xn,yn"
比如"长安,100,20|大雁塔,30,40" 表示找到了两个,第一个是长安 ,坐标是(100,20),第二个是大雁塔,坐标(30,40)

示例:

    res = vu.FindStrFastExS(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0);

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        const char* str = v.StrSplitGet(0);

        long x = v.StrToNum(v.StrSplitGet(1), 10);

        long y = v.StrToNum(v.StrSplitGet(2), 10);

        std::cout << "找到: 字串 = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 此函数比FindStrExS要快很多，尤其是在字库很大时，或者模糊识别时，效果非常明显。
推荐使用此函数。

另外由于此函数是只识别待查找的字符，所以可能会有如下情况出现问题。

比如 字库中有"张和三" 一共3个字符数据，然后待识别区域里是"张和三",如果用FindStrExS查找
"张三"肯定是找不到的，但是用FindStrFastExS却可以找到，因为"和"这个字符没有列入查找计划中
所以，在使用此函数时，也要特别注意这一点。

---

## 

函数简介:

同FindStrS. 

函数原型:

string FindStrFastS(x1,y1,x2,y2,string,color_format,sim,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串,可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例 .注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
intX 变参指针:返回X坐标 没找到返回-1
intY 变参指针:返回Y坐标 没找到返回-1

返回值:

字符串:
返回找到的字符串. 没找到的话返回长度为0的字符串.

示例:

    res = vu.FindStrFastS(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到字符:" << intX << "," << intY << std::endl;

注: 此函数比FindStrS要快很多，尤其是在字库很大时，或者模糊识别时，效果非常明显。
推荐使用此函数。
另外由于此函数是只识别待查找的字符，所以可能会有如下情况出现问题。

比如 字库中有"张和三" 一共3个字符数据，然后待识别区域里是"张和三",如果用FindStrS查找
"张三"肯定是找不到的，但是用FindStrFastS却可以找到，因为"和"这个字符没有列入查找计划中
所以，在使用此函数时，也要特别注意这一点。

---

## 

函数简介:

在屏幕范围(x1,y1,x2,y2)内,查找string(可以是任意个字符串的组合),并返回符合color_format的坐标位置,相似度sim同Ocr接口描述.

(多色,差色查找类似于Ocr接口,不再重述).此函数同FindStr,只是返回值不同.

函数原型:

string FindStrS(x1,y1,x2,y2,string,color_format,sim,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串,可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例 .注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
intX 变参指针:返回X坐标 没找到返回-1
intY 变参指针:返回Y坐标 没找到返回-1

返回值:

字符串:
返回找到的字符串. 没找到的话返回长度为0的字符串.

示例:

    res = vu.FindStrS(0, 0, 2000, 2000, "长安", "9f2e3f-000000", 1.0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到字符:" << intX << "," << intY << std::endl;

注: 此函数的原理是先Ocr识别，然后再查找。所以速度比FindStrFastS要慢，尤其是在字库
很大，或者模糊度不为1.0时。

一般字库字符数量小于100左右，模糊度为1.0时，用FindStrS要快一些,否则用FindStrFastS.

---

## 

函数简介:

同FindStr，但是不使用SetDict设置的字库，而利用系统自带的字库，速度比FindStr稍慢.

函数原型:

long FindStrWithFont(x1,y1,x2,y2,string,color_format,sim,font_name,font_size,flag,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串,可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例 .注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
font_name 字符串:系统字体名,比如"宋体"
font_size 整数型:系统字体尺寸，这个尺寸一定要以大漠综合工具获取的为准.如果获取尺寸看视频教程.
flag 整数型:字体类别 取值可以是以下值的组合,比如1+2+4+8,2+4. 0表示正常字体.
    1 : 粗体
    2 : 斜体
    4 : 下划线
    8 : 删除线
intX 变参指针:返回X坐标没找到返回-1
intY 变参指针:返回Y坐标没找到返回-1

返回值:

整数型:
返回字符串的索引 没找到返回-1, 比如"长安|洛阳",若找到长安，则返回0

示例:

    ret = vu.FindStrWithFont(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0, "宋体", 9, 1 + 2, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到字符:" << intX << "," << intY << std::endl;

注: 对于如何获取字体尺寸以及名字等信息，可以参考视频教程，如何使用系统字库.

---

## 

函数简介:

同FindStrE，但是不使用SetDict设置的字库，而利用系统自带的字库，速度比FindStrE稍慢

函数原型:

string FindStrWithFontE(x1,y1,x2,y2,string,color_format,sim,font_name,font_size,flag)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
font_name 字符串:系统字体名,比如"宋体"
font_size 整数型:系统字体尺寸，这个尺寸一定要以大漠综合工具获取的为准.如果获取尺寸看视频教程.
flag 整数型:字体类别 取值可以是以下值的组合,比如1+2+4+8,2+4. 0表示正常字体.
    1 : 粗体
    2 : 斜体
    4 : 下划线
    8 : 删除线

返回值:

字符串:
返回字符串序号以及X和Y坐标,形式如"id,x,y", 比如"0,100,200",没找到时，id和X以及Y均为-1，"-1,-1,-1"

示例:

    res = vu.FindStrWithFontE(0, 0, 2000, 2000, "长安", "9f2e3f-000000", 1.0, "宋体", 9, 0);

    vusoft vs;

    long len = vs.StrSplitInit(res, ",");

    if (len == 3)

    {

        const char* str = vs.StrSplitGet(0);

        long x = vs.StrToNum(vs.StrSplitGet(1), 10);

        long y = vs.StrToNum(vs.StrSplitGet(2), 10);

        std::cout << "找到: id = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 对于如何获取字体尺寸以及名字等信息，可以参考视频教程，如何使用系统字库.

---

## 

函数简介:

同FindStrEx，但是不使用SetDict设置的字库，而利用系统自带的字库，速度比FindStrEx稍慢

函数原型:

string FindStrWithFontEx(x1,y1,x2,y2,string,color_format,sim,font_name,font_size,flag)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
font_name 字符串:系统字体名,比如"宋体"
font_size 整数型:系统字体尺寸，这个尺寸一定要以大漠综合工具获取的为准.如果获取尺寸看视频教程.
flag 整数型:字体类别 取值可以是以下值的组合,比如1+2+4+8,2+4. 0表示正常字体.
    1 : 粗体
    2 : 斜体
    4 : 下划线
    8 : 删除线

返回值:

字符串:
返回所有找到的坐标集合,格式如下:
"id,x0,y0|id,x1,y1|......|id,xn,yn"
比如"0,100,20|2,30,40" 表示找到了两个,第一个,对应的是序号为0的字符串,坐标是(100,20),第二个是序号为2的字符串,坐标(30,40)

示例:

    res = vu.FindStrWithFontEx(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0, "宋体", 9, 1 + 2);

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        const char* str = v.StrSplitGet(0);

        long x = v.StrToNum(v.StrSplitGet(1), 10);

        long y = v.StrToNum(v.StrSplitGet(2), 10);

        std::cout << "找到: id = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 对于如何获取字体尺寸以及名字等信息，可以参考视频教程，如何使用系统字库.

---

## 

函数简介:

同FindStrExS，但是不使用SetDict设置的字库，而利用系统自带的字库，速度比FindStrExS稍慢

函数原型:

string FindStrWithFontExS(x1,y1,x2,y2,string,color_format,sim,font_name,font_size,flag)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
font_name 字符串:系统字体名,比如"宋体"
font_size 整数型:系统字体尺寸，这个尺寸一定要以大漠综合工具获取的为准.如果获取尺寸看视频教程.
flag 整数型:字体类别 取值可以是以下值的组合,比如1+2+4+8,2+4. 0表示正常字体.
    1 : 粗体
    2 : 斜体
    4 : 下划线
    8 : 删除线

返回值:

字符串:
返回所有找到的坐标集合,格式如下:
"str,x0,y0| str,x1,y1|......| str,xn,yn"
比如"长安,100,20|大雁塔,30,40" 表示找到了两个,第一个是长安 ,坐标是(100,20),第二个是大雁塔,坐标(30,40)

示例:

    res = vu.FindStrWithFontExS(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0, "宋体", 9, 1 + 2);

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        const char* str = v.StrSplitGet(0);

        long x = v.StrToNum(v.StrSplitGet(1), 10);

        long y = v.StrToNum(v.StrSplitGet(2), 10);

        std::cout << "找到: 字串 = " << str << " 坐标 = " << x << "," << y << std::endl;

}

注: 对于如何获取字体尺寸以及名字等信息，可以参考视频教程，如何使用系统字库.

---

## 

函数简介:

同FindStrEx，但是不使用SetDict设置的字库，而利用系统自带的字库，速度比FindStrEx稍慢

函数原型:

string FindStrWithFontS(x1,y1,x2,y2,string,color_format,sim,font_name,font_size,flag,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
string 字符串:待查找的字符串, 可以是字符串组合，比如"长安|洛阳|大雁塔",中间用"|"来分割字符串
color_format 字符串:颜色格式串, 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0
font_name 字符串:系统字体名,比如"宋体"
font_size 整数型:系统字体尺寸，这个尺寸一定要以大漠综合工具获取的为准.如果获取尺寸看视频教程.
flag 整数型:字体类别 取值可以是以下值的组合,比如1+2+4+8,2+4. 0表示正常字体.
    1 : 粗体
    2 : 斜体
    4 : 下划线
    8 : 删除线

intX 变参指针:返回X坐标没找到返回-1
intY 变参指针:返回Y坐标没找到返回-1

返回值:
字符串:
返回找到的字符串. 没找到的话返回长度为0的字符串.

示例:

    res = vu.FindStrWithFontS(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0, "宋体", 9, 1 + 2, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到字符:" << intX << "," << intY << std::endl;

注: 对于如何获取字体尺寸以及名字等信息，可以参考视频教程，如何使用系统字库.

---

## 

函数简介:

获取指定字库中指定条目的字库信息.

函数原型:

string GetDict(index,font_index)

参数定义:

index 整数型: 字库序号
font_index 整数型: 字库条目序号(从0开始计数,数值不得超过指定字库的字数上限,具体参考GetDictCount)

返回值:

字符串:
返回字库条目信息. 失败返回空串.

示例:

    res = vu.GetDict(0, 123);

    std::cout << "字库内容:" << res << std::endl;

---

## 

函数简介:

获取指定的字库中的字符数量.

函数原型:

long GetDictCount(index)

参数定义:

index 整数型: 字库序号

返回值:

整数型:
字库数量

示例:

    ret = vu.GetDictCount(0);

    std::cout << "0号字库使用的字库数量是:" << ret << std::endl;

---

## 

函数简介:

根据指定的文字，以及指定的系统字库信息，获取字库描述信息.

函数原型:

string GetDictInfo(str,font_name,font_size,flag)

参数定义:

str 字符串:需要获取的字符串
font_name 字符串:系统字体名,比如"宋体"
font_size 整数型:系统字体尺寸，这个尺寸一定要以大漠综合工具获取的为准.如何获取尺寸看视频教程.
flag 整数型:字体类别 取值可以是以下值的组合,比如1+2+4+8,2+4. 0表示正常字体.
    1 : 粗体
    2 : 斜体
    4 : 下划线
    8 : 删除线

返回值:

字符串:
返回字库信息,每个字符的字库信息用"|"来分割

示例:

    //下面的代码是获取"回收站"这3个字符的字库信息，然后加入到字库0中

    font_desc = vu.GetDictInfo("回收站", "宋体", 9, 0);

    long len = vu.StrSplitInit(font_desc, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vu.StrSplitGet(i);

        if (ss == NULL)

            continue;

        std::cout << "字体信息:" << ss << std::endl;

        vu.AddDict(0, ss);

    }

---

## 

函数简介:

获取系统中所有字体列表

函数原型:

string GetFontList()

参数定义:

无

返回值:

字符串:

返回所有字体,每种字体用"|"来分割

示例:

	res = vu.GetFontList();

	std::cout << "系统所有字体 : " << res << std::endl;

---

## 

函数简介:

获取当前使用的字库序号

函数原型:

long GetNowDict()

参数定义:

无

返回值:

整数型:
字库序号(支持任意正整数型,例如0或65535)

示例:

    index = vu.GetNowDict();

    std::cout << "当前字库序号:" << index << std::endl;

---

## 

函数简介:

识别屏幕范围(x1,y1,x2,y2)内符合color_format的字符串,并且相似度为sim,sim取值范围(0.1-1.0),

这个值越大越精确,越大速度越快,越小速度越慢,请斟酌使用!

函数原型:

string Ocr(x1,y1,x2,y2,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color_format 字符串:颜色格式串. 可以包含换行分隔符,语法是","后加分割字符串. 具体可以查看下面的示例.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回识别到的字符串

示例:

	string s;

	//RGB单色识别

	s = vu.Ocr(0, 0, 2000, 2000, "9f2e3f-000000", 1.0);

 

	//RGB单色差色识别

	s = vu.Ocr(0, 0, 2000, 2000, "9f2e3f-030303", 1.0);

 

	//RGB多色识别(最多支持10种,每种颜色用"|"分割)

	s = vu.Ocr(0, 0, 2000, 2000, "9f2e3f-030303|2d3f2f-000000|3f9e4d-100000", 1.0);

---

## 

函数简介:

识别屏幕范围(x1,y1,x2,y2)内符合color_format的字符串,并且相似度为sim,sim取值范围(0.1-1.0),

这个值越大越精确,越大速度越快,越小速度越慢,请斟酌使用!

这个函数可以返回识别到的字符串，以及每个字符的坐标.

函数原型:

string OcrEx(x1,y1,x2,y2,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color_format 字符串:颜色格式串.RGB格式,例如"FF00AA",可以带色偏,例如"FF00AA-203040".
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回识别到的字符串 格式如  "字符0$x0$y0|…|字符n$xn$yn"

示例:

    res = vu.OcrEx(0, 0, 2000, 2000, "ffffff|000000", 1.0);

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, "$");

        if (n != 3)

            continue;

        const char* str = v.StrSplitGet(0);

        long x = v.StrToNum(v.StrSplitGet(1), 10);

        long y = v.StrToNum(v.StrSplitGet(2), 10);

        std::cout << "识别文本:" << str << "," << x << "," << y << std::endl;

    }

---

## 

函数简介:

识别屏幕范围(x1,y1,x2,y2)内符合color_format的字符串,并且相似度为sim,sim取值范围(0.1-1.0),

这个值越大越精确,越大速度越快,越小速度越慢,请斟酌使用!

这个函数可以返回识别到的字符串，以及每个字符的坐标.这个同OcrEx,另一种返回形式.

函数原型:

string OcrExOne(x1,y1,x2,y2,color_format,sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color_format 字符串:颜色格式串.注意，RGB和HSV,以及灰度格式都支持.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回识别到的字符串 格式如  "识别到的信息|x0,y0|…|xn,yn"

示例:

	// 和Ocr函数相同，只是结果处理有所不同如下

	s = vu.OcrExOne(0, 0, 2000, 2000, "ffffff|000000", 1.0);

	vusoft vs;

	long len = vs.StrSplitInit(s, "|");

	if (len == 2)

	{

		str = vs.StrSplitGet(0);

		std::cout << "识别文本:" << str << std::endl;

		for (size_t i = 1; i < len; i++)

		{

			s = vs.StrSplitGet(0);

			std::cout << "第:" << i << "个值所在位置:" << vs.StrSplitGet(i) << std::endl;

		}

	}

---

## 

函数简介:

识别位图中区域(x1,y1,x2,y2)的文字

函数原型:

string OcrInFile(x1, y1, x2, y2, pic_name, color_format, sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
pic_name 字符串:图片文件名
color_format 字符串:颜色格式串.

sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

字符串:
返回识别到的字符串

示例:

    s = vu.OcrInFile(0, 0, 2000, 2000, "test.bmp", "000000-000000", 1.0);

    std::cout << "识别文本:" << str << std::endl;

---

## 

函数简介:

保存指定的字库到指定的文件中

函数原型:

long SaveDict(index,file)

参数定义:

index 整数型:字库索引序号 

file 字符串:文件名

返回值:

整数型:
0:失败
1:成功

示例:

    vu.SetPath("c:\test_game");

    vu.AddDict(0, "FFF00A7D49292524A7D402805FFC$回$0.0.54$11");

    vu.AddDict(0, "3F0020087FF08270B9A108268708808$收$0.0.43$11");

    vu.AddDict(0, "2055C98617420807C097F222447C800$站$0.0.44$11");

    vu.SaveDict(0, "test.txt");

---

## 

函数简介:

设置字库文件

函数原型:

long SetDict(index,file)

参数定义:

index 整数型:字库的序号,支持任意正整数型,例如0或65535
file 字符串:字库文件名

返回值:

整数型:
0:失败
1:成功

示例:

    vu.SetPath("c:\test");

ret = vu.SetDict(0, "dict.txt");

注: 此函数速度很慢，全局初始化时调用一次即可，切换字库用UseDict

---

## 

函数简介:

从内存中设置字库

函数原型:

long SetDictMem(index,addr,size)

参数定义:

index 整数型:字库的序号,支持任意正整数型,例如0或65535
addr 整数型: 数据地址
size 整数型: 字库长度

返回值:

整数型:
0:失败
1:成功

示例:

ret = vu.SetDictMem(0,234324,1000);

注: 此函数速度很慢，全局初始化时调用一次即可，切换字库用UseDict

---

## 

函数简介:

表示使用哪个字库文件进行识别

设置之后，永久生效，除非再次设定

函数原型:

long UseDict(index)

参数定义:

index 整数型:字库编号(支持任意正整数型,例如0或65535)

返回值:

整数型:
0:失败
1:成功

示例:

    //使用序号为1的字库,进行ocr文字识别

    ret = vu.UseDict(1);

    res = vu.Ocr(0, 0, 2000, 2000, "ffffff-000000", 1.0);

    //切换为字库0

    ret = vu.UseDict(0);

    //其他操作

    //...

---

## 

函数简介:

把BGR的颜色格式转换为RGB

函数原型:

string BGR2RGB(bgr_color)

参数定义:

bgr_color 字符串:bgr格式的颜色字符串

返回值:

字符串:
RGB格式的字符串

示例:

rgb_color = vu.BGR2RGB(bgr_color)

---

## 

函数简介:

比较指定坐标点(x,y)的颜色

函数原型:

long CmpColor(x,y,color,sim)

参数定义:

x 整数型: X坐标

y 整数型: Y坐标

color 字符串: 颜色字符串,可以支持偏色,多色,例如 "ffffff-202020|000000-000000" 这个表示白色偏色为202020,和黑色偏色为000000.颜色最多支持10种颜色组合. 注意，这里只支持RGB颜色.

sim 双精度浮点型: 相似度(0.1-1.0)

返回值:

整数型:
0: 颜色匹配
1: 颜色不匹配

示例:

    ret = vu.CmpColor(200, 300, "000000-000000|ff00ff-101010", 0.9);

    if (ret == 0)

        std::cout << "颜色匹配" << std::endl;

---

## 

函数简介:

查找指定区域内的颜色,颜色格式"RRGGBB-DRDGDB"

函数原型:

long FindColor(x1, y1, x2, y2, color, sim, dir,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020". 也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020".  注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 
             1: 从左到右,从下到上 
             2: 从右到左,从上到下 
             3: 从右到左,从下到上 
             4：从中心往外查找
             5: 从上到下,从左到右 
             6: 从上到下,从右到左
             7: 从下到上,从左到右
             8: 从下到上,从右到左
intX 变参指针:返回X坐标
intY 变参指针:返回Y坐标

返回值:

整数型:
0:没找到
1:找到

示例:

    ret = vu.FindColor(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到颜色:" << intX << "," << intY << std::endl;

---

## 

函数简介:

查找指定区域内的颜色块,颜色格式"RRGGBB-DRDGDB"

函数原型:

long FindColorBlock(x1, y1, x2, y2, color, sim, count,width,height,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下方注释.注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0
count整数型:在宽度为width,高度为height的颜色块中，符合color颜色的最小数量.(注意,这个颜色数量可以在综合工具的二值化区域中看到)
width 整数型:颜色块的宽度
height 整数型:颜色块的高度
intX 变参指针:返回X坐标(指向颜色块的左上角)
intY 变参指针:返回Y坐标(指向颜色块的左上角)

返回值:

整数型:
0:没找到
1:找到

示例:

    ret = vu.FindColorBlock(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0, 350, 100, 200, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到色块:" << intX << "," << intY << std::endl;

---

## 

函数简介:

查找指定区域内的颜色块,颜色格式"RRGGBB-DRDGDB"

函数原型:

string FindColorBlockE(x1, y1, x2, y2, color, sim, count,width,height,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下方注释.注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0
count整数型:在宽度为width,高度为height的颜色块中，符合color颜色的最小数量.(注意,这个颜色数量可以在综合工具的二值化区域中看到)
width 整数型:颜色块的宽度
height 整数型:颜色块的高度

返回值:
字符串:
返回X和Y坐标 形式如"x,y", 比如"100,200"

示例:

    res = vu.FindColorBlockE(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0, 350, 100, 200);

    if (strstr(res, ","))

        std::cout << "找到色块:" << res << std::endl;

    else

        std::cout << "未找到" << std::endl;

---

## 

函数简介:

查找指定区域内的所有颜色块,颜色格式"RRGGBB-DRDGDB"

函数原型:

string FindColorBlockEx(x1, y1, x2, y2, color, sim, count,width,height,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下方注释.注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0
count整数型:在宽度为width,高度为height的颜色块中，符合color颜色的最小数量.(注意,这个颜色数量可以在综合工具的二值化区域中看到)
width 整数型:颜色块的宽度
height 整数型:颜色块的高度

返回值:
字符串:
返回所有颜色块信息的坐标值,然后通过GetResultCount等接口来解析

示例:

    res = vu.FindColorBlockEx(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0, 350, 100, 200);

    ret = vu.GetResultCount(res, "|", ",");

    for (long i = 0; i < ret; i++)

    {

        vu.GetResultPos(res, i, intX, intY, "|", ",");

        std::cout << "第" << i << "个色块:" << intX << "," << intY << std::endl;

    }

---

## 

函数简介:

查找指定区域内的颜色,颜色格式"RRGGBB-DRDGDB"

函数原型:

string FindColorE(x1, y1, x2, y2, color, sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 
             1: 从左到右,从下到上 
             2: 从右到左,从上到下 
             3: 从右到左,从下到上 
             4：从中心往外查找
             5: 从上到下,从左到右 
             6: 从上到下,从右到左
             7: 从下到上,从左到右
             8: 从下到上,从右到左

返回值:

字符串:
返回X和Y坐标 形式如"x,y", 比如"100,200"

示例:

    res = vu.FindColorE(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0, 0);

    if (strstr(res, ","))

        std::cout << "找到颜色:" << res << std::endl;

    else

        std::cout << "未找到" << std::endl;

---

## 

函数简介:

查找指定区域内的所有颜色,颜色格式"RRGGBB-DRDGDB"

函数原型:

string FindColorEx(x1, y1, x2, y2, color, sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 
             1: 从左到右,从下到上 
             2: 从右到左,从上到下 
             3: 从右到左,从下到上 
             4：从中心往外查找
             5: 从上到下,从左到右 
             6: 从上到下,从右到左
             7: 从下到上,从左到右
             8: 从下到上,从右到左

返回值:

字符串:
返回所有颜色信息的坐标值,然后通过GetResultCount等接口来解析

示例:

    res = vu.FindColorEx(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0, 0);

    ret = vu.GetResultCount(res, "|", ",");

    for (long i = 0; i < ret; i++)

    {

        vu.GetResultPos(res, i, intX, intY, "|", ",");

        std::cout << "第" << i << "个颜色:" << intX << "," << intY << std::endl;

    }

---

## 

函数简介:

查找指定区域内的所有颜色

函数原型:

long FindMulColor(x1, y1, x2, y2, color, sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下方注释.注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

整数型:
0:没找到或者部分颜色没找到
1:所有颜色都找到

示例:

    ret = vu.FindMulColor(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0);

    if (ret == 1)

        std::cout << "找到了" << std::endl;

---

## 

函数简介:

根据指定的多点查找颜色坐标

函数原型:

long FindMultiColor(x1, y1, x2, y2,first_color,offset_color,sim, dir,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
first_color 字符串:颜色格式为"RRGGBB-DRDGDB|RRGGBB-DRDGDB|…………",比如"123456-000000"

这里的含义和按键自带Color插件的意义相同，只不过我的可以支持偏色和多种颜色组合

所有的偏移色坐标都相对于此颜色.注意，这里只支持RGB颜色.
offset_color 字符串: 偏移颜色可以支持任意多个点 格式和按键自带的Color插件意义相同, 只不过我的可以支持偏色和多种颜色组合

格式为"x1|y1|RRGGBB-DRDGDB|RRGGBB-DRDGDB……,……xn|yn|RRGGBB-DRDGDB|RRGGBB-DRDGDB……"

比如"1|3|aabbcc|aaffaa-101010,-5|-3|123456-000000|454545-303030|565656"等任意组合都可以，支持偏色

还可以支持反色模式，比如"1|3|-aabbcc|-334455-101010,-5|-3|-123456-000000|-353535|454545-101010","-"表示除了指定颜色之外的颜色.

sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回X坐标(坐标为first_color所在坐标)
intY 变参指针:返回Y坐标(坐标为first_color所在坐标)

返回值:

整数型:
0:没找到
1:找到

示例:

    ret = vu.FindMultiColor(0, 0, 2000, 2000, "cc805b-020202|606060-010101", "9|2|-00ff00|-ff0000,15|2|2dff1c-010101,6|11|a0d962|aabbcc,11|14|-ffffff", 1.0, 1, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到多点颜色:" << intX << "," << intY << std::endl;

---

## 

函数简介:

根据指定的多点查找颜色坐标

函数原型:

string FindMultiColorE(x1, y1, x2, y2,first_color,offset_color,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
first_color 字符串:颜色格式为"RRGGBB-DRDGDB|RRGGBB-DRDGDB|…………",比如"123456-000000"

这里的含义和按键自带Color插件的意义相同，只不过我的可以支持偏色和多种颜色组合

所有的偏移色坐标都相对于此颜色.注意，这里只支持RGB颜色.
offset_color 字符串: 偏移颜色可以支持任意多个点 格式和按键自带的Color插件意义相同, 只不过我的可以支持偏色和多种颜色组合

格式为"x1|y1|RRGGBB-DRDGDB|RRGGBB-DRDGDB……,……xn|yn|RRGGBB-DRDGDB|RRGGBB-DRDGDB……"

比如"1|3|aabbcc|aaffaa-101010,-5|-3|123456-000000|454545-303030|565656"等任意组合都可以，支持偏色

还可以支持反色模式，比如"1|3|-aabbcc|-334455-101010,-5|-3|-123456-000000|-353535|454545-101010","-"表示除了指定颜色之外的颜色.

sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:
字符串:
返回X和Y坐标 形式如"x,y", 比如"100,200"

 

示例:

    res = vu.FindMultiColorE(0, 0, 2000, 2000, "cc805b-020202|606060-010101", "9|2|-00ff00|-ff0000,15|2|2dff1c-010101,6|11|a0d962|aabbcc,11|14|-ffffff", 1.0, 1);

    if (strstr(res, ","))

        std::cout << "找到多点颜色:" << res << std::endl;

    else

        std::cout << "未找到" << std::endl;

---

## 

函数简介:

根据指定的多点查找所有颜色坐标

函数原型:

string FindMultiColorEx(x1, y1, x2, y2,first_color,offset_color,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
first_color 字符串:颜色 格式为"RRGGBB-DRDGDB|RRGGBB-DRDGDB|…………",比如"123456-000000"

这里的含义和按键自带Color插件的意义相同，只不过我的可以支持偏色和多种颜色组合

所有的偏移色坐标都相对于此颜色.注意，这里只支持RGB颜色.
offset_color 字符串: 偏移颜色 可以支持任意多个点 格式和按键自带的Color插件意义相同, 只不过我的可以支持偏色和多种颜色组合

格式为"x1|y1|RRGGBB-DRDGDB|RRGGBB-DRDGDB……,……xn|yn|RRGGBB-DRDGDB|RRGGBB-DRDGDB……"

比如"1|3|aabbcc|aaffaa-101010,-5|-3|123456-000000|454545-303030|565656"等任意组合都可以，支持偏色

还可以支持反色模式，比如"1|3|-aabbcc|-334455-101010,-5|-3|-123456-000000|-353535|454545-101010","-"表示除了指定颜色之外的颜色.

sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:

字符串:
返回所有颜色信息的坐标值,然后通过GetResultCount等接口来解析

坐标是first_color所在的坐标

示例:

    res = vu.FindMultiColorEx(0, 0, 2000, 2000, "cc805b-020202|606060-010101", "9|2|-00ff00|-ff0000,15|2|2dff1c-010101,6|11|a0d962|aabbcc,11|14|-ffffff", 1.0, 1);

    ret = vu.GetResultCount(res, "|", ",");

    for (long i = 0; i < ret; i++)

    {

        vu.GetResultPos(res, i, intX, intY, "|", ",");

        std::cout << "第" << i << "个多点颜色:" << intX << "," << intY << std::endl;

    }

---

## 

函数简介:

查找指定的形状. 形状的描述同按键的抓抓. 具体可以参考按键的抓抓. 

函数原型:

long FindShape(x1, y1, x2, y2, offset_info,color_format,sim, dir,intX,intY)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
offset_info 字符串: 坐标偏移描述 可以支持任意多个点 格式和按键自带的Color插件意义相同

格式为"x1|y1|e1,……xn|yn|en"

比如"1|3|1,-5|-3|0"等任意组合都可以(含义:针对某个像素位置的颜色,相对偏移位置(1,3)像素颜色相同,(-5,-3)像素颜色不同,具体可以参考下方解释)

color_format 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上
intX 变参指针:返回X坐标(坐标为形状(0,0)所在坐标)
intY 变参指针:返回Y坐标(坐标为形状(0,0)所在坐标)

返回值:

整数型:
0:没找到
1:找到

示例:

    ret = vu.FindShape(0, 0, 2000, 2000, "1|1|0,1|6|1,0|10|1,9|10|1,7|6|1,7|8|0,8|9|0,2|2|1,3|1|1","203040", 1.0, 0, intX, intY);

    if (intX >= 0 && intY >= 0)

        std::cout << "找到形状:" << intX << "," << intY << std::endl;

 

假如结果intX=10,intY=20,而且图像中(10,20)坐标位置的颜色为ff00ff,那么offset_info参数中相对于坐标(10,20)各个相对位置匹配方式:

相对坐标1,1位置(图像坐标11,21)颜色不是ff00ff而且不在色偏203040范围内.

相对坐标1,6位置(图像坐标11,26)颜色是ff00ff或者在其色偏203040范围内.

相对坐标0,10位置(图像坐标10,30)颜色是ff00ff或者在其色偏203040范围内.

......

以此类推,直到将offset_info参数表示的形状完全匹配.

当然,在接口内部会将x1,y1,x2,y2区域内每个像素都按offset_info形状进行当前坐标颜色进行形状匹配.如果找到和形状描述相同的色块数据,则返回其坐标位置,否则返回0.

---

## 

函数简介:

查找指定的形状. 形状的描述同按键的抓抓. 具体可以参考按键的抓抓. 

函数原型:

string FindShapeE(x1, y1, x2, y2, offset_info,color_format,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
offset_info 字符串: 坐标偏移描述 可以支持任意多个点 格式和按键自带的Color插件意义相同

格式为"x1|y1|e1,……xn|yn|en"

比如"1|3|1,-5|-3|0"等任意组合都可以(含义:针对某个像素位置的颜色,相对偏移位置(1,3)像素颜色相同,(-5,-3)像素颜色不同,具体可以参考下方解释)

color_format 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:
字符串:
返回X和Y坐标 形式如"x,y", 比如"10,20"

示例:

    res = vu.FindShapeE(0, 0, 2000, 2000, "1|1|0,1|6|1,0|10|1,9|10|1,7|6|1,7|8|0,8|9|0,2|2|1,3|1|1", "203040", 1.0, 0);

    if (strstr(res, ","))

        std::cout << "找到形状:" << res << std::endl;

    else

        std::cout << "未找到" << std::endl;

 

假如结果res="10,20",而且图像中(10,20)坐标位置的颜色为ff00ff,那么offset_info参数中相对于坐标(10,20)各个相对位置匹配方式:

相对坐标1,1位置(图像坐标11,21)颜色不是ff00ff而且不在色偏203040范围内.

相对坐标1,6位置(图像坐标11,26)颜色是ff00ff或者在其色偏203040范围内.

相对坐标0,10位置(图像坐标10,30)颜色是ff00ff或者在其色偏203040范围内.

......

以此类推,直到将offset_info参数表示的形状完全匹配.

当然,在接口内部会将x1,y1,x2,y2区域内每个像素都按offset_info形状进行当前坐标颜色进行形状匹配.如果找到和形状描述相同的色块数据,则返回其坐标位置,否则返回0.

---

## 

函数简介:

查找所有指定形状的坐标. 形状的描述同按键的抓抓. 具体可以参考按键的抓抓. 

函数原型:

string FindShapeEx(x1, y1, x2, y2, offset_info,color_format,sim, dir)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
offset_info 字符串: 坐标偏移描述 可以支持任意多个点 格式和按键自带的Color插件意义相同

格式为"x1|y1|e1,……xn|yn|en"

比如"1|3|1,-5|-3|0"等任意组合都可以(含义:针对某个像素位置的颜色,相对偏移位置(1,3)像素颜色相同,(-5,-3)像素颜色不同,具体可以参考下方解释)

color_format 字符串:颜色色偏 比如"203040" 表示RGB的色偏分别是20 30 40 (这里是16进制表示) . 如果这里的色偏是2位，表示使用灰度找图. 比如"20"
sim 双精度浮点型:相似度,取值范围0.1-1.0
dir 整数型:查找方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

返回值:
字符串:
返回所有形状的坐标值,然后通过GetResultCount等接口来解析

示例:

    res = vu.FindShapeEx(0, 0, 2000, 2000, "1|1|0,1|6|1,0|10|1,9|10|1,7|6|1,7|8|0,8|9|0,2|2|1,3|1|1", "203040", 1.0, 0);

    ret = vu.GetResultCount(res, "|", ",");

    for (long i = 0; i < ret; i++)

    {

        vu.GetResultPos(res, i, intX, intY, "|", ",");

        std::cout << "第" << i << "个形状:" << intX << "," << intY << std::endl;

}

 

假如结果输出结果中有个坐标为"10,20",而且图像中(10,20)坐标位置的颜色为ff00ff,那么offset_info参数中相对于坐标(10,20)各个相对位置匹配方式:

相对坐标1,1位置(图像坐标11,21)颜色不是ff00ff而且不在色偏203040范围内.

相对坐标1,6位置(图像坐标11,26)颜色是ff00ff或者在其色偏203040范围内.

相对坐标0,10位置(图像坐标10,30)颜色是ff00ff或者在其色偏203040范围内.

......

以此类推,直到将offset_info参数表示的形状完全匹配.

当然,在接口内部会将x1,y1,x2,y2区域内每个像素都按offset_info形状进行当前坐标颜色进行形状匹配.如果找到和形状描述相同的色块数据,则返回其坐标位置,否则返回0.

---

## 

函数简介:

获取范围(x1,y1,x2,y2)颜色的均值,返回格式"RRGGBB"

函数原型:

string GetAveRGB(x1,y1,x2,y2)

参数定义:

x1 整数型: 左上角X

y1 整数型: 左上角Y

x2 整数型: 右下角X

y2 整数型: 右下角Y

返回值:

字符串:
颜色字符串

示例:

    color = vu.GetAveRGB(30, 30, 100, 100);

    std::cout << "平均颜色:" << color << std::endl;

---

## 

函数简介:

获取(x,y)的颜色,颜色返回格式"RRGGBB"

函数原型:

string GetColor(x,y)

参数定义:

x 整数型:X坐标
y 整数型:Y坐标

返回值:

字符串:
颜色字符串(注意这里都是小写字符，和工具相匹配)

示例:

    color = vu.GetColor(10, 20);

    std::cout << "颜色:" << color << std::endl;

---

## 

函数简介:

获取(x,y)的颜色,颜色返回格式"BBGGRR"

函数原型:

string GetColorBGR(x,y)

参数定义:

x 整数型:X坐标
y 整数型:Y坐标

返回值:

字符串:
颜色字符串(注意这里都是小写字符，和工具相匹配)

示例:

    color = vu.GetColorBGR(10, 20);

    std::cout << "颜色:" << color << std::endl;

---

## 

函数简介:

获取指定区域的颜色数量,颜色格式"RRGGBB-DRDGDB"

函数原型:

long GetColorNum(x1, y1, x2, y2, color, sim)

参数定义:

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标
color 字符串:颜色 格式为"RRGGBB-DRDGDB",比如"123456-000000|aabbcc-202020".也可以支持反色模式. 前面加@即可. 比如"@123456-000000|aabbcc-202020". 具体可以看下放注释.注意，这里只支持RGB颜色.
sim 双精度浮点型:相似度,取值范围0.1-1.0

返回值:

整数型:
颜色数量

示例:

    ret = vu.GetColorNum(0, 0, 2000, 2000, "123456-000000|aabbcc-030303|ddeeff-202020", 1.0);

    std::cout << "颜色数量:" << color << std::endl;

---

## 

函数简介:

把RGB的颜色格式转换为BGR

函数原型:

string RGB2BGR(rgb_color)

参数定义:

rgb_color 字符串:rgb格式的颜色字符串

返回值:

字符串:
BGR格式的字符串

示例:

bgr_color = dm.RGB2BGR(rgb_color)

---

## 

函数简介:

虚拟BOIS,将其序号虚拟为指定信息

函数原型:

LONG GuardBOIS(Serial_Number)

参数定义:

Serial_Number 字符串:需要被虚拟的指定序号,设置之后无法恢复,需要重启才能恢复原始序号,当调用成功后,系统任意程序都将只能获取本参数设置的序号,而非真实序号.

返回值:

整数型:

0:失败

1:成功

示例:

   ret = vu.GuardBOIS("AABBCCDDEEFFF");

---

## 

函数简介:

虚拟硬盘,将硬盘序号虚拟为指定信息

函数原型:

LONG GuardDisk(Serial_Number)

参数定义:

Serial_Number 字符串:需要被虚拟的指定序号,设置之后无法恢复,需要重启才能恢复原始序号,当调用成功后,系统任意程序都将只能获取本参数设置的序号,而非真实序号.

返回值:

整数型:

0:失败

1:成功

示例:

   ret = vu.GuardDisk("AABBCCDDEEFFF");

---

## 

函数简介:

对指定的所有应用程序进行环境隔离,使得互相之间无法在系统层面获取对方信息.

类似于沙盘保护,当前测试阶段,暂时可以完美做到实现类似于沙盘多开的效果.

请勿使用其进行任何非法行为!!!

函数原型:

LONG64 GuardEnvironment(exeName,title)

参数定义:

exeName 字符串:需要进行隔离的应用程序名字,例如360.exe

title 字符串:窗口标题,被隔离程序的窗口标题,支持模糊匹配,若为空则不进行窗口隔离.

返回值:

整数型:

0:失败

1:成功

示例:

    ret = vu.GuardEnvironment("360.exe", "杀毒软件");

---

## 

函数简介:

保护并隐藏文件,防止任何其他程序对指定文件进行读取.

开启后,除了调用插件的程序之外,任何人都无法看到该文件.

函数原型:

LONG64 GuardFile(path,enble)

参数定义:

path 字符串:要隐藏的文件路径

enble 整数型:是否开启,1表示打开,0表示关闭

返回值:

整数型:

0:失败

1:成功

示例:

    vu.GuardFile("d:\\game\\test.exe", 1);

---

## 

函数简介:

保护并隐藏文件夹,防止任何其他程序对指定文件夹内容进行读取.

开启后,除了调用插件的程序之外,任何人都无法看到文件夹.

函数原型:

LONG64 GuardFolder(path,enble)

参数定义:

path 字符串:要隐藏的文件夹路径

enble 整数型:是否开启,1表示打开,0表示关闭

返回值:

整数型:

0:失败

1:成功

示例:

    vu.GuardFolder("d:\\game\\", 1);

---

## 

函数简介:

虚拟GPU,将其序号虚拟为指定信息

函数原型:

LONG GuardGPU(Serial_Number)

参数定义:

Serial_Number 字符串:需要被虚拟的指定序号,设置之后无法恢复,需要重启才能恢复原始序号,当调用成功后,系统任意程序都将只能获取本参数设置的序号,而非真实序号.

返回值:

整数型:

0:失败

1:成功

示例:

   ret = vu.GuardGPU("AABBCCDDEEFFF");

---

## 

函数简介:

安装护盾驱动,某些功能想要正常使用前需要加载驱动,所以提供外部加载接口,避免调用失败。

需要用到护盾的功能一般有内存、HOOK、驱动后台、各种防护等功能,有时候直接调用可以成功,如果不成功则需要提前加载驱动。

函数原型:

LONG64 GuardInstall(LONG mode)

参数定义:

mode 整数型:驱动初始化模式,取值如下:

0:正常加载

1:vt模式加载,需要在bios中开启了vt. 仅支持intel的CPU.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.GuardInstall(1);

	ret = vu.GuardEnvironment("acle.exe","计算器");

---

## 

函数简介:

关闭指定进程指定类型的句柄.

使用本功能能够关闭任意程序的句柄、互斥体、信号量等内核对象.

请勿用其做侵害他人软件的违法活动,否则后果自负.

函数原型:

LONG GuardKillHandle(pid, type,name)

参数定义:

pid 整数型:目标进程的PID

type 字符串:要关闭的句柄类型,比如Section Event Mutant等. 具体的类型可以用pchunter查看

name 字符串:要关闭的句柄名字.一般为程序编程人员自定义的名字.

注意type和name都是大小写敏感的.

返回值:

整数型:

0:失败

1:成功

示例:

    vu.GuardKillHandle(1024, "Mutant","test");

    vu.GuardKillHandle(1024, "Event", "test");

---

## 

函数简介:

虚拟MAC,将其序号虚拟为指定信息

函数原型:

LONG GuardMAC(Serial_Number)

参数定义:

Serial_Number 字符串:需要被虚拟的指定序号,设置之后无法恢复,需要重启才能恢复原始序号,当调用成功后,系统任意程序都将只能获取本参数设置的序号,而非真实序号.

返回值:

整数型:

0:失败

1:成功

示例:

   ret = vu.GuardMAC("AABBCCDDEEFFF");

---

## 

函数简介:

保护指定的进程不被非法访问.

函数原型:

LONG64 GuardProcess(pid,enable,hide)

参数定义:

pid 整数型:要被保护的进程ID,如果为0则保护程序自身.

enable 整数型:是否开启,1表示打开,0表示关闭

hide 整数型:是否在隐藏,1表示隐藏,0表示不隐藏(可以在任务管理器中看到,如果enable为1则同样会进行保护,只是不进行隐藏而已)

返回值:

整数型:

0:失败

1:成功

示例:

    ret = vu.GuardProcess(1234, 1, 1);

---

## 

函数简介:

对指定进程虚拟注册表信息,当指定进程读取指定被虚拟的注册表项时,只会获取到我们虚拟的信息,无法获取真实注册表信息.

函数原型:

LONG GuardRegistry(pid,section,key,data,len)

参数定义:

pid 整数型:需要被虚拟的进程PID

section 字符串:注册表项名

key 字符串:注册表键名

data 长整数型:虚拟的数据的内存地址

len 长整数型:虚拟的数据的长度

返回值:

整数型:

0:失败

1:成功

示例:

std::string uuid = "{8BF606EC-F222-4B69-8A4D-CA2FF68AC9F6}";

ret = vu.GuardRegistry(10086, "HKEY_LOCAL_MACHINE\\SOFTWARE\\NVIDIA Corporation\\Global", "ClientUUID", uuid.data(), uuid.size());

 

//直接传入数据

BYTE data[1024] = { 0xAA,0xBB,0xCC,0xDD,0xEE,0xFF,0x11,0x22,0x33 };

ret = vu.GuardRegistry(10086, "HKEY_LOCAL_MACHINE\\SOFTWARE\\NVIDIA Corporation\\Global", "ClientUUID", data, sizeof(data));

---

## 

函数简介:

对指定进程虚拟注册表信息,当指定进程读取指定被虚拟的注册表项时,只会获取到我们虚拟的信息,无法获取真实注册表信息.

函数原型:

LONG GuardRegistryData(pid,section,key,data)

参数定义:

pid 整数型:需要被虚拟的进程PID

section 字符串:注册表项名

key 字符串:注册表键名

data 字符串:需要虚拟的二进制数据,例如”AA BB CC DD EE FF”

返回值:

整数型:

0:失败

1:成功

示例:

    std::string uuid = "{8BF606EC-F222-4B69-8A4D-CA2FF68AC9F6}";

    data = vu.BytesToData(uuid.data(), uuid.size());

    ret = vu.GuardRegistry(10086, "HKEY_LOCAL_MACHINE\\SOFTWARE\\NVIDIA Corporation\\Global", "ClientUUID", data);

---

## 

函数简介:

保护指定窗口句柄的窗口不被非法访问,可以完美过窗口扫描检测,包括类名和标题都无法被任何程序捕获.

函数原型:

LONG GuardWindow(hwnd,enable,display)

参数定义:

hwnd 整数型:需要被保护的窗口的窗口句柄

enable 整数型:是否开启,1表示打开,0表示关闭

display 整数型:是否防止截图,1表示防止截图,0表示不防止

返回值:

整数型:

0:失败

1:成功

示例:

    ret = vu.GuardWindow(hWnd, 1, 1);

---

## 

函数简介:

拷贝文件.

函数原型:

long CopyFile(src_file,dst_file,over)

参数定义:

src_file 字符串: 原始文件名

dst_file 字符串: 目标文件名.

over整数型: 取值如下,
            0 : 如果dst_file文件存在则不覆盖返回.
            1 : 如果dst_file文件存在则覆盖.

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    //绝对路径

    vu.CopyFile("c:\\123.txt", "d:\\456.txt", 1);

 

    //相对路径

    vu.SetPath("c:\\game\\");

    vu.CopyFile("123.txt", "456.txt", 1);

---

## 

函数简介:

创建指定目录.

函数原型:

long CreateFolder(folder)

参数定义:

folder 字符串: 目录名

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    vu.CreateFolder( "c:\\123\\456\\789")

---

## 

函数简介:

删除文件.

函数原型:

long DeleteFile(file)

参数定义:

file 字符串: 文件名

返回值:

整数型:
0 : 失败
1 : 成功

示例:

	//绝对路径

	ret = vu.DeleteFile("c:\\test.txt");

 

	//相对路径

	vu.SetPath("c:\\game\\");

	ret = vu.DeleteFile("test.txt");

---

## 

函数简介:

删除指定目录

函数原型:

long DeleteFolder(folder)

参数定义:

folder 字符串: 目录名

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    vu.DeleteFolder("c:\\game\\");

---

## 

函数简介:

获取当前程序路径

函数原型:

string GetCurrentFile()

参数定义:

无

返回值:

字符串:

当前的程序全路径

示例:

res = vu.GetCurrentFile();

---

## 

函数简介:

得到指定的路径

函数原型:

string GetDir(type)

参数定义:

type 整数型: 取值为以下类型

     0 : 获取当前路径

     1 : 获取系统路径(system32路径)

     2 : 获取windows路径(windows所在路径)

     3 : 获取临时目录路径(temp)

     4 : 获取当前进程(exe)所在的路径

返回值:

字符串:
返回路径

示例:

path = vu.GetDir(2)

---

## 

函数简介:

获取指定文件的属性

函数原型:

LONG GetFileAttribute(file)

参数定义:

file 字符串:文件名

返回值:

整数型:
返回文件的属性

示例:

    //绝对路径

    ret = vu.GetFileAttribute("c:\test.txt");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret = vu.GetFileAttribute("test.txt");

---

## 

函数简介:

获取指定的文件长度

函数原型:

long GetFileLength(file)

参数定义:

file 字符串: 文件名

返回值:

整数型:
文件长度(字节数)

示例:

    //绝对路径

    ret = vu.GetFileLength("c:\\test.txt");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret = vu.GetFileLength("test.txt");

---

## 

函数简介:

判断指定文件是否存在.

函数原型:

long IsFileExist(file)

参数定义:

file 字符串: 文件名

返回值:

整数型:
0 : 不存在
1 : 存在

示例:

    //判断绝对路径文件

    ret = vu.IsFileExist("c:\\test.txt");

 

    //判断相对路径文件

    vu.SetPath("c:\\game\\");

    ret = vu.IsFileExist("test.txt");

---

## 

函数简介:

判断指定目录是否存在.

函数原型:

long IsFolderExist (folder)

参数定义:

folder 字符串: 目录名

返回值:

整数型:
0 : 不存在
1 : 存在

示例:

    ret = vu.IsFolderExist ("c:\\game\\");

---

## 

函数简介:

移动文件

函数原型:

long MoveFile(src_file,dst_file)

参数定义:

src_file 字符串: 原始文件名

dst_file 字符串: 目标文件名

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    //绝对路径

    ret = vu.MoveFile("c:\\123.txt","d:\\456.txt");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret = vu.MoveFile("123.txt","456.txt");

---

## 

函数简介:

从指定的文件读取内容

函数原型:

string ReadFile(file)

参数定义:

file 字符串: 文件

返回值:

字符串:
读入的文件内容

示例:

    //绝对路径

    res = vu.ReadFile("c:\\test.txt");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    res = vu.ReadFile("test.txt");

---

## 

函数简介:

读取文件的二进制数据.

注意:本函数会将文件读入到插件内存中,每次调用都会将旧的数据释放,所以想要读入后能长久有效,请拷贝数据到自己程序内存.

函数原型:

LONG64 ReadFileData(file,len)

参数定义:

file 字符串:文件路径

len 变参指针:返回文件的大小

返回值:

长整数型:

返回文件读入插件后存放的内存地址

示例:

    //绝对路径

    ret= vu.ReadFileData("c:\\test.txt",len);

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret= vu.ReadFileData("test.txt",len);

---

## 

函数简介:

从Ini中读取指定信息

函数原型:

string ReadIni(section,key,file)

参数定义:

section 字符串: 小节名

key 字符串: 变量名.

file 字符串: ini文件名.

返回值:

字符串:
字符串形式表达的读取到的内容

示例:

    //绝对路径

    res = vu.ReadIni("Global", "var1", "c:\test_game\cfg.ini");

 

    //相对路径

    vu.SetPath("c:\\game\\");

res = vu.ReadIni("Global", "var1", "cfg.ini");

注 : 此函数是多线程安全的. 多线程同时读写同个文件不会造成文件错乱.

---

## 

函数简介:

弹出选择文件夹对话框，并返回选择的文件夹

函数原型:

string SelectDirectory()

参数定义:

无

返回值:

字符串:
选择的文件夹全路径

示例:

    res = vu.SelectDirectory();

std::cout << "选择目录的结果:" << res << std::endl;

注意:某些编程语言如果是在ui事件中调用本函数,可能会导致界面卡死,解决方法是使用线程,在线程中调用本函数.

---

## 

函数简介:

弹出选择文件对话框，并返回选择的文件

函数原型:

string SelectFile()

参数定义:

无

返回值:

字符串:
选择的文件全路径

示例:

    res = vu.SelectFile();

    std::cout << "选择文件的结果:" << res << std::endl;

---

## 

函数简介:

设置文件属性

函数原型:

LONG SetFileAttribute(file,attributes)

参数定义:

file 字符串:文件名

attributes 整数型:要被设置的属性,取值为以下类型
1:只读文件
2:隐藏不可见的
4:系统文件
16:指定的文件名是目录而非文件
若要具备多个属性,请将属性值相加,例如:2+4

 

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    //绝对路径

    ret = vu.SetFileAttribute("c:\test.txt", 1 + 2 + 4);

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret = vu.SetFileAttribute("test.txt", 1 + 2 + 4);

---

## 

函数简介:

向指定文件追加字符串

函数原型:

long WriteFile(file,content)

参数定义:

file 字符串: 文件

content 字符串: 写入的字符串

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    //绝对路径

    ret = vu.WriteFile("c:\\123.txt", "哈哈哈");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret = vu.WriteFile("123.txt", "哈哈哈");

---

## 

函数简介:

写入字节集数据到文件中

函数原型:

long WriteFileData(file,data,len,pos)

参数定义:

file 字符串:文件路径

data 长整数型:写入数据的指针

len 整数型:写入数据的大小

pos 整数型:要写入的位置,0表示从文件头开始,否则从指定的pos个字节的位置进行写入

返回值:

整数型:

0:失败

1:成功

示例:

    //绝对路径

    ret= vu.WriteFileData("c:\\test.txt",data,len,0);

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret= vu.ReadFileData("test.txt",data,len,0);

---

## 

函数简介:

向指定的Ini写入信息

函数原型:

long WriteIni(section,key,value,file)

参数定义:

section 字符串: 小节名

key 字符串: 变量名.

value 字符串: 变量内容

file 字符串: ini文件名

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    //绝对路径

    ret = vu.WriteIni("Global", "var1", "123","c:\test_game\cfg.ini");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    ret = vu.WriteIni("Global", "var1", "123", "cfg.ini");

---

## 

函数简介:

进入临界区,成功返回1,失败返回0. 此函数如果返回1，则调用对象就会占用此互斥信号量,直到此对象调用LeaveCri,否则不会释放.

注意:如果调用对象在释放时，会自动把本对象占用的互斥信号量释放.

另外,与EnterCriTry不同的是,EnterCriTry是会尝试一次进入临界区,无论是否成功都会立即返回,而本函数则是会在暂时无法进入时等待信号直到可以进入(会阻塞线程).

函数原型:

long EnterCri()

参数定义:

无

返回值:

整数型:
0 : 失败(可能临界区不存在)

1 : 已经进入临界区

示例:

    ret = vu.EnterCri();

    if (ret == 1)

    {

        //进入临界区成功

        //做一些事情

        //......

        //做完后记得退出临界区

    }

    else

    {

        std::cout << "进入临界区失败,请重新调用InitCri进行初始化" << std::endl;

    }

---

## 

函数简介:

尝试是否可以进入临界区,如果可以返回1,否则返回0. 此函数如果返回1，则调用对象就会占用此互斥信号量,直到此对象调用LeaveCri,否则不会释放.注意:如果调用对象在释放时，会自动把本对象占用的互斥信号量释放.

函数原型:

LONG EnterCriTry()

参数定义:

无

返回值:

整数型:
0 : 不可以

1 : 已经进入临界区

示例:

    ret = vu.EnterCriTry();

    if (ret == 1)

    {

        //进入临界区成功

        //做一些事情

        //......

        //做完后记得退出临界区

    }

    else

    {

        std::cout << "未进入临界区,请重新尝试" << std::endl;

    }

---

## 

函数简介:

初始化临界区,必须在脚本开头调用一次.这个函数是强制把插件内的互斥信号量归0,无论调用对象是否拥有此信号量.

函数原型:

long InitCri()

参数定义:

无

返回值:

整数型:
0 : 失败

1 : 成功

示例:

vu.InitCri();

---

## 

函数简介:

和EnterCri对应,离开临界区。此函数是释放调用对象占用的互斥信号量. 注意，只有调用对象占有了互斥信号量，此函数才会有作用. 否则没有任何作用. 如果调用对象在释放时，会自动把本对象占用的互斥信号量释放.

函数原型:

long LeaveCri()

参数定义:

无

返回值:

整数型:
0 : 失败

1 : 成功

示例:

vu.LeaveCri();

---

## 

函数简介:

设置当前对象的退出线程标记，之后除了调用此接口的线程之外，调用此对象的任何接口的线程会被强制退出.

函数原型:

long SetExitThread(mode)

参数定义:

enable 整数型: 1和2都为开启标记,0为关闭标记。 1和2的区别是,1会解绑当前对象的绑定,2不会.

返回值:

整数型:
0 : 失败

1 : 成功

示例:

vu.SetExitThread(1);

 

一般我们在写多线程程序时，如何正确的结束线程是个难题.  脚本语言一般没这种烦恼，但高级语言比如E vc等就很麻烦.
一般来说，让线程自然的结束，那是最好的结果. 但是事实上，高级语言中很难做到。 因为调用的函数是一层套一层，很难返回.
所以，我们退而求其次，让线程自己调用退出，这样虽然也有一定的资源泄漏（主要是线程中创建的局部变量，比如类对象等),但总比强制结束线程要好的多.
所以，我们这个接口的目的也很明显，设置以后，除了调用线程之外的线程，如果调用到插件，那么线程就自己退出了。

---

## 

函数简介:

设置调用对象的线程状态,用来暂停/恢复/停止当前对象线程.

本函数在暂停和停止线程时并不对绑定窗口进行解绑,可以在调用前后手动解绑.

函数原型:

LONG SetThreadStatus(status)

参数定义:

status 整数型:要设置的线程状态,取值如下

0:恢复线程正常状态

1:暂停调用本对象的线程

2:停止调用本对象的线程(强制结束)

返回值:

整数型:
0 : 失败

1 : 成功

示例:

    //暂停调用对象线程

    vu.SetThreadStatus(1);

    //可以进行其他操作

    //......

    //恢复调用对象线程

    vu.SetThreadStatus(0);

    //程序继续执行

 

    //停止

    vu.SetThreadStatus(2);

 

    //解绑

    vu.UnBindWindow();

---

## 

函数简介:

添加指定的MASM汇编指令. 支持标准的masm汇编指令. 

函数原型:

long AsmAdd(asm_ins)

参数定义:

asm_ins 字符串:MASM汇编指令,大小写均可以  比如 "mov eax,1" ,也支持直接加入字节，比如"emit 90 90 90 90"等. 

返回值:

整数型:
0:失败
1:成功

示例:

    vu.AsmAdd("push 0x100");

    vu.AsmAdd("push 0x60304d");

    vu.AsmAdd("emit 90 90 90");

    vu.AsmAdd("push qword ptr ds:[0x12345678]");

    vu.AsmAdd("call 0x123456789");

---

## 

函数简介:

执行用AsmAdd加到缓冲中的指令.

函数原型:

LONG64 AsmCall(hwnd,mode)

参数定义:

hwnd 整数型: 窗口句柄

mode 整数型: 模式，取值如下

0 : 在本进程中进行执行，这时hwnd无效. 注: 此模式会创建线程.

1 : 对hwnd指定的进程内执行,注入模式为创建远程线程

2 ：必须在对目标窗口进行注入绑定后,才可以用此模式(直接在目标进程创建线程).此模式下的call的执行是排队的,如果同时有多个call在此窗口执行,那么必须排队.所以执行效率不如模式1. 同时此模式受目标窗口刷新速度的影响,目标窗口刷新太慢，也会影响此模式的速度. 注: 此模式会创建线程.

3 ：同模式2,但是此模式不会创建线程,而直接在hwnd所在线程执行.
4 ：同模式0, 但是此模式不会创建线程,直接在当前调用AsmCall的线程内执行.
5 : 对hwnd指定的进程内执行,注入模式为APC. 此模式将加载驱动

6 : 直接hwnd所在线程执行. 此模式将加载驱动

返回值:

长整数型:

获取执行汇编代码以后的EAX的值(32位进程),或者RAX的值(64位进程).一般是函数的返回值. 如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

vu.AsmClear();

vu.AsmAdd("mov eax,1");

vu.AsmAdd("push 0123456");

vu.AsmAdd("call 0343434");

vu.AsmCall(hWnd, 1);

 

另要注意的是，AsmAdd里所有的数值都是16进制.

 

注: 这里特别对64位的汇编执行做一个简单的说明. 因为64位寻址的限制,那么类似下面的call可能会无法正确寻址.
call 0x1234aabbccdd
因为call 绝对地址只能寻址上下2G的范围,超过以后就无法寻址. 所以类似这样的语句，我们要改为下面的方式,比如
mov rax,0x1234aabbccdd
call rax

另外，由于64位调用的约定,前4个参数通过rcx rdx r8 r9来传递,后面的参数通过栈来传递,同时要给call预留28h字节的栈空间.
比如上面的call正确的写法如下:
mov rax,0x1234aabbccdd
sub rsp,0x28
call rax
add rsp,0x28

也就说，所有的call前后，一定得有sub rsp,0x28和add rsp,0x28

如果要传递超过4个参数，则按照从右往左的顺序压栈. 具体以MoveWindow这个接口为例.
BOOL WINAPI MoveWindow(HWND hWnd,int X,int Y,int nWidth,int nHeight, BOOL bRepaint)
MoveWindow这个API是6个参数,由于多了2个参数，所以这里的sub rsp,0x28也要改变，每个参数多8个字节(无论参数是不是8个字节). 也就是这里变成sub rsp,0x38
看这里的例子
mov rcx, hWnd   这里传入第一个参数hWnd
mov rdx, X      这里传入第二个参数X
mov r8d, Y      这里传入第三个参数Y
mov r9d, nWidth 这里传入第四个参数nWidth
mov r11,rsp 保存原始的rsp,方便后面传递参数
sub rsp,0x38
mov dword ptr[r11-0x10],bRepaint 这里传入第六个参数.(从右往左)
mov dword ptr[r11-0x18],nHeight  这里传入第五个参数.
call MoveWindow
add rsp,0x38

 

如何测试rsp需要增减多少?

假如你不知道调用call时传递了几个参数,导致在调用时目标程序发生崩溃,那么你可以尝试逐8个字节增减,最低从0x20开始,例如进行以下尝试:

add rsp,0x20

add rsp,0x28

add rsp,0x30

add rsp,0x38

add rsp,0x40

add rsp,0x48

add rsp,0x50

....

无论call需要传递多少个参数,逐个增加需要修改的rsp值,总有一个适合你的.

---

## 

函数简介:

执行用AsmAdd加到缓冲中的指令.  这个接口同AsmCall,但是由于插件内部在每次AsmCall时,都会有对目标进程分配内存的操作,这样会不够效率.
所以增加这个接口，可以让调用者指定分配好的内存,并在此内存上执行call的操作.

函数原型:

LONG64 AsmCallEx(hwnd,mode,base_addr)

参数定义:

hwnd 整数型: 窗口句柄

mode 整数型: 模式，取值如下

0 : 在本进程中进行执行，这时hwnd无效. 注: 此模式会创建线程.

1 : 对hwnd指定的进程内执行,注入模式为创建远程线程

2 ：必须在对目标窗口进行注入绑定后,才可以用此模式(直接在目标进程创建线程).此模式下的call的执行是排队的,如果同时有多个call在此窗口执行,那么必须排队.所以执行效率不如模式1. 同时此模式受目标窗口刷新速度的影响,目标窗口刷新太慢，也会影响此模式的速度. 注: 此模式会创建线程.

3 ：同模式2,但是此模式不会创建线程,而直接在hwnd所在线程执行.
4 ：同模式0, 但是此模式不会创建线程,直接在当前调用AsmCall的线程内执行.
5 : 对hwnd指定的进程内执行,注入模式为APC. 此模式将加载驱动

6 : 直接hwnd所在线程执行. 此模式将加载驱动

base_addr 字符串: 16进制格式. 比如"45A00000",此参数指定的地址必须要求有可读可写可执行属性. 并且内存大小最少要200个字节. 模式6要求至少400个字节. 如果Call的内容较多,那么长度相应也要增加.   如果此参数为空,那么效果就和AsmCall一样.

返回值:

长整数型:

获取执行汇编代码以后的EAX的值(32位进程),或者RAX的值(64位进程).一般是函数的返回值. 如果要想知道函数是否执行成功，请查看GetLastError函数.

示例:

base_addr = vu.VirtualAllocEx(hwnd, 0, 200, 0);

vu.AsmClear();

vu.AsmAdd("mov eax,1");

vu.AsmAdd("push 0123456");

vu.AsmAdd("call 0343434");

vu.AsmCallEx(hWnd, 1, vu.StrNumConvert(base_addr, 16));

vu.VirtualFreeEx(hwnd, base_addr);

 

    //或者直接使用AsmMemAlloc进行分配

    //完整代码如下

    vu.AsmClear();

    vu.AsmAdd("mov eax,1");

    vu.AsmAdd("push 0123456");

    vu.AsmAdd("call 0343434");

    ret = vu.AsmMemAlloc(hWnd, addr, size);

    vu.AsmCallEx(hWnd, 1, vu.StrNumConvert(addr, 16));

ret = vu.AsmMemFree(hWnd, addr);

 

另要注意的是，AsmAdd里所有的数值都是16进制.

 

注: 这里特别对64位的汇编执行做一个简单的说明. 因为64位寻址的限制,那么类似下面的call可能会无法正确寻址.
call 0x1234aabbccdd
因为call 绝对地址只能寻址上下2G的范围,超过以后就无法寻址. 所以类似这样的语句，我们要改为下面的方式,比如
mov rax,0x1234aabbccdd
call rax

另外，由于64位调用的约定,前4个参数通过rcx rdx r8 r9来传递,后面的参数通过栈来传递,同时要给call预留28h字节的栈空间.
比如上面的call正确的写法如下:
mov rax,0x1234aabbccdd
sub rsp,0x28
call rax
add rsp,0x28

也就说，所有的call前后，一定得有sub rsp,0x28和add rsp,0x28

如果要传递超过4个参数，则按照从右往左的顺序压栈. 具体以MoveWindow这个接口为例.
BOOL WINAPI MoveWindow(HWND hWnd,int X,int Y,int nWidth,int nHeight, BOOL bRepaint)
MoveWindow这个API是6个参数,由于多了2个参数，所以这里的sub rsp,0x28也要改变，每个参数多8个字节(无论参数是不是8个字节). 也就是这里变成sub rsp,0x38
看这里的例子
mov rcx, hWnd   这里传入第一个参数hWnd
mov rdx, X      这里传入第二个参数X
mov r8d, Y      这里传入第三个参数Y
mov r9d, nWidth 这里传入第四个参数nWidth
mov r11,rsp 保存原始的rsp,方便后面传递参数
sub rsp,0x38
mov dword ptr[r11-0x10],bRepaint 这里传入第六个参数.(从右往左)
mov dword ptr[r11-0x18],nHeight  这里传入第五个参数.
call MoveWindow
add rsp,0x38

 

如何测试rsp需要增减多少?

假如你不知道调用call时传递了几个参数,导致在调用时目标程序发生崩溃,那么你可以尝试逐8个字节增减,最低从0x20开始,例如进行以下尝试:

add rsp,0x20

add rsp,0x28

add rsp,0x30

add rsp,0x38

add rsp,0x40

add rsp,0x48

add rsp,0x50

....

无论call需要传递多少个参数,逐个增加需要修改的rsp值,总有一个适合你的.

---

## 

函数简介:

清除汇编指令缓冲区 用AsmAdd添加到缓冲的指令全部清除

函数原型:

long AsmClear()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.AsmClear()

---

## 

函数简介:

将使用AsmAdd加到缓冲中的指令写到内存中,函数内部会申请一段内存,使用完后需要调用AsmMemFree进行释放.

函数原型:

LONG64 AsmMemAlloc(hwnd,retAddr,retSize)

参数定义:

hwnd 整数型: 窗口句柄,若为0则写到本进程内存空间中

retAddr 变参指针:返回写入指令的内存地址(使用完毕后需要使用AsmMemFree释放此内存)

retSize 变参指针:返回写入指令的总字节数

返回值:

长整数型:
0:失败
1:成功

示例:

    vu.AsmAdd("push 0x100");

    vu.AsmAdd("push 0x60304d");

    vu.AsmAdd("emit 90 90 90");

    vu.AsmAdd("push qword ptr ds:[0x12345678]");

    vu.AsmAdd("call 0x123456789");

 

    ret = vu.AsmMemAlloc(hWnd, addr, size);

    std::cout << "内存地址:" << addr << std::endl;

    std::cout << "内存大小:" << size << std::endl;

---

## 

函数简介:

将AsmMemAlloc函数所分配的内存释放,以节省目标窗口的内存资源.

函数原型:

LONG64 AsmMemFree(hwnd,addr)

参数定义:

hwnd 整数型: 窗口句柄,若为0则写到本进程内存空间中

addr 长整数型:AsmMemAlloc所分配的内存地址

返回值:

长整数型:
0:失败
1:成功

示例:

ret = vu.AsmMemAlloc(hWnd, addr, size);

//做某些事情

//....

//在目标窗口中释放分配的内存

    ret = vu.AsmMemFree(hWnd, addr);

---

## 

函数简介:

把汇编缓冲区的指令转换为机器码 并用16进制字符串的形式输出

函数原型:

string Assemble(base_addr,is_64bit)

参数定义:

base_addr 长整数型: 用AsmAdd添加到缓冲区的第一条指令所在的地址

is_64bit  整数型:   表示缓冲区的指令是32位还是64位. 32位表示为0,64位表示为1

返回值:

字符串:
机器码，比如 "aa bb cc"这样的形式

示例:

    bin = vu.Assemble(0x123456, 0);

    std::cout << "Assemble:" << bin << std::endl;

---

## 

函数简介:

把指定的机器码转换为汇编语言输出

函数原型:

string DisAssemble(asm_code,base_addr, is_64bit)

参数定义:

asm_code 字符串: 机器码，形式如 "aa bb cc"这样的16进制表示的字符串(空格无所谓)

base_addr 长整数型: 指令所在的地址

is_64bit  整数型:  表示asm_code表示的指令是32位还是64位. 32位表示为0,64位表示为1

返回值:

字符串:
MASM汇编语言字符串.如果有多条指令，则每条指令以字符"\n"(换行)连接.

示例:

    sasm = vu.DisAssemble(bin, 0, TRUE);

    std::cout << "DisAssemble:" << sasm << std::endl;

---

## 

函数简介:

使用AsmCall时的hwnd参数当作进程pid. 注:仅对AsmCall的模式1起作用,因为其它模式都需要窗口.

函数原型:

long SetAsmHwndAsProcessId(enable)

参数定义:

enable 整数型: 0关闭,1打开

返回值:

整数型:
0:失败
1:成功

示例:

    vu.SetAsmHwndAsProcessId(1);

    vu.AsmCall(pid, 1);

---

## 

函数简介:

设置是否弹出汇编功能中的错误提示,默认是打开.

函数原型:

long SetShowAsmErrorMsg(show)

参数定义:

show 整数型: 0表示不打开,1表示打开

返回值:

整数型:
0 : 失败

1 : 成功

示例:

ret = vu.SetShowAsmErrorMsg(0)

---

## 

函数简介:

把窗口坐标转换为屏幕坐标

函数原型:

long ClientToScreen(hwnd,x,y)

参数定义:

hwnd 整数型: 指定的窗口句柄

x 变参指针: 窗口X坐标

y 变参指针: 窗口Y坐标

返回值:

整数型:

0: 失败

1: 成功

示例:

    x = 0, y = 0;

    ret = vu.ClientToScreen(hwnd, x, y);

---

## 

函数简介:

根据指定条件,枚举系统中符合条件的窗口

函数原型:

string EnumWindow(parent,title,class_name,filter)

参数定义:

parent 整数型: 获得的窗口句柄是该窗口的子窗口的窗口句柄,取0时为获得桌面句柄

title 字符串: 窗口标题. 此参数是模糊匹配.

class_name 字符串: 窗口类名. 此参数是模糊匹配.

filter整数型: 取值定义如下

1 : 匹配窗口标题,参数title有效 

2 : 匹配窗口类名,参数class_name有效.

4 : 只匹配指定父窗口的第一层孩子窗口

8 : 匹配父窗口为0的窗口,即顶级窗口

16 : 匹配可见的窗口

32 : 匹配出的窗口按照窗口打开顺序依次排列

这些值可以相加,比如4+8+16就是类似于任务管理器中的窗口列表

返回值:

字符串 :
返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"

示例:

hwnds = vu.EnumWindow(0, "QQ三国", "", 1 + 4 + 8 + 16);

---

## 

函数简介:

根据指定进程以及其它条件,枚举系统中符合条件的窗口

函数原型:

string EnumWindowByProcess(process_name,title,class_name,filter)

参数定义:

process_name 字符串: 进程映像名.比如(svchost.exe). 此参数是精确匹配,但不区分大小写.

title 字符串: 窗口标题. 此参数是模糊匹配.

class_name 字符串: 窗口类名. 此参数是模糊匹配.

filter 整数型: 取值定义如下

1 : 匹配窗口标题,参数title有效

2 : 匹配窗口类名,参数class_name有效

4 : 只匹配指定映像的所对应的第一个进程. 可能有很多同映像名的进程，只匹配第一个进程的.

8 : 匹配父窗口为0的窗口,即顶级窗口

16 : 匹配可见的窗口

32 : 匹配出的窗口按照窗口打开顺序依次排列

这些值可以相加,比如4+8+16

返回值:

字符串:
返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"

示例:

hwnds = vu.EnumWindowByProcess("game.exe","天龙八部","",1+8+16)

这句是获取到所有标题栏中有"天龙八部"这个字符串的窗口句柄集合,并且所在进程是"game.exe"指定的进程集合.

---

## 

函数简介:

根据指定进程pid以及其它条件,枚举系统中符合条件的窗口

函数原型:

string EnumWindowByProcessId(pid,title,class_name,filter) 

参数定义:

pid 整数型: 进程pid.

title 字符串: 窗口标题. 此参数是模糊匹配.

class_name 字符串: 窗口类名. 此参数是模糊匹配.

filter 整数型: 取值定义如下

1 : 匹配窗口标题,参数title有效

2 : 匹配窗口类名,参数class_name有效

8 : 匹配父窗口为0的窗口,即顶级窗口

16 : 匹配可见的窗口

这些值可以相加,比如2+8+16

返回值:

字符串:
返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"

示例:

hwnds = vu.EnumWindowByProcessId(1124,"天龙八部","",1+8+16)

这句是获取到所有标题栏中有"天龙八部"这个字符串的窗口句柄集合,并且所在进程是1124指定的进程.

---

## 

函数简介:

根据两组设定条件来枚举指定窗口

函数原型:

string EnumWindowSuper(spec1,flag1,type1,spec2,flag2,type2,sort) 

参数定义:

spec1 字符串: 查找串1. (内容取决于flag1的值)

flag1整数型: 取值如下:

   0表示spec1的内容是标题

   1表示spec1的内容是程序名字. (比如notepad)

   2表示spec1的内容是类名

   3表示spec1的内容是程序路径.(不包含盘符,比如\windows\system32)

   4表示spec1的内容是父句柄.(十进制表达的串)

   5表示spec1的内容是父窗口标题

   6表示spec1的内容是父窗口类名

   7表示spec1的内容是顶级窗口句柄.(十进制表达的串)

   8表示spec1的内容是顶级窗口标题

   9表示spec1的内容是顶级窗口类名

type1 整数型: 取值如下

0精确判断

1模糊判断

spec2 字符串: 查找串2. (内容取决于flag2的值)

flag2 整数型: 取值如下:

   0表示spec2的内容是标题

   1表示spec2的内容是程序名字. (比如notepad)

   2表示spec2的内容是类名

   3表示spec2的内容是程序路径.(不包含盘符,比如\windows\system32)

   4表示spec2的内容是父句柄.(十进制表达的串)

   5表示spec2的内容是父窗口标题

   6表示spec2的内容是父窗口类名

   7表示spec2的内容是顶级窗口句柄.(十进制表达的串)

   8表示spec2的内容是顶级窗口标题

   9表示spec2的内容是顶级窗口类名

type2  整数型: 取值如下

0精确判断

1模糊判断

sort  整数型: 取值如下

0不排序.

1对枚举出的窗口进行排序,按照窗口打开顺序.

返回值:

字符串:
返回所有匹配的窗口句柄字符串,格式"hwnd1,hwnd2,hwnd3"

示例:

hwnds = dm.EnumWindowSuper("记事本",0,1,"notepad",1,0,0)

---

## 

函数简介:

查找符合类名或者标题名的顶层可见窗口

函数原型:

long FindWindow(class,title) 

参数定义:

class 字符串: 窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.

title 字符串: 窗口标题,如果为空，则匹配所有.这里的匹配是模糊匹配

返回值:

整数型:
整形数表示的窗口句柄，没找到返回0

示例:

hwnd = vu.FindWindow("","记事本")

---

## 

函数简介:

根据指定的进程名字，来查找可见窗口

函数原型:

long FindWindowByProcess(process_name,class,title) 

参数定义:

process_name 字符串: 进程名. 比如(notepad.exe).这里是精确匹配,但不区分大小写.
class 字符串: 窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.

title 字符串: 窗口标题,如果为空，则匹配所有.这里的匹配是模糊匹配

返回值:

整数型:
整形数表示的窗口句柄，没找到返回0

示例:

hwnd = vu.FindWindowByProcess("noteapd.exe","","记事本")

---

## 

函数简介:

根据指定的进程Id，来查找可见窗口

函数原型:

long FindWindowByProcessId(process_id,class,title)

参数定义:

process_id 整数型: 进程id. 
class 字符串: 窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.

title 字符串: 窗口标题,如果为空，则匹配所有.这里的匹配是模糊匹配.

返回值:

整数型:
整形数表示的窗口句柄，没找到返回0

示例:

hwnd = vu.FindWindowByProcessId(123456,"","记事本")

---

## 

函数简介:

查找符合类名或者标题名的顶层可见窗口,如果指定了parent,则在parent的第一层子窗口中查找

函数原型:

long FindWindowEx(parent,class,title) 

参数定义:

parent 整数型: 父窗口句柄，如果为空，则匹配所有顶层窗口

class 字符串: 窗口类名，如果为空，则匹配所有. 这里的匹配是模糊匹配.

title 字符串: 窗口标题,如果为空，则匹配所有. 这里的匹配是模糊匹配

返回值:

整数型:
整形数表示的窗口句柄，没找到返回0

示例:

hwnd = vu.FindWindowEx(0,"","记事本")

---

## 

函数简介:

根据两组设定条件来查找指定窗口. 

函数原型:

long FindWindowSuper(spec1,flag1,type1,spec2,flag2,type2) 

参数定义:

spec1 字符串: 查找串1. (内容取决于flag1的值)

flag1整数型: 取值如下:

   0表示spec1的内容是标题

   1表示spec1的内容是程序名字. (比如notepad)

   2表示spec1的内容是类名

   3表示spec1的内容是程序路径.(不包含盘符,比如\windows\system32)

   4表示spec1的内容是父句柄.(十进制表达的串)

   5表示spec1的内容是父窗口标题

   6表示spec1的内容是父窗口类名

   7表示spec1的内容是顶级窗口句柄.(十进制表达的串)

   8表示spec1的内容是顶级窗口标题

   9表示spec1的内容是顶级窗口类名

type1 整数型: 取值如下

0精确判断

1模糊判断

spec2 字符串: 查找串2. (内容取决于flag2的值)

flag2 整数型: 取值如下:

   0表示spec2的内容是标题

   1表示spec2的内容是程序名字. (比如notepad)

   2表示spec2的内容是类名

   3表示spec2的内容是程序路径.(不包含盘符,比如\windows\system32)

   4表示spec2的内容是父句柄.(十进制表达的串)

   5表示spec2的内容是父窗口标题

   6表示spec2的内容是父窗口类名

   7表示spec2的内容是顶级窗口句柄.(十进制表达的串)

   8表示spec2的内容是顶级窗口标题

   9表示spec2的内容是顶级窗口类名

type2  整数型: 取值如下

0精确判断

1模糊判断

返回值:

整数型:
整形数表示的窗口句柄，没找到返回0

示例:

hwnd = vu.FindWindowSuper("记事本",0,1,"notepad",1,0)

---

## 

函数简介:

获取窗口客户区域在屏幕上的位置

函数原型:

long GetClientRect(hwnd,x1,y1,x2,y2) 

参数定义:

hwnd 整数型: 指定的窗口句柄
x1 变参指针: 返回窗口客户区左上角X坐标

y1 变参指针: 返回窗口客户区左上角Y坐标

x2 变参指针: 返回窗口客户区右下角X坐标

y2 变参指针: 返回窗口客户区右下角Y坐标

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.GetClientRect(hwnd,x1,y1,x2,y2)

---

## 

函数简介:

获取窗口客户区域的宽度和高度

函数原型:

long GetClientSize(hwnd,width,height) 

参数定义:

hwnd 整数型: 指定的窗口句柄
width 变参指针: 宽度

height 变参指针: 高度

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.GetClientSize(hwnd, w, h);

    std::cout << "宽:" << w << "高:" << h << std::endl;

---

## 

函数简介:

获取顶层活动窗口中具有输入焦点的窗口句柄

函数原型:

long GetForegroundFocus()

参数定义:

无

返回值:

整数型:
返回整型表示的窗口句柄

示例:

hwnd = vu.GetForegroundFocus()

---

## 

函数简介:

获取顶层活动窗口

函数原型:

long GetForegroundWindow() 

参数定义:

无

返回值:

整数型:
返回整型表示的窗口句柄

示例:

hwnd = vu.GetForegroundWindow()

---

## 

函数简介:

获取鼠标指向的可见窗口句柄

函数原型:

long GetMousePointWindow()

参数定义:

无

返回值:

整数型:
返回整型表示的窗口句柄

示例:

hwnd = vu.GetMousePointWindow()

---

## 

函数简介:

获取给定坐标的可见窗口句柄

函数原型:

long GetPointWindow(x,y) 

参数定义:

X 整数型: 屏幕X坐标

Y 整数型: 屏幕Y坐标

返回值:

整数型:
返回整型表示的窗口句柄

示例:

hwnd = vu.GetPointWindow(100,100)

---

## 

函数简介:

获取特殊窗口

函数原型:

long GetSpecialWindow(flag) 

参数定义:

Flag 整数型: 取值定义如下

0 : 获取桌面窗口

1 : 获取任务栏窗口

返回值:

整数型:
以整型数表示的窗口句柄

示例:

desk_win = vu.GetSpecialWindow(0)

---

## 

函数简介:

获取给定窗口相关的窗口句柄

函数原型:

long GetWindow(hwnd,flag)

参数定义:

hwnd 整数型: 窗口句柄

flag 整数型: 取值定义如下

0 : 获取父窗口

1 : 获取第一个儿子窗口

2 : 获取First 窗口

3 : 获取Last窗口

4 : 获取下一个窗口

5 : 获取上一个窗口

6 : 获取拥有者窗口

7 : 获取顶层窗口

返回值:

整数型:
返回整型表示的窗口句柄

示例:

own_hwnd = vu.GetWindow(hwnd,6)

---

## 

函数简介:

获取指定窗口边框的宽和高

函数原型:

LONG GetWindowBorder(hwnd,width,height)

参数定义:

hwnd 整数型: 指定的窗口句柄
width 变参指针: 返回窗口边框的宽度

height 变参指针: 返回窗口边框的高度

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.GetWindowBorder(hwnd, width, height);

---

## 

函数简介:

获取窗口的类名

函数原型:

string GetWindowClass(hwnd)

参数定义:

hwnd 整数型: 指定的窗口句柄

返回值:

字符串:
窗口的类名

示例:

class_name = vu.GetWindowClass(hwnd)

---

## 

函数简介:

获取指定窗口所在的进程ID

函数原型:
long GetWindowProcessId(hwnd) 

参数定义:

hwnd 整数型: 窗口句柄

返回值:

整数型:
返回整型表示的是进程ID

示例:

process_id = vu.GetWindowProcessId(hwnd)

---

## 

函数简介:

获取指定窗口所在的进程的exe文件全路径

函数原型:

string GetWindowProcessPath(hwnd)

参数定义:

hwnd 整数型: 窗口句柄

返回值:

字符串:
返回字符串表示的是exe全路径名

示例:

process_path = vu.GetWindowProcessPath(hwnd)

---

## 

函数简介:

获取窗口在屏幕上的位置

函数原型:

long GetWindowRect(hwnd,x1,y1,x2,y2) 

参数定义:

hwnd 整数型: 指定的窗口句柄
x1 变参指针: 返回窗口左上角X坐标

y1 变参指针: 返回窗口左上角Y坐标

x2 变参指针: 返回窗口右下角X坐标

y2 变参指针: 返回窗口右下角Y坐标

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.GetWindowRect(hwnd,x1,y1,x2,y2)

---

## 

函数简介:

获取窗口在屏幕上的位置以及窗口大小

函数原型:

LONG GetWindowRectSize(hwnd,x,y,w,h,type)

参数定义:

hwnd 整数型: 指定的窗口句柄
x变参指针: 返回窗口左上角X坐标

y变参指针: 返回窗口左上角Y坐标

w变参指针: 返回窗口宽度

h变参指针: 返回窗口高度

type 整数型:指定需要的类型,取值如下

0:获取完整窗口的位置和大小(正常窗口)

1:获取窗口中客户区位置和大小(不带标题和边框)

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.GetWindowRectSize(hwnd, x, y, w, h, 0);

---

## 

函数简介:

获取指定窗口的一些属性

函数原型:

long GetWindowState(hwnd,flag)

参数定义:

hwnd 整数型: 指定的窗口句柄
flag 整数型: 取值定义如下

0 : 判断窗口是否存在

1 : 判断窗口是否处于激活

2 : 判断窗口是否可见

3 : 判断窗口是否最小化

4 : 判断窗口是否最大化

5 : 判断窗口是否置顶

6 : 判断窗口是否无响应

7 : 判断窗口是否可用(灰色为不可用)

8 : 另外的方式判断窗口是否无响应,如果6无效可以尝试这个

9 : 判断窗口所在进程是不是64位

返回值:

整数型:
0: 不满足条件
1: 满足条件

示例:

    ret = vu.GetWindowState(hwnd, 3);

    if (ret == 1)

        std::cout << "窗口是最小化状态" << std::endl;

---

## 

函数简介:

获取指定窗口所在的线程ID

函数原型:

long GetWindowThreadId(hwnd)

参数定义:

hwnd 整数型: 窗口句柄

返回值:

整数型:
返回整型表示的是线程ID

示例:

thread_id = vu.GetWindowThreadId(hwnd)

---

## 

函数简介:

获取窗口的标题

函数原型:

string GetWindowTitle(hwnd)

参数定义:

hwnd 整数型: 指定的窗口句柄

返回值:

字符串:
窗口的标题

示例:

title = vu.GetWindowTitle(hwnd)

---

## 

函数简介:

移动指定窗口到指定位置

函数原型:

long MoveWindow(hwnd,x,y) 

参数定义:

hwnd 整数型: 指定的窗口句柄
x 整数型: X坐标

y 整数型: Y坐标

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.MoveWindow(hwnd, 100, 100);

---

## 

函数简介:

把屏幕坐标转换为窗口坐标

函数原型:

long ScreenToClient(hwnd,x,y)

参数定义:

hwnd 整数型: 指定的窗口句柄
x 变参指针: 屏幕X坐标

y 变参指针: 屏幕Y坐标

返回值:

整数型:
0: 失败
1: 成功

示例:

    x = 100, y = 100;

    ret = vu.ScreenToClient(hwnd, x, y);

---

## 

函数简介:

向指定窗口发送粘贴命令. 把剪贴板的内容发送到目标窗口

函数原型:

long SendPaste(hwnd) 

参数定义:

hwnd 整数型: 指定的窗口句柄. 如果为0,则对当前激活的窗口发送.

返回值:

整数型:
0: 失败
1: 成功

示例:

    vu.SetClipboard("abc123");

    vu.SendPaste(hwnd);

---

## 

函数简介:

向指定窗口发送文本数据

函数原型:

long SendString(hwnd,str) 

参数定义:

hwnd 整数型: 指定的窗口句柄. 如果为0,则对当前激活的窗口发送.
str 字符串: 发送的文本数据

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.SendString(hwnd, "测试发送文本");

---

## 

函数简介:

向指定窗口发送文本数据

函数原型:

long SendString2(hwnd,str) 

参数定义:

hwnd 整数型: 指定的窗口句柄. 如果为0,则对当前激活的窗口发送.
str 字符串: 发送的文本数据

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.SendString2(hwnd, "测试发送文本");

---

## 

函数简介:

向指定窗口发送文本数据,效果等同SendString只不过本函数是利用系统输入法执行输入文本.

函数原型:

long SendStringIme(hwnd,str) 

参数定义:

hwnd 整数型: 指定的窗口句柄. 如果为0,则对当前激活的窗口发送.
str 字符串: 发送的文本数据

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.SendStringIme(hwnd, "测试发送文本");

---

## 

函数简介:

设置窗口客户区域的宽度和高度

函数原型:

long SetClientSize(hwnd,width,height) 

参数定义:

hwnd 整数型: 指定的窗口句柄
width 整数型: 宽度

height 整数型: 高度

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.SetClientSize(hwnd, 800, 600);

---

## 

函数简介:

设置指定窗口在屏幕上的位置,已经重设窗口宽高

函数原型:

LONG SetWindowRectSize(hwnd,x,y,width,height,type)参数定义:

hwnd 整数型: 指定的窗口句柄

x整数型: 宽度

y整数型: 高度
width 整数型: 宽度

height 整数型: 高度

type 整数型: 高度

 

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.SetWindowRectSize(hwnd, 50, 50, 800, 600, 0);

---

## 

函数简介:

设置窗口的大小

函数原型:

long SetWindowSize(hwnd,width,height) 

参数定义:

hwnd 整数型: 指定的窗口句柄
width 整数型: 宽度

height 整数型: 高度

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.SetWindowSize(hwnd,300,400);

---

## 

函数简介:

设置窗口的状态

函数原型:

long SetWindowState(hwnd,flag) 

参数定义:

hwnd 整数型: 指定的窗口句柄

flag 整数型: 取值定义如下

0 : 关闭指定窗口

1 : 激活指定窗口

2 : 最小化指定窗口,但不激活

3 : 最小化指定窗口,并释放内存,但同时也会激活窗口.(释放内存可以考虑用FreeProcessMemory函数)

4 : 最大化指定窗口,同时激活窗口.

5 : 恢复指定窗口 ,但不激活

6 : 隐藏指定窗口

7 : 显示指定窗口

8 : 置顶指定窗口

9 : 取消置顶指定窗口

10 : 禁止指定窗口

11 : 取消禁止指定窗口

12 : 恢复并激活指定窗口

13 : 强制结束窗口所在进程.

14 : 闪烁指定的窗口

15 : 使指定的窗口获取输入焦点

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.SetWindowState(hwnd,0)

---

## 

函数简介:

设置窗口的标题

函数原型:

long SetWindowText(hwnd,title) 

参数定义:

hwnd 整数型: 指定的窗口句柄
titie 字符串: 标题

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.SetWindowText(hwnd,"test")

---

## 

函数简介:

设置窗口的透明度

函数原型:

long SetWindowTransparent(hwnd,trans) 

参数定义:

hwnd 整数型: 指定的窗口句柄
trans 整数型: 透明度取值(0-255) 越小透明度越大 0为完全透明(不可见) 255为完全显示(不透明)

返回值:

整数型:
0: 失败
1: 成功

示例:

ret = vu.SetWindowTransparent(hwnd,200)

---

## 

函数简介:

检测窗口是被挂起(卡死)

函数原型:

LONG WindowIsHunging(hwnd,time)

参数定义:

hwnd 整数型: 指定的窗口句柄
time 整数型: 检测超时时间,单位毫秒

返回值:

整数型:
0: 失败
1: 成功

示例:

    ret = vu.WindowIsHunging(hwnd, 1000);

---

## 

函数简介:

根据部分Ex接口的返回值，排除指定范围区域内的坐标.

函数原型:

string ExcludePos(all_pos,x1,y1,x2,y2,splitRows,splitCols)

参数定义:

all_pos 字符串: 坐标描述串。  一般是FindStrEx,FindStrFastEx,FindStrWithFontEx, FindColorEx, FindMultiColorEx,和FindPicEx的返回值.

x1 整数型: 左上角横坐标
y1 整数型: 左上角纵坐标
x2 整数型: 右下角横坐标
y2 整数型: 右下角纵坐标

splitRows字符串: 行分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的"|"

splitCols字符串: 列分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的","

返回值:

字符串:
经过筛选以后的返回值.

示例:

    res = vu.FindStrExS(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0);

    res = vu.ExcludePos(res, 100, 100, 300, 400, "|", ",");

    std::cout << "排除坐标范围后结果:" << res << std::endl;

---

## 

函数简介:

寻找多边形点集(坐标集合)中最短的边(表示线条的两个点A和B的xy值)

函数原型:

string FindMinDistanceLine(pos_list,beginX,beginY,endX,endY,splitRows,splitCols)

参数定义:

pos_list 字符串: 坐标描述集合,如果将这些坐标按顺序连接线条,那么应该是一个多边形图像.  也可以是FindStrEx,FindStrFastEx,FindStrWithFontEx, FindColorEx, FindMultiColorEx,和FindPicEx的返回值.

beginX 变参指针: 返回第一个点的X坐标
beginY 变参指针: 返回第一个点的Y坐标

endX 变参指针: 返回第二个点的X坐标
endY 变参指针: 返回第二个点的Y坐标

splitRows字符串: 行分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的"|"

splitCols字符串: 列分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的","

返回值:

字符串:
返回的内容为两个点的坐标,格式为:x1,y1|x2,y2

示例:

    res = "1,2|3,4|5,6|9,0|1,1";

    // 或者可以是

    res = vu.FindColorEx(0, 0, 2000, 2000, "aaaaaa-000000", 1.0, 0);

res = vu.FindMinDistanceLine(res, beginX, beginY, endX, endY, "|", ",");

std::cout << "多边形中最短的线条是: " << beginX << "," << beginY << "到" << endX << "," << endY << std::endl;

 

注意:此接口一般在图色识别中用不到,除非您有特殊需求.

它是为图像编辑而设计的,以获取多边形哪个边最短.

---

## 

函数简介:

根据部分Ex接口的返回值，然后在所有坐标里找出距离指定坐标最近的那个坐标.

函数原型:

string FindNearestPos(all_pos,x,y,splitRows,splitCols)

参数定义:

all_pos 字符串: 坐标描述串。  一般是FindStrEx,FindStrFastEx,FindStrWithFontEx, FindColorEx, FindMultiColorEx,和FindPicEx的返回值.

x 整数型: 横坐标
y 整数型: 纵坐标

splitRows字符串: 行分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的"|"

splitCols字符串: 列分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的","

返回值:

字符串:
返回的格式和传入的坐标描述符表示一致，例如传入的是"id0,x0,y0|id1,x1,y1",那么返回的格式是"id,x,y"

示例:

    res = vu.FindColorEx(0, 0, 2000, 2000, "aaaaaa-000000", 1.0, 0);

    res = vu.FindNearestPos(res, 100, 200, "|", ",");

    std::cout << "获取最近坐标的结果:" << res << std::endl;

---

## 

函数简介:

取线条倾斜角度

函数原型:

double GetLineAngle(beginX, beginY, endX, endY)

参数定义:

beginX 整数型:第一个坐标点的X值

beginY 整数型:第一个坐标点的Y值

endX 整数型:第二个坐标点的X值

endY 整数型:第二个坐标点的Y值

返回值:

双精度小数型:

线条的倾斜角度,取值范围(0-359)

示例:

    ret = vu.GetLineAngle(0, 0, 100, 100);

    std::cout << "线条的角度是:" << ret << std::endl;

---

## 

函数简介:

对插件部分接口的返回值进行解析,并返回ret中的坐标个数

函数原型:

long GetResultCount(ret,splitRows,splitCols)

参数定义:

ret 字符串: 部分接口的返回串

splitRows字符串: 行分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的"|"

splitCols字符串: 列分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的","

返回值:

整数型:
返回ret中的坐标个数

示例:

    res = vu.FindStrEx(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0);

    ret = vu.GetResultCount(res, "|", ",");

    std::cout<< "找到" << ret << "个结果" << std::endl;

---

## 

函数简介:

对插件部分接口的返回值进行解析,并根据指定的第index个坐标,返回具体的值

函数原型:

long GetResultPos(ret,index,& intX,& intY,splitRows,splitCols)

参数定义:

ret 字符串:部分接口的返回串
index 整数型: 第几个坐标
intX 变参指针: 返回X坐标
intY 变参指针: 返回Y坐标

splitRows字符串: 行分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的"|"

splitCols字符串: 列分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的","

返回值:

整数型:
0:失败
1:成功

示例:

    res = vu.FindStrEx(0, 0, 2000, 2000, "长安|洛阳", "9f2e3f-000000", 1.0);

    ret = vu.GetResultCount(res, "|", ",");

    std::cout<< "找到" << ret << "个结果" << std::endl;

    for (size_t i = 0; i < ret; i++)

    {

        vu.GetResultPos(res, i, intX, intY, "|", ",");

        std::cout << "第 " << i << " 个坐标 = " << intX << "," << intY << std::endl;

    }

---

## 

函数简介:

根据部分Ex接口的返回值，然后对所有坐标根据对指定坐标的距离(或者指定X或者Y)进行从小到大的排序.

函数原型:

string SortPosDistance(all_pos,x,y,splitRows,splitCols)

参数定义:

all_pos 字符串: 坐标描述串。  一般是FindStrEx,FindStrFastEx,FindStrWithFontEx, FindColorEx, FindMultiColorEx,和FindPicEx的返回值.

x 整数型: 横坐标 
y 整数型: 纵坐标

          注意:如果x为65535并且y为0时，那么排序的结果是仅仅对x坐标进行排序,如果y为65535并且x为0时，那么排序的结果是仅仅对y坐标进行排序.

splitRows字符串: 行分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的"|"

splitCols字符串: 列分隔符,例如ret="id0,x0,y0|id1,x1,y1"中的","

返回值:

字符串:
返回的格式和传入的坐标描述符表示一致，例如传入的是"id0,x0,y0|id1,x1,y1",那么返回的格式是"id,x,y"

示例:

    res = vu.FindColorEx(0, 0, 2000, 2000, "aaaaaa-000000", 1.0, 0);

    res = vu.SortPosDistance(res, 100, 200, "|", ",");

    std::cout << "获取最近坐标的结果:" << res << std::endl;

---

## 

函数简介:

将数值转为文本表示形式,本接口和StrToNum一个性质,都是对数值进行文本转换,只不过StrToNum是将文本型转为数值,而本接口是将数值转为文本型进行表示.

函数原型:

string StrNumConvert(num, radix)

参数定义:

num 双精度小数型:需要被转为文本的数值

radix 整数型:需要将num转换为文本的进制格式,例如10表示str是10进制数值文本,若为16则表示str是16进制数值文本

 

返回值:

文本型:

返回指定进制格式的数值文本,如果失败则返回空文本.

示例:

    ret = 65535;

 

    //将数值转10进制文本

    res = vu.StrNumConvert(ret, 10);

 

    //将数值转16进制文本

    res = vu.StrNumConvert(ret, 16);

 

    std::cout << "文本内容:" << res<< std::endl;

---

## 

函数简介:

分割字符串之后,使用本接口实现读取分割后数组中的字符串成员.

注意:必须先调用了StrSplitInit之后才能调用本接口,而且请保持调用本接口的对象和使用StrSplitInit的对象是同一个,只有这样才能获取到正确的分割文本数据.

函数原型:

string StrSplitGet(index)

参数定义:

index 整数型:要读取的分割数组的成员索引.

返回值:

字符串:

返回的内容为分割后指定索引的文本,若失败则返回空字符串.

示例:

    //1.新建一个vu对象

    vusoft vs;

    //2.定义文本内容,假设是"长安|洛阳|宝象国|花果山"

    res = "长安|洛阳|宝象国|花果山";

    //3.使用分割符"|"进行分割,并返回数组成员数

    num  = vs.StrSplitInit(res, "|");

    //4.获取指定索引的文本内容

    res = vs.StrSplitGet(2);

    std::cout << "获取到的字符串是:" << res << std::endl;

---

## 

函数简介:

字符串分割初始化,某些编程语言使用分割字符串不太方便,所以推出本接口,方便各语言调用.

注意:对某个字符串分割时,如果调用本接口,则会重置分割后的字符串数组,所以建议每次分割时用一个新的vu对象来调用,不要在同一个对象中重复使用本接口.

函数原型:

LONG StrSplitInit(str,split)

参数定义:

str 字符串:用来被分割的原始文本内容

split 字符串:指定的分割字符,不可以为空

返回值:

整数型:

分割成功后的字符串数组成员数量.若失败则返回0

示例:

    //1.新建一个vu对象

    vusoft vs;

    //2.定义文本内容,假设是"长安|洛阳|宝象国|花果山"

    res = "长安|洛阳|宝象国|花果山";

    //3.使用分割符"|"进行分割,并返回数组成员数

    num  = vs.StrSplitInit(res, "|");

    std::cout << "字符串分割后数组成员数:" << num << std::endl;

---

## 

函数简介:

将文本形式的字符串转为对应的数值,例如将十进制数值文本"65535"转为整数型65535,或者16进制数值文本"0xffff"转为整数型65535

函数原型:

DOUBLE StrToNum(str,radix)

参数定义:

str 字符串:数值的文本表现形式,例如十进制的"65535"或者十六进制的"0xffff"

radix 整数型:参数str的进制格式,例如10表示str是10进制数值文本,若为16则表示str是16进制数值文本

返回值::

双精度小数型:

转换后的数值,使用双精度小数接收返回值,或者您可以再次将其转为整数型.

示例:

    res = "65535";

    //参数是10进制的数值文本

    ret = (long)vu.StrToNum(res, 10);

    std::cout << "字符串" << res << "转为十进制数值是:" << ret << std::endl;

 

    //参数时十六进制的数值文本

    ret = (long)vu.StrToNum(res, 16);

    std::cout << "字符串" << res << "转为十六进制数值是:" << ret << std::endl;

---

## 

函数简介:

蜂鸣器

函数原型:

long Beep(f,duration)

参数定义:

f 整数型: 频率

duration 整数型: 时长(ms).

返回值:

整数型:
0 : 失败

1 : 成功

示例:

    vu.Beep(1000, 500);

---

## 

函数简介:

延时指定的毫秒,过程中不阻塞UI操作

函数原型:

long Delay(mis)

参数定义:

mis整数型: 毫秒数. 必须大于0

返回值:

整数型:
0 : 失败

1 : 成功

示例:

vu.Delay(1000);

---

## 

函数简介:

设置当前的电源设置，禁止关闭显示器，禁止关闭硬盘，禁止睡眠，禁止待机. 不支持XP

函数原型:

long DisableCloseDisplayAndSleep()

参数定义:

无

返回值:

整数型:
0 : 失败

1 : 成功

示例:

vu.DisableCloseDisplayAndSleep()

---

## 

函数简介:

执行指定的CMD指令,并返回cmd的输出结果

函数原型:

string ExecuteCmd(cmd,current_dir,time_out)

参数定义:

cmd字符串: 需要执行的CMD指令. 比如"dir"

current_dir字符串: 执行此cmd命令时,所在目录. 如果为空，表示使用当前目录. 比如""或者"c:"

time_out 整数型: 超时设置,单位是毫秒. 0表示一直等待. 大于0表示等待指定的时间后强制结束,防止卡死

返回值:

字符串: cmd指令的执行结果.  返回空字符串表示执行失败

示例:

    res = vu.ExecuteCmd("dir", "", 0);

    res = vu.ExecuteCmd("dir", "c:", 2000);

res = vu.ExecuteCmd("dir", "c:\windows", 3000);

 

介于很多人不会用命令行操作CMD,这里写一份常用的adb命令来给大家参考.

 

首先,adb.exe是一个操作android系统的应用程序，一般都在你安装的模拟器的对应的目录下. 

 

比如雷电模拟器,我们假如安装再d:\dnplayer2,那么adb.exe一般就位于这个目录. 其它模拟器同理.

 

知道adb.exe的路径，那么我们就开始调用adb来实现一些常用的功能. 以下所有的例子，都假定adb.exe位于d:\dnplayer2

 

1. 查看adb的版本信息. 这个可以用于测试adb.exe是否是你想要的版本,如下:

adb_version = vu.ExecuteCmd("adb.exe version","d:\dnplayer2",0)

比如我的机器的返回值是以下内容

Android Debug Bridge version 1.0.31

 

2. 接下来我们开始对模拟器里的东东做一些操作.比如安装APK，拷贝文件之类的。 我们首先要先列出当前系统的所有device(可以是模拟器，也可以是用USB连接的手机),例子如下:

adb_devices = vu.ExecuteCmd("adb.exe devices","d:\dnplayer2",0)

比如我的机器的返回值如下:(我打开了2个模拟器)

List of devices attached

127.0.0.1:5555    device

127.0.0.1:5557    device

 

这里要说明一下,前面这个IP地址和端口号，就标识了一个device,我们后面要操作这些devcie，必须依赖于这个标识.

有的时候，这个标识不一定是ip地址和端口号，也可能是序列号之类的东西. 但意思都一样.

 

3. 接下来我们来对127.0.0.1:5555这个device来查看下安装的应用,例子如下:(这里我们要用到adb shell命令,顾名思义，这个shell的意思就是去device上去执行命令,这里的语法都和linux的语法一样)

adb_device_1_apps = vu.ExecuteCmd("adb.exe -s 127.0.0.1:5555 shell pm list packages","d:\dnplayer2",0)

这里输出的内容比较多，我就不列举了

简单的说一下，这里的-s 设备标识 的意思就是对这台device来执行命令.  设备标识在之前adb devices中有列出来.

 

那么我们要执行其它的操作，也是如此,比如"adb.exe -s 设备标识  命令"

比如安装apk

vu.ExecuteCmd("adb.exe -s 127.0.0.1:5555 install -r d:\xxx.apk","d:\dnplayer2",0)

比如卸载某apk

vu.ExecuteCmd("adb.exe -s 127.0.0.1:5555 uninstall com.qihoo360.mobilesafe","d:\dnplayer2",0)

 

 

好到此为止，如何操作adb去控制模拟器，就说到这里。  

这里贴一份常用详细的adb中文说明给大家参考

https://blog.csdn.net/u010375364/article/details/52344120

---

## 

函数简介:

获取剪贴板的内容

函数原型:

string GetClipboard()

参数定义:

无

返回值:

字符串:
以字符串表示的剪贴板内容

示例:

    res = vu.GetClipboard();

    std::cout << "剪切板内容:" << res << std::endl;

---

## 

函数简介:

查询CPU名称

函数原型:

string GetCpuName()

参数定义:

无

返回值:

整数型:

CPU名称

示例:

    res = vu.GetCpuName();

    std::cout << "CPU名称:" << res << std::endl;

---

## 

函数简介:

获取当前CPU的使用率. 用百分比返回

函数原型:

long GetCpuUsage()

参数定义:

无

返回值:

整数型:
0-100表示的百分比

示例:

ret = vu.GetCpuUsage()

---

## 

函数简介:

获取本机硬盘的序列号.要求调用进程必须有管理员权限. 否则返回空串.

函数原型:

string GetDiskSerial()

参数定义:

无

返回值:

字符串:
字符串表达的硬盘序列号

示例:

sirial = vu.GetDiskSerial()

---

## 

函数简介:

获取GPU共享内存占用率,用百分比返回

注意:这里获取到的是GPU的共享内存占用,若要获取常规意思的显存占用,请使用GetGpuMemUsage

函数原型:

LONG GetGpuMemShareUsage()

参数定义:

无

返回值:

整数型:
0-100表示的百分比

示例:

ret = vu.GetGpuMemShareUsage()

---

## 

函数简介:

获取GPU显存占用率(专用内存),用百分比返回

注意:这里获取到的是常规意义上的显存占用率,若要获取GPU的共享内存占用率,请使用GetGpuMemShareUsage

函数原型:

LONG GetGpuMemUsage()

参数定义:

无

返回值:

整数型:
0-100表示的百分比

示例:

ret = vu.GetGpuMemUsage()

---

## 

函数简介:

查询GPU名称

函数原型:

string GetGpuName()

参数定义:

无

返回值:

整数型:

GPU名称

示例:

    res = vu.GetGpuName();

    std::cout << "GPU名称:" << res << std::endl;

---

## 

函数简介:

获取当前GPU的使用率. 用百分比返回

函数原型:

long GetGpuUsage()

参数定义:

无

返回值:

整数型:
0-100表示的百分比

示例:

ret = vu.GetGpuUsage()

---

## 

函数简介:

获取当前内存的使用率. 用百分比返回.

函数原型:

LONG GetMemUsage()

参数定义:

无

返回值:

整数型:
0-100表示的百分比

示例:

ret = vu.GetMemUsage();

---

## 

函数简介:

得到操作系统的类型

函数原型:

long GetOsType()

参数定义:

返回值:

整数型:
0 : win95/98/me/nt4.0

1 : xp/2000

2 : 2003/2003 R2/xp-64

3 : vista/2008

4 : win7/2008 R2

5 : win8/2012

6 : win8.1/2012 R2	

7 : win10/2016 TP/win11

示例:

    os_type = vu.GetOsType();

---

## 

函数简介:

获取屏幕的高度

函数原型:

long GetScreenHeight()

参数定义:

无

返回值:

整数型:
返回屏幕的高度

示例:

    ScreenH = vu.GetScreenHeight();

---

## 

函数简介:

获取屏幕的宽度

函数原型:

long GetScreenWidth()

参数定义:

无

返回值:

整数型:
返回屏幕的宽度

示例:

    ScreenW = vu.GetScreenWidth();

---

## 

函数简介:

获取当前系统从开机到现在所经历过的时间，单位是毫秒

函数原型:

long GetTime()

参数定义:

无

返回值:

整数型:
时间(单位毫秒)

示例:

    long t1, t2;

    t1 = vu.GetTime();

    ret = vu.FindPic(0, 0, 2000, 2000, "test.bmp", "000000", 1.0, 0, x, y);

    t2 = vu.GetTime();

    std::cout << "耗时:" << t2 - t1 << "毫秒" << std::endl;

---

## 

函数简介:

判断当前系统是否是64位操作系统

函数原型:

long Is64Bit()

参数定义:

无

返回值:

整数型:
0 : 不是64位系统
1 : 是64位系统

示例:

    ret = vu.Is64Bit();

    if(ret==1)

        std::cout << "64位" << std::endl;

    else

        std::cout << "32位" << std::endl;

---

## 

函数简介:

判断当前CPU是否支持vt,并且是否在bios中开启了vt. 仅支持intel的CPU

函数原型:

long IsSurrpotVt()

参数定义:

无

返回值:

整数型:
0 : 当前cpu不是intel的cpu,或者当前cpu不支持vt,或者bios中没打开vt.
1 : 支持

示例:

    ret = vu.IsSurrpotVt();

    if (ret == 1)

        std::cout << "支持VT" << std::endl;

    else

        std::cout << "不支持VT" << std::endl;

---

## 

函数简介:

播放指定的MP3或者wav文件.

函数原型:

long Play(media_file)

参数定义:

media_file 字符串: 指定的音乐文件，可以采用文件名或者绝对路径的形式.

返回值:

整数型:
0 : 失败
非0表示当前播放的ID。可以用Stop来控制播放结束.

示例:

    //绝对路径

    id = vu.Play("c:\test.mp3");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    id = vu.Play("test.mp3");

 

    vu.Delay(1000);

 

    vu.Stop(id);

---

## 

函数简介:

运行指定的应用程序

函数原型:

long RunApp(app_path,mode)

参数定义:

app_path 字符串: 指定的可执行程序全路径.

mode 整数型: 取值如下

      0 : 普通模式

      1 : 加强模式

返回值:

整数型:
0 : 失败

1 : 成功

示例:

    vu.RunApp("c:/windows/notepad.exe",0);

    vu.RunApp("notepad.exe", 1);

---

## 

函数简介:

设置剪贴板的内容

函数原型:

long SetClipboard(value)

参数定义:

value 字符串: 以字符串表示的剪贴板内容

返回值:

整数型:
0 : 失败
1 : 成功

示例:

vu.SetClipboard(“111222333”)

---

## 

函数简介:

设置系统的分辨率

函数原型:

long SetScreen(width,height)

参数定义:

width 整数型: 屏幕宽度

height 整数型: 屏幕高度

返回值:

整数型:
0 : 失败

1 : 成功

示例:

    ret = vu.SetScreen(1024, 768);

---

## 

函数简介:

设置当前系统的UAC(用户账户控制).

函数原型:

long SetUAC(enable)

参数定义:

enable 整数型: 取值如下

		 0 : 关闭UAC
       1 : 开启UAC

返回值:
整数型:
0 : 操作失败

1 : 操作成功

示例:

    ret = vu.SetUAC(0);

    if (ret == 1)

        std::cout << "设置成功" << std::endl;

    else

        std::cout << "设置失败" << std::endl;

注: 只有WIN7 WIN8 VISTA WIN2008以及以上系统才有UAC设置. 关闭UAC以后，必须重启系统才会生效.

如果关闭了UAC，那么默认启动所有应用程序都是管理员权限，就不会再发生绑定失败这样的尴尬情况了

---

## 

函数简介:

停止指定的音乐

函数原型:

long Stop(id)

参数定义:

id 整数型: Play返回的播放id.

返回值:

整数型:
0 : 失败
1 : 成功

示例:

    //绝对路径

    id = vu.Play("c:\test.mp3");

 

    //相对路径

    vu.SetPath("c:\\game\\");

    id = vu.Play("test.mp3");

 

    vu.Delay(1000);

//停止

    vu.Stop(id);

---

## 

函数简介:

系统退出(关机,重启,注销)

函数原型:

LONG SysExitOs(type)

参数定义:

type 整数型:系统退出模式,取值如下
0:注销
1:关机
2:重启

返回值:

整数型:

0:失败

1:成功

示例:

    vu.SysExitOs(1);

---

## 

函数简介:

清除绘制内容,本函数用来清空上一帧渲染的所有绘制内容,必须在每帧的绘制之前调用本函数,否则旧的绘制内容会残留在屏幕上.

需要与DrawRender()成对使用,才能正确进行绘制图形.

函数原型:

LONG DrawClear()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

示例:

以下示例构建了一个完整的渲染循环,专门用来绘制文本/线条/图像等元素.

推荐在创建绘制之后,使用线程调用渲染循环.

// 渲染循环,最好使用线程调用本函数,在循环中进行绘制

DWORD WINAPI DrawLoop(LPVOID arg)

{

    DWORD res = 0;

    vusoft* vu = (vusoft*)arg;

 

    // 渲染循环

    while (vu->DrawIsRunning())

    {

        // 清除绘制内容

        vu->DrawClear();

 

        std::string strFps = std::to_string(vu->DrawGetFps());

        strFps = "FPS:" + strFps;

        // 绘制字符串

        vu->DrawString(strFps.c_str(), 0, 0, 0x00ffff, 255, "微软雅黑", 0, 0, 20);

 

        // 绘制直线

        vu->DrawLine(0, 0, 100, 200, 0xFF00FF, 255, 2);

 

        // 绘制多边形

        vu->DrawPolygon(300, 300, 0x00ffff, 128, 0);

        vu->DrawPolygon(400, 200, 0x00ffff, 128, 0);

        vu->DrawPolygon(600, 600, 0x00ffff, 128, 2);

 

        // 绘制矩形

        vu->DrawRectangle(400, 400, 500, 500, 20, 20, 0xffffff, 128, 0, 128, 1, 3);

 

        // 绘制椭圆

        vu->DrawEllipse(300, 300, 50, 80, 0xffffff, 128, 0xff00ff, 128, 2, 3);

 

        // 绘制图片

        vu->DrawImg(1, 100, 100, 100, 100, 255, 0);

 

 

        // 渲染

        vu->DrawRender();

    }

    return res;

}

---

## 

函数简介:

创建绘制,默认创建一个指定位置和宽高的透明窗口,并且使用dx设备进行渲染,可以通过DrawSetStyle()以及DrawSetPosition()修改窗体属性.

函数原型:

LONG DrawCreate(int x, int y, int w, int h, int isFast)

参数定义:

x 整数型:绘制窗口的x坐标.

y 整数型:绘制窗口的y坐标.

w 整数型:绘制窗口的宽度.

h 整数型:绘制窗口的高度.

isFast 整数型:是否极速渲染,取值如下:

0:正常模式(支持跨机绘制.)

1:极速模式(不支持跨机,仅可以本机绘制.)

返回值:

整数型:

返回创建的绘制窗口的句柄,失败返回0.

如果失败,可以通过调用DrawGetError()来获取错误信息.

示例:

	vusoft vu;

	vu.Create(); // 或者使用CreateRemote()创建跨机绘制

	LONG hwnd = NULL;

	hwnd = vu.DrawCreate(0, 0, 800, 600, 0);

	std::cout << "hwnd:" << hwnd << std::endl;

---

## 

函数简介:

创建绘制,此函数创建的绘制将与目标窗口绑定,并且始终贴在目标窗口表面,当目标窗口关闭后,绘制也会结束.(不支持跨机绘制)

函数原型:

LONG DrawCreateByWindow(LONG hTarget)

参数定义:

hTarget 整数型:目标窗口的窗口句柄.

返回值:

整数型:

返回创建的绘制窗口的句柄,失败返回0.

如果失败,可以通过调用DrawGetError()来获取错误信息.

示例:

	vusoft vu;

	vu.Create(); // 不支持使用CreateRemote()创建跨机绘制

	LONG hTarget = vu.FindWindow(NULL, "测试测试测试");

	LONG hwnd = NULL;

	hwnd = vu.DrawCreateByWindow(hTarget);

	std::cout << "hwnd:" << hwnd << std::endl;

---

## 

函数简介:

绘制圆形/椭圆

函数原型:

LONG DrawEllipse(x, y, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode)

参数定义:

x 整数型:中心点x坐标.

y 整数型:中心点y坐标.

radiusX 整数型:x轴半径长度.

radiusY 整数型:y轴半径长度.

rgbFill 整数型:填充颜色值.

alphaFill 整数型:填充颜色透明度,取值范围0-255,值越大越不透明.

rgbSide 整数型:边框的颜色值.

alphaSide 整数型:边框的颜色透明度,取值范围0-255,值越大越不透明.

sideWidth 整数型:边框线条的粗细粒度.

mode 整数型:绘制模式,取值如下:

1:只画边,不填充颜色.

2:只填充颜色,不画边.

3:既填充颜色,也画边.

返回值:

整数型:

0:失败

1:成功

示例:

    // 绘制椭圆,只画边,蓝色

    vu->DrawEllipse(100, 100, 10, 20, -1, -1, 0x0000FF, 255, 1, 1);

 

    // 绘制圆形,只填充,红色

    vu->DrawEllipse(200, 200, 20, 20, 0xFF0000, 255, -1, -1, -1, 2);

 

    // 绘制椭圆,白色半透明填充,黑色半透明边框,线宽为5

    vu->DrawEllipse(300, 300, 20, 10, 0xFFFFFF, 128, 0x000000, 128, 5, 3);

---

## 

函数简介:

获取绘制函数的错误信息.

函数原型:

string DrawGetError()

参数定义:

无

返回值:

字符串:

返回当前Draw_XXXX系列函数的错误信息.

示例:

	err = vu.DrawGetError();

	std::cout << err << std::endl;

---

## 

函数简介:

获取绘制的FPS(每秒渲染的帧数).

函数原型:

LONG DrawGetFps()

参数定义:

无

返回值:

整数型:

返回当前绘制的FPS.

示例:

		LONG nFPS = vu.DrawGetFps();

		std::cout << "FPS:" << nFPS << std::endl;

---

## 

函数简介:

绘制图片.

将预加载的图片进行渲染,只有调用本函数后,图片才会显示出来.

函数原型:

LONG DrawImg(LONG64 id, int x, int y, int w, int h, int alpha, int maintain)

参数定义:

id 长整数型:图片id,可以通过DrawImgLoad()函数在加载图片时进行指定.

x 整数型:指定绘制图片的左上角x坐标.

y 整数型:指定绘制图片的左上角y坐标.

w 整数型:指定绘制图片的宽度.若取值为-1,则不更改宽度.

h 整数型:指定绘制图片的高度.若取值为-1,则不更改高度.

alpha 整数型:指定绘制图片的透明度,取值范围0-255,值越大越不透明.若取值为-1,则不更改透明度.

maintain 整数型:是否保存原始图片的宽高比.取值如下:

0:不保持原始宽高比,拉伸图片到指定的宽度和高度.宽高由参数w和h进行指定,此时图片可能会变形.

1:保持原始宽高比,此时图片会自适应大小以尽量调整为指定的宽度和高度.

-1:保持上次设置的本参数的值不变.

返回值:

整数型:

0:失败

1:成功

示例:

    // 加载多张图片

    string img_path_1 = "D:/image/img_1.png";

    vu->DrawImgLoad(1, (LONG64)img_path_1, 0);

    string img_path_2 = "D:/image/img_2.png";

    vu->DrawImgLoad(2, (LONG64)img_path_2, 0);

    string img_path_3 = "D:/image/img_3.png";

    vu->DrawImgLoad(3, (LONG64)img_path_3, 0);

 

    /*---------------假设下面代码位于渲染循环中--------------------*/

    vu->DrawClear();

    vu->DrawImg(1, 100, 100, 100, 100, 255, 0);// 拉伸图片到指定位置大小(会变形).

    vu->DrawImg(2, 200, 100, 100, 100, 255, 1);// 缩放图片到指定位置大小(不变形).

    vu->DrawImg(3, 300, 100, 100, 100, 128, 1);// 半透明图片

    vu->DrawRender();

    // 再次绘制图片,图片不会重新加载,只改变位置,不改变大小和透明度

    vu->DrawClear();

    vu->DrawImg(1, 300, 100, -1, -1, -1, -1);

    vu->DrawImg(2, 100, 100, -1, -1, -1, -1);

    vu->DrawImg(3, 200, 100, -1, -1, -1, -1);

    vu->DrawRender();

    /****************假设上面代码位于渲染循环中*********************/

 

    // 清空图片

    vu->DrawImgClear();

---

## 

函数简介:

清空所有已经加载的图片.

函数原型:

LONG DrawImgClear()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

示例:

    // 加载多张图片

    string img_path_1 = "D:/image/img_1.png";

    vu->DrawImgLoad(1, (LONG64)img_path_1, 0);

    string img_path_2 = "D:/image/img_2.png";

    vu->DrawImgLoad(2, (LONG64)img_path_2, 0);

    string img_path_3 = "D:/image/img_3.png";

    vu->DrawImgLoad(3, (LONG64)img_path_3, 0);

 

    /*

    * 使用这些图片,例如多次在渲染循环中绘制

    */

 

    // 清空图片

    vu->DrawImgClear();

---

## 

函数简介:

预加载图片,此时仅仅是将图片加载到内存中,并且给这张图片进行指定id的映射,并不进行绘制.

加载成功后,只有使用DrawImg()函数调用指定id的图片才会被绘制,若图片加载后,并未使用DrawImg()操作,则不会被绘制.

支持加载内存中的图片数据,也支持加载本机/跨机硬盘中的图片文件.

 

为什么要预加载图片?

因为dx绘制时,每帧都需要清除渲染的内容重新渲染新画面.

如果在绘制图片期间,每一帧都需要加载图片的话,将会极速消耗硬件性能以及浪费大量时间在读取图片数据之上.

所以我们需要在渲染之前,预先将需要绘制的图片加载进来,并且给每张图片都设置一个id,这样,在渲染期间,我们仅需要对指定id的图片进行操作,即可绘制出来想要的结果.

函数原型:

LONG DrawImgLoad(id, pImg, nImgSize)

参数定义:

id 长整数型:映射加载后图片的id,可以设置为任意值,但最好每张图片指定的id均不相同,相同id的图片仅最后加载的有效.

pImg 长整数型:图片路径文本地址或图片数据指针,具体情况根据参数nImgSize的值而定.

nImgSize 长整数型:图片大小,取值如下:

0:表示使用硬盘文件加载方式,参数pImg必须为图片路径字符串的内存地址.

非0:表示使用内存数据加载方式,参数pImg必须为图片数据在内存中的地址.

 

注意:跨机远程绘制不支持内存数据加载图片.

 

返回值:

整数型:

0:失败

1:成功

当返回值为0时,可以调用DrawGetError()来获取失败的错误信息.

示例:

    // 硬盘文件加载图片,支持跨机绘制

    string img_path = "D:/image/img_1.png";

    vu->DrawImgLoad(1, (LONG64)img_path, 0);

 

 

    // 内存文件加载图片,不支持跨机绘制

    LONG len = 0;

    LONG64 img_data = vu->ReadFileData("D:/image/img_2.png", len);

    vu->DrawImgLoad(2, img_data, len);

---

## 

函数简介:

将指定id的图片移除,释放内存资源.

 

为什么要移除图片?

预加载图片是为了在dx绘制时能更快速高效的渲染,然而某些情况下我们会加载很多张图片,例如像显示直播或者视频画面,每秒会有多帧图片被加载并渲染,如果不加节制的一直这样下去,电脑内存迟早会耗尽.

所以我们需要在适当时候将失去作用的图片从内存中卸载,释放内存资源.

函数原型:

LONG DrawImgRemove(LONG64 id)

参数定义:

id 长整数型:图片的id,通过函数DrawImgLoad()加载图片时进行指定.

返回值:

整数型:

0:失败

1:成功

示例:

    // 加载图片

    string img_path = "D:/image/img_1.png";

    vu->DrawImgLoad(1, (LONG64)img_path, 0);

 

    /*

    * 使用这张图片,例如多次在渲染循环中绘制

    */

 

    // 移除图片

    vu->DrawImgRemove(1);

---

## 

函数简介:

绘制是否在运行.

一般用来在渲染循环中调用,判断绘制是否已经被停止或者绑定的目标窗口已经关闭.

如果绘制未运行,应该结束渲染循环,不再继续绘制.

函数原型:

LONG DrawIsRunning()

参数定义:

无

返回值:

整数型:

0:绘制已结束

1:绘制正在运行

示例:

		std::string err;

		vusoft vu;

		vu.Create(); // 或者使用CreateRemote()创建跨机绘制

 

		LONG hwnd = NULL;

		hwnd = vu.DrawCreate(0, 0, 800, 600, 0);

		std::cout << "hwnd:" << hwnd << std::endl;

 

		LONG isRunning = vu.DrawIsRunning();

		std::cout << "isRunning:" << isRunning << std::endl;

 

		vu.DrawStop();	// 停止绘制

---

## 

函数简介:

绘制线条

函数原型:

LONG DrawLine(int x1, int y1, int x2, int y2, int rgb, int alpha, int lineWidth)

参数定义:

x1 整数型:线条的起始x坐标.

y1 整数型:线条的起始y坐标.

x2 整数型:线条的终点x坐标.

y2 整数型:线条的终点y坐标.

rgb 整数型:颜色值
alpha 整数型:透明度,取值范围0-255,值越大越不透明.
lineWidth 整数型:线宽,值越大线条越粗.

返回值:

整数型:

0:失败

1:成功

示例:

vu->DrawLine(0, 0, 100, 100, 0xffffff, 255, 2);

---

## 

函数简介:

绘制多边形,支持任意顶点数量和边的多边形.

理论上支持无限条边的多边形,但是不支持小于3个顶点的多边形,否则可能绘制失败.

多边形中,顶点与边的关系:

2顶点组成1条边,相连的2个边有3个顶点,其中2边相交的点为共同点,其他两个顶点是两条线的端点.

本函数的用法为:

当参数mode = 0时,每次调用本函数都会给多边形增加一个顶点,此时多边形还在继续构建,暂不进行绘制,多次调用本函数,直到多边形只剩下最后一个顶点待添加.

当参数mode > 0时,则会将最后一个顶点与第一个顶点进行衔接,构建出完整的多边形.

当多边形构建完成时,若需要绘制新的多边形,则重复上述步骤.

 

函数原型:

LONG DrawPolygon(int x, int y, int rgb, int alpha, int mode)

参数定义:

x 整数型:新增多边形的顶点x坐标.

y 整数型:新增多边形的顶点y坐标.

rgb 整数型:颜色值.当mode < 1时,本参数无效.

alpha 整数型:透明度,值越大越不透明.当mode < 1时,本参数无效.

mode 整数型:多边形的构建模式,取值如下:

0:将x,y作为顶点加入多边形顶点列表中,此时多边形为编辑状态,并不进行绘制.

1:边线渲染,将x,y作为最后一个顶点加入多边形中,并形成所有顶点的连接,构建完整的多边形.(用rgb指定的颜色画出多边形的边)

2:填充渲染,将x,y作为最后一个顶点加入多边形中,并形成所有顶点的连接,构建完整的多边形.(用rgb指定的颜色填充整个多边形)

返回值:

整数型:

0:失败

1:成功

示例:

    // 画最简单的多边形:三角形

    // 多边形编辑,新增顶点

    vu->DrawPolygon(0, 0, -1, -1, 0);

    vu->DrawPolygon(10, 10, -1, -1, 0);

    // 添加最后一个顶点,形成多边形闭合,并绘制

    vu->DrawPolygon(5, 20, 0x00FF00, 255, 1);

    // 此时绘制出的多边形应该是一个绿色线条的三角形

 

 

    // 再画一个四边形,并用红色填充,且设置为半透明

    vu->DrawPolygon(100, 100,-1, -1, 0);

    vu->DrawPolygon(200, 100, -1, -1, 0);

    vu->DrawPolygon(200, 200, -1, -1, 0);

    // 添加最后一个顶点,形成多边形闭合,并绘制

    vu->DrawPolygon(100, 200, 0xFF0000, 128, 2);

---

## 

函数简介:

绘制矩形

函数原型:

LONG DrawRectangle(x1, y1, x2, y2, radiusX, radiusY, rgbFill, alphaFill, rgbSide, alphaSide, sideWidth, mode)

参数定义:

x1 整数型:矩形的左上角x坐标.

y1 整数型:矩形的左上角y坐标.

x2 整数型:矩形的右下角x坐标.

y2 整数型:矩形的右下角y坐标.

radiusX 整数型:矩形的x轴圆角半径,如果为0则绘制直角矩形.

radiusY 整数型:矩形的y轴圆角半径,如果为0则绘制直角矩形.

rgbFill 整数型:填充矩形的颜色值.

alphaFill 整数型:填充矩形的颜色透明度,取值范围0-255,值越大越不透明.

rgbSide 整数型:矩形边框的颜色值.

alphaSide 整数型:矩形边框的颜色透明度,取值范围0-255,值越大越不透明.

sideWidth 整数型:矩形边框线条的粗细粒度.

mode 整数型:绘制模式,取值如下:
1:只画边,不填充颜色.
2:只填充颜色,不画边.
3:既填充颜色,也画边.

返回值:

整数型:

0:失败

1:成功

示例:

    // 绘制一个矩形,直角,只画边,蓝色

    vu->DrawRectangle(0, 0, 100, 100, 0, 0, -1, -1, 0x0000FF, 255, 1, 1);

 

    // 绘制一个矩形,圆角,填充,红色

    vu->DrawRectangle(100, 100, 200, 200, 10, 20, 0xFF0000, 255, -1, -1, -1, 2);

 

    // 绘制一个矩形,圆角,白色半透明填充,黑色半透明边框,线宽为5

    vu->DrawRectangle(200, 200, 300, 300, 20, 20, 0xFFFFFF, 128, 0x000000, 128, 5, 3);

---

## 

函数简介:

渲染需要绘制的内容,在调用前必须先使用DrawClear()清空旧内容,之后使用DrawString()、DrawLine()、DrawPolygon()等函数绘制需要的图形,调用本函数时会在屏幕中渲染画面.

必须和DrawClear()成对使用才能正确渲染画面.

函数原型:

LONG DrawRender()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

示例:
以下示例构建了一个完整的渲染循环,专门用来绘制文本/线条/图像等元素.
推荐在创建绘制之后,使用线程调用渲染循环.
// 渲染循环,最好使用线程调用本函数,在循环中进行绘制
DWORD WINAPI DrawLoop(LPVOID arg)
{
    DWORD res = 0;
    vusoft* vu = (vusoft*)arg;
 
    // 渲染循环
    while (vu->DrawIsRunning())
    {
        // 清除绘制内容
        vu->DrawClear();
 
        std::string strFps = std::to_string(vu->DrawGetFps());
        strFps = "FPS:" + strFps;
        // 绘制字符串
        vu->DrawString(strFps.c_str(), 0, 0, 0x00ffff, 255, "微软雅黑", 0, 0, 20);
 
        // 绘制直线
        vu->DrawLine(0, 0, 100, 200, 0xFF00FF, 255, 2);
 
        // 绘制多边形
        vu->DrawPolygon(300, 300, 0x00ffff, 128, 0);
        vu->DrawPolygon(400, 200, 0x00ffff, 128, 0);
        vu->DrawPolygon(600, 600, 0x00ffff, 128, 2);
 
        // 绘制矩形
        vu->DrawRectangle(400, 400, 500, 500, 20, 20, 0xffffff, 128, 0, 128, 1, 3);
 
        // 绘制椭圆
        vu->DrawEllipse(300, 300, 50, 80, 0xffffff, 128, 0xff00ff, 128, 2, 3);
 
        // 绘制图片
        vu->DrawImg(1, 100, 100, 100, 100, 255, 0);
 
 
        // 渲染
        vu->DrawRender();
    }
    return res;
}

---

## 

函数简介:

运行绘制功能,此函数会进入绘制窗口的消息循环,只有当绘制结束后才会返回,请尽量在线程中调用很函数,勿在UI控件事件中调用(会卡界面).

结束绘制请使用DrawStop()

函数原型:

LONG DrawRun()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

示例:

	vusoft vu;

	vu.Create(); // 或者使用CreateRemote()创建跨机绘制

 

	LONG hwnd = NULL;

	hwnd = vu.DrawCreate(0, 0, 800, 600, 0);

	std::cout << "hwnd:" << hwnd << std::endl;

 

	if (hwnd)

	{

		// 创建渲染线程,在渲染线程中进行绘制

		CreateThread(NULL, 0, DrawLoop, &vu, 0, NULL);

	}

	// 运行绘制,直到调用DrawStop()才会退出.

	vu.DrawRun();

---

## 

函数简介:

设置绘制位置和显示隐藏.

函数原型:

LONG DrawSetPosition(LONG isShow, LONG x, LONG y, LONG w, LONG h)

参数定义:

isShow 整数型:显示绘制模式,取值如下:

0:隐藏绘制

1:显示绘制

x 整数型:绘制窗体的x坐标,值为-1则表示忽略此参数,不进行修改.

y 整数型:绘制窗体的y坐标,值为-1则表示忽略此参数,不进行修改.

w 整数型:绘制窗体的宽度,值为-1则表示忽略此参数,不进行修改.

h 整数型:绘制窗体的高度,值为-1则表示忽略此参数,不进行修改.

返回值:

整数型:

0:失败

1:成功

示例:

	vusoft vu;

	vu.Create(); // 或者使用CreateRemote()创建跨机绘制

 

	LONG hwnd = NULL;

	hwnd = vu.DrawCreate(0, 0, 800, 600, 0);

	std::cout << "hwnd:" << hwnd << std::endl;

 

	vu.DrawSetPosition(false, -1, -1, -1, -1);	// 隐藏绘制,窗口位置和宽高不变

	vu.DrawSetPosition(true, 0, 0, -1, -1);		// 显示绘制,窗口位置设置为0,0坐标处,宽高不变

	vu.DrawSetPosition(true, -1, -1, 800, 600);	// 显示绘制,窗口位置不变,宽高设置为800,600

---

## 

函数简介:

设置已创建绘制的风格.

函数原型:

LONG DrawSetStyle(LONG isThrough, LONG alpha)

参数定义:

isThrough 整数型:鼠标穿透模式,取值如下:

0:鼠标不可穿透.

1:鼠标可穿透绘制.

alpha 整数型:绘制窗体的透明度,取值范围0-255,值越大越不透明.当值为-1时,则忽略此参数,不进行透明度的修改.

返回值:

整数型:

0:失败

1:成功

示例:

	vusoft vu;

	vu.Create(); // 或者使用CreateRemote()创建远程调用对象

	LONG hwnd = NULL;

	hwnd = vu.DrawCreate(0, 0, 800, 600, 0);

	std::cout << "hwnd:" << hwnd << std::endl;

	vu.DrawSetStyle(true, -1);	// 设置鼠标可穿透,透明度不变

	vu.DrawSetStyle(true, 128);// 设置绘制半透明

---

## 

函数简介:

停止绘制.

函数原型:

LONG DrawStop()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

示例:

	vusoft vu;

	vu.Create(); // 或者使用CreateRemote()创建跨机绘制

 

	LONG hwnd = NULL;

	hwnd = vu.DrawCreate(0, 0, 800, 600, 0);

	std::cout << "hwnd:" << hwnd << std::endl;

 

	vu.DrawStop();	// 停止绘制

---

## 

函数简介:

绘制文本

函数原型:

LONG DrawString(str, x, y, rgb, alpha, fontFamilyName, fontWeight, fontStyle, fontSize)

参数定义:

str 字符串:要绘制的文本内容.

x 整数型:文本在绘制窗体上的x坐标.

y 整数型:文本在绘制窗体上的y坐标.

rgb 整数型:颜色值

alpha 整数型:透明度,取值范围0-255,值越大越不透明.

fontFamilyName 字符串:系统字体名字,例如:"微软雅黑"、 "宋体"、"SimHei"等.

fontWeight 整数型:字体的粗细粒度,取值范围-4到6,值越大字体越粗.

fontStyle 整数型:字体风格,取值如下:

0:正常

1:斜字

2:斜体

注意:1和2都会将字倾斜,不同的是:1将整个字都按角度倾斜,2是一种倾斜字体,更美观一点.

fontSize 整数型:字体尺寸,值越大,字越大.

返回值:

整数型:

0:失败

1:成功

示例:

    for (int i = 0; i <= 10; i++)

    {

        vu->DrawString("测试字体粗细", 0, (i + 1) * 30, 0xff00ff, 255, "微软雅黑", i - 4, 0, 20);

 

        int fontSize = (i + 1) * 2;

        vu->DrawString(("测试大小" + std::to_string(fontSize)).c_str(), 200, (i + 1) * 30, 0x00ff00, 255, "宋体", 0, 0, fontSize);

    }

 

    vu->DrawString("测试不透明字体", 300, 0, 0xff0000, 255, "SimHei", 0, 0, 20);

    vu->DrawString("测试半透明字体", 300, 30, 0xff0000, 128, "SimHei", 0, 0, 20);

 

    vu->DrawString("测试倾斜字体1", 400, 0, 0xffff00, 255, "SimHei", 0, 1, 20);

    vu->DrawString("测试倾斜字体2", 400, 30, 0xffff00, 255, "SimHei", 0, 2, 20);

---

## 

函数简介:

将浮点型的HSV值转换为用十六进制表示的RGB颜色.

函数原型:

string Hsv2Rgb(h, s, v)

参数定义:

h 整数型:颜色的色相值,用来表示红绿蓝,取值范围一般在0-360之间

s 整数型:颜色的饱和度,用来表示颜色的纯度或深浅程度,取值范围一般在0-100之间

v 整数型:颜色的亮度,用来表示颜色的明暗程度,取值范围一般在0-100之间

返回值:

字符串:

返回十六进制的RGB表示.

示例:

    res = vu.Hsv2Rgb(360, 100, 100);

---

## 

函数简介:

对二值化黑白图指定区域内图像进行形变操作,通常用来对图像中的噪点进行处理.

函数原型:

long ImgBinMorph(LONG id, int x1, int y1, int x2, int y2, long mode, long strength, long kmode)

参数定义:

id 整数型:图层ID.

x1 整数型:区域的左上X坐标,值为-1表示自动获取
y1 整数型:区域的左上Y坐标,值为-1表示自动获取
x2 整数型:区域的右下X坐标,值为-1表示自动获取
y2 整数型:区域的右下Y坐标,值为-1表示自动获取

mode 整数型:形变的模式,取值如下

0:腐蚀(变瘦)

1:膨胀(变胖)

2:开运算(消除色块外噪点)

3:闭运算(消除色块内噪点)

4:梯度运算(提取边缘)

5:顶帽操作(获取色块外噪点)

6:黑帽操作(获取色块内噪点)

每一种形变操作对图像造成的影响均不相同.具体可以参考实例.

strength 整数型:形变的强度

kmode 整数型:形变的形状区域,取值如下

0:矩形区域

1:十字形区域

2:椭圆形区域

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\test.bmp");

	vu.ImgBinMorph(0, -1, -1, -1, -1, 0, 1, 0);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

对二值化黑白图进行形变操作是一种处理图像噪点的技术,通常用来去除或者提取噪点.

下面是对各种形变模式产生结果的展示.

---

## 

函数简介:

轮廓获取,取指定图层中指定索引的轮廓的坐标集合.

函数原型:

string ImgContoursGetPoints(LONG id, int index)

参数定义:

id 整数型:图层ID.

index 整数型:要获取的轮廓的索引.

返回值:

字符串:

返回当前获取到的轮廓的所有坐标集合,格式为:x1,y1|x2,y2|...xn,yn

示例:

	res = vu.ImgContoursGetPoints(0, 0);

	//对轮廓进行解析

	vusoft vs;

	long len = vs.StrSplitInit(res, "|");

	for (long i = 0; i < len; i++)

	{

		    const char* ss = vs.StrSplitGet(i);

		    vusoft v;

		    long n = v.StrSplitInit(ss, ",");

		    if (n != 2)

			    continue;

		    long x = v.StrToNum(v.StrSplitGet(0), 10);

		    long y = v.StrToNum(v.StrSplitGet(1), 10);

		    std::cout << "轮廓顶点:" << x << "," << y << std::endl;

	}

---

## 

函数简介:

轮廓获取,取指定图层中指定索引的轮廓的坐标集合(精简版本).

此函数是在ImgContoursGetPoints的基础上对获取到的轮廓坐标集进行精简,避免在数据传输时传输过多的坐标数据.

函数原型:

string ImgContoursGetPointsSimplify(LONG id, int index, double epsilon)

参数定义:

id 整数型:图层ID.

index 整数型:要获取的轮廓的索引.

epsilon 双精度浮点型:逼近精度,用于控制逼近多边形与原始轮廓之间的最大距离。这个值越大，逼近后的多边形顶点越少，形状越简化；值越小，顶点越多，形状越接近原始轮廓(如果为-1,则使用凸起的外包多边形来实现轮廓坐标集合).

返回值:

字符串:

返回当前获取到的轮廓的所有坐标集合,格式为:x1,y1|x2,y2|...xn,yn

示例:

	res = vu.ImgContoursGetPointsSimplify(0, 0,-1);

	//对轮廓进行解析

	vusoft vs;

	long len = vs.StrSplitInit(res, "|");

	for (long i = 0; i < len; i++)

	{

		    const char* ss = vs.StrSplitGet(i);

		    vusoft v;

		    long n = v.StrSplitInit(ss, ",");

		    if (n != 2)

			    continue;

		    long x = v.StrToNum(v.StrSplitGet(0), 10);

		    long y = v.StrToNum(v.StrSplitGet(1), 10);

		    std::cout << "轮廓顶点:" << x << "," << y << std::endl;

	}

---

## 

函数简介:

轮廓获取,图层轮廓初始化.

注意:图像中物品轮廓获取,一般需要先将图像进行二值化,或者转为边线图.

函数原型:

long ImgContoursInit(LONG id, int x1, int y1, int x2, int y2)

参数定义:

id 整数型:图层ID.

x1 整数型:区域的左上X坐标,值为-1表示自动获取
y1 整数型:区域的左上Y坐标,值为-1表示自动获取
x2 整数型:区域的右下X坐标,值为-1表示自动获取
y2 整数型:区域的右下Y坐标,值为-1表示自动获取

返回值:

整数型:

返回图像中对象轮廓的数量.

示例:

	vu.ImgLoadFile(0,"c:\\pic\\test.bmp" );

	//转边线图,或者二值化为黑白图

	vu.ImgToEdges(0, 50, 100, 1, 1);

	//轮廓初始化,返回值是轮廓数量

	ret = vu.ImgContoursInit(0, -1, -1, -1, -1);

	std::cout << "轮廓数量:" << ret << std::endl;

	for (size_t i = 0; i < ret; i++)

	{

		res = vu.ImgContoursGetPoints(0, i);

		std::cout << "轮廓:" << res << std::endl;

	}

---

## 

函数简介:

在指定图层中复制一份图像对象(本函数不新建图层).

注意:复制后的对象存储在临时内存中,在下次相同的图层调用本函数时会被释放,如果想要长期使用,请用一个新建的图层加载复制的对象,可以使用ImgLoadImgObj.

函数原型:

LONG64 ImgCopy(LONG id, LONG64 pImg)

参数定义:

id 整数型:图层ID.

pImg 长整数型:要被复制的图层图像对象指针.

返回值:

长整数型:

返回在图层中复制的图像对象指针.

示例:

    vu.ImgLoadFile(0, "c:\\test.png");

    vu.ImgLoadFile(1, "c:\\demo.png");

    obj_0 = vu.ImgGetImgObj(0);

    obj_cpy = vu.ImgCopy(1, obj_0);

---

## 

函数简介:

创建一张空白图层

函数原型:

long ImgCreate(LONG id, long width, long height, long rgb)

参数定义:

id 整数型:要创建的图层ID,创建成功之后如果要对此图层进行操作均需要使用此次设置的ID.

width 整数型:要创建的图层宽度.

height 整数型:要创建的图层高度.

rgb 整数型:图层背景颜色的rgb数值,如果为-1,则表示图层是没有任何背景颜色的透明图层.

返回值:

整数型:

0:失败

1:成功

示例:

    ret = vu.ImgCreate(0, 800, 600, -1);

---

## 

函数简介:

对指定区域范围内的图层图像进行裁剪.

函数原型:

long ImgCropped(LONG id, int x1, int y1, int x2, int y2)

参数定义:

id 整数型:图层ID.

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgCropped(0, 10, 10, 50, 50);

---

## 

函数简介:

对指定范围内的四边形目标图像进行裁剪,并且拉伸为指定宽高的标准矩形图像.

本函数裁剪出来的图片将会自动修正相机拍摄角度,将原图带有倾斜角度的图像修正为正向朝向拍摄的图像.

函数原型:

long ImgCroppedEx(LONG id, int ltX, int ltY, int rtX, int rtY, int lbX, int lbY, int rbX, int rbY, int width, int height)

参数定义:

id 整数型:图层ID.

ltX 整数型:左上X坐标

ltY 整数型:左上Y坐标

rtX 整数型:右上X坐标

rtY 整数型:右上Y坐标

lbX 整数型:左下X坐标

lbY 整数型:左下X坐标

rbX 整数型:右下X坐标

rbY 整数型:右下Y坐标

width 整数型:新图像的宽度

height 整数型:新图像的高度

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\test.bmp");

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

	vu.ImgCroppedEx(0, 77, 56, 416, 84, 80, 294, 422, 268, 300, 200);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

上述示例是从图像中截取电视机画面,并且修正为标准矩形图像.

处理前图像:

 

处理后图像

---

## 

函数简介:

在图层上绘制一个圆形.

函数原型:

long ImgDrawCircle(LONG id, long x, long y, long radius, long rgb, long thickness, long alpha)

参数定义:

id 整数型:图层ID.

x 整数型:圆心的x坐标

y 整数型:圆心的y坐标

radius 整数型:圆的半径长度

rgb 整数型:绘制的画笔颜色(RGB格式)

thickness 整数型:画笔厚度,若值为-1则进行填充绘制

alpha 整数型:透明度,取值范围0-255

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgDrawCircle(0, 100, 100, 20, vu.Rgb2Long("FF00FF"), 1, 255);

---

## 

函数简介:

在图层上绘制椭圆.

函数原型:

long ImgDrawEllipse(LONG id, long x, long y, long width, long height, double angle, double startAngle, double endAngle, long rgb, long thickness, long alpha)

参数定义:

id 整数型:图层ID.

x 整数型:椭圆中心x坐标

y 整数型:椭圆中心y坐标

width 整数型:椭圆的宽度

height 整数型:椭圆的高度

angle 双精度浮点型:椭圆绕其中心的旋转角度

startAngle 双精度浮点型:椭圆弧的起始角度

endAngle 双精度浮点型:椭圆弧的结束角度

rgb 整数型:绘制的画笔颜色(RGB格式)

thickness 整数型:画笔厚度,若值为-1则进行填充绘制

alpha 整数型:透明度,取值范围0-255

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgDrawEllipse(0, 100, 100, 30, 50, 0, 0, 360, vu.Rgb2Long("FF00FF"), 1, 255);

---

## 

函数简介:

在图层上绘制一条直线.

函数原型:

long ImgDrawLine(LONG id, long beginX, long beginY, long endX, long endY, long rgb, long thickness, long alpha)

参数定义:

id 整数型:图层ID.

beginX 整数型:起始x坐标

beginY 整数型:起始y坐标

endX 整数型:结束x坐标

endY 整数型:结束y坐标

rgb 整数型:绘制的画笔颜色(RGB格式)

thickness 整数型:画笔厚度

alpha 整数型:透明度,取值范围0-255

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgDrawLine(0, 10, 10, 50, 50, vu.Rgb2Long("FF00FF"), 1, 255);

---

## 

函数简介:

在图层上绘制一张图片(新增图片).

函数原型:

long ImgDrawPic(LONG id, LONG64 pImg, long x, long y, long alpha, long bg_rgb)

参数定义:

id 整数型:图层ID.

pImg 长整数型:一个图片对象指针,一般是通过ImgGetImgObj来获取.

x 整数型:要绘制图片的左上角x坐标

y 整数型:要绘制图片的左上角y坐标

alpha 整数型:要绘制图片的透明度,取值范围0-255

bg_rgb 整数型:要绘制图片的背景色RGB数值,此颜色会被作为背景色处理,不在图层上绘制,若此参数值为-1,则保留所有颜色,不做背景处理.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\0.bmp");

	vu.ImgLoadFile(1, "c:\\pic\\1.bmp");

	obj_1 = vu.ImgGetImgObj(1);

	vu.ImgDrawPic(0, obj_1, 100, 100, 255, -1);

---

## 

函数简介:

在图层上绘制一张图片(新增图片+投影转换).

与ImgDrawPic不同的是,本函数可以将一张标准矩形图片投影在指定顶点的四边形上,并且自动进行形状适配,使其符合相机角度.

函数原型:

long ImgDrawPicEx(LONG id, LONG64 pImg, int ltX, int ltY, int rtX, int rtY, int lbX, int lbY, int rbX, int rbY, long alpha, long bg_color)

参数定义:

id 整数型:图层ID.

pImg 长整数型:一个图片对象指针,一般是通过ImgGetImgObj来获取.

ltX 整数型:要将图片投影的左上X坐标

ltY 整数型:要将图片投影的左上Y坐标

rtX 整数型:要将图片投影的右上X坐标

rtY 整数型:要将图片投影的右上Y坐标

lbX 整数型:要将图片投影的左下X坐标

lbY 整数型:要将图片投影的左下X坐标

rbX 整数型:要将图片投影的右下X坐标

rbY 整数型:要将图片投影的右下Y坐标

alpha 整数型:要绘制图片的透明度,取值范围0-255

bg_rgb 整数型:要绘制图片的背景色RGB数值,此颜色会被作为背景色处理,不在图层上进行绘制,若此参数值为-1,则保留所有颜色,不做背景处理.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\0.bmp");

	vu.ImgLoadFile(1, "c:\\pic\\1.bmp");

	obj_1 = vu.ImgGetImgObj(1);

	vu.ImgDrawPicEx(0, obj_1,89,98,457,14,90,330,453,397,255,1 );

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

上述示例是将图像1.bmp以投影形式绘制在0.bmp指定的四边形区域内.

两张图片的原图分别为:

 

投影后的成品图片为:

---

## 

函数简介:

在图层上绘制出多边形.

注意:本函数必须和ImgPolyAdd搭配使用才可以正常绘制多边形.

函数原型:

long ImgDrawPoly(LONG id, long rgb, long thickness, long alpha, bool isClosed)

参数定义:

id 整数型:图层ID.

rgb 整数型:绘制的画笔颜色(RGB格式)

thickness 整数型:画笔厚度,若值为-1则进行填充绘制

alpha 整数型:透明度,取值范围0-255

isClosed 整数型:是否闭口,取值如下

0:不将最后的顶点与第一个顶点相连接

1:将最后的顶点与第一个顶点连接(闭口,封口,蛇衔尾)

返回值:

整数型:

0:失败

1:成功

示例:

vu.ImgPolyClear(0);

 

vu.ImgPolyAdd(0, 10, 10);

vu.ImgPolyAdd(0, 10, 20);

vu.ImgPolyAdd(0, 20, 30);

vu.ImgPolyAdd(0, 30, 40);

vu.ImgPolyAdd(0, 10, 50);

 

vu.ImgDrawPoly(0, vu.Rgb2Long("FF00FF"), 1, 255, 1);

---

## 

函数简介:

在图层上绘制一个矩形.

函数原型:

long ImgDrawRect(LONG id, int x1, int y1, int x2, int y2, long rgb, long thickness, long alpha)

参数定义:

id 整数型:图层ID.

x1 整数型:左上X坐标
y1 整数型:左上Y坐标
x2 整数型:右下X坐标
y2 整数型:右下Y坐标

rgb 整数型:绘制的画笔颜色(RGB格式)

thickness 整数型:画笔厚度,若值为-1则进行填充绘制

alpha 整数型:透明度,取值范围0-255

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgDrawRect(0, 10, 10, 50, 50, vu.Rgb2Long("FF00FF"), 1, 255);

---

## 

函数简介:

在图层上绘制字符串

函数原型:

long ImgDrawString( LONG id, long x, long y, const char* str, const char* font_name, long font_size, long flag, long rgb, long alpha, long gradient, double gd_sim)

参数定义:

id 整数型:图层ID.

x 整数型:字符串第一个字所在x坐标

y 整数型:字符串第一个字所在y坐标

str 字符串:要绘制的字符串

font_name 字符串:字体名字,例如:"宋体"或者"simsun"

font_size 字符串:字体尺寸

flag 整数型:字体类别 取值可以是以下值的组合,比如1+2+4+8,2+4. 0表示正常字体.
    1 : 粗体
    2 : 斜体
    4 : 下划线
    8 : 删除线

rgb 整数型:绘制的画笔颜色(RGB格式)

alpha 整数型:透明度,取值范围0-255

gradient 整数型:渐变色模式,取值如下

0:不渐变,纯色文本

1:按X轴渐变色

2:按Y轴渐变色

gd_sim 双精度浮点型:渐变色的精度,取值范围0-10.0

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgDrawString(0, 10, 10, "你好,测试!", "宋体", 20, 0, vu.Rgb2Long("FF00FF"), 255, 1, 0);

---

## 

函数简介:

在大图片中匹配小图.

函数原型:

string ImgFindPic(LONG64 pLarge, LONG64 pSmall, long isFast, long dir, double sim, long matchMethod)

参数定义:

pLarge 长整数型:大图对象指针

pSmall 长整数型:小图对象指针

isFast 整数型:是否快速模式,取值范围如下

0:标准模式

1:快速模式,注意:快速模式是当在大图中找到图就返回,不去匹配大图中是否有多张小图.

dir 整数型:匹配方向 0: 从左到右,从上到下 1: 从左到右,从下到上 2: 从右到左,从上到下 3: 从右到左, 从下到上

sim 双精度浮点型:匹配精确度,取值范围一般为0-1.0.注意:当sim值为负数时,则表示取最佳匹配的结果.

matchMethod 整数型:匹配模式,取值范围为0-5,每一种模式使用的匹配方法都不相同,一般默认为5即可.如果修改本参数,可能需要调整sim值以获取最佳匹配.

返回值:

字符串:

大图中符合小图特征的图片所在的所有坐标,格式如下:"x1,y1|x2,y2|...xN,yN".

匹配失败返回空字符串.

示例:

    vu.SetPath("D:\\test\\");

    //加载屏幕截图和小图

    vu.ImgLoadScreen(1, 0, 0, 2000, 2000);

    vu.ImgLoadFile(2, "小图.bmp");

    

    //获取图片对象

    pic1 = vu.ImgGetImgObj(1);

    pic2 = vu.ImgGetImgObj(2);

    //查找图片

    res = vu.ImgFindPic(pic1, pic2,0,0,0.5,5);

 

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        long x = v.StrToNum(v.StrSplitGet(0), 10);

        long y = v.StrToNum(v.StrSplitGet(1), 10);

        std::cout << "找到图片:" << x << "," << y << std::endl;

    }

---

## 

函数简介:

在大图片中匹配小图.

与ImgFindPic不同的是,本函数支持对缩放和旋转图像的查找,但是如果图像过于简单或者尺寸过小,将会影响搜索结果

函数原型:

string ImgFindPicSuper(LONG64 pLarge, LONG64 pSmall, long isFast, long detMode, double matchThresh, bool showDbg)

参数定义:

pLarge 长整数型:大图对象指针

pSmall 长整数型:小图对象指针

isFast 整数型:是否快速模式,取值范围如下

0:标准模式

1:快速模式,注意:快速模式是当在大图中找到图就返回,不去匹配大图中是否有多张小图.

detMode 整数型:推理模式,取值如下

0:均衡模式

1:精准模式

2:快速模式

matchThresh 双精度浮点型:匹配精确度,取值范围一般为0-1.0.

showDbg 整数型:是否显示调试图片.

返回值:

字符串:

大图中符合小图特征的图片所在的所有坐标,格式如下:"x1,y1|x2,y2|...xN,yN".

匹配失败返回空字符串.

示例:

    vu.SetPath("D:\\test\\");

    //加载屏幕截图和小图

    vu.ImgLoadScreen(1, 0, 0, 2000, 2000);

    vu.ImgLoadFile(2, "小图.bmp");

    

    //获取图片对象

    pic1 = vu.ImgGetImgObj(1);

    pic2 = vu.ImgGetImgObj(2);

    //查找图片

    res = vu.ImgFindPicSuper(pic1, pic2, 0, 0, 0.5, 0);

 

    vusoft vs;

    long len = vs.StrSplitInit(res, "|");

    for (long i = 0; i < len; i++)

    {

        const char* ss = vs.StrSplitGet(i);

        vusoft v;

        long n = v.StrSplitInit(ss, ",");

        if (n != 3)

            continue;

        long x = v.StrToNum(v.StrSplitGet(0), 10);

        long y = v.StrToNum(v.StrSplitGet(1), 10);

        std::cout << "找到图片:" << x << "," << y << std::endl;

    }

---

## 

函数简介:

对图像进行翻转操作.

函数原型:

long ImgFlip(LONG id, int flipCode)

参数定义:

id 整数型:图层ID.

flipCode 整数型:翻转轴,取值如下

0:沿着x轴翻转

1:沿着y轴翻转

-1:同时沿着x轴和y轴进行翻转

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgFlip(0, 0);

---

## 

函数简介:

获取图层图像的通道数.

图像通道:

单通道：一个像素点只需一个数值表示，这种图像通常只能表示灰度，0表示黑色，255表示白色。灰度图像就是典型的单通道图像。

多通道：一个像素点需要多个数值来表示，这些数值分别对应不同的颜色成分。常见的多通道图像有RGB三通道图像和RGBA四通道图像。

函数原型:

long ImgGetChannels(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

返回指定id图层中图像的通道数量.

示例:

    vu.ImgLoadFile(0, "c:\\test.png");

    ret = vu.ImgGetChannels(0);

---

## 

函数简介:

获取图层指定位置的rgb颜色值.

函数原型:

long ImgGetColor(LONG id, long x, long y)

参数定义:

id 整数型:图层ID.

x 整数型:要被设置颜色的x位置

y 整数型:要被设置颜色的y位置

返回值:

整数型:

返回指定坐标位置的rgb颜色数值.

示例:

    vu.ImgSetColor(0, 100, 200, vu.Rgb2Long("ff00ff"), 123);

 

    vu.ImgGetColor(0, 100, 200);

---

## 

函数简介:

获取指定图层中复制的图像对象指针.

函数原型:

LONG64 ImgGetCopy(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

长整数型:

返回在图层中复制的图像对象指针.

示例:

    vu.ImgLoadFile(0, "c:\\test.png");

    vu.ImgLoadFile(1, "c:\\demo.png");

    obj_0 = vu.ImgGetImgObj(0);

    vu.ImgCopy(1, obj_0);

    obj_cpy = vu.ImgGetCopy(1);

---

## 

函数简介:

获取图层图像的高度

函数原型:

long ImgGetHeight(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

返回图层图像的高度

示例:

    ret = vu.ImgGetHeight(0);

---

## 

函数简介:

获取图层图像的数据.

函数原型:

long ImgGetImgData(LONG id, PBYTE& pData, LONG& nLen)

参数定义:

id 整数型:图层ID.

pData 变参指针:返回图像数据的存放指针.

nLen 变参指针:返回图像数据的大小.

返回值:

整数型:

0:失败

1:成功

示例:

    vu.ImgGetImgData(0, data, len);

    std::cout << "图片数据:" << data << std::endl;

    std::cout << "图片大小:" << len << std::endl;

---

## 

函数简介:

获取图层图像对象指针

函数原型:

LONG64 ImgGetImgObj(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

长整数型:

返回指定id的图层对象指针

示例:

    vu.ImgLoadFile(0, "c:\\test.png");

    obj_0 = vu.ImgGetImgObj(0);

---

## 

函数简介:

获取图层图像对象指针.

与ImgGetImgObj不同的是,ImgGetImgObj仅仅支持三通道对象的获取,本函数支持任意通道数图像对象的获取,包括透明图.

函数原型:

LONG64 ImgGetImgObjEx(LONG id, long alpha_rgb, long offset_rgb)

参数定义:

id 整数型:图层ID.

alpha_rgb 整数型:指定透明的RGB颜色,如果传入的值为-1,则不使用透明通道.

offset_rgb 整数型:指定透明RGB颜色的色偏.

返回值:

长整数型:

返回指定id的图层对象指针

示例:

    vu.ImgLoadFile(0, "c:\\test.png");

    obj_0 = vu.ImgGetImgObjEx(0, vu.Rgb2Long("ff00ff"), vu.Rgb2Long("202020"));

---

## 

函数简介:

获取图层图像的宽度.

函数原型:

long ImgGetWidth(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

返回图层图像的宽度

示例:

    ret = vu.ImgGetWidth(0);

---

## 

函数简介:

将内存中的图片加载到一个新的图层中.

函数原型:

long ImgLoadData(LONG id, LONG64 data, long len)

参数定义:

id 整数型:要创建的图层ID,创建成功之后如果要对此图层进行操作均需要使用此次设置的ID.

data 长整数型:内存图片的指针

len 整数型:内存图片的数据大小

返回值:

整数型:

0:失败

1:成功

示例:

    vu.SetPath("c:\\PS\\");

    data = vu.ReadFileData("test.png", len);

    vu.ImgLoadData(0, data, len);

---

## 

函数简介:

将图片文件加载到一个新的图层中.

函数原型:

long ImgLoadFile(LONG id, string file)

参数定义:

id 整数型:要创建的图层ID,创建成功之后如果要对此图层进行操作均需要使用此次设置的ID.

file 字符串:图片文件的路径.

返回值:

整数型:

0:失败

1:成功

示例:

    //绝对路径

    vu.ImgLoadFile(0, "c:\\test.png");

 

    //相对路径

    vu.SetPath("c:\\PS\\");

    vu.ImgLoadFile(0, "test.png");

---

## 

函数简介:

将一张图层/图像对象加载到新的图层中.

函数原型:

long ImgLoadImgObj(LONG id, LONG64 pImg)

参数定义:

id 整数型:要创建的图层ID,创建成功之后如果要对此图层进行操作均需要使用此次设置的ID.

pImg 长整数型:图层或图像对象的指针.

返回值:

整数型:

0:失败

1:成功

示例:

    vu.ImgLoadFile(0, "c:\\test.png");

    obj_0 = vu.ImgGetImgObj(0);

 

    vu.ImgLoadImgObj(1, obj_0);

---

## 

函数简介:

将窗口或者屏幕范围的图像加载到新的图层.

函数原型:

long ImgLoadScreen(LONG id, long x1, long y1, long x2, long y2)

参数定义:

id 整数型:要创建的图层ID,创建成功之后如果要对此图层进行操作均需要使用此次设置的ID.

x1 整数型:区域的左上X坐标
y1 整数型:区域的左上Y坐标
x2 整数型:区域的右下X坐标
y2 整数型:区域的右下Y坐标

返回值:

整数型:

0:失败

1:成功

示例:

    vu.BindWindowEx(1200, "dx", "normal", "normal", "", 0);

    vu.ImgLoadScreen(0, 0, 0, 2000, 2000);

---

## 

函数简介:

在不改变原图像大小的情况下,对图层进行边缘扩展(会改变图像尺寸,但是原图大小不会变,只是在图像边缘进行扩张).

函数原型:

long ImgMakeBorder(LONG id, int top, int bottom, int left, int right, long borderType, long rgb)

参数定义:

id 整数型:图层ID.

top 整数型:图像顶部需要增加的边界尺寸

bottom 整数型:图像底部需要增加的边界尺寸

left整数型:图像左边需要增加的边界尺寸

right 整数型:图像右边需要增加的边界尺寸

borderType 整数型:边界扩展模式,取值如下

0:用指定的rgb值进行边界填充

1:用图像最边缘的像素进行边界填充,形式如:aaaaaa|abcdefgh|hhhhhhh

2:用图像边缘进行边界的镜像填充,形式如:fedcba|abcdefgh|hgfedcb

3:用图像边缘进行边界的环绕填充,形式如:cdefgh|abcdefgh|abcdefg

4:同2,但是在填充的时候不包含原图最后一个像素,形式如:gfedcb|abcdefgh|gfedcba

注意:中间部分abcdefgh是图像像素.

rgb 整数型:要填充的背景颜色数值.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgMakeBorder(0, 10, 10, 10, 10, 0, vu.Rgb2Long("FF00FF"));

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置进行模糊处理.

函数原型:

long ImgMaskBlur(LONG id, LONG64 pMask, int strength, long mode, double sigmaColor, double sigmaSpace)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

strength 整数型:强度,取值范围1-10.

mode 整数型:处理模式,取值如下

0:均值滤波,计算每个像素邻域内像素值的平均值来替代原像素值

1:高斯滤波,在一定程度上保留图像的边缘信息

2:中值滤波,用于去除图像中的椒盐噪声等随机噪声

3:双边滤波,能够在平滑图像的同时，较好地保留图像的边缘和细节信息(拥有磨皮效果)

sigmaColor 双精度浮点型:颜色滤波程度,只有当mode值为3时本参数才有用.

这个参数控制了在颜色空间中哪些像素将被视为“相似”的，即它决定了颜色相似性的敏感程度。

sigmaColor的值越大，意味着更多的颜色不同的像素将被视为相似，从而导致更平滑的结果，但也可能导致边缘细节的丢失。

相反，较小的sigmaColor值会使得滤波器对颜色变化更加敏感，从而更好地保留边缘细节，但降噪效果可能较弱。

sigmaSpace 双精度浮点型:空间滤波程度,只有当mode值为3时本参数才有用.

这个参数控制了在坐标空间中哪些像素将被视为“邻近”的，即它决定了空间邻近性的敏感程度。

sigmaSpace的值越大，意味着更多的空间上远离的像素将被考虑进来，这会导致更广泛的平滑效果。

相反，较小的sigmaSpace值会使得滤波器仅考虑空间上非常接近的像素，从而有助于保留更多的细节和纹理。

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

 

	vu.ImgMaskBlur(0, mask, 1, 3, 20, 50);

---

## 

函数简介:

蒙版,构建圆形蒙版区域.

对蒙版区域的图像进行处理时,非蒙版标记的位置不会受到图像操作的影响.

函数原型:

LONG64 ImgMaskCircle(LONG id, int x, int y, int radius, bool isGradient)

参数定义:

id 整数型:图层ID.

x 整数型:圆心所在的x坐标

y 整数型:圆心所在的y坐标

radius 整数型:圆形蒙版的半径

isGradient 整数型:是否渐变(羽化),值为0表示不渐变,为1表示靠近边缘位置的蒙版会发生渐变效果.

返回值:

长整数型:

成功返回一个蒙版对象指针,失败返回0.

示例:

	mask = vu.ImgMaskCircle(0, 100, 100, 50, 0);

	//对蒙版标记的像素进行操作

	vu.ImgMaskFill(0, mask, vu.Rgb2Long("000000"), 255);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置进行颜色改变.

函数原型:

long ImgMaskColorChange(LONG id, LONG64 pMask, long rgb, long tg_rgb, long offset)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

rgb 整数型:需要被改变的颜色数值.

tg_rgb 整数型:需要改变成的目标颜色数值.

offset 整数型:色偏,取值范围0-255.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskColorChange(0, mask, vu.Rgb2Long("000000"), vu.Rgb2Long("ff0000"), 0x20);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置进行颜色反转(类似于所有黑色变白色,白色变黑色).

函数原型:

long ImgMaskColorInvert(LONG id, LONG64 pMask)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskColorInvert(0, mask);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置进行颜色交换.

函数原型:

long ImgMaskColorSwap(LONG id, LONG64 pMask, long rgb1, long rgb2, long offset)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

rgb1 整数型:需要修改为rgb2的颜色数值.

rgb2 整数型:需要修改为rgb1的颜色数值.

offset 整数型:色偏,取值范围0-255.

注意:颜色交换是将两个颜色进行互相替换的功能,例如rgb1为红色,rgb2为绿色,那么执行本函数后,原图像中所有红色会变成绿色,所有绿色会变成红色.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskColorSwap(0, mask, vu.Rgb2Long("00ff00"), vu.Rgb2Long("ff0000"), 0x20);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置进行擦除处理.

函数原型:

long ImgMaskErase(LONG id, LONG64 pMask, long bg_rgb, int strength)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

bg_rgb 整数型:处理后的背景颜色数值.

strength 整数型:强度,取值范围1-10.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskErase(0, mask, vu.Rgb2Long("000000"), 1);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置,进行颜色填充.

函数原型:

long ImgMaskFill(LONG id, LONG64 pMask, long rgb, long alpha)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

rgb 整数型:要填充的颜色数值(RGB格式).

alpha 整数型:透明度,取值范围0-255.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskFill(0, mask, vu.Rgb2Long("000000"), 255);

---

## 

函数简介:

蒙版,获取蒙版的轮廓.

在编图时,可以将蒙版当做一个二值化的图像,所以也可以对蒙版进行轮廓检测.

调用本函数后,可以像调用过了ImgContoursInit一样使用轮廓检测的相关函数.

函数原型:

long ImgMaskGetContours(LONG id, LONG64 pMask)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

返回值:

整数型:

返回蒙版中轮廓的数量.

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	ret = vu.ImgMaskGetContours(0, mask);

	std::cout << "轮廓数量:" << ret << std::endl;

	for (size_t i = 0; i < ret; i++)

	{

		res = vu.ImgContoursGetPoints(0, i);

		std::cout << "轮廓:" << res << std::endl;

	}

---

## 

函数简介:

蒙版,将指定的蒙版区域中所有标记进行反转.

注意:如果反转通过ImgMaskCircle或者ImgMaskRect构建的蒙版,那么其参数isGradient导致的渐变将会无法反转.

函数原型:

LONG64 ImgMaskInvert(LONG id, LONG64 pMask)

参数定义:

id 整数型:图层ID.

pMask 长整数型:通过ImgMaskSelected、ImgMaskCircle等函数构建的蒙版指针.

返回值:

长整数型:

成功返回一个新的蒙版对象指针,失败返回0.

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	//蒙版标记反转

	mask  = vu.ImgMaskInvert(0, mask);

	//对蒙版标记的像素进行操作

	vu.ImgMaskFill(0, mask, vu.Rgb2Long("000000"), 255);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置进行抠图处理.

函数原型:

long ImgMaskMatting(LONG id, LONG64 pMask, long bg_rgb, bool isCropped)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

bg_rgb 整数型:处理后的背景颜色数值.

isCropped 整数型:是否对新图片进行裁剪,以适应抠出来的图片的大小.值为0不裁剪,值为1表示进行裁剪.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskMatting(0, mask, vu.Rgb2Long("000000"), 0);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

---

## 

函数简介:

蒙版,构建多边形蒙版区域.必须配合ImgPolyAdd增加多边形顶点后才可以调用本函数.

函数原型:

LONG64 ImgMaskPoly(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

长整数型:

成功返回一个蒙版对象指针,失败返回0.

示例:

	//构建多边形顶点

	vu.ImgPolyClear(0);

	vu.ImgPolyAdd(0, 10, 10);

	vu.ImgPolyAdd(0, 10, 20);

	vu.ImgPolyAdd(0, 20, 30);

	vu.ImgPolyAdd(0, 30, 40);

	vu.ImgPolyAdd(0, 10, 50);

 

	//根据多边形顶点构建蒙版标记

	mask = vu.ImgMaskPoly(0);

 

	//对蒙版标记的像素进行操作

	vu.ImgMaskFill(0, mask, vu.Rgb2Long("000000"), 255);

---

## 

函数简介:

蒙版,构建矩形蒙版区域.

对蒙版区域的图像进行处理时,非蒙版标记的位置不会受到图像操作的影响.

函数原型:

LONG64 ImgMaskRect(LONG id, int x1, int y1, int x2, int y2, bool isGradient)

参数定义:

id 整数型:图层ID.

x1 整数型:左上X坐标

y1 整数型:左上Y坐标

x2 整数型:右下X坐标

y2 整数型:右下Y坐标

isGradient 整数型:是否渐变(羽化),值为0表示不渐变,为1表示靠近边缘位置的蒙版会发生渐变效果.

返回值:

长整数型:

成功返回一个蒙版对象指针,失败返回0.

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	//对蒙版标记的像素进行操作

	vu.ImgMaskFill(0, mask, vu.Rgb2Long("000000"), 255);

---

## 

函数简介:

蒙版,根据选择器中的标记,构建蒙版.

对蒙版区域的图像进行处理时,非蒙版标记的位置不会受到图像操作的影响.

函数原型:

LONG64 ImgMaskSelected(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

长整数型:

成功返回一个蒙版对象指针,失败返回0.

示例:

	//初始化并标记选择

	vu.ImgSelectInit(0);

	vu.ImgSelectAddColor(0, vu.Rgb2Long("ff0000"), vu.Rgb2Long("202020"), 1);

	vu.ImgSelectAddLine(0, 10, 10, 50, 50, 1, 1);

	vu.ImgSelectAddPoint(0, 10, 10, 1);

	//通过选择标记来构建蒙版

	mask = vu.ImgMaskSelected(0);

 

	//对蒙版标记的像素进行操作

	vu.ImgMaskFill(0, mask, vu.Rgb2Long("000000"), 255);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置,设置HSV.

函数原型:

long ImgMaskSetHSV(LONG id, LONG64 pMask, long mode, long h, long s, long v)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

mode 整数型:设置模式,取值如下

0:自增模式,此时hsv的值是与参数传递的hsv参数进行相加.

1:改值模式,此时hsv的值等于参数传递的hsv参数.

h 整数型:色相值,用来表示红绿蓝,取值范围0-180.

s 整数型:饱和度,用来表示颜色的纯度或深浅程度,取值范围0-255.

v 整数型:亮度,用来表示颜色的明暗程度,取值范围0-255.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskSetHSV(0, mask, 0, 10, 10, 10);

---

## 

函数简介:

蒙版,对指定图层中蒙版标记位置进行锐化处理.

函数原型:

long ImgMaskSharpen(LONG id, LONG64 pMask, int strength)

参数定义:

id 整数型:图层ID.

pMask 长整数型:蒙版对象指针.

strength 整数型:强度,取值范围1-10.

返回值:

整数型:

0:失败

1:成功

示例:

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	vu.ImgMaskSharpen(0, mask, 1);

---

## 

函数简介:

对指定图像/蒙版对象进行基础运算或位运算.

一般用来实现画面增强,也可以用来对两张图片的融合.

如果是对两个图像进行运算,请务必保证两个图像尺寸和通道数都相同,否则可能产生不可预知错误.

函数原型:

LONG64 ImgOperator(LONG id, long mode, LONG64 pObj1, LONG64 pObj2, LONG64 pMask)

参数定义:

id 整数型:图层ID.

mode 整数型:运算方式,取值如下

0:矩阵相加,pObj1和pObj2执行相加操作

1:矩阵相减,用pObj1减去pObj2

2:矩阵相乘,pObj1和pObj2执行相乘操作

3:矩阵相除,用pObj1除以pObj2

4:矩阵位与(and),pObj1和pObj2执行and操作

5:矩阵位或(or),pObj1和pObj2执行or操作

6:矩阵异或(xor),pObj1和pObj2执行xor操作

7:矩阵取反(not),将pObj1中的所有数据执行not操作,当使用此模式时,参数pObj2为无效参数,仅对pObj1执行.

pMask 长整数型:蒙版指针,需要对图像矩阵数据进行运算的蒙版区域,此参数值为0则表示对整个图像矩阵进行运算.

返回值:

长整数型:

返回一个存储着运算结果的对象指针,它根据参数决定是什么类型,

例如:

当pObj1和pObj2都是图像对象时,返回的就是运算后的图像对象指针.

当pObj1和pObj2都是蒙版对象时,返回的就是运算后的蒙版对象指针.

失败返回0.

示例:

	//两张图片实现相加融合

	vu.ImgLoadFile(0, "c:\\pic\\0.bmp");

	vu.ImgLoadFile(1, "c:\\pic\\1.bmp");

	obj_0 = vu.ImgGetImgObj(0);

	obj_1 = vu.ImgGetImgObj(1);

	obj = vu.ImgOperator(0, 0, obj_0, obj_1, 0);

	//新建图层并显示图片

	vu.ImgLoadImgObj(3, obj);

	vu.ImgShow(3, "");

	vu.WaitKey(3, 0);

 

	//对指定区域进行位与运算

	mask = vu.ImgMaskRect(0, 100, 100, 200, 300, 0);

	obj = vu.ImgOperator(0, 4, obj_0, obj_1, mask);

	//新建图层并显示图片

	vu.ImgLoadImgObj(3, obj);

	vu.ImgShow(3, "");

	vu.WaitKey(3, 0);

---

## 

函数简介:

在指定图层中新增多边形顶点坐标,用以构建多边形.

函数原型:

long ImgPolyAdd(LONG id, long x, long y)

参数定义:

id 整数型:图层ID.

x 整数型:多边形顶点的x坐标

y 整数型:多边形顶点的y坐标

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgPolyClear(0);

 

	vu.ImgPolyAdd(0, 10, 10);

	vu.ImgPolyAdd(0, 10, 20);

	vu.ImgPolyAdd(0, 20, 30);

	vu.ImgPolyAdd(0, 30, 40);

	vu.ImgPolyAdd(0, 10, 50);

 

	vu.ImgDrawPoly(0, vu.Rgb2Long("FF00FF"), 1, 255, 1);

---

## 

函数简介:

清除多边形中的顶点数据,用ImgPolyAdd增加的顶点全部清除

函数原型:

long ImgPolyClear(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgPolyClear(0);

---

## 

函数简介:

获取多边形数据中多边形的面积.

函数原型:

double ImgPolyGetArea(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

双精度浮点型:

返回多边形的面积.

示例:

	vu.ImgPolyClear(0);

	vu.ImgPolyAdd(0, 10, 10);

	vu.ImgPolyAdd(0, 10, 20);

	vu.ImgPolyAdd(0, 20, 30);

	vu.ImgPolyAdd(0, 30, 40);

	vu.ImgPolyAdd(0, 10, 50);

	ret = vu.ImgPolyGetArea(0);

---

## 

函数简介:

获取多边形数据中多边形的周长.

函数原型:

double ImgPolyGetGirth(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

双精度浮点型:

返回多边形的周长.

示例:

vu.ImgPolyClear(0);

vu.ImgPolyAdd(0, 10, 10);

vu.ImgPolyAdd(0, 10, 20);

vu.ImgPolyAdd(0, 20, 30);

vu.ImgPolyAdd(0, 30, 40);

vu.ImgPolyAdd(0, 10, 50);

ret = vu.ImgPolyGetGirth(0);

---

## 

函数简介:

获取多边形的最小外接矩形(一个包含多边形所有点的最小面积的矩形).

函数原型:

string ImgPolyGetPointsRange(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

字符串:

返回的是最小外接矩形的所有顶点坐标,格式如下:"id,x,y|id,x,y..|id,x,y" 

示例:

	vu.ImgPolyClear(0);

	vu.ImgPolyAdd(0, 10, 10);

	vu.ImgPolyAdd(0, 10, 20);

	vu.ImgPolyAdd(0, 20, 30);

	vu.ImgPolyAdd(0, 30, 40);

	vu.ImgPolyAdd(0, 10, 50);

	res = vu.ImgPolyGetPointsRange(0);

	vusoft vs;

	long len = vs.StrSplitInit(res, "|");

	for (long i = 0; i < len; i++)

	{

		  const char* ss = vs.StrSplitGet(i);

		  vusoft v;

		  long n = v.StrSplitInit(ss, ",");

		  if (n != 2)

			  continue;

		  long x = v.StrToNum(v.StrSplitGet(0), 10);

		  long y = v.StrToNum(v.StrSplitGet(1), 10);

		  std::cout << "矩形顶点:" << x << "," << y << std::endl;

	}

---

## 

函数简介:

检测指定坐标是否包含在多边形中.

函数原型:

long ImgPolyIsContain(LONG id, long x, long y)

参数定义:

id 整数型:图层ID.

x 整数型:要检测的x坐标

y 整数型:要检测的y坐标

返回值:

整数型:

0:目标坐标位于多边形边线上.

1:目标坐标位于多边形内部.

-1:目标坐标位于多边形外部.

示例:

	ret = vu.ImgPolyIsContain(0, 10, 10);

	if (ret == 0)

		    std::cout << "点在多边形的边线上" << std::endl;

	if (ret == 1)

		    std::cout << "点在多边形内部" << std::endl;

	if (ret == -1)

		    std::cout << "点在多边形外部" << std::endl;

---

## 

函数简介:

获取在多边形中距离指定坐标最近的边(两个点组成的线条).

函数原型:

double ImgPolyNearestEdge(LONG id, int x, int y, int& beginX, int& beginY, int& endX, int& endY)

参数定义:

id 整数型:图层ID.

x 整数型:要检测的x坐标

y 整数型:要检测的y坐标

beginX 变参指针:返回起始x坐标

beginY 变参指针:返回起始y坐标

endX 变参指针:返回结束x坐标

endY 变参指针:返回结束y坐标

返回值:

双精度浮点型:

返回x,y坐标与最近的边的距离.

示例:

	distance = vu.ImgPolyNearestEdge(0, 10, 10, beginX, beginY, endX, endY);

---

## 

函数简介:

对图像进行旋转操作.

函数原型:

long ImgRotate(LONG id, double angle, long rgb)

参数定义:

id 整数型:图层ID.

angle 双精度浮点型:选择的角度,取值范围0-359

rgb 整数型:要填充的背景颜色数值,发生旋转后往往图像尺寸也会发生改变,空白出来的区域用此值的颜色进行填充.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgRotate(0, 15, vu.Rgb2Long("FF00FF"));

---

## 

函数简介:

将图层保存为图片文件

函数原型:

long ImgSaveToFile(LONG id, string file, long alpha_rgb, long offset_rgb)

参数定义:

id 整数型:图层ID.

file 字符串:保存到的文件路径,后缀通常是.bmp/png/jpg

alpha_rgb 整数型:指定透明的RGB颜色,仅支持png格式图片

offset_rgb 整数型:透明RGB颜色的色偏值,默认填0即可

返回值:

整数型:

0:失败

1:成功

示例:

    //绝对路径

    vu.ImgSaveToFile(0, "c:\\test.png", vu.Rgb2Long("ff00ff"), vu.Rgb2Long("202020"));

    //相对路径

    vu.SetPath("c:\\PS\\");

    vu.ImgSaveToFile(0, "test.png", vu.Rgb2Long("ff00ff"), vu.Rgb2Long("202020"));

---

## 

函数简介:

选择器,在选择器中新增颜色.

所有被增加的颜色将会被标记为选中或未选中状态,可以用来对这些已经标记状态的图像位置进行抠图、换色、模糊、锐化等处理.

函数原型:

long ImgSelectAddColor(LONG id, long rgb, long offset, int mode)

参数定义:

id 整数型:图层ID.

rgb 整数型:需要在选择器中新增的颜色数值

offset 整数型:指定新增颜色的色偏,需要通过Rgb2Long将其转换为对应RGB的色偏

mode 整数型:选择模式,取值如下

0:设置x,y点位为取消选择/未选择状态

1:设置x,y点位为被选择状态

返回值:

整数型:

0:失败

1:成功

示例:

	ret = vu.ImgSelectInit(0);

	vu.ImgSelectAddColor(0, vu.Rgb2Long("ff0000"), vu.Rgb2Long("202020"), 1);

---

## 

函数简介:

选择器,在选择器中新增线条.

所有被增加的线条将会被标记为选中或未选中状态,可以用来对这些已经标记状态的图像位置进行抠图、换色、模糊、锐化等处理.

函数原型:

long ImgSelectAddLine(LONG id, int beginX, int beginY, int endX, int endY, long thickness, int mode)

参数定义:

id 整数型:图层ID.

beginX 整数型:新增线条的起始x位置

beginY 整数型:新增线条的起始y位置

endX 整数型:新增线条的结束x位置

endY 整数型:新增线条的结束y位置

thickness 整数型:线条厚度,或者说是线条宽度

mode 整数型:选择模式,取值如下

0:设置x,y点位为取消选择/未选择状态

1:设置x,y点位为被选择状态

返回值:

整数型:

0:失败

1:成功

示例:

	ret = vu.ImgSelectInit(0);

	vu.ImgSelectAddLine(0, 10, 10, 50, 50, 1, 1);

---

## 

函数简介:

选择器,在选择器中新增点位.

所有被增加的点位将会被标记为选中或未选中状态,可以用来对这些已经标记状态的图像位置进行抠图、换色、模糊、锐化等处理.

函数原型:

long ImgSelectAddPoint(LONG id, int x, int y, int mode)

参数定义:

id 整数型:图层ID.

x 整数型:新增点的x坐标

y 整数型:新增点的y坐标

mode 整数型:选择模式,取值如下

0:设置x,y点位为取消选择/未选择状态

1:设置x,y点位为被选择状态

返回值:

整数型:

0:失败

1:成功

示例:

	ret = vu.ImgSelectInit(0);

	vu.ImgSelectAddPoint(0, 10, 10, 1);

---

## 

函数简介:

选择器,通过选择器获取选中部分的轮廓,返回轮廓数量.

调用本函数之后,便可以像调用过ContoursInit一样,去调用关于轮廓处理的各个函数.

函数原型:

long ImgSelectGetContours(LONG id, bool isInvert)

参数定义:

id 整数型:图层ID.

isInvert 整数型:是否反转选择状态,值为0表示不进行反转,值为1表示将所有标记进行反转.

返回值:

整数型:

0:失败

1:成功

示例:

	ret = vu.ImgSelectGetContours(0, 0);

	std::cout << "轮廓数量:" << ret << std::endl;

	for (size_t i = 0; i < ret; i++)

	{

		    res = vu.ImgContoursGetPoints(0, i);

		    std::cout << "轮廓:" << res << std::endl;

	}

---

## 

函数简介:

选择器,初始化.

在图层中使用选择器对图像指定区域(可以是一个多边形区域)进行蒙版处理.

一般用于抠图、换色、模糊、锐化等处理.

函数原型:

long ImgSelectInit(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

0:失败

1:成功

示例:

	ret = vu.ImgSelectInit(0);

---

## 

函数简介:

选择器,对当前选择器所有标记状态进行优化,以获取最佳蒙版.

函数原型:

long ImgSelectOptimize(LONG id, long mode)

参数定义:

id 整数型:图层ID.

mode 整数型:优化模式,取值如下

0:常规模式,效果普通

1:加强模式,效果最好,速度会慢

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgSelectOptimize(0,1);

---

## 

函数简介:

设置图层指定位置的像素颜色.

函数原型:

long ImgSetColor(LONG id, long x, long y, long rgb, long alpha)

参数定义:

id 整数型:图层ID.

x 整数型:要被设置颜色的x位置

y 整数型:要被设置颜色的y位置

rgb 整数型:要被设置新颜色的rgb数值

alpha 整数型:要被设置新颜色的透明度,取值范围0-255.

返回值:

整数型:

0:失败

1:成功

示例:

    vu.ImgSetColor(0, 100, 200, vu.Rgb2Long("ff00ff"), 123);

---

## 

函数简介:

设置图层图片尺寸.

函数原型:

long ImgSetSize(LONG id, long width, long height, long mode, long rgb)

参数定义:

id 整数型:图层ID.

width 整数型:图片的新宽度

height 整数型:图片的新高度

mode 整数型:缩放模式,取值如下

0:不进行自适应缩放(新图片会被拉伸变形)

1:进行自适应缩放(新图片不会被拉伸变形,保存与原图像宽高同比例)

rgb 整数型:要填充的背景颜色数值.只有当mode为1时才起作用,当图像比例未变,新图多余的部分用此颜色进行填充.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgSetSize(0, 100, 100, 1, vu.Rgb2Long("FF00FF"));

---

## 

函数简介:

显示图层图像,一般调试用.

函数原型:

long ImgShow(LONG id, string title)

参数定义:

id 整数型:图层ID.

title 字符串:显示窗口的窗口标题.

返回值:

整数型:

0:失败

1:成功

示例:

    vu.ImgLoadFile(0, "c:\\test.png");

    vu.ImgShow(0, "test");

---

## 

函数简介:

将指定id图层的图片与指定的另外一张图片进行拼接,形成一张新的融合图片,可用来实现制作全景图、VR场景、场景地图等.

注意:本函数是利用图片特征进行拼接,所以两张图片必须同时具有相同特征的部分,否则有可能拼接失败.

本函数制作的图片不同于制作九宫图,而是将两张图片拼接融合为一张图片,若想实现类似于九宫图的制作,请直接使用ImgDrawPic或者ImgDrawPicEx进行实现.

函数原型:

long ImgStitch(LONG id, LONG64 pImg, long mode, long detMode, double matchThresh, long matchMode, long rgb)

参数定义:

id 整数型:图层ID.

pImg 长整数型:一个图片对象指针,一般是通过ImgGetImgObj来获取.

mode 整数型:拼接模式,取值如下

0:常规模式,不处理接缝

1:接缝优化,尽量淡化两张图片接缝

detMode 整数型:推理模式,取值如下

0:均衡模式

1:精准模式

2:快速模式

matchThresh 双精度浮点型:特征阈值,取值范围0-1.0,用来限定匹配到的特征个数

matchMode 整数型:匹配模式,取值如下

0:常规模式,速度较慢,但是效果最好

1:快速模式,速度快但是可能会出现特征匹配错误的情况.

rgb 整数型:拼接后新图片的背景颜色数值

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\左图.bmp");

	vu.ImgLoadFile(1, "c:\\pic\\右图.bmp");

	obj_1 = vu.ImgGetImgObj(1);

	vu.ImgStitch(0, obj_1, 1, 0, 0.75, 0, vu.Rgb2Long("000000"));

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

上述示例是将左图和右图进行特征拼接.

两张图片的原图分别为:

    

拼接后的成品图片为:

---

## 

函数简介:

拼接器,在指定图层的拼接器中新增需要拼接的图像对象.

函数原型:

long ImgStitcherAdd(LONG id, LONG64 pImg)

参数定义:

id 整数型:图层ID.

pImg 长整数型:一个图片对象指针,一般是通过ImgGetImgObj来获取.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(1, "c:\\pic\\test.bmp");

	obj = vu.ImgGetImgObj(1);

	vu.ImgStitcherAdd(0, obj);

---

## 

函数简介:

拼接器,获取当前图层拼接器中已经加载的待拼接图像数量.

函数原型:

long ImgStitcherCount(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

返回待拼接图像数量

示例:

	ret = vu.ImgStitcherCount(0);

---

## 

函数简介:

拼接器,图片拼接器初始化.

拼接器功能与函数Stitch的功能类似,但是拼接器可以同时对多个图片进行拼接,而且效果更好,不过相应的它的使用方法会更复杂,执行速度也可能会慢一些.

若需要实时拼接图像,请做好测试,因为有些情况拼接器反而比Stitch速度更快.

函数原型:

long ImgStitcherInit(LONG id, long detMode, bool isScans)

参数定义:

id 整数型:图层ID.

detMode 整数型:推理模式,取值如下

0:均衡模式

1:精准模式

2:快速模式

-1:优化模式,效果好,速度也差不多

isScans 整数型:是否扫描模式,取值如下

0:通用拼接器,通常用来实现对风景、室内、全景图等图像拼接

1:扫描拼接器,通常用来对文档、页面、图像碎片的排列和复原

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgStitcherInit(0, -1, 0);

---

## 

函数简介:

拼接器,将指定图层中已经加载的所有图像进行拼接.

函数原型:

long ImgStitcherRun(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

0:失败

1:成功

示例:

	//加载图像

	vu.ImgLoadFile(1, "c:\\pic\\左图.bmp");

	vu.ImgLoadFile(2, "c:\\pic\\右图.bmp");

 

	//初始化拼接器

	vu.ImgStitcherInit(0, 0, 0);

	//将图像对象加载到拼接器中

	vu.ImgStitcherAdd(0, vu.ImgGetImgObj(1));

	vu.ImgStitcherAdd(0, vu.ImgGetImgObj(2));

	//拼接器执行拼接

	ret = vu.ImgStitcherRun(0);

	//显示拼接后的图像

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

 

以上示例展示了完整的拼接器使用方法,效果如下

两张图片的原图分别为:

    

经过拼接器拼接后的图像:

---

## 

函数简介:

将其他颜色格式的图层转为BGR格式,一般情况下只有图层被转为HSV格式后才需要调用本函数转换回来.

注意:在图像编辑的所有功能中,默认图像格式均为BGR格式.无论是在哪个函数中传递RGB颜色,内部都会转换为BGR,这是因为在图像编辑的底层,只有对BGR格式的图像进行操作才最方便.

不过为了统一和其他图色功能的接口,在图像编辑时会使用RGB格式作为参数进行传递,或者将RGB作为图像结果进行输出.例如ImgGetColor函数和ImgMaskFill函数,均是针对RGB的(但是在编图时还是用的BGR).

函数原型:

long ImgToBGR(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

0:失败

1:成功

示例:

    //载入图层图像

    vu.ImgLoadFile(0, "c:\\test.png");

    //转换为HSV格式

    vu.ImgToHSV(0);

    //构建遮罩

    obj_mask = vu.ImgMaskRect(0, 10, 10, 100, 100, 0);

    //设置遮罩中的HSV值

    vu.ImgMaskSetHSV(0, obj_mask, 1, 180, 100, 100);

    //转换为BGR格式

    vu.ImgToBGR(0);

    //其他操作

    //....

---

## 

函数简介:

将彩色图层转为二值化的黑白图像.

函数原型:

long ImgToBinary(LONG id, long thresh)

参数定义:

id 整数型:图层ID.

thresh 整数型:黑白转换的阈值,有两种模式可用.

1.取值范围1-255,所有大于此值的像素都被设置为白色,否则为黑色.

2.取值范围-1到-10(负数),自适应二值化黑白图,值为强度,默认为-1

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\test.bmp");

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

	vu.ImgToBinary(0, -1);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

 

上述示例是将一张彩色图转换为黑白图.

转换前图像:

 

转换后图像:

---

## 

函数简介:

将一幅灰度图或彩色图应用一个预定义的颜色映射，从而转换为一个伪彩色图像.

它可以将灰度图像转换为彩色图像，以便在显示或进一步处理时更容易区分不同的灰度级别.此外，它也可以用于增强彩色图像的视觉效果，或者在特定的图像处理任务中改变图像的颜色表示.

函数原型:

long ImgToColor(LONG id, long colormap)

参数定义:

id 整数型:图层ID.

colormap 整数型:指定颜色映射类型,取值范围0-21.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\test.bmp");

	vu.ImgToGray(0);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

	vu.ImgToColor(0, 0);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

 

上述示例是将一张灰度图转换为伪彩图.

转换前图像:

 

转换后图像:

---

## 

函数简介:

将指定图层图片转为二值化的边线图,转换后的图层一般可以用来进行轮廓查找,物体识别等.

注意:调用本函数后会将彩色BGR图片转换为二值化图片,但是如果您对边线图精度有要求,尽量在调用前先自主将图层转二值化处理,这样边线图效果会更好一些.

函数原型:

long ImgToEdges(LONG id, double lower_thresh, double upper_thresh, int strength, bool fast)

参数定义:

id 整数型:图层ID.

lower_thresh 双精度浮点型:下限阈值,只有当像素的颜色强度大于或等于这个阈值时，它才可能被接受为边缘的一部分,依赖周围像素.

upper_thresh 双精度浮点型:上限阈值,只有当像素的颜色强度大于或等于这个阈值时，它才会被直接认为是边缘的一部分,不依赖周围像素.

strength 整数型:转换强度,取值范围1-10.

fast 整数型:是否快速检测,取值如下

0:精确检测

1:快速检测

返回值:

整数型:

0:失败

1:成功

示例:

    vu.ImgLoadFile(0, "c:\\pic\\test.bmp");

    vu.ImgShow(0, "");

    vu.WaitKey(0, 0);

    vu.ImgToEdges(0, 50, 100, 2, 1);

    vu.ImgShow(0, "");

    vu.WaitKey(0, 0);

 

上述示例是将一张彩色图像转为默认的二值化边线图.

转换前图像:

 

转换后图像:

---

## 

函数简介:

将指定图层图片转为二值化的灰度图.

函数原型:

long ImgToGray(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgLoadFile(0, "c:\\pic\\test.bmp");

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

	vu.ImgToGray(0);

	vu.ImgShow(0, "");

	vu.WaitKey(0, 0);

 

上述示例是将一张彩色图像转为默认的二值化灰度图.

转换前图像:

 

转换后图像:

---

## 

函数简介:

将图层颜色模式转为HSV格式.

注意:在修改HSV值时必须提前将图层修改为HSV格式,也仅限修改HSV值时才可以调用本函数,如果需要对图像进行其他操作,请务必转换回BGR格式,否则图像将会发生不可预知的错误.

函数原型:

long ImgToHSV(LONG id)

参数定义:

id 整数型:图层ID.

返回值:

整数型:

0:失败

1:成功

示例:

    //载入图层图像

    vu.ImgLoadFile(0, "c:\\test.png");

    //转换为HSV格式

    vu.ImgToHSV(0);

    //构建遮罩

    obj_mask = vu.ImgMaskRect(0, 10, 10, 100, 100, 0);

    //设置遮罩中的HSV值

    vu.ImgMaskSetHSV(0, obj_mask, 1, 180, 100, 100);

    //转换为BGR格式

    vu.ImgToBGR(0);

    //其他操作

    //....

---

## 

函数简介:

对图像进行平移操作.

函数原型:

long ImgTranslation(LONG id, int offsetX, int offsetY, long rgb)

参数定义:

id 整数型:图层ID.

offsetX 整数型:需要移动相对x轴的相对距离,以像素为单位

offsetY 整数型:需要移动相对y轴的相对距离,以像素为单位

rgb 整数型:要填充的背景颜色数值,发生平移后,空白出来的区域用此值的颜色进行填充.

返回值:

整数型:

0:失败

1:成功

示例:

	vu.ImgTranslation(0, 100, 100, vu.Rgb2Long("FF00FF"));

---

## 

函数简介:

提取RGB颜色的hsv值.

函数原型:

string Rgb2Hsv(rgb,h,s,v)

参数定义:

rgb 整数型:rgb颜色的数值.

h 变参指针:返回RGB颜色的色相值,用来表示红绿蓝,取值范围一般在0-360之间.

s 变参指针:返回RGB颜色的饱和度,用来表示颜色的纯度或深浅程度,取值范围一般在0-100之间.

v 变参指针:返回RGB颜色的亮度,用来表示颜色的明暗程度,取值范围一般在0-100之间.

返回值:

字符串:

返回另一种表示HSV的颜色形式,它和Rgb2String类似,返回的都是一个十六进制表示的颜色,格式为HHSSVV.

注意:H部分的数值范围为0-0xB4(180),这是因为常规的H取值范围是0-360,但是在内存中如果需要用一个字节来表示它的最大值360会溢出,如果想将HSV用十六进制进行存储无疑会变得困难.但是H值的影响却是从0-180为最大(递增循环),180之后再增大其实是向0衰减(递减循环),所以我们在这里直接用180作为最大值.

示例:

    res = vu.Rgb2Hsv(123456, h, s, v);

---

## 

函数简介:

将文本型RGB颜色转数值型

函数原型:

long Rgb2Long(string rgb_str)

参数定义:

rgb_str 字符串:RGB颜色的字符串,需要用十六进制表示.格式为RRGGBB,例如:"FF00AA"

返回值:

整数型:

RGB的数值形式.

示例:

    str = "FF00AA";

    ret = vu.Rgb2Long(str);

---

## 

函数简介:

将数值型RGB颜色转为十六进制文本型.

函数原型:

string Rgb2String(long rgb)

参数定义:

rgb 整数型:rgb颜色的数值.

返回值:

字符串:

返回十六进制的RGB表示.

示例:

    res = vu.Rgb2String(123456);

---

## 

函数简介:

枚举指定进程中所有的模块名字

函数原型:

string EnumModules(DWORD hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

返回值:

字符串:
返回所有模块名字,格式"模块1,模块2,模块3"

示例:

    res = vu.EnumModules(1030);

 

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        std::cout << "进程模块:" << res << std::endl;

    }

---

## 

函数简介:

根据指定进程名,枚举系统中符合条件的进程PID,并且按照进程打开顺序排序.

函数原型:

string EnumProcess(name)

参数定义:

name 字符串:进程名,比如qq.exe

返回值:

字符串 :
返回所有匹配的进程PID,并按打开顺序排序,格式"pid1,pid2,pid3"

示例:

    res = vu.EnumProcess("notepad.exe");

 

    vusoft vs;

    ret = vs.StrSplitInit(res, ",");

    for (size_t i = 0; i < ret; i++)

    {

        res = vs.StrSplitGet(i);

        pid = vs.StrToNum(res, 10);

        std::cout << "进程id:" << pid << std::endl;

    }

---

## 

函数简介:

获取指定窗口所在进程的启动命令行

函数原型:

string GetCommandLine(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

返回值:

字符串:
读取到的启动命令行

示例:

    res = vu.GetCommandLine(hWnd);

    std::cout << "命令行参数:" << res << std::endl;

---

## 

函数简介:

根据指定的pid或者窗口句柄,获取进程详细信息,(进程名,进程全路径,CPU占用率(百分比),内存占用量(字节))

函数原型:

string GetProcessInfo(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

返回值:

字符串:
格式"进程名|进程路径|cpu|内存"

示例:

    res = vu.GetProcessInfo(hWnd);

 

    vusoft vs;

    num = vs.StrSplitInit(res, "|");

    std::cout << "进程名称:" << vs.StrSplitGet(0) << std::endl;

    std::cout << "进程路径:" << vs.StrSplitGet(1) << std::endl;

    std::cout << "CPU占用率:" << vs.StrSplitGet(2) << std::endl;

    std::cout << "内存占用量:" << vs.StrSplitGet(3) << std::endl;

---

## 

函数简介:

创建并运行一个指定程序

函数原型:

LONG ProcessCreate(file,cmdLine,showType,waitForEnd)

参数定义:

file 字符串:要被运行的程序文件路径,必须是完整的绝对路径

cmdLine 字符串:程序的启动命令行参数

showType 整数型:显示方式,取值如下

1:隐藏窗口

2:普通激活

3:最小化激活

4:最大化激活

5:普通不激活

6:最小化不激活

waitForEnd 整数型:是否阻塞等待创建的程序运行结束,1表示进行等待,不等待则填写0

返回值:

整数型:

返回创建的进程的PID,如果失败返回0

示例:

    ret = vu.ProcessCreate("c:/windows/notepad.exe","",3,0);

    std::cout << "创建的进程的Pid:" << ret << std::endl;

---

## 

函数简介:

获取当前调用插件的进程的PID

函数原型:

LONG ProcessGetCurrentPid()

参数定义:

无

返回值:

整数型:

返回当前调用进程的PID

示例:

    pid = vu.ProcessGetCurrentPid();

---

## 

函数简介:

获取指定窗口/进程的文件名

函数原型:

string ProcessGetName(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

返回值:

字符串:

程序的文件名

示例:

    res = vu.ProcessGetName(hWnd);

    std::cout << "程序名字:" << res << std::endl;

---

## 

函数简介:

获取指定窗口进程所在的文件路径

函数原型:

string ProcessGetPath(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId.

返回值:

字符串:

程序所在的路径

示例:

    res = vu.ProcessGetPath(hWnd);

    std::cout << "程序路径:" << res << std::endl;

---

## 

函数简介:

检测进程是否存活

函数原型:

LONG ProcessIsAliving(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId

返回值:

整数型:
0 : 进程不存在或者已经结束

1 : 进程存在

示例:

    //直接通过窗口句柄

    hWnd = vu.GetMousePointWindow();

    ret = vu.ProcessIsAliving(hWnd);

    std::cout << "进程是否存活:" << ret << std::endl;

 

    //或者通过PID

    vu.SetMemoryHwndAsProcessId(1);

    pid = vu.GetWindowProcessId(hwnd);

    ret = vu.ProcessIsAliving(pid);

    std::cout << "进程是否存活:" << ret << std::endl;

---

## 

函数简介:

检测进程是否被挂起.

有些时候进程存在并未被结束,但是却是被挂起状态,导致一切对进程的操作都阻塞或者无效,所以在操作进程之前,使用本函数就很管用了.

函数原型:

LONG ProcessIsHunging(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId

返回值:

整数型:
0 : 进程未被挂起

1 : 进程已经被挂起或者状态异常

 示例:

    //直接通过窗口句柄

    hWnd = vu.GetMousePointWindow();

    ret = vu.ProcessIsHunging(hWnd);

    std::cout << "进程是否挂起:" << ret << std::endl;

 

    //或者通过PID

    vu.SetMemoryHwndAsProcessId(1);

    pid = vu.GetWindowProcessId(hwnd);

    ret = vu.ProcessIsHunging(pid);

    std::cout << "进程是否挂起:" << ret << std::endl;

---

## 

函数简介:

检测进程是否64位进程

函数原型:

LONG ProcessIsX64(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId

返回值:

整数型:
0 : 32位进程

1 : 64位进程

示例:

    //直接通过窗口句柄

    hWnd = vu.GetMousePointWindow();

    ret = vu.ProcessIsX64(hWnd);

    std::cout << "进程是否64位:" << ret << std::endl;

 

    //或者通过PID

    vu.SetMemoryHwndAsProcessId(1);

    pid = vu.GetWindowProcessId(hwnd);

    ret = vu.ProcessIsX64(pid);

    std::cout << "进程是否64位:" << ret << std::endl;

---

## 

函数简介:

挂起/恢复 指定进程.

可以将指定的窗口进程挂起(暂停运行),以及恢复运行.

函数原型:

LONG ProcessSetIsSuspend(hwnd,isSuspend)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId

isSuspend 整数型:挂起或恢复运行,取值如下

1:暂停进程(挂起)

0:恢复进程(解除挂起)

返回值:

整数型:
0 : 失败

1 : 成功

示例:

    //直接通过窗口句柄

    hWnd = vu.GetMousePointWindow();

    ret = vu.ProcessSetIsSuspend(hWnd,1);

 

 

    //或者通过PID

    vu.SetMemoryHwndAsProcessId(1);

    pid = vu.GetWindowProcessId(hwnd);

    ret = vu.ProcessSetIsSuspend(pid,0);

---

## 

函数简介:

根据指定的窗口句柄，强制结束进程

函数原型:

LONG TerminateProcess(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId

返回值:

整数型:
0 : 失败

1 : 成功

示例:

    //直接通过窗口句柄操作

    hWnd = vu.GetMousePointWindow();

    vu.TerminateProcess(hWnd);

 

    //或者通过PID进行操作

    vu.SetMemoryHwndAsProcessId(1);

    pid = vu.GetWindowProcessId(hwnd);

    vu.TerminateProcess(pid);

---

## 

函数简介:

根据指定的窗口句柄，强制结束进程以及此进程创建的所有子进程

函数原型:

LONG TerminateProcessTree(hwnd)

参数定义:

hwnd 整数型: 窗口句柄或者进程ID.  默认是窗口句柄. 如果要指定为进程ID,需要调用SetMemoryHwndAsProcessId

返回值:

整数型:
0 : 失败

1 : 成功

示例:

    //直接通过窗口句柄操作

    hWnd = vu.GetMousePointWindow();

    vu.TerminateProcessTree(hWnd);

 

    //或者通过PID进行操作

    vu.SetMemoryHwndAsProcessId(1);

    pid = vu.GetWindowProcessId(hwnd);

    vu.TerminateProcessTree(pid);

---

## 

函数简介:

键盘动作模拟真实操作,点击延时随机.

函数原型:

long EnableRealKeypad(enable)

参数定义:

enable 整数型: 0 关闭模拟
               1 开启模拟

返回值:

整数型:
0: 失败
1: 成功

示例:

vu.EnableRealKeypad(1);

vu.KeyPressChar("E");

注: 此接口对KeyPress KeyPressChar KeyPressStr起作用。具体表现是键盘按下和弹起的间隔会在当前设定延时的基础上,上下随机浮动50%. 

假如设定的键盘延时是100,那么这个延时可能就是50-150之间的一个值.

设定延时的函数是 SetKeypadDelay().

---

## 

函数简介:

鼠标动作模拟真实操作,带移动轨迹,以及点击延时随机. 

函数原型:

long EnableRealMouse(enable,mousedelay,mousestep)

参数定义:

enable 整数型: 0 关闭模拟
               1 开启模拟(直线模拟)
               2 开启模拟(随机曲线,更接近真实)
               3 开启模拟(小弧度曲线,弧度随机)
               4 开启模拟(大弧度曲线,弧度随机)

mousedelay 整数型: 单位是毫秒. 表示在模拟鼠标移动轨迹时,每移动一次的时间间隔.这个值越大,鼠标移动越慢. 必须大于0,否则会失败.

Mousestep 整数型: 表示在模拟鼠标移动轨迹时,每移动一次的距离. 这个值越大，鼠标移动越快速.

返回值:

整数型:
0: 失败
1: 成功

示例:

vu.EnableRealMouse(1, 10, 20);

vu.MoveTo(100, 100);

vu.MoveTo(500, 500);

 

注: 此接口同样对LeftClick RightClick MiddleClick LeftDoubleClick起作用。

具体表现是鼠标按下和弹起的间隔会在当前设定延时的基础上,上下随机浮动50%. 

假如设定的鼠标延时是100,那么这个延时可能就是50-150之间的一个值.

设定延时的函数是 SetMouseDelay()

---

## 

函数简介:

获取鼠标位置.

函数原型:

long GetCursorPos(x,y)

参数定义:

x 变参指针: 返回X坐标

y 变参指针: 返回Y坐标

返回值:

整数型:
0 : 失败

1 : 成功

示例:

vu.GetCursorPos(x, y);

std::cout << "GetCursorPos = " << x << "," << y << std::endl;

 

注: 此接口同大多数接口一样,返回的x,y坐标是根据绑定的鼠标参数来决定.  

如果绑定了窗口，那么获取的坐标是相对于绑定窗口，否则是屏幕坐标.  
另外，此函数获取的坐标是真实的鼠标坐标，对于某些自绘鼠标位置不一定准确。请自行测试.

---

## 

函数简介:

获取鼠标特征码. 当BindWindow或者BindWindowEx中的mouse参数含有dx时，获取到的是后台鼠标特征，否则是前台鼠标特征. 

函数原型:

string GetCursorShape()

参数定义:

无

返回值:

字符串:
成功时，返回鼠标特征码.  
失败时，返回空的串.

示例:

    mouse_tz = vu.GetCursorShape();

    if(strlen(mouse_tz))

        std::cout << "找到特征码:"<< mouse_tz << std::endl;

---

## 

函数简介:

获取鼠标特征码. 当BindWindow或者BindWindowEx中的mouse参数含有dx时，获取到的是后台鼠标特征，否则是前台鼠标特征

函数原型:

string GetCursorShapeEx(type)

参数定义:

type 整数型:获取鼠标特征码的方式. 和工具中的方式1 方式2对应. 方式1此参数值为0. 方式2此参数值为1.

返回值:

字符串:
成功时，返回鼠标特征码.  
失败时，返回空的串.

示例:

    mouse_tz = vu.GetCursorShapeEx(0);

    if(strlen(mouse_tz))

        std::cout << "找到特征码:"<< mouse_tz << std::endl;

---

## 

函数简介:

获取鼠标热点位置.

函数原型:

long GetCursorSpot(x,y)

参数定义:

x 变参指针: 返回X坐标

y 变参指针: 返回Y坐标

返回值:

整数型:
0 : 失败

1 : 成功

示例:

vu.GetCursorSpot(x, y);

std::cout << x << "," << y << std::endl;

---

## 

函数简介:

获取指定的按键状态.(前台信息,不是后台)

函数原型:

long GetKeyState(vk_code)

参数定义:

vk_code 整数型:虚拟按键码

返回值:

整数型:
0:弹起
1:按下

示例:

    ret = vu.GetKeyState(13);

    std::cout << "键 [enter](13) 状态:" << ret << std::endl;

---

## 

函数简介:

获取系统鼠标的移动速度.  如图所示红色区域. 一共分为11个级别. 从1开始,11结束. 这仅是前台鼠标的速度. 后台不用理会这个.

 

函数原型:

long GetMouseSpeed()

参数定义:

无

返回值:

整数型:
0:失败
其他值,当前系统鼠标的移动速度

示例:

    ret = vu.GetMouseSpeed();

    std::cout << ret << std::endl;

---

## 

函数简介:

按住指定的虚拟键码

函数原型:

long KeyDown(vk_code)

参数定义:

vk_code 整数型:虚拟按键码

返回值:

整数型:
0:失败
1:成功

示例:

    vu.KeyDown(13);

---

## 

函数简介:

按住指定的虚拟键码

函数原型:

long KeyDownChar(key_str)

参数定义:

key_str 字符串: 字符串描述的键码. 大小写无所谓.

返回值:

整数型:
0:失败
1:成功

示例:

    vu.KeyDownChar("enter");

    vu.KeyDownChar("1");

    vu.KeyDownChar("F1");

    vu.KeyDownChar("a");

    vu.KeyDownChar("B");

---

## 

函数简介:

按下指定的虚拟键码

函数原型:

long KeyPress(vk_code)

参数定义:

vk_code 整数型:虚拟按键码

返回值:

整数型:
0:失败
1:成功

示例:

    vu.KeyPress(13);

---

## 

函数简介:

按下指定的虚拟键码

函数原型:

long KeyPressChar(key_str)

参数定义:

key_str 字符串: 字符串描述的键码. 大小写无所谓.

返回值:

整数型:
0:失败
1:成功

示例:

    vu.KeyPressChar("enter");

    vu.KeyPressChar("1");

    vu.KeyPressChar("F1");

    vu.KeyPressChar("a");

    vu.KeyPressChar("B");

---

## 

函数简介:

根据指定的字符串序列，依次按顺序按下其中的字符.

函数原型:

long KeyPressStr(key_str,delay)

参数定义:

key_str 字符串: 需要按下的字符串序列. 比如"1234","abcd","7389,1462"等.

delay 整数型: 每按下一个按键，需要延时多久. 单位毫秒.这个值越大，按的速度越慢。

返回值:

整数型:
0:失败
1:成功

示例:

vu.KeyPressStr("123,456", 20);

注: 在某些情况下，SendString和SendString2都无法输入文字时，可以考虑用这个来输入.

但这个接口只支持标准ASCII可见字符,其它字符一律不支持.(包括中文)

---

## 

函数简介:

弹起来虚拟键vk_code

函数原型:

long KeyUp(vk_code)

参数定义:

vk_code 整数型:虚拟按键码

返回值:

整数型:
0:失败
1:成功

示例:

    vu.KeyUp(13);

---

## 

函数简介:

弹起来指定的虚拟键码

函数原型:

long KeyUpChar(key_str)

参数定义:

key_str 字符串: 字符串描述的键码. 大小写无所谓.

返回值:

整数型:
0:失败
1:成功

示例:

    vu.KeyUpChar("enter");

    vu.KeyUpChar("1");

    vu.KeyUpChar("F1");

    vu.KeyUpChar("a");

    vu.KeyUpChar("B");

---

## 

函数简介:

按下鼠标左键

函数原型:

long LeftClick()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.LeftClick();

---

## 

函数简介:

双击鼠标左键

函数原型:

long LeftDoubleClick()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.LeftDoubleClick();

---

## 

函数简介:

按下鼠标左键

函数原型:

long LeftDown()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.LeftDown();

---

## 

函数简介:

弹起鼠标左键

函数原型:

long LeftUp()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.LeftUp();

---

## 

函数简介:

按下鼠标中键

函数原型:

long MiddleClick()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.MiddleClick();

---

## 

函数简介:

按住鼠标中键

函数原型:

long MiddleDown()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.MiddleDown();

---

## 

函数简介:

弹起鼠标中键

函数原型:

long MiddleUp()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.MiddleUp();

---

## 

函数简介:

鼠标相对于上次的位置移动rx,ry.

函数原型:

long MoveR(rx,ry)

参数定义:

rx 整数型:相对于上次的X偏移
ry 整数型:相对于上次的Y偏移

返回值:

整数型:
0:失败
1:成功

示例:

vu.MoveR(rx, ry);

---

## 

函数简介:

把鼠标移动到目的点(x,y)

函数原型:

long MoveTo(x,y)

参数定义:

x 整数型:X坐标

y 整数型:Y坐标

返回值:

整数型:
0:失败
1:成功

示例:

vu.MoveTo(x, y);

---

## 

函数简介:

把鼠标移动到目的范围内的任意一点

函数原型:

string MoveToEx(x,y,w,h)

参数定义:

x 整数型:X坐标
y 整数型:Y坐标
w 整数型:宽度(从x计算起)
h 整数型:高度(从y计算起)

返回值:

字符串:
返回要移动到的目标点. 格式为x,y.  比如MoveToEx 100,100,10,10,返回值可能是101,102

示例:

// 移动鼠标到(100,100)到(110,110)这个矩形范围内的任意一点.

vu.MoveToEx(100,100,10,10)

注: 此函数的意思是移动鼠标到指定的范围(x,y,x+w,y+h)内的任意随机一点.

---

## 

函数简介:

按下鼠标右键

函数原型:

long RightClick()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.RightClick();

---

## 

函数简介:

按住鼠标右键

函数原型:

long RightDown()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.RightDown();

---

## 

函数简介:

弹起鼠标右键

函数原型:

long RightUp()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.RightUp();

---

## 

函数简介:

设置按键时,键盘按下和弹起的时间间隔。高级用户使用。某些窗口可能需要调整这个参数才可以正常按键。

函数原型:

long SetKeypadDelay(delay)

参数定义:

delay 整数型: 延时,单位是毫秒

返回值:

整数型:
0:失败
1:成功

示例:

    vu.SetKeypadDelay(50);

---

## 

函数简介:

设置鼠标单击或者双击时,鼠标按下和弹起的时间间隔。高级用户使用。某些窗口可能需要调整这个参数才可以正常点击。

函数原型:

long SetMouseDelay(delay)

参数定义:

delay 整数型: 延时,单位是毫秒

返回值:

整数型:
0:失败
1:成功

示例:

vu.SetMouseDelay(50);

---

## 

函数简介:

设置系统鼠标的移动速度.  如图所示红色区域. 一共分为11个级别. 从1开始,11结束。此接口仅仅对前台鼠标有效.

 

函数原型:

long SetMouseSpeed(speed)

参数定义:

speed 整数型:鼠标移动速度, 最小1，最大11.  居中为6. 推荐设置为6

返回值:

整数型:
0:失败
1:成功

示例:

    vu.SetMouseSpeed(6);

---

## 

函数简介:

等待指定的按键按下 (前台,不是后台)

函数原型:

long WaitKey(vk_code,time_out)

参数定义:

vk_code 整数型:虚拟按键码,当此值为0，表示等待任意按键。 鼠标左键是1,鼠标右键时2,鼠标中键是4.
time_out 整数型:等待多久,单位毫秒. 如果是0，表示一直等待

返回值:

整数型:
0:超时
1:指定的按键按下 (当vk_code不为0时)
按下的按键码:(当vk_code为0时)

示例:

    vu.WaitKey(13, 0);

---

## 

函数简介:

滚轮向下滚

函数原型:

long WheelDown()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.WheelDown();

---

## 

函数简介:

滚轮向上滚

函数原型:

long WheelUp()

参数定义:

无

返回值:

整数型:
0:失败
1:成功

示例:

vu.WheelUp();

---

## 

函数简介:

对音频数据进行裁剪,将输入的音频转为仅保留指定帧数区间的输出音频.

音频帧数:

由于音频是以时间为序列的,所以需要靠帧数进行控制.

音频的帧数与采样率相关,每秒帧数=采样率.

假如有一段音频采样率为16000,那么其每秒便会有16000帧.

函数原型:

int AudioCropping(inChannels, input, inCount, beginFrame, endFrame, output, outCount, isInvert)

参数定义:

inChannels 整数型:输入音频的通道数.
input 长整数型:输入音频数据的内存指针.类型为浮点型数据(C/C++中的float *).
inCount 长整数型:输入音频数据中浮点数的个数.
 
beginFrame 整数型:需要裁剪的起始帧位置.
endFrame 整数型:需要裁剪的结束帧位置.
 
output 变参指针:返回裁剪后输出音频数据所在内存指针.因为数据是以浮点数存储,所以这里的指针可以当做浮点数类型指针(C/C++中的float *)
outCount 变参指针:返回裁剪后输出音频数据浮点数个数.
 
isInvert 整数型:裁剪方式,取值如下:
0:输出的是从beginFrame开始到endFrame结束位置中间的音频数据(去除头部和尾部音频).
1:输出的是除了从beginFrame开始到endFrame结束之外的剩余音频数据(仅留头部和尾部音频).

返回值:

整数型:

0:失败

1:成功

示例:

    {

        // 示例,将一段音频进行裁剪,仅保留从音频开头2秒-6秒之间的部分(去除头部和尾部音频)

        int inSampleRate = 16000;// 假设输入音频采样率

        int inChannels = 2;     // 假设原始音频通道数为2

        LONG64 input;           // 假设输入音频数据的内存指针

        LONG64 inCount;         // 假设输入音频数据的浮点数个数 

        int beginFrame = 0;     // 用来计算输入音频在2秒时的帧数位置

        int endFrame = 0;       // 用来计算输入音频在6秒时的帧数位置

        LONG64 output;          // 用来接收输出音频数据的内存指针

        LONG64 outCount;        // 用来接收输出音频数据的浮点数个数

 

        // 计算起始帧位置->2秒时帧所在位置.

        beginFrame = 2 * inSampleRate;

        // 计算结束帧位置->6秒时帧所在位置.

        endFrame = 6 * inSampleRate;

        // 裁剪音频,并获取新音频数据

        ret = vu.AudioCropping(inChannels, input, inCount, beginFrame, endFrame, output, outCount, false);

        std::cout << "输出音频指针:" << output << std::endl;

        std::cout << "输出音频浮点个数:" << outCount << std::endl;

 

 

        // 示例,将一段音频进行裁剪,将从全音频长度0.3-0.6之间的部分音频去除(仅留头部和尾部音频)

        int inChannels = 2;     // 假设原始音频通道数为2

        LONG64 input;           // 假设输入音频数据的内存指针

        LONG64 inCount;         // 假设输入音频数据的浮点数个数 

        int beginFrame = 0;     // 用来起始帧数位置

        int endFrame = 0;       // 用来结束帧数位置

        LONG64 output;          // 用来接收输出音频数据的内存指针

        LONG64 outCount;        // 用来接收输出音频数据的浮点数个数

 

        // 计算输入音频的总帧数,计算公式 : 总帧数 = 浮点个数 ÷ 通道数

        LONG64 nFrames = inCount / inChannels;

        // 计算起始帧位置->全音频长度0.3位置.

        beginFrame = 0.3 * nFrames;

        // 计算结束帧位置->全音频长度0.6位置.

        endFrame = 0.6 * nFrames;

        // 裁剪音频,并获取新音频数据

        ret = vu.AudioCropping(inChannels, input, inCount, beginFrame, endFrame, output, outCount, true);

        std::cout << "输出音频指针:" << output << std::endl;

        std::cout << "输出音频浮点个数:" << outCount << std::endl;

 

    }

---

## 

函数简介:

获取音频输入(麦克风)或者音频输出(扬声器)的默认设备.

函数原型:

string AudioGetDeviceDefault(mode)

参数定义:

mode 整数型:获取设备信息类型,取值如下:

0:取输入设备名称

1:取输出设备名称

2:取输入设备ID

3:取输出设备ID

返回值:

字符串:

返回当前默认设备的字符串信息.

示例:

    vusoft vu;

    vu.Create(); // 或者使用CreateRemote()创建远程调用对象

 

    res = vu.AudioGetDeviceDefault(0);

    std::cout << "麦克风名称:" << res << std::endl;

 

    res = vu.AudioGetDeviceDefault(1);

std::cout << "扬声器名称:" << res << std::endl;

 

    res = vu.AudioGetDeviceDefault(2);

    std::cout << "麦克风ID:" << res << std::endl;

 

    res = vu.AudioGetDeviceDefault(3);

std::cout << "扬声器ID:" << res << std::endl;

---

## 

函数简介:

获取当前系统可用的音频输入输出设备.

函数原型:

string AudioGetDeviceList()

参数定义:

无

返回值:

字符串:

返回JSON格式的字符串内容,包含所有音频设备名称.

示例:

    vusoft vu;

    vu.Create(); // 或者使用CreateRemote()创建远程调用对象

 

    // 获取音频设备列表

    res = vu.AudioGetDeviceList();

    std::cout << "JSON数据:" << std::endl << std::endl;

    std::cout << res << std::endl;

 

 

    // 下面开始解析数据

    

    // 多次输出进行控制输出分隔

    for (size_t i = 0; i < 10; i++)

        std::cout << "====" ;

    std::cout  << std::endl;

 

    std::cout << "进行解析:" << std::endl << std::endl;

    LONG64 pJson = vu.JsonReadInPut(res);

    LONG64 pList = vu.JsonReadGetValObjByKey(pJson, "audio");

    

    LONG num = vu.JsonReadGetArraySize(pList);

    for (size_t i = 0; i < num; i++)

    {

        LONG64 pVal = vu.JsonReadGetArrayObj(pList, i);

        std::string strVal = vu.JsonReadGetStr(pVal);

        std::cout << res << std::endl;

}
 

 

 

运行上面代码后,控制台输出如下内容:

 

JSON数据:

 

{

"audio":  [

"Microsoft Sound Mapper - Input",

"麦克风 (4- EDIFIER G4)",

"Microphone (High Definition Aud",

"Microsoft Sound Mapper - Output",

"扬声器 (High Definition Audio Devi",

"扬声器 (4- EDIFIER G4)",

"主声音捕获驱动程序",

"麦克风 (4- EDIFIER G4)",

"Microphone (High Definition Audio Device)",

"主声音驱动程序",

"扬声器 (High Definition Audio Device)",

"扬声器 (4- EDIFIER G4)",

"扬声器 (4- EDIFIER G4)",

"扬声器 (High Definition Audio Device)",

"Microphone (High Definition Audio Device)",

"麦克风 (4- EDIFIER G4)",

"扬声器 (4- EDIFIER G4) [Loopback]",

"扬声器 (High Definition Audio Device) [Loopback]",

"Speakers (HD Audio Speaker)",

"麦克风 (HD Audio Mixed capture)",

"扬声器 (EDIFIER G4)",

"麦克风 (EDIFIER G4)"

]

}

========================================

进行解析:

 

Microsoft Sound Mapper - Input

麦克风 (4- EDIFIER G4)

Microphone (High Definition Aud

Microsoft Sound Mapper - Output

扬声器 (High Definition Audio Devi

扬声器 (4- EDIFIER G4)

主声音捕获驱动程序

麦克风 (4- EDIFIER G4)

Microphone (High Definition Audio Device)

主声音驱动程序

扬声器 (High Definition Audio Device)

扬声器 (4- EDIFIER G4)

扬声器 (4- EDIFIER G4)

扬声器 (High Definition Audio Device)

Microphone (High Definition Audio Device)

麦克风 (4- EDIFIER G4)

扬声器 (4- EDIFIER G4) [Loopback]

扬声器 (High Definition Audio Device) [Loopback]

Speakers (HD Audio Speaker)

麦克风 (HD Audio Mixed capture)

扬声器 (EDIFIER G4)

麦克风 (EDIFIER G4)

---

## 

函数简介:

获取指定工作流中,当前存在的有效音频数据的浮点数个数.

函数原型:

LONG64 AudioGetStreamSize(mode)

参数定义:

mode 整数型:目标工作模式,取值如下:
0:正在进行的录音工作.由AudioRecordStart()进行启动.
1:正在进行的播放工作.由AudioPlayStart()进行启动.

返回值:

长整数型:

返回有效音频流数据中浮点数个数.

示例:

 

    // 通过AudioGetStreamSize()计算播放进度

    int channels = 1;           // 假设通道数为1

    int sample_rate = 16000;    // 假设采样率为16kHz

    LONG64 pBuf;                // 假设已经拥有音频流数据

    LONG64 count;               // 假设已经拥有流数据中浮点数个数

    // 播放这段音频

    vu.AudioPlayWriteStream(channels, sample_rate, pBuf, count);

    vu.AudioPlayStart(channels, sample_rate, -1);

    // 获取当前还未被播放的剩余音频浮点个数

    LONG64 num = vu.AudioGetStreamSize(1);

    double fProcessed = num / count;

    std::cout << "播放进度:" << fProcessed << std::endl;

 

 

 

 

    // 获取当前已经录入的音频浮点个数.

    // 启动录音

    vu.AudioRecordStart(sample_rate, -1);

    // 延时1毫秒后再获取,否则还未使录制获取不到数据

    Sleep(1);

    num = vu.AudioGetStreamSize(0);

    std::cout << "当前录入:" << num << "个浮点数音频" << std::endl;

---

## 

函数简介:

混音添加音频数据.

将指定的音频添加到混音列表中,当调用AudioMixRun()时将会和混音列表中其他音频混合.

混音的作用是将两条甚至多条的音频混合在新的音频中.现实生活中,我们听到的音乐往往就是靠混音,将歌手的声音和多种乐器的声音混合在一条音频中的.

函数原型:

int AudioMixAdd(input, inCount, volume)

参数定义:
input 长整数型:添加的音频数据内存指针.类型为浮点型数据(C/C++中的float *).
inCount 长整数型:添加的音频数据中浮点数个数.
voluem 小数型:混音后在新声音中音量的倍数,取值范围0-10之间,不可为0.
如果上述参数的值全部为0,则会清空混音列表,将之前调用本函数添加的待混音数据清除.
注意:添加到混音列表中的所有音频,必须确保其通道数和采样率与其他添加的音频一致.

返回值:

整数型:

返回当前添加到混音列表中所有待混音数据的个数.

示例:

    {

        // 使用混音功能将多个音频混合.

 

        // 先清空一下混音列表,确保没有其他音频混杂进来

        vu.AudioMixAdd(0, 0, 0);

 

        // 添加第一条音频进入混音列表

        LONG64 input1;          // 假设为本条音频数据内存指针

        LONG64 inCount1;        // 假设为本条音频数据浮点数个数

        float volume1 = 1;      // 混合时音量保持不变

        vu.AudioMixAdd(input1, inCount1, volume1);

 

        // 添加第二条音频

        LONG64 input2;          // 假设为本条音频数据内存指针

        LONG64 inCount2;        // 假设为本条音频数据浮点数个数

        float volume2 = 0.5;    // 混合时音量降低0.5倍

        vu.AudioMixAdd(input2, inCount2, volume2);

 

        // 添加第三条音频

        LONG64 input3;          // 假设为本条音频数据内存指针

        LONG64 inCount3;        // 假设为本条音频数据浮点数个数

        float volume3 = 1.5;    // 混合时音量提升1.5倍

        vu.AudioMixAdd(input3, inCount3, volume3);

 

        // 执行混音,并获取新的音频数据

        LONG64 output;

        LONG64 outCount;

        ret = vu.AudioMixRun(output, outCount);

    }

---

## 

函数简介:

执行混音操作,将通过AudioMixAdd()添加到混音列表中的音频混合为新的音频.

当混音执行成功后,新音频长度将会是混音列表中最长的音频长度.

混音的作用是将两条甚至多条的音频混合在新的音频中.现实生活中,我们听到的音乐往往就是靠混音,将歌手的声音和多种乐器的声音混合在一条音频中的.

函数原型:

int AudioMixRun( output,  outCount)

参数定义:
output 变参指针:返回混音后新音频数据所在内存指针.因为数据是以浮点数存储,所以这里的指针可以当做浮点数类型指针(C/C++中的float *)
outCount 变参指针:返回混音后新音频数据的浮点数个数.

返回值:

整数型:

0:失败

1:成功

示例:

    {

        // 使用混音功能将多个音频混合.

 

        // 先清空一下混音列表,确保没有其他音频混杂进来

        vu.AudioMixAdd(0, 0, 0);

 

        // 添加第一条音频进入混音列表

        LONG64 input1;          // 假设为本条音频数据内存指针

        LONG64 inCount1;        // 假设为本条音频数据浮点数个数

        float volume1 = 1;      // 混合时音量保持不变

        vu.AudioMixAdd(input1, inCount1, volume1);

 

        // 添加第二条音频

        LONG64 input2;          // 假设为本条音频数据内存指针

        LONG64 inCount2;        // 假设为本条音频数据浮点数个数

        float volume2 = 0.5;    // 混合时音量降低0.5倍

        vu.AudioMixAdd(input2, inCount2, volume2);

 

        // 添加第三条音频

        LONG64 input3;          // 假设为本条音频数据内存指针

        LONG64 inCount3;        // 假设为本条音频数据浮点数个数

        float volume3 = 1.5;    // 混合时音量提升1.5倍

        vu.AudioMixAdd(input3, inCount3, volume3);

 

        // 执行混音,并获取新的音频数据

        LONG64 output;

        LONG64 outCount;

        ret = vu.AudioMixRun(output, outCount);

    }

---

## 

函数简介:

将指定音频文件加载到音频流数据中.

本函数第一次调用,需要在调用AudioPlayStart()之前,否则音频设备无法进行正常播放.

在启动播放之前或者之后,都可以多次加载相同或不同的音频文件,但是要确保不同音频文件的通道数和采样率是一致的.

函数原型:

int AudioPlayLoadFile(path)

参数定义:

path 字符串:需要被播放的音频文件路径.支持wav格式与mp3格式的音频文件.

返回值:

整数型:

0:失败

1:成功

示例:

    // 使用绝对路径加载音频

    vu.AudioPlayLoadFile("c:/play/test.wav");

 

    // 使用插件设定的相对路径加载音频

    vu.SetPath("c:/paly/");

    vu.AudioPlayLoadFile("test.mp3");

 

    // 启动音频设备进行播放

    vu.AudioPlayStart(-1, -1, -1);

 

    // 继续播放其他音频文件,但是一定要确保和首次加载的音频,是相同的通道数和采样率.

    vu.AudioPlayLoadFile("c:/play/test_01.mp3");

    vu.AudioPlayLoadFile("c:/play/test_02.wav");

 

    /*等待播放结束,或者达成什么条件后,调用AudioPlayStop()结束播放*/

    while (vu.AudioGetStreamSize(1) != 0)

    {

        Sleep(1);

    }

    vu.AudioPlayStop();

---

## 

函数简介:

启动音频设备进行播放音频.仅支持扬声器类型的设备.

本插件以音频流数据刷新扬声器设备的端口,播放结束后,请使用AudioPlayStop()停止播放,否则就算不写入流数据给扬声器,也仅仅是保持静音,而非真正的停止,依然会占用系统资源.

函数原型:

int AudioPlayStart(channels, sample_rate, device_id)

参数定义:

channels 整数型:音频数据的通道数(模式),取值如下:

-1:通过AudioPlayLoadFile()函数加载的音频.

>0的值:其他方式提供的音频的通道数,需提前了解,务必让本参数与其保持一致.(单声道音频本参数值为1,立体声为2)

sample_rate 整数型:音频数据的采样率(模式),取值如下:

-1:通过AudioPlayLoadFile()函数加载的音频.

>0的值:其他方式提供的音频的采样率,需提前了解,正常情况下需要让本参数与其保持一致,否则音频播放的速度会发生变化(可以实现变速播放).
device_id 整数型:音频设备ID,可以如下取值:
-1:当前系统的默认扬声器.
>=0的值:表示获取到的音频设备ID,此值就是AudioGetDeviceList()获取的设备的索引,从0开始,第一个设备的ID为0,第二个为1,第三个为2,以此类推(本参数仅支持扬声器类型的设备,麦克风等其他设备无法用来播放声音).

返回值:

整数型:

0:失败

1:成功

示例:

 

    // 使用单通道,16kHz采样率,默认扬声器进行播放

    ret = vu.AudioPlayStart(1, 16000, -1);

 

    // 使用双通道,48kHz采样率,指定音频设备进行播放

    device_id = 2;// 假如id为2的设备是扬声器类型设备.

    ret = vu.AudioPlayStart(1, 48000, device_id);

 

 

    // 播放音频文件

    vu.AudioPlayLoadFile("c:/test.wav");

    vu.AudioPlayStart(-1, -1, -1);

 

    // 播放音频流数据,需提前了解音频流的通道数和采样率

    int channels = 1;           // 假如提供的音频数据是单声道的(单声道=1,立体声=2)

    int sample_rate = 48000;    // 假如提供的音频数据是48kHz采样率
int device_id = 2;          // 假如id为2的设备是扬声器类型设备.

    LONG64 buf;     // 假如buf是音频流数据指针

    LONG64 count;   // 假如count是音频流中浮点数的个数

    vu.AudioPlayWriteStream(channels, sample_rate, buf, count);

    vu.AudioPlayStart(channels, sample_rate, device_id);

---

## 

函数简介:

停止音频设备的播放.

函数原型:

int AudioPlayStop()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

示例:

 

    ret = vu.AudioPlayStop();

---

## 

函数简介:

将音频数据写入需要播放的数据流中.

本函数可以在AudioPlayStart()调用前使用,也可以在它调用后使用,尽量保持与它相同的通道数和采样率.

注意:本插件所有音频数据均需要为浮点型,如果您提供的音频是其他类型数据,需自行转换为浮点数.

函数原型:

int AudioPlayWriteStream(channels, sample_rate, pBuf, count)

参数定义:
channels 整数型:音频数据的通道数(模式),取值如下:
-1:使用与AudioPlayStart()相同的通道数.
>0的值:设置播放的音频通道数为当前值.(单声道音频本参数值为1,立体声为2)
sample_rate 整数型:音频数据的采样率(模式),取值如下:
-1:使用与AudioPlayStart()相同的采样率.
>0的值:设置播放的音频采样率为当前值.正常情况下需要设置此参数为原始音频的真实采样率,但是您也可以通过修改此参数,实现实时变速播放的功能.
pBuf 长整数型:音频流数据所在的内存指针,必须是浮点型数据(C/C++中的float *).
count 长整数型:音频流数据中浮点数的个数.

返回值:

整数型:

0:失败

1:成功

示例:

    // 通过写入音频流实现播放

 

    int channels = 1;           // 假设通道数为1

    int sample_rate = 16000;    // 假设采样率为16kHz

    LONG64 pBuf;                // 假设已经拥有音频流数据

    LONG64 count;               // 假设已经拥有流数据中浮点数个数

 

    // 先将音频数据写入流中

    vu.AudioPlayWriteStream(channels, sample_rate, pBuf, count);

    // 启动音频播放设备

    vu.AudioPlayStart(channels, sample_rate, -1);

    // 此时就已经开始播放音频了.

 

    // 再次重复播放当前音频,此时通道数和采样率都可以设置为-1,保持与AudioPlayStart()具有相同设置.

    vu.AudioPlayWriteStream(-1, -1, pBuf, count);

 

    /*等待播放结束,或者达成什么条件后,调用AudioPlayStop()结束播放*/

    while (vu.AudioGetStreamSize(1) != 0)

    {

        Sleep(1);

    }

 

    vu.AudioPlayStop();

---

## 

函数简介:

读取音频文件,并将音频数据解析.

支持wav格式与mp3格式的音频.

支持读取硬盘文件和内存文件.
本插件所有音频数据均以浮点数(float)进行存写,在这里读取到的音频数据在内存中都是浮点类型,如果您需要其他类型的音频数据,请自行转换(可以将读取到的每个浮点数都转8-32位整数,或转双精度浮点).

函数原型:

int AudioReadFile(path_or_buf, in_size_out_channels, sample_rate, buf,count)

参数定义:

path_or_buf 长整数型:音频文件路径的字符串指针,或者是读入到内存中的二进制音频文件数据所在内存地址.

 

in_size_out_channels 变参指针:返回音频数据的通道数.并且对传入的接收变量的值有所要求,要求如下:

值为0:当path_or_buf为路径字符串指针时,需要将本参数的接收变量赋值为0.

其他:当path_or_buf为音频数据的内存地址时,本参数的接收变量必须赋值为音频数据的大小(字节为单位).

 

sample_rate 变参指针:返回音频数据的采样率.

 
buf 变参指针:返回解析成功后的音频数据所在内存指针.因为数据是以浮点数存储,所以这里的指针可以当做浮点数类型指针(C/C++中的float *)
 
count 变参指针:返回解析成功后的音频数据浮点数个数.

返回值:

整数型:

0:失败

1:成功

示例:

    {

        // 读取存放在硬盘的音频文件

        std::string path = "c:/read/test.wav";

        LONG64 pPath = (LONG64)path.data();         // 获取路径字符串的指针.

        int channels = 0;                           // 读硬盘文件时,必须将接收通道数的参数赋值为0

        int sample_rate;                            // 用来接收采样率的变量

        LONG64 buf;                                 // 用来接收解析后的音频数据指针的变量

        LONG64 count;                               // 用来接收解析后的音频数据浮点数个数的变量.

        ret = vu.AudioReadFile(pPath, channels, sample_rate, buf, count);

 

 

        // 读取存放在内存中的音频文件

        LONG64 pBufFile = 0x987654321;              // 假设此为音频二进制数据地址

        int channels = 123456789;                   // 读内存文件时,必须将接收通道数的参数赋值为内存文件的大小.此处的值为假设的文件大小.

        int sample_rate;                            // 用来接收采样率的变量

        LONG64 buf;                                 // 用来接收解析后的音频数据指针的变量

        LONG64 count;                               // 用来接收解析后的音频数据浮点数个数的变量.

        ret = vu.AudioReadFile(pPath, channels, sample_rate, buf, count);

 

        // 将解析后的音频信息打印出来.

        std::cout << "解析结果:" << ret << std::endl;

        std::cout << "通道数:" << channels << std::endl;

        std::cout << "采样率:" << sample_rate << std::endl;

        std::cout << "数据指针:" << buf << std::endl;

        std::cout << "浮点个数:" << count << std::endl;

    }

---

## 

函数简介:

获取当前录音流数据的信息.

函数原型:

LONG64 AudioRecordGetStreamInfo( channelse,  sampleRate)

参数定义:

channelse 变参指针:返回音频通道数.

sampleRate 变参指针:返回音频采样率.

返回值:

长整数型:

返回当前音频数据流中浮点数的个数.

示例:

        int channels = 0, sampleRate = 0;

        ret = vu.AudioRecordGetStreamInfo(channels, sampleRate);

        std::cout << "通道数:" << channels << " 采样率:" << sampleRate << "浮点个数:" << ret << std::endl;

---

## 

函数简介:

在录音时,将音频流数据从当前内存中读取出来.适合对它进行其他操作,例如语音转文本、二次合成、剪辑、混音等.

注意:调用本函数时,插件会分配一段临时内存用来存储音频流,并在下次调用本函数时覆盖旧的读取数据.所以需要长久保留音频数据的话,需要将读取到的数据拷贝到你自己分配的内存中.

本插件所有音频数据均以浮点数(float)进行存写,在这里读取到的音频流数据在内存中都是浮点类型,如果您需要其他类型的音频数据,请自行转换(可以将读取到的每个浮点数都转8-32位整数,或转双精度浮点).

函数原型:

int AudioRecordReadStream( buf, count)

参数定义:

buf 变参指针:返回当前音频流数据所在的内存指针,可以从这里读取缓冲的音频数据.因为数据是以浮点数存储,所以这里的指针可以当做浮点数类型指针(C/C++中的float *)

count 变参指针:返回当前音频数据流中浮点数的个数,可以通过它计算出读取到的音频数据的总大小,计算方式为 count × 4 .

返回值:

整数型:

0:失败,或暂无音频流数据.

1:成功.

示例:

    // 读取音频流数据示例

 

    // 使用16kHz采样率,使用默认麦克风设备进行录音

    vu.AudioRecordStart(16000, -1);

 

    bool is_stop = false;

    while (is_stop == false)

    {

        //每1000毫秒读一次

        Sleep(1000);

 

        LONG64 buf = 0;

        LONG64 count = 0;

        vu.AudioRecordReadStream(buf, count);

        LONG64 nBufSize = count * 4;

        

        // 此时可以对音频流进行处理,例如语音转文本、二次合成、剪辑、混音等

        processAudio(buf, count, nBufsize);

 

        // 复制数据到自己分配的内存中

        memcpy(pMyAudioData, buf, nBufSize);

    }

 

    vu.AudioRecordStop();

---

## 

函数简介:

启动音频设备进行录音.可以支持麦克风的录音(常规录音)和扬声器的录音(录制系统音频).

函数原型:

int AudioRecordStart(sample_rate, device_id)

参数定义:

sample_rate 整数型:音频采样率,即每秒从声音信号中采集多少次样本,影响录制到的音频质量,常规音频采样率一般取值如下:

8000： 8kHz 电话音质，足够用于语音识别，但音乐效果很差。

16000： 16kHz 宽带音频，常用于 VoIP（网络电话）、视频会议等，语音清晰度比 8kHz 好。

22050： 22.05kHz 一般用于网络流媒体的低质量音频。

44100： 44.1kHz CD音质标准。这是音乐录制和播放中最常见的采样率。

48000： 48kHz DVD 音质标准。也是专业音频设备和影视制作中广泛使用的采样率。

device_id 整数型:音频设备ID,可以如下取值:

-1:当前系统的默认麦克风.

-2:当前系统的默认扬声器,此时参数sample_rate无效.

>=0的值:表示获取到的音频设备ID,此值就是AudioGetDeviceList()获取的设备的索引,从0开始,第一个设备的ID为0,第二个为1,第三个为2,以此类推(仅支持麦克风类型的音频设备).

注意:当录制系统默认扬声器/耳机设备的声音时,使用的是系统内置音频采样率,此时参数sample_rate无效,如果需要明确当前录制时使用的采样率,可以通过调用函数AudioRecordGetStreamInfo()来获取.

返回值:

整数型:

0:失败

1:成功

注意:录制的音频会占用极多的内存,如果不及时进行读取,或者录音结束后没有调用AudioRecordStop()停止录制,将会耗尽系统内存.

示例:

         // 使用16kHz采样率,录制默认麦克风设备的录音

        ret = vu.AudioRecordStart(16000, -1);

 

        // 录制系统当前输出的音频

        ret = vu.AudioRecordStart(0, -2);

 

        // 使用48kHz采样率,录制指定音频设备的声音

        device_id = 2;// 假如id为2为其他麦克风设备,则会使用此设备进行录音

        ret = vu.AudioRecordStart(48000, device_id);

---

## 

函数简介:

停止音频录制.

函数原型:

int AudioRecordStop()

参数定义:

无

返回值:

整数型:

0:失败

1:成功

示例:

    ret = vu.AudioRecordStop();

---

## 

函数简介:

将录制的音频保存到文件中.

函数原型:

int AudioRecordToFile(path)

参数定义:

path 字符串:要保存音频的目标文件路径.支持wav格式与mp3格式.

返回值:

整数型:

0:失败

1:成功

示例:

    // 录制声音到文件的示例

 

    // 使用16kHz采样率,使用默认麦克风设备进行录音

    vu.AudioRecordStart(16000, -1);

 

    /* 此时可以等待一段时间,或者达成什么条件后才保存录音*/

 

    // 保存到绝对路径文件

    ret = vu.AudioRecordToFile("c:\\record\\test.wav");

 

 

    // 保存到插件设置的资源路径

    vu.SetPath("c:/record/");

    ret = vu.AudioRecordToFile("test.mp3");

 

    vu.AudioRecordStop();

---

## 

函数简介:

对音频数据进行通道数和采样率转换,将输入的音频转为指定通道数和采样率的输出音频.

在某些情况下,需要使用特定通道数和采样率的音频,如果提供的原始音频与之不符,那么本函数就会非常有用了.

函数原型:

int AudioResample(inChannels, inSampleRate, input, inCount, outChannels, outSampleRate, output, outCount)

参数定义:

inChannels 整数型:输入音频的通道数.

inSampleRate 整数型:输入音频的采样率.

input 长整数型:输入音频数据的内存指针.类型为浮点型数据(C/C++中的float *).
inCount 长整数型:输入音频数据中浮点数的个数.
 
outChannels 整数型:输处音频的目标通道数.
outSampleRate 整数型:输出音频的目标采样率.
output 变参指针:返回转换后输出音频数据所在内存指针.因为数据是以浮点数存储,所以这里的指针可以当做浮点数类型指针(C/C++中的float *)
outCount 变参指针:返回转后输出音频数据浮点数个数.

返回值:

整数型:

0:失败

1:成功

示例:

    {

        // 示例将音频数据转换为指定通道数和采样率,并返回新数据的指针和浮点数个数

 

        int inChannels = 1;         // 假设输入音频通道数

        int inSampleRate = 16000;   // 假设输入音频采样率

        LONG64 input;               // 假设输入音频数据的内存指针

        LONG64 inCount;             // 假设输入音频数据的浮点数个数

 

        int outChannels = 2;        // 设置输出音频通道数

        int outSampleRate = 22050;  // 设置输出音频采样率

        LONG64 output;              // 用来接收输出音频数据的内存指针

        LONG64 outCount;            // 用来接收输出音频数据的浮点数个数

 

        ret = vu.AudioResample(inChannels, inSampleRate, input, inCount, outChannels, outSampleRate, output, outCount);

 

    }

---

## 

函数简介:

设置当前音频流工作的状态.

函数原型:

int AudioSetStatus(mode, status)

参数定义:

mode 整数型:要设置的目标工作模式,取值如下:

0:正在进行的录音工作.由AudioRecordStart()进行启动.

1:正在进行的播放工作.由AudioPlayStart()进行启动.

status 整数型:要设置的状态,取值如下:

0:暂停工作

1:进行工作

返回值:

整数型:

返回调用本函数之前,原本目标工作模式的状态.

示例:

 

    // 设置录音暂停工作

    vu.AudioSetStatus(0, 0);

    // 设置录音进行工作

    vu.AudioSetStatus(0, 1);

 

 

    // 设置播放暂停工作

    vu.AudioSetStatus(1, 0);

    // 设置播放进行工作

    vu.AudioSetStatus(1, 1);

---

## 

函数简介:

将音频数据写出到硬盘.

支持将音频数据写为wav和mp3格式.

本插件使用浮点型进行音频数据的存写,但是可以在写出时将对应的数据转为指定格式的文件.支持任意支持对应格式播放的播放器进行播放.

函数原型:

int AudioWriteFile(path, channels, sample_rate, buf, count)

参数定义:

path 字符串:要写出的文件路径,写出成功后会在硬盘新建此文件.写出的文件以后缀为区分,如果后缀是".wav"则将会写出wav格式的音频文件,mp3文件同理.

channels 整数型:音频数据的通道数.(单声道音频本参数值为1,立体声为2)

sample_rate 整数型:音频数据的采样率.如16000表示为16kHz.
buf 长整数型:音频数据所在的内存指针,类型为浮点型数据(C/C++中的float *).

count 长整数型:音频数据中浮点数的个数.

返回值:

整数型:

0:失败

1:成功

示例:

    {

        // 录制麦克风声音并写出到硬盘文件.

        int channels = 1;           // 录音的数据通道数永远为1

        int sample_rate = 16000;    // 使用16kHz采样率进行录制

        LONG64 buf;                 // 用来接收录音数据的内存指针.

        LONG64 count;               // 用来接收录音数据的浮点数个数.

        // 启动默认麦克风进行录音

        vu.AudioRecordStart(sample_rate, -1);

        // 录制10秒音频

        Sleep(10000);

        // 获取音频数据

        vu.AudioRecordReadStream(buf, count);

        // 将录音数据写出

        ret = vu.AudioWriteFile("c:/write/record.wav", channels, sample_rate, buf, count);

        // 录音结束后必须调用下面函数以停止录制,否则长时间系统内存将会耗尽

        vu.AudioRecordStop();

    }

---

