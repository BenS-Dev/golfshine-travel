<tr>
	<td width="1000">
		<table width="1000" height="110" cellspacing="0" cellpadding="0" valign="top" bgcolor="082E00">
		
			<tr>
				<td width="540" height="110"><a href="index.php"><img src="img/cabecera-logo.jpg" border="0"></a></td>
				
				<td width="100" height="110"><img src="img/separdor-vertical.jpg" width="100" height="110"></td>
				
				<td width="200" height="110"><a href="book-golf.php"><img src="img/book-golf.jpg" border="0"></a></td>
				
				<td width="160" height="110"><a href="mailto:golf@wingolftravel.com"><img src="img/tope-links.jpg" border="0"></a></td>
				
			</tr>
		</table>	
	</td>
</tr>	

<tr>
	<td width="1000">
		<table width="1000" height="66" cellspacing="0" cellpadding="0" valign="top">
			
			<tr>
						
			<? 
				if ($pagina=="home") { ?>
					<td align="center" valign="middle"><a href="index.php" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('home','','img/home-on.jpg',1);"><img name="home" src="img/home-on.jpg" width="95" height="66" border="0" title="home"></a></td>
				<? } else  { ?>
					<td align="center" valign="middle"><a href="index.php" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('home','','img/home-on.jpg',1);"><img name="home" src="img/home-off.jpg" width="95" height="66" border="0" title="home"></a></td>
				<? } ?>
				
				
				<? 
				if ($pagina=="itineraries") { ?>
					<td align="center" valign="middle"><a href="itineraries.php?categoriaselec=10&nivel=1" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('itineraries','','img/itineraries-on.jpg',1);"><img name="itineraries" src="img/itineraries-on.jpg" width="110" height="66" border="0" title="itineraries"></a></td>
				<? } else  { ?>
					<td align="center" valign="middle"><a href="itineraries.php?categoriaselec=10&nivel=1" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('itineraries','','img/itineraries-on.jpg',1);"><img name="itineraries" src="img/itineraries-off.jpg" width="110" height="66" border="0" title="itineraries"></a></td>
				<? } ?>

				
				<? 
				if ($pagina=="video") { ?>
					<td align="center" valign="middle"><a href="video.php?id=10" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('video','','img/video-on.jpg',1);"><img name="video" src="img/video-on.jpg" width="135" height="66" border="0" title="video gallery"></a></td>
				<? } else  { ?>
					<td align="center" valign="middle"><a href="video.php?id=10" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('video','','img/video-on.jpg',1);"><img name="video" src="img/video-off.jpg" width="135" height="66" border="0" title="video gallery"></a></td>
				<? } ?>
				
				
				<? 
				if ($pagina=="photo") { ?>
					<td align="center" valign="middle"><a href="photo.php?categoriaselec=10&nivel=1" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('photo','','img/photo-on.jpg',1);"><img name="photo" src="img/photo-on.jpg" width="135" height="66" border="0" title="photo gallery"></a></td>
				<? } else  { ?>
					<td align="center" valign="middle"><a href="photo.php?categoriaselec=10&nivel=1" onMouseOut="MM_swapImgRestore();" onMouseOver="MM_swapImage('photo','','img/photo-on.jpg',1);"><img name="photo" src="img/photo-off.jpg" width="135" height="66" border="0" title="photo gallery"></a></td>
				<? } ?>
				
				
				
				
				
				<td align="center" valign="middle"><img name="contacto" src="img/barra-pie-central.jpg" width="505" height="66" border="0" title="contact"></td>
				
				<td align="center" valign="middle"><img src="img/barra-pie-cierre.jpg" width="20" height="66" border="0"></td>
								
			</tr>
		</table>	
	</td>
</tr>

<map name="topelinks">
  <area shape="rect" coords="150,0,270,35" href="mailto:golf@wingolftravel.com">
</map>