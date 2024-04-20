# SK
- Načítajte súbor [`f03_loremIpsum.txt`](https://github.com/SpsKnSK/api/blob/main/Exercies/16_files/f03_loremIpsum.txt).
- Nájdite najdlhšiu vetu a vypíšte ju.
- Nájdite najkratšiu vetu a vypíšte ju, následne vyhľadajte v nej najdlhšie slovo a vypíšte ho na obrazovku.

# HU
- Olvassátok be a [`f03_loremIpsum.txt`](https://github.com/SpsKnSK/api/blob/main/Exercies/16_files/f03_loremIpsum.txt) fájlt
- Keressétek meg, és írassátok ki a leghosszabb sorát
- Keressétek meg a legrövidebb sorát, és a legrövidebb sorból írjátok ki a leghosszabb szót

> `allLinesSortedByLength = sorted(f.readlines(),key=len, reverse=True)`

# Output

```
The longest paragraph in the file has 1069 characters: In egestas erat imperdiet sed euismod nisi porta. Nulla facilisi etiam dignissim diam quis enim lobortis. Eleifend mi in nulla posuere sollicitudin aliquam ultrices sagittis. Lorem sed risus ultricies tristique nulla aliquet enim. Lectus vestibulum mattis ullamcorper velit sed ullamcorper morbi tincidunt. Lacus viverra vitae congue eu consequat ac felis donec. Placerat in egestas erat imperdiet sed euismod nisi porta. Luctus accumsan tortor posuere ac ut consequat semper viverra nam. Vehicula ipsum a arcu cursus. Fermentum dui faucibus in ornare quam viverra orci sagittis. Donec massa sapien faucibus et molestie ac feugiat sed lectus. Nec ullamcorper sit amet risus nullam. Elementum pulvinar etiam non quam lacus suspendisse faucibus interdum. Bibendum ut tristique et egestas quis ipsum suspendisse ultrices gravida. Semper auctor neque vitae tempus quam pellentesque nec nam. Sed augue lacus viverra vitae congue. Iaculis eu non diam phasellus vestibulum. Fames ac turpis egestas integer eget aliquet nibh. Tellus at urna condimentum mattis pellentesque id.

The shortest paragraph in the file has 411 characters: 'Tincidunt vitae semper quis lectus nulla at volutpat diam ut. Et leo duis ut diam quam nulla. Pellentesque nec nam aliquam sem et. Ut etiam sit amet nisl purus in. Porta lorem mollis aliquam ut porttitor leo a. Mi eget mauris pharetra et ultrices neque. Auctor elit sed vulputate mi sit amet. Odio eu feugiat pretium nibh ipsum. Elit duis tristique sollicitudin nibh sit. In mollis nunc sed id semper risus in.
'
 and the its longest word is 'sollicitudin'
 ```