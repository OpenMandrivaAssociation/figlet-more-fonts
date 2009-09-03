%define name figlet-more-fonts
%define version 20040514
%define release %mkrel 9

Summary: Program for making large letters out of ordinary text 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: contributed.tar.bz2
Source2: international.tar.gz
Source3: ms-dos.tar.bz2
License: Artistic
Group: Toys
Url: http://ianchai.50megs.com/figlet.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: figlet

%description
FIGlet is a program for making large letters out 
of ordinary text.

This package allready include lot of fonts.

%prep
%setup -q -n %name%version -c 0 
%setup -q -T -D -n %name%version -a 2 
%setup -q -T -D -n %name%version -a 3 

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%_datadir/figlet

(#SOURCE2
cd contributed

# Conflict with figlet itself
find . -name banner.flf -exec rm -f {} \;

cp -af *.fl? $RPM_BUILD_ROOT%_datadir/figlet
tar xzf Obanner.tgz
cp -af Obanner/*.fl? $RPM_BUILD_ROOT%_datadir/figlet
tar xzf Obanner-canon.tgz
cp -af Obanner-canon/*.fl? $RPM_BUILD_ROOT%_datadir/figlet
cp -af bdffonts/*.fl? $RPM_BUILD_ROOT%_datadir/figlet
cp -af C64-fonts/*.fl? $RPM_BUILD_ROOT%_datadir/figlet
)

ls contributed/*.fl? | sed 's!^.*/!%_datadir/figlet/!' >> files.list
ls contributed/Obanner/*.fl? | sed 's!^.*/!%_datadir/figlet/!' >> files.list
ls contributed/Obanner-canon/*.fl? | sed 's!^.*/!%_datadir/figlet/!' >> files.list
ls contributed/bdffonts/*.fl? | sed 's!^.*/!%_datadir/figlet/!' >> files.list
ls contributed/C64-fonts/*.fl? | sed 's!^.*/!%_datadir/figlet/!' >> files.list
(#SOURCE3
cd international
tar xzf cjkfonts.tar.gz
cp -af *.fl? $RPM_BUILD_ROOT%_datadir/figlet
)

ls international/*.fl? | sed 's!^.*/!%_datadir/figlet/!' >> files.list

(#SOURCE4
cd ms-dos
cp -af *.fl? $RPM_BUILD_ROOT%_datadir/figlet
)

ls ms-dos/*.fl? | sed 's!^.*/!%_datadir/figlet/!' >> files.list

chmod 644 $RPM_BUILD_ROOT%_datadir/figlet/*

cat files.list | sort | uniq >> files.list.uniq

%clean
rm -rf $RPM_BUILD_ROOT

%files -f files.list.uniq
%defattr(-,root,root)
%doc contributed/Obanner.README international/cjkfonts.readme  

