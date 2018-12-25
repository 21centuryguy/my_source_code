	function initialize() {

	//−−−−−−−−−−−オプションを指定−−−−−−−−−−−−−

		//目的地の座標を指定
		var myLatlng = new google.maps.LatLng(35.4478586,139.6378361);

		//地図のスタイルを設定
		var styleOptions = [
			{
				//スタイルを有効にする地物タイプを指定
				//all:すべてに対して有効（デフォルト）
				//landscape:風景に対してのみ有効
				//poi:公園や公共施設など、緑色の部分に対してのみ有効
				//road:道路に対してのみ有効
				//transit:駅や線路に対してのみ有効
				//water:水の要素に対してのみ有効
				//また、landscape.man_madeのようにさらに詳細に指定することも可能
				featureType: "all",

				//featureTypeで指定した地物タイプのうち、地形のみ、ラベルのみと更に詳細に設定する
				//all:すべてに対して有効（デフォルト）
				//geometry:地形のみに対して有効
				//labels:ラベルのみに対して有効
				//また、labels.iconのようにさらに詳細に指定することも可能
				elementType: "geometry",

				//スタイルを指定
				stylers: [
					//hue:基本色
					{ hue: "#21a1f8" },

					//lightness:明度 -100~100
					{ lightness: 0 },

					//saturation:彩度 -100~100
					{ saturation: 40 },

					//gamma: ガンマ補正の量 コントラストを変更する 0.01~10 通常は1.0
					{ gamma: 1.5 },

					//invert_lightness:明度の反転 true/false
					{ invert_lightness: false },

					//visibility:要素の表示のon/off
					//	on:表示する（デフォルト）
					//	off:表示しない
					//	simplified:ラベルのアウトラインのみ削除
					{ visibility: "simplified" },

					//color:地物周辺の色 設定しないほうが良い
					//weight:地物周辺の厚み 0~255 設定しないほうが良い
				]
			},
			//地図のスタイルを複数指定したい場合は以下に設定
			{
				featureType: "poi",
				elementType: "geometry",
				stylers: [
					{ hue: "#ffb400" },
					{ lightness: 0 },
					{ saturation: 100 },
					{ gamma: 1.2 },
					{ invert_lightness: false },
					{ visibility: "on" },
				]
			},
			{
				featureType: "transit",
				elementType: "geometry",
				stylers: [
					{ hue: "#ffb400" },
					{ lightness: 0 },
					{ saturation: 100 },
					{ gamma: 1.0 },
					{ invert_lightness: false },
					{ visibility: "on" },
				]
			},
		];

		//オプション
		var myOptions = {
			//拡大率 大きいほど拡大 1~21
			zoom: 16,

			//中心の座標
			center: myLatlng,

			//地図種類指定
			//ROADMAP:通常の道路地図（デフォルト）
			//SATELLITE:Google Earth 航空写真
			//TERRAIN:ROADMAPの[地形]のチェックがついた状態
			//HYBRID:SATELLITEに[ラベル]のチェックがついた状態
			mapTypeId: google.maps.MapTypeId.TERRAIN,

			//設定した地図スタイルを適用
			styles: styleOptions,

			//trueにするとコントローラーが全部消える
			disableDefaultUI: false,

			//マップタイプ切り替えの表示
			mapTypeControl: true,

			//マップタイプ切り替えのオプション
			mapTypeControlOptions: {
				//マップタイプ切り替えのデザイン
				//HORIZONTAL_BAR:横並び（デフォルト）
				//DROPDOWN_MENU:ドロップダウンメニュー
				style: google.maps.MapTypeControlStyle.DROPDOWN_MENU,

				//コントローラーの場所を指定
				//TOP_CENTER:中央上
				//TOP_LEFT:左上
				//TOP_RIGHT:右上
				//LEFT_TOP:左上 TOP_LEFTの下に配置される
				//RIGHT_TOP:右上 TOP_RIGHTの下に配置される
				//LEFT_CENTER:左中央
				//RIGHT_CENTER:右中央
				//LEFT_BOTTOM:左下 BOTTOM_LEFTの上に配置される
				//RIGHT_BOTTOM:右下 BOTTOM_RIGHTの上に配置される
				//BOTTOM_CENTER:中央下
				//BOTTOM_LEFT:左下
				//BOTTOM_RIGHT:右下
				position: google.maps.ControlPosition.LEFT_TOP,
			},

			//ズームイン・ズームアウトコントローラーの表示
			zoomControl: true,

			//ズームイン・ズームアウトコントローラーのオプション
			zoomControlOptions: {
				//コントローラーの場所を指定
				//指定可能箇所はmapTypeControlOptionsと同じ
				position: google.maps.ControlPosition.RIGHT_BOTTOM,
			},

			//長さの目安の表示
			scaleControl: true,

			//ストリートビュー切り替えの表示
			streetViewControl: true,

			//ストリートビュー切り替えのオプション
			streetViewControlOptions: {
				//コントローラーの場所を指定
				//指定可能箇所はmapTypeControlOptionsと同じ
				position: google.maps.ControlPosition.RIGHT_BOTTOM,
			},

			//マウスホイールの操作を有効にするか
			scrollwheel: true,
		}

		//マップを描画
		var map = new google.maps.Map(document.getElementById("map-canvas-access"), myOptions);

	//−−−−−−−−−−−インフォウィンドウ−−−−−−−−−−−−−

		var infowindow = new google.maps.InfoWindow({
			//情報ウィンドウの内容
			content: '<p class="txt12"><strong>株式会社DOE</strong></p>',

			//インフォウインドウの場所を微調整する
			pixelOffset: new google.maps.Size(-9, -15),

			//インフォウィンドウのコンテンツ部分の最大幅
			maxWidth: 200,

			//インフォウインドウが複数ある場合は重なり順を指定
			zIndex: 1,
		});

	//−−−−−−−−−−−マーカ−−−−−−−−−−−−−

		var marker = new google.maps.Marker({
			//マーカ位置
			position: myLatlng,

			//地図情報
			map: map,

			//アイコン画像
			//画像のパスを記述するだけでもOK
			icon: {
				//画像のパス
				url:"images/icon-flag.png",

				//アイコンのサイズ
				size: new google.maps.Size(33, 49),

				//原点
				origin: new google.maps.Point(0, 0),

				//マーカ位置と画像の接する点
				anchor: new google.maps.Point(0, 49),

				//画像のサイズ Retina対応のとき設定する
				scaledSize: new google.maps.Size(33, 49),
			},

			//アイコンの一部だけをクリックできるようにしたい場合に設定する。
			shape: {
				//shapeのタイプ指定
				//circle:円形
				//rect:長方形
				//poly:四角形
				type: 'rect',

				//typeに合わせて座標を指定する
				//circle:x,y,radiusと指定 xとyには原点の座標が入る
				//coords: [17,25,10],
				//rect:x1,y1,x2,y2と指定 左上の座標と右下の座標が入る
				coords: [0,0,33,49],
				//poly:左上を基点にして反時計回りに4点の座標を指定する
				//coords: [0,0,0,49,20,49,33,20,20,0],
			},

			//タイトル
			title: '株式会社DOE',

			//非表示切り替え（デフォルト:true）
			visible: true,

			//クリックイベントを有効にするか（デフォルト:true）
			clickable: true,

			//ドラッグでアイコンを移動できるか（デフォルト:false）
			draggable: false,
			
			//不透明度
			opacity: 1,
			
			//マーカが複数ある場合は重なり順を指定
			zIndex: 1,

			//アイコンにアニメーションを設定できる
			//DROP:マーカ位置にアイコンが落ちてきて終了
			//BOUNCE:ポインタがバウンドし続ける
			animation: google.maps.Animation.DROP,
		});

	//−−−−−−−−−−−インフォウィンドウ呼び出し−−−−−−−−−−−−−

		//google.maps.event.addListener()を使ってイベントを呼び出す
		//第一引数に監視する要素、第二引数にイベントハンドラ、第三引数にイベント関数を設定する
		//イベントリスナの詳細：https://developers.google.com/maps/documentation/javascript/events?hl=ja
		//
		//監視できる要素の一例
		//map,marker,windowなど
		//
		//イベントハンドラ一覧
		//bounds_changed:ビューポートが変わったら
		//center_changed:中心点が変わったら
		//click:クリックしたら
		//dblclick:ダブルクリックしたら
		//drag:ドラッグしたら
		//dragend:ドラッグが終わったら
		//dragstart:ドラッグが始まったら
		//heading_changed:ヘディングプロパティが変更されたら
		//idle:動いている状態が止まったら
		//maptypeid_changed:マップタイプが変わったら
		//mousemove:要素上のカーソルが動いたら
		//mouseout:要素上からカーソルが外に出たら
		//mouseover:要素上にカーソルが入ったら
		//projection_changed:プロジェクションが変わったら
		//rightclick:右クリックされたら
		//tilesloaded:読み込み時やマップスクロールなどで、マップの読み込みが終わったら
		//tilt_changed:航空写真の傾きが変わったら
		//zoom_changed:ズーム値が変更されたら
		//
		//markerに設定できるイベントハンドラは
		//click,dblclick,mousemove,mouseout,mouseover,rightclick
		google.maps.event.addListener(marker, 'click', function() {
			//インフォウィンドウ呼び出し
			infowindow.open(map,marker);

			//マーカのアニメーションはクリックイベントに登録できる
			//DROP:マーカ位置にアイコンが落ちてきて終了
			//BOUNCE:ポインタがバウンドし続ける
			var bounceMotion = marker.getAnimation() !== null ? null : google.maps.Animation.BOUNCE;
			marker.setAnimation(bounceMotion);
		});


	//−−−−−−−−−−−レスポンシブ−−−−−−−−−−−−−

		google.maps.event.addDomListener(window, "resize", function() {
			//ブラウザがリサイズされたらマップのセンターを更新する
			var center = map.getCenter();
			google.maps.event.trigger(map, "resize");
			map.setCenter(center);
		});

	//−−−−−−−−−−−地図上にオーバーレイを表示する−−−−−−−−−−−−−
		var overlay = new google.maps.GroundOverlay(
			//画像のパス
			"images/fukidashi.png",

			//画像のそれぞれの座標
			//座標で指定するので画像のアスペクト比がずれやすい
			{
				north: 35.4504586,
				south: 35.4489586,
				west: 139.6376361,
				east: 139.6397361,
			},
			//その他のオプション
			{
				//画像をクリックできるかどうか
				clickable:true,

				//画像を挿入するマップを指定
				map: map,

				//不透明度
				opacity: 1,
			}
		);

		//画像に対するイベントリスナを登録できる
		//設定できるイベントハンドラはclickとdblclick
		google.maps.event.addListener(overlay, 'click', function() {
			//オーバーレイを削除
			overlay.setMap(null);
		});
	}