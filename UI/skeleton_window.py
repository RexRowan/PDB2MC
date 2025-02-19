from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QDesktopServices, QIcon
from PyQt6 import QtCore, QtGui, QtWidgets
import os
from .utilities import InformationBox, MyComboBox,IncludedPDBPopup, MinecraftPopup, FileExplorerPopup
from PDB2MC.variables import decorative_blocks
import pandas as pd
from PDB2MC import minecraft_functions as mcf, pdb_manipulation as pdbm, skeleton
import sys
import pkg_resources
class SkeletonWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # current_directory = os.path.basename(os.getcwd())
        # if current_directory == "PDB2MC":
        #     mcpdb_directory = os.path.join(os.getcwd(), ".." "UI")
        #     os.chdir(mcpdb_directory)

        os.chdir(get_images_path())

        self.user_pdb_file = None
        self.user_minecraft_save = None
        self.setWindowTitle("Skeleton Mode")
        self.setWindowIcon(QIcon('images/icons/logo.png'))
        self.resize(450, 411)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.switchModeLabel = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        self.switchModeLabel.setFont(font)
        self.switchModeLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.switchModeLabel.setObjectName("switchModeLabel")
        self.vSepLine = QtWidgets.QFrame(parent=self.centralwidget)

        self.vSepLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.vSepLine.setLineWidth(2)
        self.vSepLine.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.vSepLine.setObjectName("vSepLine")
        self.CustomMode = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.CustomMode.setFont(font)
        self.CustomMode.setObjectName("CustomMode")
        self.SkeletonMode = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.SkeletonMode.setFont(font)
        self.SkeletonMode.setObjectName("SkeletonMode")
        self.XRayMode = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.XRayMode.setFont(font)
        self.XRayMode.setObjectName("XRayMode")
        self.SpaceFillingMode = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(8)
        self.SpaceFillingMode.setFont(font)
        self.SpaceFillingMode.setObjectName("SpaceFillingMode")
        self.AminoAcidMode = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(8)
        self.AminoAcidMode.setFont(font)
        self.AminoAcidMode.setObjectName("AminoAcidMode")
        self.RibbonMode = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(11)
        self.RibbonMode.setFont(font)
        self.RibbonMode.setObjectName("RibbonMode")
        self.github = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.github.setFont(font)
        self.github.setObjectName("github")
        self.help = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.help.setFont(font)
        self.help.setObjectName("help")
        self.rcsbButton = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.rcsbButton.setFont(font)
        self.rcsbButton.setObjectName("rcsbButton")
        self.mc2pdbLabel = QtWidgets.QLabel(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.mc2pdbLabel.setFont(font)
        self.mc2pdbLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.mc2pdbLabel.setObjectName("mc2pdbLabel")
        self.pdbDatabaseLabel = QtWidgets.QLabel(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        self.pdbDatabaseLabel.setFont(font)
        self.pdbDatabaseLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.pdbDatabaseLabel.setObjectName("pdbDatabaseLabel")
        self.modeInfoHLine = QtWidgets.QFrame(parent=self.centralwidget)

        self.modeInfoHLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.modeInfoHLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.modeInfoHLine.setObjectName("modeInfoHLine")
        self.infoDatabaseHLine = QtWidgets.QFrame(parent=self.centralwidget)

        self.infoDatabaseHLine.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.infoDatabaseHLine.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.infoDatabaseHLine.setObjectName("infoDatabaseHLine")
        self.bg = QtWidgets.QLabel(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(7)
        self.bg.setFont(font)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("images/MC2PDB bg.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/black_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/red_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/icons/orange_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/icons/yellow_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/icons/lime_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/icons/green_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("images/icons/cyan_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("images/icons/light_blue_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("images/icons/blue_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("images/icons/purple_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("images/icons/magenta_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("images/icons/magenta_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("images/icons/brown_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("images/icons/gray_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("images/icons/light_gray_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("images/icons/white_concrete.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon17 = QtGui.QIcon()
        icon17.addPixmap(QtGui.QPixmap("images/icons/red_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap("images/icons/orange_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap("images/icons/yellow_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon20 = QtGui.QIcon()
        icon20.addPixmap(QtGui.QPixmap("images/icons/lime_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon21 = QtGui.QIcon()
        icon21.addPixmap(QtGui.QPixmap("images/icons/green_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon22 = QtGui.QIcon()
        icon22.addPixmap(QtGui.QPixmap("images/icons/cyan_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon23 = QtGui.QIcon()
        icon23.addPixmap(QtGui.QPixmap("images/icons/light_blue_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon24 = QtGui.QIcon()
        icon24.addPixmap(QtGui.QPixmap("images/icons/blue_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon25 = QtGui.QIcon()
        icon25.addPixmap(QtGui.QPixmap("images/icons/purple_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon26 = QtGui.QIcon()
        icon26.addPixmap(QtGui.QPixmap("images/icons/magenta_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon27 = QtGui.QIcon()
        icon27.addPixmap(QtGui.QPixmap("images/icons/pink_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon28 = QtGui.QIcon()
        icon28.addPixmap(QtGui.QPixmap("images/icons/brown_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon29 = QtGui.QIcon()
        icon29.addPixmap(QtGui.QPixmap("images/icons/black_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon30 = QtGui.QIcon()
        icon30.addPixmap(QtGui.QPixmap("images/icons/gray_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon31 = QtGui.QIcon()
        icon31.addPixmap(QtGui.QPixmap("images/icons/light_gray_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon32 = QtGui.QIcon()
        icon32.addPixmap(QtGui.QPixmap("images/icons/white_glazed_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon33 = QtGui.QIcon()
        icon33.addPixmap(QtGui.QPixmap("images/icons/red_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon34 = QtGui.QIcon()
        icon34.addPixmap(QtGui.QPixmap("images/icons/orange_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon35 = QtGui.QIcon()
        icon35.addPixmap(QtGui.QPixmap("images/icons/yellow_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon36 = QtGui.QIcon()
        icon36.addPixmap(QtGui.QPixmap("images/icons/lime_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon37 = QtGui.QIcon()
        icon37.addPixmap(QtGui.QPixmap("images/icons/green_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon38 = QtGui.QIcon()
        icon38.addPixmap(QtGui.QPixmap("images/icons/cyan_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon39 = QtGui.QIcon()
        icon39.addPixmap(QtGui.QPixmap("images/icons/light_blue_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon40 = QtGui.QIcon()
        icon40.addPixmap(QtGui.QPixmap("images/icons/blue_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon41 = QtGui.QIcon()
        icon41.addPixmap(QtGui.QPixmap("images/icons/purple_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon42 = QtGui.QIcon()
        icon42.addPixmap(QtGui.QPixmap("images/icons/magenta_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon43 = QtGui.QIcon()
        icon43.addPixmap(QtGui.QPixmap("images/icons/pink_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon44 = QtGui.QIcon()
        icon44.addPixmap(QtGui.QPixmap("images/icons/brown_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon45 = QtGui.QIcon()
        icon45.addPixmap(QtGui.QPixmap("images/icons/black_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon46 = QtGui.QIcon()
        icon46.addPixmap(QtGui.QPixmap("images/icons/gray_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon47 = QtGui.QIcon()
        icon47.addPixmap(QtGui.QPixmap("images/icons/light_gray_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon48 = QtGui.QIcon()
        icon48.addPixmap(QtGui.QPixmap("images/icons/white_terracotta.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon49 = QtGui.QIcon()
        icon49.addPixmap(QtGui.QPixmap("images/icons/red_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon50 = QtGui.QIcon()
        icon50.addPixmap(QtGui.QPixmap("images/icons/orange_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon51 = QtGui.QIcon()
        icon51.addPixmap(QtGui.QPixmap("images/icons/yellow_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon52 = QtGui.QIcon()
        icon52.addPixmap(QtGui.QPixmap("images/icons/lime_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon53 = QtGui.QIcon()
        icon53.addPixmap(QtGui.QPixmap("images/icons/green_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon54 = QtGui.QIcon()
        icon54.addPixmap(QtGui.QPixmap("images/icons/cyan_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon55 = QtGui.QIcon()
        icon55.addPixmap(QtGui.QPixmap("images/icons/light_blue_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon56 = QtGui.QIcon()
        icon56.addPixmap(QtGui.QPixmap("images/icons/blue_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon57 = QtGui.QIcon()
        icon57.addPixmap(QtGui.QPixmap("images/icons/purple_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon58 = QtGui.QIcon()
        icon58.addPixmap(QtGui.QPixmap("images/icons/magenta_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon59 = QtGui.QIcon()
        icon59.addPixmap(QtGui.QPixmap("images/icons/pink_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon60 = QtGui.QIcon()
        icon60.addPixmap(QtGui.QPixmap("images/icons/brown_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon61 = QtGui.QIcon()
        icon61.addPixmap(QtGui.QPixmap("images/icons/black_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon62 = QtGui.QIcon()
        icon62.addPixmap(QtGui.QPixmap("images/icons/gray_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon63 = QtGui.QIcon()
        icon63.addPixmap(QtGui.QPixmap("images/icons/light_gray_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        icon64 = QtGui.QIcon()
        icon64.addPixmap(QtGui.QPixmap("images/icons/white_wool.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.backboneColorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.backboneColorLabel.setObjectName("backboneColorLabel")

        self.sidechainColorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.sidechainColorLabel.setObjectName("sidechainColorLabel")

        self.otherColorLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.otherColorLabel.setObjectName("otherColorLabel")

        self.otherColorBox = MyComboBox(self.centralwidget)
        self.otherColorBox.setObjectName("otherColorBox")
        self.otherColorBox.setEditable(True)

        self.backboneColorBox = MyComboBox(self.centralwidget)
        self.backboneColorBox.setObjectName("backboneColorBox")
        self.backboneColorBox.setEditable(True)

        self.sidechainColorBox = MyComboBox(self.centralwidget)
        self.sidechainColorBox.setObjectName("sidechainColorBox")
        self.sidechainColorBox.setEditable(True)

        icon_dict = {
            "red_concrete": "icon2",
            "orange_concrete": "icon3",
            "yellow_concrete": "icon4",
            "lime_concrete": "icon5",
            "green_concrete": "icon6",
            "cyan_concrete": "icon7",
            "light_blue_concrete": "icon8",
            "blue_concrete": "icon9",
            "purple_concrete": "icon10",
            "magenta_concrete": "icon11",
            "pink_concrete": "icon12",
            "brown_concrete": "icon13",
            "black_concrete": "icon1",
            "gray_concrete": "icon14",
            "light_gray_concrete": "icon15",
            "white_concrete": "icon16",
            "red_glazed_terracotta": "icon17",
            "orange_glazed_terracotta": "icon18",
            "yellow_glazed_terracotta": "icon19",
            "lime_glazed_terracotta": "icon20",
            "green_glazed_terracotta": "icon21",
            "cyan_glazed_terracotta": "icon22",
            "light_blue_glazed_terracotta": "icon23",
            "blue_glazed_terracotta": "icon24",
            "purple_glazed_terracotta": "icon25",
            "magenta_glazed_terracotta": "icon26",
            "pink_glazed_terracotta": "icon27",
            "brown_glazed_terracotta": "icon28",
            "black_glazed_terracotta": "icon29",
            "gray_glazed_terracotta": "icon30",
            "light_gray_glazed_terracotta": "icon31",
            "white_glazed_terracotta": "icon32",
            "red_terracotta": "icon33",
            "orange_terracotta": "icon34",
            "yellow_terracotta": "icon35",
            "lime_terracotta": "icon36",
            "green_terracotta": "icon37",
            "cyan_terracotta": "icon38",
            "light_blue_terracotta": "icon39",
            "blue_terracotta": "icon40",
            "purple_terracotta": "icon41",
            "magenta_terracotta": "icon42",
            "pink_terracotta": "icon43",
            "brown_terracotta": "icon44",
            "black_terracotta": "icon45",
            "gray_terracotta": "icon46",
            "light_gray_terracotta": "icon47",
            "white_terracotta": "icon48",
            "red_wool": "icon49",
            "orange_wool": "icon50",
            "yellow_wool": "icon51",
            "lime_wool": "icon52",
            "green_wool": "icon53",
            "cyan_wool": "icon54",
            "light_blue_wool": "icon55",
            "blue_wool": "icon56",
            "purple_wool": "icon57",
            "magenta_wool": "icon58",
            "pink_wool": "icon59",
            "brown_wool": "icon60",
            "black_wool": "icon61",
            "gray_wool": "icon62",
            "light_gray_wool": "icon63",
            "wool": "icon64",
            "red_stained_glass": "icon2",
            "orange_stained_glass": "icon3",
            "yellow_stained_glass": "icon4",
            "lime_stained_glass": "icon5",
            "green_stained_glass": "icon6",
            "cyan_stained_glass": "icon7",
            "light_blue_stained_glass": "icon8",
            "blue_stained_glass": "icon9",
            "purple_stained_glass": "icon10",
            "magenta_stained_glass": "icon11",
            "pink_stained_glass": "icon12",
            "brown_stained_glass": "icon13",
            "black_stained_glass": "icon1",
            "gray_stained_glass": "icon14",
            "light_stained_glass": "icon15",
            "white_stained_glass": "icon16"
        }

        color_boxes = [self.otherColorBox, self.sidechainColorBox, self.backboneColorBox]

        for color_box in color_boxes:
            for value, icon in icon_dict.items():
                color_box.addItem(eval(icon), value)
            color_box.insertSeparator(16)
            color_box.insertSeparator(33)
            color_box.insertSeparator(50)
            color_box.insertSeparator(67)

        self.otherColorBox.setCurrentIndex(10)
        self.sidechainColorBox.setCurrentIndex(13)
        self.backboneColorBox.setCurrentIndex(13)

        self.aScaleLabel = QtWidgets.QLabel(parent=self.centralwidget)

        self.aScaleLabel.setObjectName("aScaleLabel")
        self.otherMoleculeCheck = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.otherMoleculeCheck.setChecked(True)
        self.otherMoleculeCheck.setObjectName("otherMoleculeCheck")
        self.otherMoleculeCheck.setToolTip("Check to show other non-protein, DNA, or RNA molecules.")
        self.aScaleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)

        self.aScaleSpinBox.setDecimals(1)
        self.aScaleSpinBox.setMinimum(1.0)
        self.aScaleSpinBox.setMaximum(50.0)
        self.aScaleSpinBox.setSingleStep(0.5)
        self.aScaleSpinBox.setProperty("value", 1.5)
        self.aScaleSpinBox.setObjectName("aScaleSpinBox")
        self.aScaleSpinBox.setToolTip("Change the diameter (rounded up) of each atom.")
        self.showBackboneCheck = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.showBackboneCheck.setChecked(True)
        self.showBackboneCheck.setObjectName("showBackboneCheck")
        self.showBackboneCheck.setToolTip("Show the N-C-C backbone of the main models.")
        self.showSidechainCheck = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.showSidechainCheck.setChecked(True)
        self.showSidechainCheck.setObjectName("showSidechainCheck")
        self.showSidechainCheck.setToolTip("Show amino acid R-groups")
        self.colorByBackboneCheck = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.colorByBackboneCheck.setChecked(False)
        self.colorByBackboneCheck.setObjectName("colorByBackboneCheck")
        self.colorByBackboneCheck.setToolTip("Color the backbones of the main models by the molecule number.")
        self.pScaleLabel = QtWidgets.QLabel(parent=self.centralwidget)

        self.pScaleLabel.setObjectName("pScaleLabel")
        self.pScaleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)

        self.pScaleSpinBox.setDecimals(1)
        self.pScaleSpinBox.setMinimum(1.0)
        self.pScaleSpinBox.setMaximum(50.0)
        self.pScaleSpinBox.setSingleStep(0.5)
        self.pScaleSpinBox.setObjectName("pScaleSpinBox")
        self.pScaleSpinBox.setToolTip("Scale the entire model by this factor.")
        self.bScaleLabel = QtWidgets.QLabel(parent=self.centralwidget)

        self.bScaleLabel.setObjectName("bScaleLabel")
        self.backboneScaleSpinBox = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)

        self.backboneScaleSpinBox.setDecimals(1)
        self.backboneScaleSpinBox.setMinimum(1.0)
        self.backboneScaleSpinBox.setMaximum(50.0)
        self.backboneScaleSpinBox.setSingleStep(0.5)
        self.backboneScaleSpinBox.setObjectName("backboneScaleSpinBox")
        self.backboneScaleSpinBox.setToolTip("Scale the width of the backbone by this factor.")
        self.selectIncludedPDBButton = QtWidgets.QPushButton(parent=self.centralwidget)

        self.selectIncludedPDBButton.setObjectName("selectIncludedPDBButton")
        self.selectMinecraftSaveButton = QtWidgets.QPushButton(parent=self.centralwidget)

        self.selectMinecraftSaveButton.setObjectName("selectMinecraftSaveButton")
        self.simpleOutputCheck = QtWidgets.QCheckBox(parent=self.centralwidget)

        self.simpleOutputCheck.setChecked(True)
        self.simpleOutputCheck.setObjectName("simpleOutputCheck")
        self.simpleOutputCheck.setToolTip("Un-select to create individual commands for each molecule")
        self.selectPDBFileButton = QtWidgets.QPushButton(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.selectPDBFileButton.setFont(font)
        self.selectPDBFileButton.setObjectName("pushButton_10")
        self.createFunctionsButton = QtWidgets.QPushButton(parent=self.centralwidget)

        self.createFunctionsButton.setToolTip("Add the selected PDB file to the Minecraft world")
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.createFunctionsButton.setFont(font)
        self.createFunctionsButton.setObjectName("pushButton_13")
        self.orText = QtWidgets.QLabel(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.orText.setFont(font)
        self.orText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.orText.setObjectName("or")
        self.andText = QtWidgets.QLabel(parent=self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(9)
        self.andText.setFont(font)
        self.andText.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.andText.setObjectName("and")

        self.bg.setGeometry(QtCore.QRect(-90, -50, 781, 461))

        self.switchModeLabel.setGeometry(QtCore.QRect(0, 0, 101, 31))
        self.CustomMode.setGeometry(QtCore.QRect(10, 30, 75, 23))
        self.SkeletonMode.setGeometry(QtCore.QRect(10, 60, 75, 23))
        self.XRayMode.setGeometry(QtCore.QRect(10, 90, 75, 23))
        self.SpaceFillingMode.setGeometry(QtCore.QRect(10, 120, 75, 23))
        self.RibbonMode.setGeometry(QtCore.QRect(10, 150, 75, 23))
        self.AminoAcidMode.setGeometry(QtCore.QRect(10, 180, 75, 23))
        self.modeInfoHLine.setGeometry(QtCore.QRect(10, 210, 71, 16))

        self.mc2pdbLabel.setGeometry(QtCore.QRect(10, 220, 71, 21))
        self.help.setGeometry(QtCore.QRect(10, 250, 75, 31))
        self.github.setGeometry(QtCore.QRect(10, 290, 75, 31))
        self.infoDatabaseHLine.setGeometry(QtCore.QRect(10, 320, 71, 16))
        self.pdbDatabaseLabel.setGeometry(QtCore.QRect(0, 330, 91, 21))
        self.rcsbButton.setGeometry(QtCore.QRect(10, 360, 75, 31))

        self.vSepLine.setGeometry(QtCore.QRect(90, 0, 20, 431))

        self.backboneColorLabel.setGeometry(QtCore.QRect(110, 10, 120, 21))
        self.backboneColorBox.setGeometry(QtCore.QRect(240, 10, 175, 22))
        self.showBackboneCheck.setGeometry(QtCore.QRect(240, 37, 121, 17))
        self.colorByBackboneCheck.setGeometry(QtCore.QRect(240, 53, 155, 21))
        self.bScaleLabel.setGeometry(QtCore.QRect(110, 75, 111, 21))
        self.backboneScaleSpinBox.setGeometry(QtCore.QRect(240, 75, 62, 22))
        self.pScaleLabel.setGeometry(QtCore.QRect(110, 100, 71, 21))
        self.pScaleSpinBox.setGeometry(QtCore.QRect(240, 100, 62, 22))

        self.sidechainColorLabel.setGeometry(QtCore.QRect(110, 140, 120, 21))
        self.sidechainColorBox.setGeometry(QtCore.QRect(240, 140, 175, 22))
        self.showSidechainCheck.setGeometry(QtCore.QRect(240, 165, 121, 17))

        self.otherColorLabel.setGeometry(QtCore.QRect(110, 200, 121, 21))
        self.otherColorBox.setGeometry(QtCore.QRect(240, 200, 175, 22))
        self.otherMoleculeCheck.setGeometry(QtCore.QRect(240, 228, 131, 17))
        self.aScaleLabel.setGeometry(QtCore.QRect(110, 250, 61, 21))
        self.aScaleSpinBox.setGeometry(QtCore.QRect(240, 250, 62, 22))

        self.selectPDBFileButton.setGeometry(QtCore.QRect(110, 290, 91, 23))
        self.orText.setGeometry(QtCore.QRect(210, 290, 31, 21))
        self.selectIncludedPDBButton.setGeometry(QtCore.QRect(250, 290, 141, 23))

        self.andText.setGeometry(QtCore.QRect(210, 325, 31, 21))
        self.selectMinecraftSaveButton.setGeometry(QtCore.QRect(250, 325, 141, 23))

        self.simpleOutputCheck.setGeometry(QtCore.QRect(110, 360, 100, 31))
        self.createFunctionsButton.setGeometry(QtCore.QRect(230, 360, 181, 31))

        self.bg.raise_()
        self.switchModeLabel.raise_()
        self.vSepLine.raise_()
        self.CustomMode.raise_()
        self.SkeletonMode.raise_()
        self.XRayMode.raise_()
        self.SpaceFillingMode.raise_()
        self.AminoAcidMode.raise_()
        self.RibbonMode.raise_()
        self.github.raise_()
        self.help.raise_()
        self.rcsbButton.raise_()
        self.mc2pdbLabel.raise_()
        self.pdbDatabaseLabel.raise_()
        self.modeInfoHLine.raise_()
        self.infoDatabaseHLine.raise_()
        self.backboneColorLabel.raise_()
        self.sidechainColorLabel.raise_()
        self.otherColorLabel.raise_()
        self.otherColorBox.raise_()
        self.backboneColorBox.raise_()
        self.sidechainColorBox.raise_()
        self.aScaleLabel.raise_()
        self.otherMoleculeCheck.raise_()
        self.aScaleSpinBox.raise_()
        self.showBackboneCheck.raise_()
        self.showSidechainCheck.raise_()
        self.colorByBackboneCheck.raise_()
        self.pScaleLabel.raise_()
        self.pScaleSpinBox.raise_()
        self.bScaleLabel.raise_()
        self.backboneScaleSpinBox.raise_()
        self.selectIncludedPDBButton.raise_()
        self.selectMinecraftSaveButton.raise_()
        self.simpleOutputCheck.raise_()
        self.selectPDBFileButton.raise_()
        self.createFunctionsButton.raise_()
        self.orText.raise_()
        self.andText.raise_()
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

        # Connect the QPushButton's clicked signal to a slot method
        self.help.clicked.connect(self.handle_help_button)
        self.rcsbButton.clicked.connect(self.handle_rscb_button)
        self.github.clicked.connect(self.handle_github_button)
        self.CustomMode.clicked.connect(self.handle_custom_mode)
        self.SkeletonMode.clicked.connect(self.handle_skeleton_mode)
        self.XRayMode.clicked.connect(self.handle_xray_mode)
        self.SpaceFillingMode.clicked.connect(self.handle_space_filling_mode)
        self.AminoAcidMode.clicked.connect(self.handle_amino_acid_mode)
        self.RibbonMode.clicked.connect(self.handle_ribbon_mode)
        self.selectIncludedPDBButton.clicked.connect(self.handle_included_pdb_button)
        self.selectPDBFileButton.clicked.connect(self.handle_select_pdb_file_button)
        self.selectMinecraftSaveButton.clicked.connect(self.handle_select_minecraft_button)
        self.createFunctionsButton.clicked.connect(self.handle_make_function_button)

        self.otherColorBox.focusOut.connect(lambda: self.check_input(self.otherColorBox, decorative_blocks))
        self.backboneColorBox.focusOut.connect(lambda: self.check_input(self.backboneColorBox, decorative_blocks))
        self.sidechainColorBox.focusOut.connect(lambda: self.check_input(self.sidechainColorBox, decorative_blocks))

        self.showBackboneCheck.stateChanged.connect(self.on_showBackboneCheck_changed)
        self.showSidechainCheck.stateChanged.connect(self.on_showSidechainCheck_changed)
        self.colorByBackboneCheck.stateChanged.connect(self.on_colorByBackboneCheck_changed)
        self.otherMoleculeCheck.stateChanged.connect(self.on_otherMoleculeCheck_changed)

    def on_showBackboneCheck_changed(self, state):
        if not self.colorByBackboneCheck.isChecked():
            self.backboneColorBox.setEnabled(state != 0)

        self.backboneScaleSpinBox.setEnabled(state !=0)

    def on_showSidechainCheck_changed(self, state):
        if not self.colorByBackboneCheck.isChecked():
            self.sidechainColorBox.setEnabled(state != 0)

    def on_colorByBackboneCheck_changed(self, state):
        self.backboneColorBox.setEnabled(state == 0)
        self.sidechainColorBox.setEnabled(state == 0)

    def on_otherMoleculeCheck_changed(self, state):
        self.otherColorBox.setEnabled(state != 0)
        self.aScaleSpinBox.setEnabled(state != 0)


    def check_input(self, combobox, valid_options):
        text = combobox.currentText()
        #ensure that text is lowercase
        text = text.lower()
        #replace any space characters with '_'
        text = text.replace(' ', '_')
        if text not in decorative_blocks:
            self.show_information_box(title_text=f"Invalid block input",
                                      text=f"{text} is not a valid block option.",
                                      icon_path="images/icons/icon_bad.png")
            #QMessageBox.warning(self, "Invalid Input", f"{text} is not a valid option.")
            combobox.setCurrentIndex(0)
        else:
            combobox.setCurrentText(text)

    # Slot methods to handle QPushButton clicks
    def handle_select_pdb_file_button(self):
        self.selectPDB = FileExplorerPopup()
        self.user_pdb_file = self.selectPDB.selected_file

    def handle_select_minecraft_button(self):
        self.selectMinecraft = MinecraftPopup()
        if self.selectMinecraft.selected_directory is None:
            self.show_information_box(title_text=f"Error",
                                      text=f"Remember to select a Minecraft save.",
                                      icon_path="images/icons/icon_bad.png")
            #QMessageBox.critical(None, "Error", "Remember to select a Minecraft save.")
            return
        self.user_minecraft_save = self.selectMinecraft.selected_directory
    def handle_included_pdb_button(self):
        self.includedPDB = IncludedPDBPopup()
        self.includedPDB.show()
        self.includedPDB.selected.connect(self.save_selected_text)

    def save_selected_text(self, text):
        self.selected_text = text        #make global variable for pdb file
        self.user_pdb_file = f"presets/{text}.pdb"

    def handle_make_function_button(self):
        # Create a dictionary to store the user options
        config_data = {'atoms': {}}

        # Add the current text of each combobox to the dictionary
        config_data['atoms']['O'] = 'red_wool'
        config_data['atoms']['N'] = 'blue_wool'
        config_data['atoms']['P'] = 'lime_wool'
        config_data['atoms']['S'] = 'yellow_wool'
        config_data['atoms']['C'] = 'black_wool'
        config_data['atoms']['FE'] = 'iron_block'
        config_data['atoms']['other_atom'] = self.otherColorBox.currentText()
        config_data['atoms']['backbone_atom'] = self.backboneColorBox.currentText()
        config_data['atoms']['sidechain_atom'] = self.sidechainColorBox.currentText()
        config_data['backbone_size'] = self.backboneScaleSpinBox.value()
        config_data['atom_scale'] = self.aScaleSpinBox.value()
        config_data['scale'] = self.pScaleSpinBox.value()

        # Add the checked state of each checkbox to the dictionary
        config_data['show_hetatm'] = self.otherMoleculeCheck.isChecked()
        config_data['backbone'] = self.showBackboneCheck.isChecked()
        config_data['sidechain'] = self.showSidechainCheck.isChecked()
        config_data['by_chain'] = self.colorByBackboneCheck.isChecked()
        config_data['simple'] = self.simpleOutputCheck.isChecked()

        # Add the current paths of the files and directories to the dictionary
        # Replace 'file_path' and 'save_path' with the actual paths
        if self.user_pdb_file is None:
            self.show_information_box(title_text=f"Error: No PDB file",
                                      text=f"Please select a PDB file.",
                                      icon_path="images/icons/icon_bad.png")
            #QMessageBox.critical(None, "Error", "Please select a PDB file.")
        elif self.user_minecraft_save is None:
            self.show_information_box(title_text=f"Error: No Minecraft save",
                                      text=f"Please select a Minecraft save.",
                                      icon_path="images/icons/icon_bad.png")
            #QMessageBox.critical(None, "Error", "Please select a Minecraft save.")
        else:
            config_data['pdb_file'] = self.user_pdb_file
            config_data['save_path'] = self.user_minecraft_save

            # Read in the PDB file and process it
            pdb_file = config_data['pdb_file']
            pdb_df = pdbm.read_pdb(pdb_file)
            pdb_name = pdbm.get_pdb_code(pdb_file)
            scalar = config_data['scale']
            scaled = pdbm.scale_coordinates(pdb_df, scalar)
            moved = pdbm.move_coordinates(scaled)
            moved = pdbm.rotate_to_y(moved)
            rounded = pdbm.round_df(moved)

            hetatom_df = pd.DataFrame()
            hetatm_bonds = pd.DataFrame()

            # Check if the user wants het-atoms, if so, process them
            if config_data["show_hetatm"] == True:
                # check if the first column of rounded contains any "HETATM" values

                if "HETATM" in rounded.iloc[:, 0].values:
                    hetatm_bonds = pdbm.process_hetatom(rounded, pdb_file)
                    hetatom_df = pdbm.filter_type_atom(rounded, remove_type="ATOM", remove_atom="H")
                    # hetatom_df = pdbm.filter_type_atom(rounded, remove_type="ATOM")
                else:
                    hetatm_bonds = None
                    hetatom_df = None
                    config_data["show_hetatm"] = False

            atom_df = pdbm.filter_type_atom(rounded, remove_type="HETATM", remove_atom="H")

            # Delete the old mcfunctions if they match the current one
            mc_dir = config_data['save_path']
            mcf.delete_mcfunctions(mc_dir, "z" + pdb_name.lower())

            try:

                skeleton.run_mode(config_data, pdb_name, pdb_file, rounded, mc_dir, atom_df, hetatom_df, hetatm_bonds)
            except Exception as e:
                self.show_information_box(title_text=f"Error encountered",
                                          text=f"Model has not generated! \nError: {e}",
                                          icon_path="images/icons/icon_bad.png")

            mcfiles = mcf.find_mcfunctions(mc_dir, pdb_name.lower())

            if config_data["simple"]:
                mcf.create_simple_function(pdb_name, mc_dir)
                mcf.create_clear_function(mc_dir, pdb_name)
                mcf.delete_mcfunctions(mc_dir, "z" + pdb_name.lower())
            else:
                mcf.create_master_function(mcfiles, pdb_name, mc_dir)
                mcf.create_clear_function(mc_dir, pdb_name)

            lower = pdb_name.lower()

            self.show_information_box(title_text = f"Model generated", text = f"Finished! \n Remember to use /reload\n Make your model with: /function protein:build_" + lower, icon_path ="images/icons/icon_good.png")

            #QMessageBox.information(None, "Model generated", f"Finished!\nRemember to /reload in your world and /function protein:build_{lower}")

    def show_information_box(self, title_text, text, icon_path):
        self.info_box = InformationBox()
        self.info_box.set_text(text)
        self.info_box.set_title(title_text)
        self.info_box.set_icon(icon_path)
        self.info_box.show()

    def handle_github_button(self):
        QDesktopServices.openUrl(QtCore.QUrl("https://github.com/markus-nevil/mcpdb"))

    def handle_help_button(self):
        from UI.help_window import HelpWindow
        help_window = HelpWindow.instance()
        if help_window.isVisible():
            # If a HelpWindow already exists, bring it to the front
            help_window.raise_()
            help_window.activateWindow()
        else:
            # If no HelpWindow exists, create a new one
            help_window.show()

        # Move the HelpWindow to the center of the current screen
        frame_geometry = help_window.frameGeometry()
        screen_center = self.screen().availableGeometry().center()
        frame_geometry.moveCenter(screen_center)
        help_window.move(frame_geometry.topLeft())
        #QDesktopServices.openUrl(QtCore.QUrl("https://github.com/markus-nevil/mcpdb/blob/main/README.md"))

    def handle_rscb_button(self):
        QDesktopServices.openUrl(QtCore.QUrl("https://www.rcsb.org/"))

    def handle_custom_mode(self):
        try:
            from UI.custom_window import CustomWindow
            self.Custom = CustomWindow()
            self.Custom.show()
            self.hide()
        except Exception as e:
            print(f"Error in handle_custom_mode: {e}")

    def handle_skeleton_mode(self):
        try:
            pass
        except Exception as e:
            print(f"Error in handle_skeleton_mode: {e}")

    def handle_xray_mode(self):
        try:
            from UI.xray_window import XrayWindow
            self.Xray = XrayWindow()
            self.Xray.show()
            self.hide()
        except Exception as e:
            print(f"Error in handle_xray_mode: {e}")

    def handle_space_filling_mode(self):
        try:
            from UI.space_filling_window import spWindow
            self.SpaceFilling = spWindow()
            self.SpaceFilling.show()
            self.hide()
        except Exception as e:
            print(f"Error in handle_space_filling_mode: {e}")

    def handle_amino_acid_mode(self):
        try:
            from UI.amino_acids_window import AAWindow
            self.AminoAcid = AAWindow()
            self.AminoAcid.show()
            self.hide()
        except Exception as e:
            print(f"Error in handle_amino_acid_mode: {e}")

    def handle_ribbon_mode(self):
        try:
            from UI.ribbon_window import RibbonWindow
            self.Ribbon = RibbonWindow()
            self.Ribbon.show()
            self.hide()
        except Exception as e:
            print(f"Error in handle_ribbon_mode: {e}")

    def retranslateUi(self, SkeletonWindow):
        _translate = QtCore.QCoreApplication.translate
        self.switchModeLabel.setText(_translate("SkeletonWindow", "Switch Mode"))
        self.CustomMode.setText(_translate("SkeletonWindow", "Custom"))
        self.SkeletonMode.setText(_translate("SkeletonWindow", "Skeleton"))
        self.XRayMode.setText(_translate("SkeletonWindow", "X-Ray"))
        self.SpaceFillingMode.setText(_translate("SkeletonWindow", "Space Filling"))
        self.AminoAcidMode.setText(_translate("SkeletonWindow", "Amino Acids"))
        self.RibbonMode.setText(_translate("SkeletonWindow", "Ribbon"))
        self.github.setText(_translate("SkeletonWindow", "Github"))
        self.help.setText(_translate("SkeletonWindow", "Help"))
        self.rcsbButton.setText(_translate("SkeletonWindow", "RCSB.org"))
        self.mc2pdbLabel.setText(_translate("SkeletonWindow", "PDB2MC"))
        self.pdbDatabaseLabel.setText(_translate("SkeletonWindow", "PDB Database"))
        self.backboneColorLabel.setText(_translate("SkeletonWindow", "Select backbone color:"))
        self.sidechainColorLabel.setText(_translate("SkeletonWindow", "Select sidechain color:"))
        self.otherColorLabel.setText(_translate("SkeletonWindow", "Select other color:"))
        self.aScaleLabel.setText(_translate("SkeletonWindow", "Atom scale:"))
        self.otherMoleculeCheck.setText(_translate("SkeletonWindow", "Show other molecules"))
        self.showBackboneCheck.setText(_translate("SkeletonWindow", "Show backbone"))
        self.showSidechainCheck.setText(_translate("SkeletonWindow", "Show sidechain"))
        self.colorByBackboneCheck.setText(_translate("SkeletonWindow", "Color backbone by chain"))
        self.pScaleLabel.setText(_translate("SkeletonWindow", "Protein scale:"))
        self.bScaleLabel.setText(_translate("SkeletonWindow", "Backbone scale:"))
        self.selectIncludedPDBButton.setText(_translate("SkeletonWindow", "Select Included PDB File"))
        self.selectMinecraftSaveButton.setText(_translate("SkeletonWindow", "Select Minecraft Save"))
        self.simpleOutputCheck.setText(_translate("SkeletonWindow", "Simple output"))
        self.selectPDBFileButton.setText(_translate("SkeletonWindow", "Select PDB File"))
        self.createFunctionsButton.setText(_translate("SkeletonWindow", "Create Minecraft Functions"))
        self.orText.setText(_translate("SkeletonWindow", "or"))
        self.andText.setText(_translate("SkeletonWindow", "and"))

def get_images_path():
    if getattr(sys, 'frozen', False):
        # The program is running as a compiled executable
        images_dir = pkg_resources.resource_filename('UI', 'images')
        images_dir = os.path.join(images_dir, '..')
        return images_dir
    else:
        # The program is running as a Python script or it's installed in the Python environment
        # Get the directory of the current script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the path to the UI/images directory
        images_dir = os.path.join(current_dir, '..', 'UI')
        return images_dir

if __name__ == "__main__":
    app = QApplication([])
    main_window = SkeletonWindow()
    main_window.show()
    app.exec()