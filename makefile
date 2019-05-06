run: main.py display.py draw.py matrix.py parser.py
	python main.py

alt:
	python alt.py

clean:
	rm -rf *.pyc
	rm -rf *~
	rm -rf *.png

