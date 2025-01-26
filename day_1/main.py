import speech_recognition as sr
from drawing import setup_turtle 
from command_processor import process_command

def main():
    r = sr.Recognizer()
    r.dynamic_energy_threshold =  True
    r.pause_threshold = 0.5
    t = setup_turtle()

    while True:
        print("Running command loop")
        with sr.Microphone() as source:
            print("\nchọn cách nhập lệnh")
            print("1. Voice")
            print("2. Text")    
            print("3. Exit")

            choice = input("Chọn cách nhập lệnh: ")
            if choice =="1":
                with sr.Microphone() as source:    
                    print("Hãy nói lệnh bạn muốn thực hiện")
                    r.adjust_for_ambient_noise(source, duration=0.5)
                    audio = r.listen(source)
                try:
                    command = r.recognize_google(audio, language="vi-VN")
                    print(f"Lệnh bạn vừa nói: {command}")
                    process_command(command, t)
                except sr.UnknownValueError:
                    print("Không nhận diện được lệnh")
                except sr.RequestError:
                    print("Không thể kết nối với máy tính để nhận diện")

            elif choice == "2":
                print("\nCác lệnh có sẵn:")
                print("- vẽ hình vuông")
                print("- vẽ hình tròn [bán kính]")
                print("- vẽ đường thẳng") 
                print("- xoay phải")       
                print("- xoay trái")
                print("- vẽ hình chữ nhật")
                print("- vẽ hình tam giác")
                print("- vẽ hình sao")
                print("- vẽ hình ngũ giác")
                print("- vẽ hình lục giác")
                print("- vẽ hình elip")
                print("- vẽ đa giác [số cạch] [kích thước]")
                command = input("\n Nhập lệnh bạn muốn thực hiện: ") 
                process_command(command, t)
            elif choice == "3":
                print("Thoát chương trình")
                break
            else:
                print("Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()
   
