\NeedsTeXFormat{LaTeX2e}[1995/12/01]
\ProvidesClass{NGPLB}[基於LaTeX Class: report and 交大論文格式]
\DeclareOption{fancyitem}{
\RequirePackage{enumerate}
% list/itemize/enumerate setting
\RequirePackage[shortlabels,inline]{enumitem}
\setlist{nolistsep}
\RequirePackage{tikz} %% load tikz without tikz
\usetikzlibrary{backgrounds,calc,shadows,positioning,fit}
\newcommand*\circled[1]{\tikz[baseline=(char.base)]{
            \node[shape=circle,draw,inner sep=1pt] (char) {#1};}}
\newcommand*{\eitemi}{\tikz \draw [baseline, ball color=structurecolor,draw=none] circle (2pt);}
\newcommand*{\eitemii}{\tikz \draw [baseline, fill=structurecolor,draw=none,circular drop shadow] circle (2pt);}
\newcommand*{\eitemiii}{\tikz \draw [baseline, fill=structurecolor,draw=none] circle (2pt);}
\setlist[enumerate,1]{label=\color{structurecolor}\arabic*.}
\setlist[enumerate,2]{label=\color{structurecolor}(\alph*).}
\setlist[enumerate,3]{label=\color{structurecolor}\Roman*.}
\setlist[enumerate,4]{label=\color{structurecolor}\Alph*.}
\setlist[itemize,1]{label={\eitemi}}
\setlist[itemize,2]{label={\eitemii}}
\setlist[itemize,3]{label={\eitemiii}}
}
\ProcessOptions\relax

\LoadClassWithOptions{report}
\PassOptionsToClass{\CurrentOption}{report}
\input{trans.def}
\RequirePackage[center]{titlesec}
\RequirePackage{titletoc}
\RequirePackage[encoding=UTF8,style={Traditional}]{zhnumber}%Financial
\RequirePackage[]{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{xpatch}
\RequirePackage{tocloft}
\RequirePackage{xcolor}

\RequirePackage{xeCJK}
\setCJKmainfont[BoldFont = 原之味黑體 TW Bold]{原之味黑體 TW Normal}

\definecolor{structurecolor}{RGB}{60,113,183}
\definecolor{main}{RGB}{0,166,82}%
\definecolor{second}{RGB}{255,134,24}%
\definecolor{third}{RGB}{0,174,247}%

\geometry{top=1.5cm,left=2cm,right=2cm,bottom=2.5cm}
\fancypagestyle{plain}{%
\fancyhf{}%
\cfoot{-\hskip1.5pt\thepage\hskip2pt-}
\renewcommand{\headrulewidth}{0pt}% Line at the header invisible
}
\pagestyle{plain}
%\RequirePackage{}
\xpatchcmd{\@chapter}{\addcontentsline{toc}{chapter}%
{\protect\numberline{\thechapter}#1}%
}{ 
\addcontentsline{toc}{chapter}%
{\protect\numberline{第\thechapter 章} #1}%
}{ }{ }
\xpatchcmd{\chapter}{\thispagestyle{plain}}{ }{ }{ }
\xpatchcmd{\@chapter}{\addtocontents{lof}{\protect\addvspace{10\p@}}}{ }{ }{ }
\xpatchcmd{\@chapter}{\addtocontents{lot}{\protect\addvspace{10\p@}}}{ }{ }{ }
\xpatchcmd{\chapter}{\if@openright\cleardoublepage\else\clearpage\fi}{\vskip12pt}{}{}

%\renewcommand{\tableofcontents}{\addcontentsline{toc}{chapter}{目錄}\if@twocolumn \@restonecoltrue \onecolumn \else \@restonecolfalse \fi \chapter *{\contentsname \@mkboth {\MakeUppercase \contentsname }{\MakeUppercase \contentsname }}\@starttoc {toc}\if@restonecol \twocolumn \fi}

\newcommand{\xchaptertitle}{\thechapter 、}
\newcommand{\xthepart}{第\@zhnum\c@part 部}
%重新定義標題的計數器
\renewcommand \thepart {第\@zhnum\c@part 部}
\renewcommand \thechapter {\@zhnum\c@chapter}
\renewcommand \thesection {\@arabic\c@chapter.\@arabic\c@section}
\renewcommand \thesubsection {\thesection.\@arabic\c@subsection}
\renewcommand \thefigure {\@arabic\c@chapter.\@arabic\c@figure }
%\renewcommand \theequation {\@arabic\c@myequation}
%\renewenvironment{equation}{\centering $$}{$$\hfill (\theequation)\refstepcounter{myequation}}
\counterwithout{equation}{chapter}
\counterwithout{table}{chapter}
\counterwithout{figure}{chapter}

\renewcommand{\partname}{\thispagestyle{empty}\color{structurecolor}}
\renewcommand{\chaptermark}[1]{\markboth{\xchaptertitle\, #1}{}}
%\renewcommand{\chaptermark}[1]{\markboth{\xchaptertitle\, #1}{}}
%重新定義標題的樣式
\titleformat{\part}{\thispagestyle{empty}\Huge\centering\bfseries\color{structurecolor}}{\noindent\thepart}{0em}{\\}
\titleformat{\chapter}{\Large\bf}{\xchaptertitle}{.1em}{ }
\titleformat{\section}{\large\bf}{\thesection}{.1em}{\hskip24pt}
\titleformat{\subsection}{\bf}{\thesubsection}{1em}{\hskip12pt}
%\renewcommand{\headrule}{\color{structurecolor}\hrule width\textwidth}

\renewcommand{\cftfigpresnum}{圖}
\renewcommand{\cfttabpresnum}{圖}


%重新定義chapter後的空間
%\titlespacing*{⟨command⟩}{⟨left⟩}{⟨beforesep⟩}{⟨aftersep⟩}[⟨right⟩]
\titlespacing*{\chapter}{0pt}{-6pt}{6pt}
\titlespacing*{\section}{0pt}{3pt}{6pt}
\titlespacing*{\subsection}{0pt}{3pt}{6pt}

%定義目錄中的縮進
%\titlecontents{section}[left]{above}{before with label}{before without label}{filler and page}[after]
\titlecontents{part}[20mm]{ }{\contentslabel{50pt}}{\hspace{-50pt}}{\titlerule*[10pt]{.}\contentspage}[\vskip6pt{\pagebreak[3]}]
\titlecontents{chapter}[20mm]{ }{\contentslabel{50pt}}{\hspace{-50pt}}{\titlerule*[10pt]{.}\contentspage}[\vskip6pt{\pagebreak[1]}]
\titlecontents{section}[20mm]{ }{\contentslabel{36pt}}{\hspace{-36pt}}{\titlerule*[10pt]{.}\contentspage} [\vskip6pt{\pagebreak[1]}]
\titlecontents{subsection}[20mm]{ }{\contentslabel{36pt}}{\hspace*{-8mm}}{\titlerule*[10pt]{.}\contentspage}[\vskip6pt{\pagebreak[1]}]
\pagenumbering{roman}

\setlength{\parskip}{10pt}

\endinput