from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/proper-study-methods-MRR')
def home():
    html_content = '''
    <!DOCTYPE html>
    <html lang="fa">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>روش درست درس خواندن - MRR</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; background-color: #f4f4f4; }
            h1 { color: #2c3e50; }
            .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); }
            .item { background: #3498db; color: white; padding: 10px; margin: 5px; border-radius: 5px; cursor: pointer; }
            .content { display: none; background: #ecf0f1; color: black; padding: 10px; border-radius: 5px; margin-top: 5px; text-align: right; }
            .important { color: red; font-weight: bold; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>روش درست درس خواندن - MRR</h1>

            <div class="item" onclick="toggleContent('planning')">📅 برنامه‌ریزی منظم (داشتن تایم‌بندی دقیق)</div>
            <div id="planning" class="content">
                <p><strong>
                 <p><span style="color: red; font-size: 23px;">چرا برنامه‌ریزی مهم است؟</span></p>
                
وقتی بدانیم چه زمانی و چه چیزی را مطالعه کنیم، تمرکزمان بیشتر می‌شود و سریع‌تر پیشرفت می‌کنیم.
<br>
</p>
<p><span style="color: red; font-size: 23px;">چگونه برنامه‌ریزی کنیم؟</span></p>
<p>
    <span style="color: red; font-size: 23px;">یک:</span>  هدف مشخص داشته باش: قبل از مطالعه، تصمیم بگیر چه مباحثی را باید بخوانی<br>

<p>
    <span style="color: red; font-size: 23px;">دو:</span>  مطالب را به بخش‌های کوچک تقسیم کن: این کار باعث می‌شود یادگیری راحت‌تر شود.<br>

<p>
    <span style="color: red; font-size: 23px;">سه:</span>  ساعت مطالعه را ثابت نگه دار: مثلاً هر روز در یک زمان مشخص مطالعه کن تا به آن عادت کنی 
 <br>
<p>
    <span style="color: red; font-size: 23px;
   ">چهار:</span>  بین مطالعه استراحت 
کوتاه داشته باش: مثلاً بعد از ۲۵ تا ۵۰ دقیقه مطالعه، ۵ تا ۱۰ دقیقه استراحت کن.
<br>
</p>

<p>
    <span style="color: red; font-size: 23px;">نتیجه:</span> 
 با برنامه‌ریزی درست، هم درس خواندن آسان‌تر می‌شود، هم مطالب را بهتر به خاطر می‌سپاری.




            </div>

            <div class="item" onclick="toggleContent('breaks')">⏳ استراحت‌های کوتاه بین مطالعه (تکنیک پومودورو)</div>
            <div id="breaks" class="content">
                <p><strong><p><span style="color: red; font-size: 23px;">چرا باید بین مطالعه استراحت کنیم؟</span></p>
                وقتی مدت طولانی بدون استراحت درس می‌خوانیم، تمرکزمان کم شده و یادگیری‌مان کاهش می‌یابد. استراحت‌های کوتاه باعث می‌شود مغز اطلاعات را بهتر پردازش کند و بازدهی مطالعه افزایش یابد.
                <p><span style="color: red; font-size: 23px;">تکنیک پومودورو چیست؟</span></p>
                پومودورو یک روش ساده و کارآمد برای افزایش تمرکز در مطالعه است. این تکنیک شامل چرخه‌های مطالعه و استراحت است:
                	<p>
    <span style="color: red; font-size: 23px;">یک:</span> ۲۵ دقیقه مطالعه کنید – در این مدت فقط روی درس تمرکز کنید و هیچ کار دیگری انجام ندهید.
    
    <p>
    <span style="color: red; font-size: 23px;">دو:</span> ۴ تا ۵ دقیقه استراحت کنید – در این مدت از جای خود بلند شوید، کمی حرکت کنید یا چشمان خود را ببندید و استراحت کنید.
    
    <p>
    <span style="color: red; font-size: 23px;">سه:</span> بعد از ۴ دوره پومودورو، یک استراحت بلندتر (۱۵ تا ۳۰ دقیقه) داشته باشید – این کار به مغز شما کمک می‌کند اطلاعات را بهتر به حافظه بلندمدت منتقل کند.
    
    <p>
    <span style="color: red; font-size: 23px;">نتیجه:</span> 
   <br>
   
    <span style="color: red; font-size: 23px;">یک:</span>  با استفاده از تکنیک پومودورو، تمرکز شما بیشتر شده و مطالعه خسته‌کننده نخواهد بود.
    <br>
   
   <span style="color: red; font-size: 23px;">دو:</span> 
به مغزتان فرصت می‌دهید تا بهتر اطلاعات را پردازش کند و کمتر احساس خستگی کنید.
<br>

    <span style="color: red; font-size: 23px;">سه:</span> 
عملکرد شما در طولانی‌مدت بهبود می‌یابد و از اتلاف وقت جلوگیری می‌شود.
       
                     </div>

            <div class="item" onclick="toggleContent('activeReview')">📖 مرور فعال مطالب (روش لایتنر و خلاصه‌نویسی)</div>
            <div id="activeReview" class="content">
                <p>
                مرور مطالب بخش مهمی از یادگیری است.  اگر مطالبی که خوانده‌ایم را به‌درستی مرور نکنیم، بعد از مدتی آن‌ها را فراموش خواهیم کرد. مرور فعال به ما کمک می‌کند اطلاعات را در حافظه‌ی بلندمدت ذخیره کنیم.
                <p><span style="color: blue; font-size: 23px;">روش لایتنر چیست؟</span></p>لایتنر یک روش علمی و مؤثر برای مرور مطالب است. این روش بر اساس فاصله‌ی زمانی مرور طراحی شده تا اطلاعات به‌مرور در ذهن تثبیت شوند.
                
                چگونه از جعبه‌ی لایتنر استفاده کنیم؟             
    <p>
    
      <span style="color: red; font-size: 23px;">کارت‌های یادگیری بسازید:</span> 
      روی یک طرف کارت، سؤال یا مطلبی که می‌خواهید یاد بگیرید بنویسید و روی طرف دیگر پاسخ آن را بنویسید.
    <p>              
<span style="color: red; font-size: 23px;">مرور در ۵ مرحله:</span>
کارت‌ها را در ۵ خانه‌ی مختلف قرار دهید. اگر جوابی را درست گفتید، کارت را به خانه‌ی بعدی ببرید. اگر اشتباه کردید، کارت به خانه‌ی اول برمی‌گردد.
<p>
<span style="color: red; font-size: 23px;">مرور بر اساس فاصله‌ی زمانی:</span>
هر چه بیشتر جواب درست بدهید، فاصله‌ی مرور طولانی‌تر می‌شود. این کار باعث تثبیت بهتر اطلاعات می‌شود.

<p>
    <span style="color: red; font-size: 23px;">نتیجه:</span> روش لایتنر کمک می‌کند مطالب را برای مدت طولانی‌تری در ذهن نگه‌داریم و یادگیری را آسان‌تر کنیم.
<br><br>

<span style="color: blue; font-size: 23px;">خلاصه‌نویسی چگونه کمک می‌کند؟</span>خلاصه‌نویسی یک روش عالی برای پردازش اطلاعات و درک بهتر مطالب است.
<p>
<span style="color: red; font-size: 23px;">چگونه خلاصه‌نویسی کنیم؟</span>
<p>
<span style="color: red; font-size: 23px;">مطالب کلیدی را پیدا کنید:</span>نیازی نیست همه‌ی متن را بنویسید، فقط نکات مهم را مشخص کنید.
<p>
<span style="color: red; font-size: 23px;">با کلمات خودتان بنویسید:</span>به‌جای کپی کردن متن، آن را با زبان خودتان بازنویسی کنید.
<p>
<span style="color: red; font-size: 23px;">از نقشه‌های ذهنی استفاده کنید:</span>اطلاعات را به‌صورت شاخه‌ای و تصویری ترسیم کنید تا بهتر درک شوند.
<p>
<span style="color: red; font-size: 23px;">نتیجه:</span>خلاصه‌نویسی باعث می‌شود مطالب را سریع‌تر مرور کنیم و درک بهتری از آن‌ها داشته باشیم.
<p>
<span style="color: red; font-size: 23px;">نکته مهم💡:</span>
<span style="color:green ; font-size: 19px;">ترکیب روش لایتنر و خلاصه‌نویسی بهترین نتیجه را برای یادگیری عمیق و ماندگار دارد.</span>
            </div>

            <div class="item" onclick="toggleContent('mentalVisualization')">🧠 استفاده از تصویرسازی ذهنی و نقشه‌های مفهومی</div>
            <div id="mentalVisualization" class="content">
                <p><strong>
                <p><span style="color: green; font-size: 23px;">تصویرسازی ذهنی:</span>
                تصویرسازی ذهنی یکی از روش‌های مؤثر برای به خاطر سپردن و درک بهتر مطالب است. در این روش، هنگام مطالعه، سعی کنید مطالب را به شکل تصاویر ذهنی درآورید. این کار باعث می‌شود که اطلاعات در حافظه‌ی بلندمدت شما ماندگارتر شوند.
                
                <p><span style="color: blue; font-size: 23px;">چگونه از تصویرسازی ذهنی استفاده کنیم؟
                <p>
<p><span style="color:red ; font-size: 23px;">یک:</span> هنگام خواندن یک مطلب، آن را در ذهن خود به یک تصویر یا داستان تبدیل کنید
<p>
<p><span style="color: red; font-size: 23px;">دو:</span> از رنگ‌ها، اشکال و حرکات برای جذاب‌تر شدن تصاویر ذهنی استفاده کنید
<p>
<p><span style="color: red; font-size: 23px;">سه:</span> مطالب پیچیده را به صورت نمادها و شکل‌های ساده در نظر بگیرید             
            
            <br><br>
            <p><span style="color: green; font-size: 23px;">نقشه‌های مفهومی:</span>نقشه‌های مفهومی ابزارهایی هستند که ارتباط بین ایده‌ها و مفاهیم را به‌صورت گرافیکی نشان می‌دهند. این روش باعث می‌شود اطلاعات ساختارمند شوند و یادگیری عمیق‌تر و سریع‌تری داشته باشید
            <p><span style="color: blue; font-size: 23px;">چگونه نقشه‌ی مفهومی بسازیم؟</span></p>
            <p><span style="color: red; font-size: 23px;">یک:</span> موضوع اصلی را در مرکز صفحه بنویسید
            <p><span style="color: red; font-size: 23px;">دو:</span>زیرموضوعات مرتبط را با خطوط به آن متصل کنید
            <p><span style="color: red; font-size: 23px;">سه:</span>           کلمات کلیدی و تصاویر را برای درک بهتر اضافه کنید
            <p><span style="color: red; font-size: 23px;">چهار:</span>از رنگ‌بندی برای تفکیک بخش‌های مختلف استفاده کنید
            <p><span style="color: green; font-size: 23px;">مزایای استفاده از تصویرسازی ذهنی و نقشه‌های مفهومی</span></p>
            ✔ افزایش سرعت یادگیری
           <p>✔ تقویت حافظه‌ی بلندمدت
           <p>✔ درک عمیق‌تر مطالب
           <p>✔ ایجاد ارتباط بین مفاهیم مختلف
           <p>با استفاده از این روش‌ها، یادگیری برای شما ساده‌تر، جذاب‌تر و ماندگارتر خواهد شد
            </div>
            
            
           <div class="item" onclick="toggleContent('focusSection')">🎯
    تمرکز کامل و دوری از عوامل حواس‌پرتی
</div>
<div id="focusSection" class="content">
    <p><strong>تمرکز یکی از مهم‌ترین عوامل موفقیت در یادگیری است. هرچه بتوانید بهتر تمرکز کنید، کیفیت مطالعه و میزان یادگیری شما افزایش خواهد یافت. اما امروزه، با وجود تلفن‌های همراه، شبکه‌های اجتماعی و سر و صدای اطراف، حفظ تمرکز به یک چالش تبدیل شده است. در ادامه روش‌هایی برای افزایش تمرکز و دوری از عوامل حواس‌پرتی ارائه می‌شود
    
    <p><span style="color: blue; font-size: 23px;">محیط مطالعه‌ی خود را کنترل کنید</span></p>
    <p><span style="color: red; font-size: 23px;">یک:</span>مکانی ساکت و آرام را برای مطالعه انتخاب کنید
    <p><span style="color: red; font-size: 23px;">دو:</span>گوشی و سایر وسایل الکترونیکی را هنگام مطالعه کنار بگذارید یا در حالت پرواز قرار دهید
    <p><span style="color: red; font-size: 23px;">سه:</span>از نور مناسب و صندلی راحت استفاده کنید تا هنگام مطالعه احساس خستگی نکنید
    <p><span style="color: blue; font-size: 23px;">تکنیک‌های افزایش تمرکز</span></p>
    <p><span style="color: red; font-size: 23px;">یک:</span>از روش پومودورو استفاده کنید که در بخش استراحت‌های کوتاه بین مطالعه (تکنیک پومودورو) توضیح دادم
    
    <p><span style="color: red; font-size: 23px;">دو:</span>هنگام مطالعه، یک هدف مشخص تعیین کنید تا ذهنتان روی آن متمرکز بماند
    <p><span style="color: red; font-size: 23px;">سه:</span>مدیتیشن و تمرینات تنفسی انجام دهید تا قدرت تمرکز خود را تقویت کنید
    <p><span style="color: blue; font-size: 23px;">از عواملی که باعث حواس‌پرتی می‌شوند دوری کنید</span></p>
<p><span style="color: red; font-size: 23px;">یک:</span>
اگر در خانه سر و صدای زیادی وجود دارد، از هدفون و موسیقی بی‌کلام استفاده کنید    
    <p><span style="color: red; font-size: 23px;">دو:</span>در صورت امکان، زمان مطالعه را زمانی انتخاب کنید که مزاحمتی وجود نداشته باشد
<p><span style="color: red; font-size: 23px;">سه:</span>یک لیست از چیزهایی که ذهنتان را درگیر می‌کنند، تهیه کنید و بعد از مطالعه به آن‌ها بپردازید    
  <p><span style="color: blue; font-size: 23px;">خواب و تغذیه‌ی مناسب داشته باشید</span></p>  
    
  <p><span style="color: red; font-size: 23px;">یک:</span>خواب کافی و منظم (حداقل ۷ ساعت در شبانه‌روز) باعث بهبود تمرکز و حافظه می‌شود  
    <p><span style="color: red; font-size: 23px;">دو:</span>مصرف غذاهای سالم و مغذی مانند آجیل، ماهی، سبزیجات و میوه‌ها می‌تواند تأثیر مثبتی روی عملکرد ذهنی شما داشته باشد
    
 <p><span style="color: blue; font-size: 23px;">با انگیزه بمانید</span></p>   
    
 <p><span style="color: red; font-size: 23px;">یک:</span>   به خودتان یادآوری کنید که چرا درس می‌خوانید و چه هدفی دارید
    
    <p><span style="color: red; font-size: 23px;">دو:</span>پس از مطالعه‌ی هر بخش، به خودتان پاداش بدهید تا مغز شما به تمرکز عادت کند
    
<p><span style="color: blue; font-size: 23px;">نتیجه:</span>
    با رعایت این نکات، می‌توانید تمرکز خود را بالا ببرید و از حواس‌پرتی دوری کنید. هرچه تمرکز بیشتری داشته باشید، مطالعه‌ی شما مؤثرتر خواهد بود!
    
</div>

<div class="item" onclick="toggleContent('exerciseAndSleep')">🏋️‍
    ورزش و خواب کافی برای تقویت حافظه
</div>
<div id="exerciseAndSleep" class="content">
    <p><strong>حافظه‌ی قوی و ذهن شفاف نقش مهمی در یادگیری و موفقیت تحصیلی دارد. دو عامل مهم که می‌توانند به بهبود حافظه و تمرکز کمک کنند، ورزش منظم و خواب کافی هستند
    
    <p><span style="color: blue; font-size: 23px;">تأثیر ورزش بر حافظه</span></p>
ورزش باعث افزایش جریان خون به مغز می‌شود و اکسیژن و مواد مغذی بیشتری را به سلول‌های مغزی می‌رساند. این فرآیند موجب تقویت ارتباطات عصبی و افزایش توانایی مغز در ذخیره‌سازی اطلاعات می‌شود

<p><span style="color: red; font-size: 23px;">بهترین ورزش‌ها برای تقویت حافظه:</span>پیاده‌روی، دویدن، یوگا، شنا و تمرینات هوازی
<p><span style="color: red; font-size: 23px;">مدت زمان توصیه‌شده:</span>حداقل ۳۰ دقیقه ورزش در روز، پنج روز در هفته

<p><span style="color: blue; font-size: 23px;">نقش خواب در بهبود حافظه</span></p>
خواب کافی و باکیفیت به مغز فرصت می‌دهد اطلاعات را پردازش و در حافظه‌ی بلندمدت ذخیره کند. در طول خواب، مغز خاطرات را تثبیت کرده و از فراموشی جلوگیری می‌کند
<p><span style="color: red; font-size: 23px;">مدت زمان مناسب خواب:</span>نوجوانان به ۸ تا ۱۰ ساعت خواب شبانه نیاز دارند

<p><span style="color: red; font-size: 23px;">بهترین روش‌ها برای خواب بهتر:</span>داشتن برنامه‌ی خواب منظم.
دوری از گوشی و صفحات نمایش قبل از خواب
استفاده از روش‌های آرام‌سازی مانند مدیتیشن یا گوش دادن به موسیقی ملایم
<p><span style="color: blue; font-size: 23px;">نتیجه‌گیری:</span>ورزش و خواب کافی، دو عامل کلیدی برای تقویت حافظه و افزایش تمرکز هستند. ترکیب این دو با روش‌های یادگیری فعال، می‌تواند به موفقیت تحصیلی و ذهنی بهتر کمک کند

                                    
</div>                                                                        
       <p                                                                                                                                          class="important">⚠ نکته مهم: همیشه یادداشت‌برداری کنید و از روش‌های علمی برای مطالعه استفاده کنید!</p>
        </div>

        <script>
            function toggleContent(id) {
                var content = document.getElementById(id);
                if (content.style.display === "none" || content.style.display === "") {
                    content.style.display = "block";
                } else {
                    content.style.display = "none";
                }
            }
        </script>
    </body>
    </html>
    '''
    return render_template_string(html_content)

if __name__ == '__main__':
    print("سایت را باز کنید: www.studyMethodsMRR.site.live")
    app.run(debug=True)
