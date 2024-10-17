%define name figlet-more-fonts
%define version 20040514
%define release 11

Summary: Program for making large letters out of ordinary text 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: contributed.tar.bz2
Source2: international.tar.gz
Source3: ms-dos.tar.bz2
License: Artistic
Group: Toys
Url: https://ianchai.50megs.com/figlet.html
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



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20040514-10mdv2011.0
+ Revision: 618284
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20040514-9mdv2010.0
+ Revision: 428730
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20040514-8mdv2009.0
+ Revision: 245142
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 20040514-6mdv2008.1
+ Revision: 170830
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Aug 21 2007 Olivier Thauvin <nanardon@mandriva.org> 20040514-5mdv2008.0
+ Revision: 68531
- rebuild


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 11:31:40 (53401)
- enable sse2 asm optimisation on ppc and sparc

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 11:22:32 (53394)
Import figlet-more-fonts

* Tue Oct 04 2005 Olivier Thauvin <nanardon@mandriva.org> 20040514-3mdk
- rebuild

* Sat Aug 28 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 20040514-2mdk
- fix conflict with figlet

